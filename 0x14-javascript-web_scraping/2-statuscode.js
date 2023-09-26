#!/usr/bin/node
// This script displays the status code of a GET request
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
