const fs = require('fs')
const _ = require('lodash')

fs.readFile('formatted.txt', 'utf-8', (err, data) => {
  const sumOfSalesQuantities = _.map(data.trim().split('\n'), line => parseFloat(_.last(line.split('|'))))
  console.log(_.sum(sumOfSalesQuantities))
})
