# **TypeScript Cheat Sheet**

## **1️⃣ String Manipulation**

### **String Declaration**

```typescript
let str: string = "Hello, TypeScript!";
let multiLine: string = `This is a multi-line string.`;
```

### **Concatenation**

```typescript
let fullName = firstName + " Doe"; // "John Doe"
let message = `Hello, ${firstName}`; // "Hello, John"
```

### **Length & Character Access**

```typescript
console.log(str.length); // Get length
console.log(str[0]); // Access character
```

### **Changing Case**

```typescript
console.log(str.toUpperCase()); // "HELLO"
console.log(str.toLowerCase()); // "hello"
```

### **Checking for Substrings**

```typescript
console.log(str.includes("Type")); // true
console.log(str.startsWith("Hello")); // true
console.log(str.endsWith("Script")); // true
```

### **Extracting Parts**

```typescript
console.log(str.slice(0, 4)); // "Type"
console.log(str.substring(4)); // "Script"
```

### **Replacing Strings**

```typescript
console.log(str.replace("Type", "Java")); // "JavaScript"
console.log(str.replaceAll("a", "X")); // Replaces all occurrences
```

### **Trimming**

```typescript
console.log(str.trim()); // Removes whitespace
```

### **Splitting & Joining**

```typescript
let arr = str.split(" ");
console.log(arr.join("-")); // Join with "-"
```

---

## **2️⃣ Function Methods**

### **Function Declaration**

```typescript
function greet(name: string): string {
    return `Hello, ${name}!`;
}
```

### **Arrow Functions**

```typescript
const greet = (name: string) => `Hello, ${name}!`;
```

### **Default Parameters**

```typescript
function greet(name: string = "User") {
    return `Hello, ${name}!`;
}
```

### **Rest Parameters**

```typescript
function sum(...numbers: number[]) {
    return numbers.reduce((acc, val) => acc + val, 0);
}
```

### **Callback Functions**

```typescript
function process(value: number, callback: (n: number) => void) {
    callback(value * 2);
}
```

### **Immediately Invoked Function**

```typescript
(() => { console.log("Hello!"); })();
```

---

## **3️⃣ Map Methods**

### **Creating a Map**

```typescript
const myMap = new Map<number, string>();
```

### **Setting Values**

```typescript
myMap.set(1, "One");
```

### **Getting Values**

```typescript
console.log(myMap.get(1)); // "One"
```

### **Checking Key Existence**

```typescript
console.log(myMap.has(2)); // false
```

### **Deleting Keys**

```typescript
myMap.delete(1);
```

### **Looping Over Map**

```typescript
for (let [key, value] of myMap.entries()) { console.log(key, value); }
```

---

## **4️⃣ Array Methods**

### **Creating an Array**

```typescript
let numbers: number[] = [1, 2, 3, 4, 5];
```

### **Adding Elements**

```typescript
numbers.push(6); // [1, 2, 3, 4, 5, 6]
```

### **Removing Elements**

```typescript
numbers.pop(); // Removes last item
numbers.shift(); // Removes first item
```

### **Finding Elements**

```typescript
console.log(numbers.indexOf(3)); // Returns index of 3
```

### **Filtering**

```typescript
let even = numbers.filter(n => n % 2 === 0);
```

### **Mapping**

```typescript
let doubled = numbers.map(n => n * 2);
```

### **Reducing**

```typescript
let sum = numbers.reduce((acc, val) => acc + val, 0);
```

### **Sorting**

```typescript
numbers.sort((a, b) => a - b); // Ascending sort
```

### **Joining**

```typescript
console.log(numbers.join(", ")); // "1, 2, 3, 4, 5"
```

---

## **5️⃣ Palindrome & Character Frequency**

### **Checking for Palindromes**

```typescript
function isPalindrome(str: string): boolean {
    const cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, "");
    return cleanStr === cleanStr.split("").reverse().join("");
}
```

### **Reversing a String**

```typescript
function reverseString(str: string): string {
    return str.split("").reverse().join("");
}
```

### **Counting Character Frequency**

```typescript
function charFrequency(str: string): Record<string, number> {
    const freq: Record<string, number> = {};
    for (const char of str) {
        freq[char] = (freq[char] || 0) + 1;
    }
    return freq;
}
```

---

This cheat sheet provides a quick reference to commonly used TypeScript methods. 🚀 Happy coding! 🎉

