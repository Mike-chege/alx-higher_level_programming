#!/usr/bin/node
// This script prints the number of movies where
// The character “Wedge Antilles” is present
const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = 18;

if (!apiUrl) {
  console.error('Usage: node script.js <API_URL>');
  process.exit(1);
}

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, body);
    return;
  }

  try {
    const filmsData = JSON.parse(body).results;
    const movies = filmsData.reduce((count, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        return count + 1;
      }
      return count;
    }, 0);

    console.log(`${movies}`);
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});
