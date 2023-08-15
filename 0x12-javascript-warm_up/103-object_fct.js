#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// This function increments the integer value
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
