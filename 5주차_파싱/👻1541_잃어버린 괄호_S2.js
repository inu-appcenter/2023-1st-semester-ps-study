const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
const input = fs.readFileSync(filePath).toString();

const List = input.split("-").map((str) =>
  str
    .split("+")
    .map(Number)
    .reduce((acc, cur) => acc + cur, 0)
);

console.log(List[0] * 2 - List.reduce((acc, cur) => acc + cur, 0));
