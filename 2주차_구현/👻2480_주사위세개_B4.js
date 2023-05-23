const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split(" ")
  .map((v) => +v);

if (input[0] === input[1] && input[1] === input[2]) {
  console.log(10000 + input[0] * 1000);
} else if (
  input[0] === input[1] ||
  input[1] === input[2] ||
  input[0] === input[2]
) {
  if (input[0] === input[1]) {
    console.log(1000 + input[1] * 100);
  } else if (input[1] === input[2]) {
    console.log(1000 + input[1] * 100);
  } else if (input[0] === input[2]) {
    console.log(1000 + input[2] * 100);
  }
} else {
  console.log(Math.max(input[0], input[1], input[2]) * 100);
}
