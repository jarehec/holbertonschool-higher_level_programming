#!/usr/bin/node
// returns a function to convert a number from base 10 to another base
exports.converter = function (base = 10) {
  return function (num) {
    return num.toString(base);
  };
};
