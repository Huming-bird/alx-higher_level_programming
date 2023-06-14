#!/usr/bin/node

// this script finds the factorial of any number

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
let n;

n = parseInt(process.argv[2]);
console.log(factorial(n));
