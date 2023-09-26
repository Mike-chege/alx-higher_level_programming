#!/usr/bin/node
// This script computes the number of tasks
// Completed by user id
const process = require('process');
const request = require('request');

const url = process.argv[2];
let tasks;
let completed;

request(url, function (error, response, body) {
  if (error == null) {
    tasks = JSON.parse(body);
    completed = {};
    tasks.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
