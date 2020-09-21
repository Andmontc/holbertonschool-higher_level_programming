#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numocur = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      numocur += 1;
    }
  }
  return (numocur);
};
