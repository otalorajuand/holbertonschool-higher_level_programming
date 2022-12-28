#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/people/', function (error, response, body) {
  let content;
  if (error) {
    console.log(error);
  } else {
    content = JSON.parse(body).results;
  }

  for (let i=0; i<content.length; i++) {
    person = content[i];
    for (const film in person.films) {
      if (film.includes(process.argv[2])) {
        console.log(person.name);
        break;
      }
    }
  }
});
