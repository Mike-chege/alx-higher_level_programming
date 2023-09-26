#!/usr/bin/node
const process = require("process");
const fs = require("fs")

let filePath = process.argv[2];

fs.readFile(filePath, "utf8", function (err, data) {
	if (err != null) {
		console.log(err);
	} else {
		process.stdout.write(data);
	}
})
