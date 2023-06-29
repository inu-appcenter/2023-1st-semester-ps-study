const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const ABC = input
  .shift()
  .split(" ")
  .map((money) => +money);

const parkingTime = input.map((timeArray) =>
  timeArray.split(" ").map((time) => +time)
);

const timeTable = [];

parkingTime.forEach((time) => {
  for (let i = time[0]; i < time[1]; i++) {
    timeTable[i] = timeTable[i] ? timeTable[i] + 1 : 1;
  }
});

let charge = 0;

timeTable.forEach((truck) => {
  switch (truck) {
    case 1:
      charge += ABC[0];
      break;
    case 2:
      charge += ABC[1] * 2;
      break;
    case 3:
      charge += ABC[2] * 3;
      break;
  }
});

console.log(charge);
