#!/usr/bin/node

// this script reverses a list

exports.esrever = function (list) {
  let a = 0;
  let b;
  let c = list.length - 1;
  while (a <= c) {
    b = list[a];
    list[a] = list[c];
    list[c] = b;
    a = a + 1;
    c = c - 1;
  }
  return (list);
};
