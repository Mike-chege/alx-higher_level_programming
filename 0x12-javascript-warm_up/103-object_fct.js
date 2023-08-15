#!/usr/bin/node
// Adding a new function to increment the current value
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
