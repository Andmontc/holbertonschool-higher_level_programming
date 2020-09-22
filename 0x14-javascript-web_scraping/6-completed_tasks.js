#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const task = JSON.parse(body);
    const taskcompleted = {};
    task.forEach((todo) => {
      if (todo.completed && taskcompleted[todo.userId] === undefined) {
        taskcompleted[todo.userId] = 1;
      } else if (todo.completed) {
        taskcompleted[todo.userId] += 1;
      }
    });
    console.log(taskcompleted);
  }
});
