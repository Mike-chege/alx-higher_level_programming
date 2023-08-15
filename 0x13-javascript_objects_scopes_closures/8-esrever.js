#!/usr/bin/node
// This function returns the reversed version of a list
exports.esrever = function (list) {
  let reversed = [];
  let val;
  for (val = list.length - 1; val >= 0; val--) {
    reversed.push(list[val]);
  }
  return reversed;
};
