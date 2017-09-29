// replaces the header with the character name https://swapi.co/api/people/5/?format=json
$.get('https://swapi.co/api/people/5/?format=json', function (body) {
  $('DIV#character').text(body['name']);
});
