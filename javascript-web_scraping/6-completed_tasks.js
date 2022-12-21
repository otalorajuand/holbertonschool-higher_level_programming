#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  let content;
  if (error) {
    console.log(error);
  } else {
    content = JSON.parse(body);
  }

  const results = { 1: 0 };
  for (let i = 0; i < content.length; i++) {
    if (content[i].completed) {
      if (!(content[i].userId in results)) {
        results[content[i].userId] = 0;
      }
      results[content[i].userId]++;
    }
  }
  console.log(results);
});
