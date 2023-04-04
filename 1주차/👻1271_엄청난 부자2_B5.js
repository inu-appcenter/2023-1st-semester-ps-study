const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split(" ");

const money = BigInt(input.shift());
const people = BigInt(input.shift());

console.log((money / people).toString());
console.log((money % people).toString());
