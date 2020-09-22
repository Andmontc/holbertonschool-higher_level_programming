#!/usr/bin/node
const request = require('request');
const data = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${data}`;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;
    chars.forEach(characters => {
      request(characters, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
