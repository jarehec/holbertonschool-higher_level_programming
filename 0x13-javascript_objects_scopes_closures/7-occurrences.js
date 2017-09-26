#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let element in list) {
    if (searchElement === list[element]) {
      count++;
    }
  }
  return count;
};
