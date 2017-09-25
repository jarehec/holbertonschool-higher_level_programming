#!/usr/bin/node
// square object that inherits from rectangle
const Rectangle = require('./4-rectangle').Rectangle;
exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
};
