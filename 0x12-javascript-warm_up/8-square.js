#!/usr/bin/node
let size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
}
if (size > 0) {
  const square = 'X'.repeat(size);

  while (size > 0) {
    console.log(square);
    size--;
  }
}
