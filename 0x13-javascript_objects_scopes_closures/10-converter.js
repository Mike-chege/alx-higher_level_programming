#!/usr/bin/node
/* This function converts a number from
 * base 10 to another base passed as argument
 */
exports.converter = function (base) { return val => val.toString(base); };
