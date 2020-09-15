#!/usr/bin/node
/* */
const nb1 = process.argv[2];
const nb2 = process.argv[3];
function add (nb1, nb2) {
  if (isNaN(nb1) || isNaN(nb2)) {
    return (NaN);
  } else {
    return (parseInt(nb1) + parseInt(nb2));
  }
}
console.log(add(nb1, nb2));
