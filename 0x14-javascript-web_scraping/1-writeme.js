#!/usr/bin/node
// This script writes a string to a file
const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  }
});
