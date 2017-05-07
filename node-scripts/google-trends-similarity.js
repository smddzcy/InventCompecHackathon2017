const googleTrends = require('google-trends-api')

const apiEndpoint = 'https://wowteam-inventcompechackathon.herokuapp.com/inventory_positions/sales_quantity?start_date=%s&end_date=%s&product_group=%s';
let key = 'battaniye'

const dateToMDY = (date) => {
  const d = date.getDate()
  const m = date.getMonth() + 1
  const y = date.getFullYear()
  return '' + (d <= 9 ? '0' + d : d) + '.' + (m <= 9 ? '0' + m : m) + '.' + y
}

googleTrends.interestOverTime({
  keyword: key,
  startTime: new Date('2015-01-01'),
  endTime: new Date(Date.now()),
  geo: 'TR'
}).then((res) => {
  const obj = JSON.parse(res)

  // Get timeline data of keyword and transform for it to a more usable one
  const timeline = obj.default.timelineData.map(el => {
    return {
      date: dateToMDY(new Date(el.time * 1000)),
      value: el.value[0]
    }
  })


  timeline.forEach(el => {

  })
}).catch((err) => {
  console.log(err)
})
