#!/usr/bin/node
let a = process.argv.length;
if (a === 2) {
  console.log('No argument');
} else if (a === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
