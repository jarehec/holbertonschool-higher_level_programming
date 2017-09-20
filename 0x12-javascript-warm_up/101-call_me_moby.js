#!/usr/bin/node
// executes a function x times
exports.callMeMoby = function (x, func) {
  for (; x > 0; x--) {
    func();
  }
};
