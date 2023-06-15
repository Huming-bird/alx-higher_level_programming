#!/usr/bin/node

// this script creates a rectangle object
const { dict } = require('./101-data.js');
const newDict = {};

for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const val = dict[key];

    if (val in newDict) {
      newDict[val].push(key);
    } else {
      newDict[val] = [key];
    }
  }
}

console.log(newDict);

