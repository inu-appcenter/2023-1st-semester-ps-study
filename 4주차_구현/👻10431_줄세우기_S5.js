const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const P = input.shift();

const test = input.map((testCase) =>
  testCase.split(" ").map((height) => +height)
);

test.forEach((testCase) => {
  let T = testCase.shift();
  let line = [];
  let tempo = 0;

  testCase.forEach((height) => {
    let tallerIndex = line.findIndex((e) => e > height);
    if (tallerIndex !== -1) {
      for (let i = line.length; i > tallerIndex; i--) {
        line[i] = line[i - 1];
        tempo++;
      }
      line[tallerIndex] = height;
    } else {
      line.push(height);
    }
  });
  console.log(T, tempo);
});
