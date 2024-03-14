#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const reverse = [];
  let j = 0;
  for (let i = len - 1; i >= 0; i--) {
    reverse[j] = list[i];
    j += 1;
  }
  return reverse;
};
