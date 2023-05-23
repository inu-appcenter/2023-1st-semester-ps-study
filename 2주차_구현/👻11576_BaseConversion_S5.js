const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [first, second, third] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const firstArr = first
  .trim()
  .split(" ")
  .map((v) => +v);
const thridArr = third
  .trim()
  .split(" ")
  .map((v) => +v)
  .reverse();

aJinbeob = firstArr[0];
bJinbeob = firstArr[1];

let ten = 0;

for (let i = 0; i < thridArr.length; i++) {
  ten += thridArr[i] * Math.pow(aJinbeob, i);
}

let result = [];

while (Math.floor(ten / bJinbeob)) {
  result.push(ten % bJinbeob);
  ten = Math.floor(ten / bJinbeob);
}
result.push(ten);

result.reverse();

console.log(result.join(" "));
