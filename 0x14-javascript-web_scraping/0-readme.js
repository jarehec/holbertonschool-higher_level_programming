#!/usr/bin/node
// reads and prints the content of a file
let fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  process.stdout.write(data);
});
