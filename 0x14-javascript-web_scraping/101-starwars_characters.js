#!/usr/bin/node
// This script prints all characters
// Of a Star Wars movie
const process = require('process');
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

let characters;

request(url, function (error, response, body) {
  if (error == null) {
    characters = JSON.parse(body).characters;
    starCharacters(characters, 0);
  }
});

function starCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error == null) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        starCharacters(characters, index + 1);
      }
    }
  });
}
