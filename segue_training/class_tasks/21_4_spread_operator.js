console.log("🔹 Spread Operator Example");

const fruits = ["apple", "banana"];
const moreFruits = ["mango", ...fruits, "orange"]; // Spreading fruits into new array

console.log("Original:", fruits);           // ["apple", "banana"]
console.log("After Spread:", moreFruits);   // ["mango", "apple", "banana", "orange"]

// Spread in object
const user = { name: "John" };
const updatedUser = { ...user, age: 25 };

console.log("User:", updatedUser); // { name: "John", age: 25 }
