#!/usr/bin/node
// prints the addition of two integers
function add (a, b) {
  console.log(a + b);
}
let x = parseInt(process.argv[2], 10);
let y = parseInt(process.argv[3], 10);
if (isNaN(x) || isNaN(y)) {
  console.log('NaN');
} else {
  add(x, y);
}
