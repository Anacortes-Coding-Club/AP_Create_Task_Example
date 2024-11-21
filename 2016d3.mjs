
import { readFileSync } from 'fs';

// Reading the file synchronously
const data = readFileSync('./input3.txt', { encoding: 'utf8', flag: 'r' });

// Displaying the file content
// console.log(data);

let newdata = data.split("\n").filter(Boolean).map((line) => line.split(/\s+/).map((str) => Number.parseInt(str))).map(nums => nums.slice(1)).filter((nums) => Math.max(...nums) < nums[(nums.indexOf(Math.max(...nums))+1) % 3] + nums[(nums.indexOf(Math.max(...nums))+2) % 3]).length
console.log(newdata)