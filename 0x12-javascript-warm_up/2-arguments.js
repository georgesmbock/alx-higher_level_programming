#!/usr/bin/node
const args = process.argv.slice(1);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argumment found');
} else {
  console.log('Arguments found');
}