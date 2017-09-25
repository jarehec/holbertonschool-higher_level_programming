#!/usr/bin/node
// defining double and rotate methods for rectangle
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    this.print = function () {
      for (let i = h; i > 0; i--) {
        console.log('X'.repeat(w));
      }
    };
    this.rotate = function () {
      let tmp = h;
      h = w;
      w = tmp;
    };
    this.double = function () {
      h *= 2;
      w *= 2;
    };
  }
};
