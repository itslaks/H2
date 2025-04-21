console.log("\n🔸 Nullish Coalescing Operator Example");

let username = null;
let defaultName = username ?? "Guest"; // if username is null/undefined, use "Guest"
        
console.log("Displayed Name:", defaultName); // "Guest"

let score = 0;
let finalScore = score ?? 10;

console.log("Final Score:", finalScore); // 0 → because 0 is not null or undefined
