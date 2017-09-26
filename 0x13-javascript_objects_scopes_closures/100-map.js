#!/usr/bin/node
// computes a new array
let ar = require('./100-data').list;
let newAr = ar.map(function (x, idx) {
  return x * idx;
});
console.log(ar);
console.log(newAr);
