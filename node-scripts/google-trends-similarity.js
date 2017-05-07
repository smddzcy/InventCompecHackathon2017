const googleTrends = require('google-trends-api')
const axios = require('axios')
const _ = require('lodash')

// Constants
const API_ENDPOINT = 'http://localhost:3000/inventory_positions/sales_quantity'
const NUM_OF_PRODUCT_GROUPS = 5
const PRODUCT_TYPES = [
  'battaniye', 'bilgisayar', 'cep telefonu',
  'defter', 'elbise', 'mutfak robotu', 'blender', 'havlu', 'mayo', 'nevresim',
  'outdoor ayakkabı', 'pantolon', 'parfüm', 'roman', 'şampuan', 'tshirt'
]

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

const gtCache = {}

const keywordsAndErrors = new Promise((resolve, reject) => {
  const result = {}

  for (let i = 1; i <= NUM_OF_PRODUCT_GROUPS; i++) {
    for (let key of PRODUCT_TYPES) {
      // Use the cached request if it's cached before
      let gtPromise;
      if (gtCache[key] == null) {
        gtPromise = googleTrends.interestOverTime({
          keyword: key,
          startTime: new Date('2015-01-01'),
          endTime: new Date(Date.now()),
          geo: 'TR'
        })
      } else {
        gtPromise = gtCache[key];
      }

      gtPromise
        .then((res) => {
          const obj = JSON.parse(res)
          if (gtCache[key] == null) {
            gtCache[key] = new Promise((resolve, reject) => resolve(res))
          }

          // Get timeline data of keyword and transform for it to a more usable one
          const timeline = obj.default.timelineData.map(el => {
            return {
              date: dateToMDY(new Date(el.time * 1000)),
              value: el.value[0]
            }
          })

          // Get the data from API to compare
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

              // Persist the keyword and error tuples on product groups
              if (result[i] == null) result[i] = []
              result[i].push({
                keyword: key,
                sse: sumOfSquaredErrors
              })

              if (i === NUM_OF_PRODUCT_GROUPS) {
                resolve(result)
              }
            }).catch(console.error)

        }).catch(console.error)
    }
  }
})

// Get the minimum error keyword
keywordsAndErrors.then(data => {
  _.each(data, (val, key) => {
    const minErrorTuple = _.minBy(val, 'sse')
    console.log("Product group: " + key)
    console.log("Minimum error keyword: " + minErrorTuple.keyword)
    console.log("All errors: " + JSON.stringify(val))
    console.log("\n")
  })
}, console.error)
