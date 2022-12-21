#!/usr/bin/node

exports.converter = function (base) {
  return function converterBase (number) {
    return number.toString(base);
  };
};
