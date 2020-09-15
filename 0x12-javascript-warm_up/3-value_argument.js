#!/usr/bin/node
const arg = process.argv.length;
if (arg === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
