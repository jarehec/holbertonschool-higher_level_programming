#!/usr/bin/node
// prints a message based on the number of arguments
let i;
for (i in process.argv) {
}
i--;
if (i === 0) {
  console.log('No argument');
}
if (i === 1) {
  console.log('Argument found');
}
if (i > 1) {
  console.log('Arguments found');
}
