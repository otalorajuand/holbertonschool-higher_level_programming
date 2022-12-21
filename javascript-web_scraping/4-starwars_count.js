#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  let results;
  if (error) {
    console.log(error);
  } else {
    results = JSON.parse(body).results;
  }
  let counter = 0;
  for (let i = 0; i < results.length; i++) {
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j].includes('18')) {
        counter++;
      }
    }
  }
  console.log(counter);
});
