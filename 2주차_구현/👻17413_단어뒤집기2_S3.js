const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const tags = input.match(/<[a-z ]+>/g) ?? [];

const words = input.split(/<[a-z ]+>/);

const reversedWords = words.map((word) =>
  word
    .split(" ")
    .map((v) => [...v].reverse().join(""))
    .join(" ")
);

const answer =
  tags.map((tag, i) => reversedWords[i] + tag).join("") +
  reversedWords[reversedWords.length - 1];

console.log(answer);
