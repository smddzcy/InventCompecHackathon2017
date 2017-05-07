const googleTrends = require('google-trends-api')
const axios = require('axios')
const _ = require('lodash')

// Constants
const API_ENDPOINT = 'http://localhost:3000/inventory_positions/sales_quantity'
const NUM_OF_PRODUCT_GROUPS = 5

// Key to search on Google Trends
const key = process.argv[2]

/**
 * Converts to Date object to String in m.d.Y format
 * @param  {Object} date A date object
 * @return {String}      String in m.d.Y format
 */
const dateToMDY = (date) => {
  const d = date.getDate()
  const m = date.getMonth() + 1
  const y = date.getFullYear()
  return '' + (d <= 9 ? '0' + d : d) + '.' + (m <= 9 ? '0' + m : m) + '.' + y
}

/**
 * Converts a m.d.Y date string to Y.m.d date string
 * @param {String} date Date string in m.d.Y
 */
const MDYtoYMD = (date) => date.split("\.").reverse().join("\.")

// Get the data from Google Trends and find the best fit in the product groups.
googleTrends.interestOverTime({
    keyword: key,
    startTime: new Date('2015-01-01'),
    endTime: new Date(Date.now()),
    geo: 'TR'
  })
  .then((res) => {
    const obj = JSON.parse(res)

    // Get timeline data of keyword and transform for it to a more usable one
    const timeline = obj.default.timelineData.map(el => {
      return {
        date: dateToMDY(new Date(el.time * 1000)),
        value: el.value[0]
      }
    })

    const productGroupsAndErrors = new Promise((resolve, reject) => {
      const result = []
      for (let i = 1; i <= NUM_OF_PRODUCT_GROUPS; i++) {
        axios.get(API_ENDPOINT, {
            params: {
              start_date: timeline[0].date,
              end_date: timeline[timeline.length - 1].date,
              product_group: i
            }
          })
          .then(function(response) {
            const maxSales = (_.maxBy(response.data, 'sales_quantity')).sales_quantity
            const normalizedData = _.map(response.data, el => {
              el.sales_quantity = el.sales_quantity / maxSales * 100
              return el
            })

            // Calculate the sum of square errors
            const sumOfSquaredErrors = _
              .chain(normalizedData)
              .map(el => {
                const closestDateOnTrend = (_.minBy(timeline, o => Math.abs(new Date(MDYtoYMD(o.date)) - new Date(MDYtoYMD(el.date)))))
                return (closestDateOnTrend.value - el.sales_quantity) ** 2
              })
              .sum()

            // Persist the product group and error tuples
            result.push({
              productGroup: i,
              sse: sumOfSquaredErrors
            })

            if (i === NUM_OF_PRODUCT_GROUPS) {
              resolve(result)
            }
          }).catch(console.error)
      }
    })

    // Get the minimum error product group
    productGroupsAndErrors.then(data => {
      const minErrorTuple = _.minBy(data, 'sse')
      console.log("Keyword: " + key)
      console.log("Minimum error on: " + JSON.stringify(minErrorTuple))
      console.log("All errors: " + JSON.stringify(data))
    }, console.error)

  }).catch(console.error)
