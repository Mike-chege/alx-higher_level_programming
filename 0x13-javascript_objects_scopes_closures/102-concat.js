#!/usr/bin/node
// This script concats 2 files
const fs = require('fs');
const num1 = fs.readFileSync(process.argv[2], 'utf8');
const num2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], num2 + num2)
