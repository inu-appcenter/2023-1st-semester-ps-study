const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [num, leftNumberString] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");
const leftNumberList = leftNumberString
  .trim()
  .split(" ")
  .map((v) => +v);

const result = new Array(Number(num)).fill(0);

leftNumberList.forEach((leftNumber, height) => {
  let leftPeopleCount = 0;
  for (let index = 0; index < result.length; index++) {
    if (leftPeopleCount === leftNumber) {
      let pointer = index;
      while (!!result[pointer]) {
        pointer++;
      }
      result[pointer] = height + 1;
      // leftPeopleCount++;
      break;
    } else if (result[index] === 0) {
      leftPeopleCount++;
    }
  }
});

console.log(result.join(" "));
