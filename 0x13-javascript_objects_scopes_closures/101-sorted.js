#!/usr/bin/node
// This script imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence
const dict = require('./101-data.js').dict;
let myDict = {};
for (let key in dict) {
  if (myDict[dict[key]] === undefined) {
    myDict[dict[key]] = [key];
  } else {
    myDict[dict[key]].push(key);
  }
}
// Printing the new dictionary
console.log(myDict);
