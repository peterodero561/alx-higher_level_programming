#!/usr/bin/node
const counter = process.argv[2];
if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < counter; i++) {
    console.log('C is fun');
  }
}
