#!/usr/bin/node
// prints 'lang  is desc'
let langs = ['C', 'Python', 'Javascript'];
let desc = ['fun', 'cool', 'amazing'];
let i;
for (i in langs) {
  console.log(langs[i] + ' is ' + desc[i]);
}
