#!/usr/bin/node
// This script prints the title of a Star Wars movie
// Where the episode number matches a given integer
const process = require('process');
const request = require('request');

const episode = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
let starwars;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    starwars = JSON.parse(body);
    console.log(starwars['title']);
  }
});
