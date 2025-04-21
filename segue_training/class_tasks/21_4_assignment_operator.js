let a = 10;
console.log("Start: a = 10");

// 1. = (Simple Assignment)
// Sets a new value to 'a'
a = 5;
console.log("a = 5 ➜", a);

// 2. += (Addition Assignment)
// Adds 3 to 'a' → a = a + 3
a += 3;
console.log("a += 3 ➜", a); // 8

// 3. -= (Subtraction Assignment)
// Subtracts 2 from 'a' → a = a - 2
a -= 2;
console.log("a -= 2 ➜", a); // 6

// 4. *= (Multiplication Assignment)
// Multiplies 'a' by 4 → a = a * 4
a *= 4;
console.log("a *= 4 ➜", a); // 24

// 5. /= (Division Assignment)
// Divides 'a' by 2 → a = a / 2
a /= 2;
console.log("a /= 2 ➜", a); // 12

// 6. %= (Modulus Assignment)
// Remainder when 'a' is divided by 5 → a = a % 5
a %= 5;
console.log("a %= 5 ➜", a); // 2

// 7. **= (Exponentiation Assignment)
// Raises 'a' to the power of 3 → a = a ** 3
a **= 3;
console.log("a **= 3 ➜", a); // 8

// 8. &= (Bitwise AND Assignment)
// a = a & 1 → Bitwise AND with 1
a &= 1;
console.log("a &= 1 ➜", a); // 0

// 9. |= (Bitwise OR Assignment)
// a = a | 2 → Bitwise OR with 2
a |= 2;
console.log("a |= 2 ➜", a); // 2

// 10. ^= (Bitwise XOR Assignment)
// a = a ^ 3 → Bitwise XOR with 3
a ^= 3;
console.log("a ^= 3 ➜", a); // 1

// 11. <<= (Left Shift Assignment)
// a = a << 2 → Shift bits to the left by 2
a <<= 2;
console.log("a <<= 2 ➜", a); // 4

// 12. >>= (Right Shift Assignment)
// a = a >> 1 → Shift bits to the right by 1 (preserves sign)
a >>= 1;
console.log("a >>= 1 ➜", a); // 2

// 13. >>>= (Unsigned Right Shift Assignment)
// a = a >>> 1 → Shift bits to the right by 1 (fills with 0)
a >>>= 1;
console.log("a >>>= 1 ➜", a); // 1
