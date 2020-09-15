#!/usr/bin/node
/* print a square */
const count = process.argv[2];
if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
}
