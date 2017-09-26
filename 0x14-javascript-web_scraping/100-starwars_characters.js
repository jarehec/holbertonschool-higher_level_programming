#!/usr/bin/node
// prints all characters of a Star Wars movie
let request = require('request');
let options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  headers: {
    'format': 'json'
  }
};
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    let res = JSON.parse(body);
    for (let item in res['characters']) {
      request(res['characters'][item], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          let characters = JSON.parse(body);
          for (let i in characters) {
            if (i === 'name') {
              console.log(characters[i]);
            }
          }
        }
      });
    }
  }
}
request(options, callback);
