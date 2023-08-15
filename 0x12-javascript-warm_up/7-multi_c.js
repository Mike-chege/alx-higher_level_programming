#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  const x = parseInt(arg);

  if (x >= 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Number of occurrences must be non-negative');
  }
} else {
  console.log('Missing number of occurrences');
}
