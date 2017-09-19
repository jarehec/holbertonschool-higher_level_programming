#!/usr/bin/node
// prints the first argument passed to it
let i;
for (i in process.argv) {
}
i--;
if (i === 0) {
  console.log('No argument');
}
if (i > 0) {
  console.log(process.argv[2]);
}
