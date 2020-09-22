#!/usr/bin/node

const request = require('request');
let count = 0;
const ar = [];
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.error('error:', err); }
  for (const i of JSON.parse(body).results) {
    ar.push(i.characters);
  }
  for (let i = 0, len = ar.length; i < len; i++) {
    for (let j = 0, len2 = ar[i].length; j < len2; j++) {
      if (ar[i][j] === 'https://swapi-api.hbtn.io/api/people/18/') { count++; }
    }
  }
  console.log(count);
});
