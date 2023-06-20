const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const numberOfTest = input.shift();

const dx = [-2, -1, 1, 2, 2, 1, -1, -2];
const dy = [1, 2, 2, 1, -1, -2, -2, -1];

for (let i = 0; i < numberOfTest; i++) {
  let testCase = input.splice(0, 3);
  let [l, start, end] = testCase;
  l = +l;
  start = start.split(" ").map((v) => +v);
  end = end.split(" ").map((v) => +v);
  let visited = Array.from(Array(l), () => Array(l).fill(0));

  const queue = [start];

  while (queue.length) {
    [x, y] = queue.shift();
    if (x === end[0] && y === end[1]) {
      console.log(visited[x][y]);
      break;
    }
    for (let i = 0; i < 8; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (nx >= 0 && nx < l && ny >= 0 && ny < l && !visited[nx][ny]) {
        visited[nx][ny] = visited[x][y] + 1;
        queue.push([nx, ny]);
      }
    }
  }
}
