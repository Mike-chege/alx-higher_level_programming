#!/usr/bin/node
// Defining a function to add two numbers
function add (a, b) {
  return a + b;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
