#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length - 1;
  const rev = [];
  while (size >= 0) {
    rev.push(list[size]);
    size--;
  }
  return (rev);
};
