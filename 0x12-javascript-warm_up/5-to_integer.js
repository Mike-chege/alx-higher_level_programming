#!/usr/bin/node
// Prints My number: <first argument converted in integer>
const value = Math.floor(Number(process.argv[2]));
console.log(isNaN(value) ? 'Not a number' : `My number: $(value}`);
