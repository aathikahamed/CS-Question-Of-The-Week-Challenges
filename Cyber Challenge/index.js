const string = "👇🏾";

console.log([...string]);
console.log([...string].length);
console.log(string.length);

if (typeof string !== "string") {
  console.log("string must be a string");
} else if ([...string].length > 5) {
  console.log("string too long");
} else if (string.length <= 5) {
  console.log("string too short");
} else {
  console.log(`${process.env}`);
}
