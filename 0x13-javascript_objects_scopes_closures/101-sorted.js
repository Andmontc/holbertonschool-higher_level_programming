#!/usr/bin/node
const dict = require('./101-data').dict;
const ndict = {};
for (const k in dict) {
  if (!ndict[dict[k]]) {
    ndict[dict[k]] = [k];
  } else {
    ndict[dict[k]].push(k);
  }
}
console.log(ndict);
