// Understanding var, let, and const in JavaScript

// PART 1: SCOPE DIFFERENCES
console.log("PART 1: SCOPE DIFFERENCES");

// Using var (function-scoped)
function varExample() {
  console.log("--- var scope example ---");
  
  if (true) {
    var x = 10;
    console.log("Inside block: x =", x); // x is 10
  }
  
  console.log("Outside block: x =", x); // x is still accessible here (10)
}
varExample();

// Using let (block-scoped)
function letExample() {
  console.log("--- let scope example ---");
  
  if (true) {
    let y = 20;
    console.log("Inside block: y =", y); // y is 20
  }
  
  // Uncomment to see error:
  // console.log("Outside block: y =", y); // ReferenceError: y is not defined
  console.log("Outside block: y = [not accessible]");
}
letExample();

// PART 2: REASSIGNMENT
console.log("\nPART 2: REASSIGNMENT");

// var can be reassigned
var name1 = "John";
name1 = "Jane";
console.log("var name1 after reassignment:", name1); // Jane

// let can be reassigned
let name2 = "Alice";
name2 = "Bob";
console.log("let name2 after reassignment:", name2); // Bob

// const cannot be reassigned
const name3 = "Sarah";
// Uncomment to see error:
// name3 = "Mike"; // TypeError: Assignment to constant variable
console.log("const name3:", name3); // Sarah

// PART 3: REDECLARATION
console.log("\nPART 3: REDECLARATION");

// var can be redeclared
var fruit1 = "Apple";
var fruit1 = "Orange"; // No error
console.log("var fruit1 after redeclaration:", fruit1); // Orange

// let cannot be redeclared in the same scope
let fruit2 = "Banana";
// Uncomment to see error:
// let fruit2 = "Grape"; // SyntaxError: Identifier 'fruit2' has already been declared
console.log("let fruit2:", fruit2); // Banana

// PART 4: HOISTING
console.log("\nPART 4: HOISTING");

// var is hoisted and initialized with undefined
console.log("var before declaration:", hoistedVar); // undefined
var hoistedVar = "I am hoisted";

// let is hoisted but not initialized (Temporal Dead Zone)
// Uncomment to see error:
// console.log("let before declaration:", hoistedLet); // ReferenceError: Cannot access 'hoistedLet' before initialization
let hoistedLet = "I am not accessible before declaration";
console.log("let after declaration:", hoistedLet); // I am not accessible before declaration

// PART 5: CONST WITH OBJECTS
console.log("\nPART 5: CONST WITH OBJECTS");

// With const objects, we can modify properties
const person = {
  name: "David",
  age: 30
};

person.name = "Michael"; // This works!
person.age = 35;        // This works!

// But we cannot reassign the entire object
// Uncomment to see error:
// person = { name: "Edward", age: 40 }; // TypeError: Assignment to constant variable

console.log("const object after property changes:", person); // { name: 'Michael', age: 35 }