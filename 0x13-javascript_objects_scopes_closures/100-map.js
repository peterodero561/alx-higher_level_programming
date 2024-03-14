#!/usr/bin/node
// Import the initial list from 100-data.js
const { list } = require('./100-data');

// Compute the new array using map
const computedList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(computedList);
