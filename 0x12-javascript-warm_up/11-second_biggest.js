#!/usr/bin/node
const arg = process.argv.length;
if (arg <= 3) {
  console.log(0);
} else {
  const maxnum = process.argv.slice(2);
  maxnum.sort((a, b) => a - b);
  console.log(maxnum[maxnum.length - 2]);
}
