#!/usr/bin/node
// prints 'My number:' is the first arguemnt can be converted into an int
let i = parseInt(process.argv[2], 10);
if (isNaN(i)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + i);
}
