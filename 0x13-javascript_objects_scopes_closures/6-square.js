#!/usr/bin/node
const square = require('./4-rectangle');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        let rect = '';
        for (let j = 0; j < this.height; j++) {
          rect += c;
        }
        console.log(rect);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
