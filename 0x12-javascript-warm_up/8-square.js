#!/usr/bin/node
// prints a square x size
let x = parseInt(process.argv[2], 10);
const i = x;
if (isNaN(x)) {
  console.log('Missing size');
}
for (; x > 0; x--) {
  console.log('X'.repeat(i));
}
