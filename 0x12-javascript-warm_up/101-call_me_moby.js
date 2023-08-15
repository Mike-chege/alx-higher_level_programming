#!/usr/bin/node
// This function executes x times a function
exports.callMeMoby = function (x, theFunction) {
  for (let val = 0; val < x; val++) theFunction();
};
