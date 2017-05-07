const axios = require('axios')
const _ = require('lodash')
const sys = require('sys')
const exec = require('child_process').exec
const fs = require('fs')
let child;


let res = ""
let inp = []
for(let i = 1; i <= 14; i++) {
axios.get("http://localhost:3000/products")
  .then(products => {
    axios.get("http://localhost:3000/stores")
      .then(stores => {
        _.each(products.data, product => {
          _.each(stores.data, store => {
              const day = i < 10 ? "0" + i : "" + i;
              const date = i < 10 ? ("0" + i + ".02.2017") : ("" + i + ".02.2017")
              if (!(/\./.exec(product.price))) {
                product.price = product.price + ".0"
              }
              inp.push("[201702" + day + "," + store.id + "," + product.id + "," + product.price + "," + store.city_id + "]")
              res += "Store" + store.id + "|Product" + product.id + "|" + date + "|" + "%s" + "\n"
          })
        })
      })
      .then(() => {
        if(i === 14) {
          fs.writeFile('toformat.txt', res, 'utf-8', (err, data) => {
            if(err) console.log(err)
          });
          fs.writeFile('inp.txt', '[' + inp.join(',') + ']', 'utf-8', (err, data) => {
            if(err) console.log(err)
          });
          console.log("writing..")
          // child = exec("python ../tensorflow-ml/predict.py " + inp, function (error, stdout, stderr) {
          //   console.log(JSON.parse(stdout))
          //   // const forecast = JSON.parse(stdout)[0].predict_sales_quantity
          //   // res += "Store" + store.id + "|Product" + product.id + "|" + date + "|" + forecast + "\n"
          // });
        }
      })

  })

}
