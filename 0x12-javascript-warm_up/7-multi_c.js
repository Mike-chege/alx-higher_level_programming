#!/usr/bin/node
// This script that prints x times “C is fun”
const val = Math.floor(Number(process.argv[2]));
if (isNaN(val)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < val; x++) {
    console.log('C is fun');
  }
}
