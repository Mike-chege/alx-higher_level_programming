#!/usr/bin/node
// This script prints the number of movies where
// The character “Wedge Antilles” is present
const process = require('process');
const request = require('request');

const url = process.argv[2];
let starwars;

request(url, function (error, response, body) {
  if (error == null) {
    starwars = JSON.parse(body).results;
    console.log(starwars.reduce((num, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? num + 1
        : num;
    }, 0));
  }
});
