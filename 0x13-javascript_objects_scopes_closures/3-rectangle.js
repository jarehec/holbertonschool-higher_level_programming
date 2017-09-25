#!/usr/bin/node
// defining print() method to print rectangle using 'X'
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    this.print = function () {
      for (let i = h; i > 0; i--) {
        console.log('X'.repeat(w));
      }
    };
  }
};
