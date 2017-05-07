const _ = require('lodash')
const util = require('util')
const fs = require('fs')

let o = ""
fs.readFile('toformat.txt', 'utf-8', (err, data) => {
  fs.readFile('out.txt', 'utf-8', (err, dataout) => {
    outdata = dataout.replace(/\[/g, '').replace(/\]/g, '').replace(/\s/g, '').split(',')
    formatted = _.map(data.split('\n'), (line, i) => {
      o += util.format(line, outdata[i]) + "\n"
    })
    fs.writeFile('formatted.txt', o, (err,data) => {
      console.log(data)
    })
  });
})
