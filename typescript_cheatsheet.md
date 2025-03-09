# **TypeScript Cheat Sheet**

## **1️⃣ String Manipulation**

### **String Declaration**
```typescript
let str: string = "Hello, TypeScript!";
let multiLine: string = `This is a multi-line string.`;
```
⏳ **Time Complexity:** O(1)

### **Concatenation**
```typescript
let fullName = firstName + " Doe"; // "John Doe"
let message = `Hello, ${firstName}`; // "Hello, John"
```
⏳ **Time Complexity:** O(n)

### **Checking for Substrings**
```typescript
console.log(str.includes("Type")); // true
console.log(str.startsWith("Hello")); // true
console.log(str.endsWith("Script")); // true
console.log(str.indexOf("Type")); // 0 (if found) or -1 (if not found)
```
⏳ **Time Complexity:** O(n)

---

## **2️⃣ Function Methods**

### **Async/Await**
```typescript
async function fetchData() {
    let response = await fetch('https://api.example.com/data');
    let data = await response.json();
    console.log(data);
}
```
⏳ **Time Complexity:** Depends on the API call

---

## **3️⃣ Math Functions**
```typescript
console.log(Math.abs(-10)); // 10
console.log(Math.ceil(4.3)); // 5
console.log(Math.floor(4.9)); // 4
console.log(Math.round(4.5)); // 5
console.log(Math.max(10, 20, 5)); // 20
console.log(Math.min(10, 20, 5)); // 5
console.log(Math.sqrt(25)); // 5
console.log(Math.pow(2, 3)); // 8
console.log(Math.random()); // Random number between 0 and 1
```
⏳ **Time Complexity:** O(1)

---

## **4️⃣ Important TypeScript Types**

### **Primitive Types**
```typescript
let isDone: boolean = false;
let count: number = 42;
let userName: string = "Alice";
let notDefined: undefined = undefined;
let empty: null = null;
```

### **Array Types**
```typescript
let numbers: number[] = [1, 2, 3];
let words: Array<string> = ["hello", "world"];
```

### **Tuple Types**
```typescript
let tuple: [string, number] = ["Alice", 25];
```

### **Enum Types**
```typescript
enum Color {
    Red,
    Green,
    Blue
}
let c: Color = Color.Green;
```

### **Union Types**
```typescript
let value: string | number;
value = "Hello";
value = 42;
```

### **Type Aliases**
```typescript
type Point = { x: number; y: number };
let p: Point = { x: 10, y: 20 };
```

### **Interfaces**
```typescript
interface Person {
    name: string;
    age: number;
}
let person: Person = { name: "Alice", age: 25 };
```

### **Generics**
```typescript
function identity<T>(arg: T): T {
    return arg;
}
console.log(identity<string>("Hello"));
console.log(identity<number>(42));
```

---

## **5️⃣ Other Useful Methods**

### **Date Methods**
```typescript
let now = new Date();
console.log(now.toISOString()); // Prints current date/time in ISO format
console.log(now.getFullYear()); // 2023
console.log(now.getMonth()); // 0-based month index
console.log(now.getDate()); // Day of the month
console.log(now.getHours());
```
⏳ **Time Complexity:** O(1)

### **Set Methods**
```typescript
const mySet = new Set<number>();
mySet.add(1);
mySet.has(1); // true
mySet.delete(1);
```
⏳ **Time Complexity:** O(1)

---

This cheat sheet provides a quick reference to commonly used TypeScript methods, types, async/await, and math functions. 🚀 Happy coding! 🎉

