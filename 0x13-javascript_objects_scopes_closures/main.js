#!/usr/bin/node

// this script creates a rectangle object

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Rectangle;

const squ = new Square(3);
console.log(squ.width);

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();
