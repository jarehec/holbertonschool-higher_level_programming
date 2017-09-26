#!/usr/bin/node
// reverses list items
exports.esrever = function (list) {
  let revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
