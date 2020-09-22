#!/usr/bin/node
exports.converter = function (base) {
  return v => v.toString(base);
};
