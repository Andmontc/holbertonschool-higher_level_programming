#!/usr/bin/node
const request = require('request');
const data = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${data}`;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
