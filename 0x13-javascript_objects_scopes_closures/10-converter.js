#!/usr/bin/node
/* This function converts a number from
 * base 10 to another base passed as argument
 */
exports.converter = function converter (base) {
  if (typeof converter.Num === 'undefined') {
    converter.Num = base;
    return converter;
  } else {
    return parseInt(converter.Num, base);
  }
};
