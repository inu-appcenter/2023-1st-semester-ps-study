const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [M, N, H] = input.shift().split(" ").map(Number);

const dx = [-1, 1, 0, 0, 0, 0];
const dy = [0, 0, -1, 1, 0, 0];
const dz = [0, 0, 0, 0, -1, 1];

const graph = input.map((tomato) => tomato.split(" ").map(Number));

const tomatos = [...Array(H)].map((_) => []);

for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
    tomatos[i].push(graph.shift());
  }
}

const queue = [];

for (let [h, hTomatos] of tomatos.entries()) {
  for (let [n, nTomatos] of hTomatos.entries()) {
    for (let [m, mTomato] of nTomatos.entries()) {
      if (mTomato === 1) {
        queue.push([h, n, m]);
      }
    }
  }
}

for (let [z, y, x] of queue) {
  for (let i = 0; i < dx.length; i++) {
    let nz = z + dz[i];
    let ny = y + dy[i];
    let nx = x + dx[i];

    if (
      nz >= 0 &&
      nz < H &&
      ny >= 0 &&
      ny < N &&
      nx >= 0 &&
      nx < M &&
      tomatos[nz][ny][nx] === 0
    ) {
      tomatos[nz][ny][nx] = tomatos[z][y][x] + 1;
      queue.push([nz, ny, nx]);
    }
  }
}

let maxDay = 0;

for (let hTomatos of tomatos) {
  for (let nTomatos of hTomatos) {
    for (let mTomato of nTomatos) {
      if (mTomato === 0) {
        console.log(-1);
        return;
      }
      maxDay = Math.max(maxDay, mTomato);
    }
  }
}

console.log(maxDay - 1);
