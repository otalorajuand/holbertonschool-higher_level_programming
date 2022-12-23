#!/usr/bin/node
const list = require('./100-data').list;
const list2 = list.map((num, index) => {
  return num * index;
});
console.log(list);
console.log(list2);
