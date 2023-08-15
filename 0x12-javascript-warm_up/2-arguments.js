#!/usr/bin/node
const nArgs = process.argv.length - 3;

if (nArgs < 3)
{
	console.log("No arguments");
}
else if (nArgs === 3)
{
	console.log("Argument found");
}
else
{
	console.log("Arguments found");
}
