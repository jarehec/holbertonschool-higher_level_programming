#!/usr/bin/node
// computes the number of tasks completed by user id
let request = require('request');
let idList = [];
let dict = {};
let options = {
  url: process.argv[2],
  headers: {
    'format': 'json'
  }
};

function countEle (list, searchElement) {
  let count = 0;
  for (let element in list) {
    if (searchElement === list[element]) {
      count++;
    }
  }
  return count;
}
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let res = JSON.parse(body);
    for (let item in res) {
      if (res[item]['completed'] === true) {
        idList.push(res[item]['userId']);
        dict[res[item]['userId']] = countEle(idList, res[item]['userId']);
      }
    }
  }
  console.log(dict);
}
request(options, callback);
