#!/usr/bin/node
// finds the second biggest int in a list of args
let i;
let max = 0;
let pent = 0;
for (i in process.argv) {
}
if (i === 0 || i === 1) {
  console.log('0');
} else {
  for (let x = 2; x <= i; x++) {
    if (process.argv[x] > max) {
      max = process.argv[x];
    }
  }
  for (let x = 2; x <= i; x++) {
    if (process.argv[x] > pent && process.argv[x] < max) {
      pent = process.argv[x];
    }
  }
  console.log(pent);
}
