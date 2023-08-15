#!/usr/bin/node
/* This script prints a message depending
 * on the number of arguments passed
 */
const num = process.argv.length - 2;
if (num === 0) {
  console.log("No argument");
} else if (num === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
