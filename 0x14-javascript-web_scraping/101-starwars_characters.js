#!/usr/bin/node
// prints all characters of a Star Wars movie
let request = require('request');
let options = {
  url: 'https://swapi.co/api/films/' + process.argv[2],
  headers: {
    'format': 'json'
  }
};
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let res = JSON.parse(body);
    for (let item of res['characters']) {
      request(item, function (error, response, body) {
        if (error) { console.log(error); } else {
          console.log(JSON.parse(body)['name']);
        }
      });
    }
  }
}
request(options, callback);
