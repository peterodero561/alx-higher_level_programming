#!/usr/bin/node
exports.converter = function (base) {
  return function (decimalNumber) {
    if (base < 2 || base > 36) {
      throw new Error('Invalid base (must be between 2 and 36).');
    }
    return decimalNumber.toString(base);
  };
};
