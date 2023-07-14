const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);
const graph = [...Array(n + 1)].map(() => []);

for (let i = 1; i < n; i++) {
  let [node1, node2] = input[i].split(" ").map(Number);
  graph[node1].push(node2);
  graph[node2].push(node1);
}

const queue = [];
const check = Array(n + 1).fill(0);

check[1] = 1;

for (let next of graph[1]) {
  // 1이 시작이고 child 노드를 넣고 check[child]엔 부모노드의 값을 넣어준다.
  check[next] = 1;
  queue.push(next);
}

while (queue.length) {
  const current = queue.shift();
  for (let next of graph[current]) {
    if (!check[next]) {
      check[next] = current; // 부모 노드의 값을 넣어준다.
      queue.push(next);
    }
  }
}

console.log(check.slice(2).join("\n"));
