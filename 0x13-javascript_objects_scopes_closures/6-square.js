#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (s) {
    super(s, s);
    this.side = s;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.side; i++) {
      let row = '';
      for (let j = 0; j < this.side; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
