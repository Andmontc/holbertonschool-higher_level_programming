#!/usr/bin/node
const request = require('request');
const file = process.argv[2];
request(file, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
