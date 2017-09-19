#!/usr/bin/node
// prints message x times
let x = parseInt(process.argv[2], 10);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
if (x > 0) {
  for (; x > 0; x--) {
    console.log('C is fun');
  }
}
