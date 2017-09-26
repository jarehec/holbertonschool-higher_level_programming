#!/usr/bin/node
// square class that inherits from square
exports.Square = function Square (size) {
  Square.prototype.charPrint = function (c = 'X') {
    for (let i = size; i > 0; i--) {
      console.log(c.repeat(size));
    }
  };
};
