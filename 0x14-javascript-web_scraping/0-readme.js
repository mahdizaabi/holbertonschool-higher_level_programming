#!/usr/bin/node

const process = require('process');
var fs = require('fs');
fs.readFile(process.argv.splice(2)[0], 'utf-8', (err, data) => {
  if (err) { console.log(err); }
  console.log(data);
});
