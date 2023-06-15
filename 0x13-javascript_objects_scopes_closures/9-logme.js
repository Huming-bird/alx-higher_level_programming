#!/usr/bin/node

// this script prints the num of args printed and next arg

let a = 0;

exports.logMe = function (item) {
  console.log(a + ': ' + item);
  a++;
};
