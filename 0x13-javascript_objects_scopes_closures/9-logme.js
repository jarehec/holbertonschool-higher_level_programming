#!/usr/bin/node
// prints the number of arguments and argument value
let funcCalls = 0;
exports.logMe = function (item) {
  console.log(funcCalls + ': ' + item);
  funcCalls++;
};
