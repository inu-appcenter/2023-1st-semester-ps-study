const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = Number(input[0]);
const [person1, person2] = input[1].split(" ").map(Number);
const m = Number(input[2]);
const graph = [...Array(n + 1)].map((e) => []);

for (let i = 3; i < m + 3; i++) {
  let [parent, child] = input[i].split(" ").map(Number);
  graph[parent].push(child);
  graph[child].push(parent);
}

const bfs = (graph, startNode, targetNode) => {
  const visited = [];
  let needVisit = [[startNode, 0]];

  while (needVisit.length !== 0) {
    const [node, count] = needVisit.shift();
    if (node === targetNode) return count;
    if (!visited.includes(node)) {
      visited.push(node);
      let nodes = graph[node].map((e) => [e, count + 1]);
      needVisit = [...needVisit, ...nodes];
    }
  }
  return -1;
};

console.log(bfs(graph, person1, person2));
