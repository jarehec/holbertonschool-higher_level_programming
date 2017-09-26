#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
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
    console.log(res['title']);
  }
}
request(options, callback);
