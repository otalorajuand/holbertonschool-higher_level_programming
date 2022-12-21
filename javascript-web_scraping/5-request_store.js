#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  let content;
  if (error) {
    console.log(error);
  } else {
    content = body;
  }

  const fs = require('fs');
  fs.writeFile(process.argv[3], content, err => {
    if (err) {
      console.error(err);
    }
  });
});
