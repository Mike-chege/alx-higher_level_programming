#!/usr/bin/node
// This script computes and prints a factorial
function factorial (val) {
  // Function definition
  return val === 0 || isNaN(val) ? 1 : val * factorial(val - 1);
}
// Printing the output
console.log(factorial(Number(process.argv[2])));
