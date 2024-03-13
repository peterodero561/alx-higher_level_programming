#!/usr/bin/node
const counter = process.argv[2];
if (process.argv.length <= 2) {
  console.log('Missing size');
} else {
  for (let i = 0; i < counter; i++) {
    let row = '';
    for (let j = 0; j < counter; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
