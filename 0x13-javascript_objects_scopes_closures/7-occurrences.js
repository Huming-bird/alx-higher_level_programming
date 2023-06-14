#!/usr/bin/node

// this script returns num of occurrence of an elem in a list

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      num = num + 1;
    }
  }
  return (num);
};
