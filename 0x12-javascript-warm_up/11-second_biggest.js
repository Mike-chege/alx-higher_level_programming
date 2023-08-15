#!/usr/bin/node
/* This script searches the second biggest
 * integer in the list of arguments
 */
if (process.argv.length <= 3) {
  // Prints 0 if args are NULL or 1
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((num1, num2) => num1 - num2);
  console.log(args[args.length - 2]);
}
