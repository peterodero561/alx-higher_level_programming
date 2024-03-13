#!/usr/bin/node
const length = process.argv.length;
let max = 0;
let max2 = 0;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    const num = parseInt(process.argv[i]);
    if (num > max) {
      max2 = max; // Update max2 to the previous maximum value
      max = num; // Update max to the new maximum value
    } else if (num > max2 && num < max) {
      max2 = num; // Update max2 to the second maximum value
    }
  }
  console.log(max);
  console.log(max2);
}
