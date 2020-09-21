#!/usr/bin/node
const dict = require('./101-data').dict;
let ndict = {};
for (let k in dict) {
  if (!ndict[dict[k]]) {
    ndict[dict[k]] = [k];
  } else {
    ndict[dict[k]].push(k);
  }
}
console.log(ndict);
