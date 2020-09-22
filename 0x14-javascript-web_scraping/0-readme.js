#!/usr/bin/node

const process = require('process');
const file = process.argv[2];
var fs = require('fs');
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) { console.log(err); }
  console.log(data);
});
