#!/usr/bin/node
// This script that prints a square
const length = Math.floor(Number(process.argv[2]));
if (isNaN(length)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < length; i++) {
    let width = '';
    for (let j = 0; j < length; j++) width += 'X';
    console.log(width);
  }
}
