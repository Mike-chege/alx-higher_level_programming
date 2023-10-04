// This script fetches and lists the title for all movies
// By using
// This URL: https://swapi-api.alx-tools.com/api/films/?format=json

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  $('UL#list_movies').append(...data.result.map(movie => `<lii>${movie.title}</li>`));
});
