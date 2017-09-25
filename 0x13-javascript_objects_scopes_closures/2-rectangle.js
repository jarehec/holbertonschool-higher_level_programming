#!/usr/bin/node
// Rectangle that sets width and height if w and h are greater than 0
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};
