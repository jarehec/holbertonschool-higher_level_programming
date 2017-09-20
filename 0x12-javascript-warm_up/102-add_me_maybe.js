#!/usr/bin/node
// increments x and executes a function
exports.addMeMaybe = function (x, func) {
  x++;
  func(x);
};
