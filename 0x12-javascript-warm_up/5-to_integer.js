#!/usr/bin/node
/* print number */
const nb = process.argv[2];
if (isNaN(nb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nb);
}
