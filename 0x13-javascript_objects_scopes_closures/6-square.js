#!/usr/bin/node
// square class that inherits from square
const quare = require('./5-square').Square;
exports.Square = function Square (size) {
  quare.call(this, size);
  Square.prototype.charPrint = function (c = 'X') {
    for (let i = size; i > 0; i--) {
      console.log(c.repeat(size));
    }
  };
};
