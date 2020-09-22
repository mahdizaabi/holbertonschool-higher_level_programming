#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';
const filter = process.argv[2];
const url = endpoint + filter;
const listx = [];
request(url, function (error, response, body) {
  if (error) { return console.log(error); } else {
    for (const star of JSON.parse(body).characters) {
      listx.push(star);
    }
  }
  for (let k = 0; k < listx.length; k++) {
    request(listx[k], function (e, r, b) {
      if (e) { return console.log(e); }
      console.log(JSON.parse(b).name);
    });
  }
});
