#!/usr/bin/node

// this script converts from base 10 to base base
exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
