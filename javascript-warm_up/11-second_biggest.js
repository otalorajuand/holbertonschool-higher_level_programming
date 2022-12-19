#!/usr/bin/node

const arr = [0, 0];
let arrSorted;

for (let i = 2; i < process.argv.length; i++) {
  arr[i] = parseInt(process.argv[i]);
}
arrSorted = arr.sort();
arrSorted = arrSorted.reverse();

console.log(arrSorted[1]);
