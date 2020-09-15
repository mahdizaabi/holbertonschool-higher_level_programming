#!/usr/bin/node
/* factorial function */
function factorial (nb) {
  if (isNaN(nb) || nb === 1) {
    return (1);
  } else {
    return (nb * factorial(nb - 1));
  }
}
const nb = process.argv[2];
console.log(factorial(parseInt(nb)));
