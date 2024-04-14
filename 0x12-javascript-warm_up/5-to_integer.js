#!/usr/bin/node
const array = process.argv;
const numConvert = parseInt(array[2], 10);
if (isNaN(numConvert)) {
	console.log('Not a number');
} else {
	console.log(`My number: ${numConvert}`);
}




