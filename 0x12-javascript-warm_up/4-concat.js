#!/usr/bin/node
const args = process.argv.slice(2);
if (Array.isArray(args) && args[0] !== undefined && args[1] !== undefined) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log('Two arguments are required');
}
