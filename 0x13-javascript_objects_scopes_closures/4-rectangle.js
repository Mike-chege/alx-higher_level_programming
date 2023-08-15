#!/usr/bin/node
// A class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (printC = 'X') {
    let val;
    let num;
    let make = '';
    for (val = 0; val < this.height; val++) {
      if (val > 0) {
        make += '\n';
      }
      for (num = 0; num < this.width; num++) {
        make += printC;
      }
    }
    console.log(make);
  }

  rotate () {
    let i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
