#!/usr/bin/node

// this script creates a square object

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row = row + c;
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
