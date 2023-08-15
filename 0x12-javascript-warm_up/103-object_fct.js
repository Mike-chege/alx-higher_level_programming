#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// Adding a new function to increment the value
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
