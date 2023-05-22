const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => +v);
const n = input.shift();

const getAverage = (arr) => {
  return `${Math.round(arr.reduce((acc, cur) => acc + cur, 0) / n)}`;
};

const getMedian = (arr) => {
  const sorted = arr.sort((a, b) => a - b);
  const mid = Math.floor(n / 2);
  return sorted[mid];
};

const getMode = (arr) => {
  const mapObj = new Map();
  let max = 1;

  arr.map((num) => {
    mapObj.get(num);
    if (mapObj.has(num)) {
      mapObj.set(num, mapObj.get(num) + 1);
      max = Math.max(max, mapObj.get(num));
    } else {
      mapObj.set(num, 1);
    }
  });

  const modeArr = [];

  for (const [key, value] of mapObj) {
    value === max && modeArr.push(key);
  }

  sortedModeArr = modeArr.sort((a, b) => a - b);

  return sortedModeArr.length > 1 ? sortedModeArr[1] : sortedModeArr[0];
};

const getRange = (arr) => {
  return Math.max(...arr) - Math.min(...arr);
};

console.log(getAverage(input));
console.log(getMedian(input));
console.log(getMode(input));
console.log(getRange(input));
