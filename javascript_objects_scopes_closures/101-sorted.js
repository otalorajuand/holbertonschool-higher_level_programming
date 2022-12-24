#!/usr/bin/node
const dict = require('./101-data').dict;

const new_dict = {};
for (let i=0; i<dict.length; i++) {
    if (new_dict[dict[i]]) {
        new_dict[dict[i]];
    } else {
        new_dict[dict[i]] = []
    }
}