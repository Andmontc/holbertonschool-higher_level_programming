#!/usr/bin/node
const loop = parseInt(process.argv[2]);
let i = 0;
if (loop) {
  while (i < loop) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
