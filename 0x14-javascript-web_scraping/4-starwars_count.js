#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body).results;
    console.log(result.reduce((num, films) => {
      films.characters.forEach(element => {
        if (element.includes('18')) {
          num++;
        }
      });
      return num;
    }, 0));
  }
});
