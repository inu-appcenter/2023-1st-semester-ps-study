const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const T = +input.shift();

for (let i = 0; i < T; i++) {
  let testCase = input.splice(0, 3);
  let [funcList, arrLength, arrList] = testCase;
  arrList = JSON.parse(arrList);
  let isReverse = false;
  let isError = false;

  for (let func of funcList) {
    if (func === "R") {
      isReverse = !isReverse;
    } else if (func === "D") {
      if (arrLength === "0" || arrList.length === 0) {
        isError = true;
        continue;
      }
      if (isReverse) {
        arrList.pop();
      } else if (!isReverse) {
        arrList.shift();
      }
    }
  }
  if (isReverse) {
    arrList.reverse();
  }

  isError ? console.log("error") : console.log(JSON.stringify(arrList));
}
