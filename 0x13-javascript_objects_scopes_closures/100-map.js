#!/usr/bin/node
// This script imports an array and computes a new array
const list = require('./100-data.js').list;
console.log(list);
// Printing both the initial list and the new list
console.log(list.map((item, index) => item * index));
