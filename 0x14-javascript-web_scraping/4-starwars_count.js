#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present
let request = require('request');
let searchEle = 'https://swapi.co/api/people/18/';
let count = 0;
let options = {
  url: process.argv[2],
  headers: {
    'format': 'json'
  }
};
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let res = (JSON.parse(body));
    for (let item in res['results']) {
      if (res['results'][item]['characters'].indexOf(searchEle) !== -1) {
        count++;
      }
    }
  }
  console.log(count);
}
request(options, callback);
