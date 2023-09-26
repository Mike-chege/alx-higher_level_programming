#!/usr/bin/node
// This script gets the contents of a webpage
// And stores it in a file
const process = require('process');
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error == null) {
    fs.writeFile(filePath, body, 'utf8', function (err, data) {
      if (err != null) {
        console.log(error);
      }
    });
  }
});
