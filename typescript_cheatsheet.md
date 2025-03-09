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

### **Extracting Parts**

```typescript
console.log(str.slice(0, 4)); // "Type"
console.log(str.substring(4)); // "Script"
```

⏳ **Time Complexity:** O(n)

### **Replacing Strings**

```typescript
console.log(str.replace("Type", "Java")); // "JavaScript"
console.log(str.replaceAll("a", "X")); // Replaces all occurrences
```

⏳ **Time Complexity:** O(n)

### **Trimming**

```typescript
console.log(str.trim()); // Removes whitespace
```

⏳ **Time Complexity:** O(n)

### **Splitting & Joining**

```typescript
let arr = str.split(" ");
console.log(arr.join("-")); // Join with "-"
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

### **Callback Functions**

```typescript
function process(value: number, callback: (n: number) => void) {
    callback(value * 2);
}
```

⏳ **Time Complexity:** Depends on the callback function

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

## **4️⃣ Array Methods**

### **Basic Operations**

```typescript
let numbers: number[] = [1, 2, 3, 4, 5];
numbers.push(6); // [1, 2, 3, 4, 5, 6] O(1)
numbers.pop(); // Removes last item O(1)
numbers.shift(); // Removes first item O(n)
```

### **Finding Elements**

```typescript
console.log(numbers.indexOf(3)); // Returns index of 3 O(n)
console.log(numbers.find(n => n > 3)); // 4 (first match) O(n)
console.log(numbers.findIndex(n => n > 3)); // 3 (index of first match) O(n)
```

### **Filtering, Mapping, Reducing**

```typescript
let even = numbers.filter(n => n % 2 === 0); // O(n)
let doubled = numbers.map(n => n * 2); // O(n)
let sum = numbers.reduce((acc, val) => acc + val, 0); // O(n)
```

### **Sorting & Joining**

```typescript
numbers.sort((a, b) => a - b); // Ascending sort O(n log n)
console.log(numbers.join(", ")); // "1, 2, 3, 4, 5" O(n)
```

---

## **5️⃣ Map Methods**

```typescript
const myMap = new Map<number, string>();
myMap.set(1, "One"); // O(1)
console.log(myMap.get(1)); // "One" O(1)
console.log(myMap.has(2)); // false O(1)
myMap.delete(1); // O(1)
```

### **Looping & Extracting Data**

```typescript
for (let [key, value] of myMap.entries()) { console.log(key, value); } // O(n)
console.log([...myMap.keys()]); // Array of all keys O(n)
console.log([...myMap.values()]); // Array of all values O(n)
myMap.clear(); // Removes all entries O(n)
```

---

## **6️⃣ React Hooks**

### **useState**

```typescript
const [count, setCount] = useState(0);
setCount(count + 1);
```

### **useEffect**

```typescript
useEffect(() => {
    console.log("Component mounted");
    return () => console.log("Component unmounted");
}, []);
```

### **useRef**

```typescript
const inputRef = useRef<HTMLInputElement>(null);
```

### **useContext**

```typescript
const theme = useContext(ThemeContext);
```

### **useMemo**

```typescript
const computedValue = useMemo(() => heavyComputation(), [dependency]);
```

### **useCallback**

```typescript
const memoizedFunction = useCallback(() => console.log("Called!"), []);
```

---

## **7️⃣ Key Maps & Event Handling**

### **Key Mapping Example**

```typescript
const keyMap: Record<string, string> = {
    Enter: "Submit",
    Escape: "Cancel",
};
console.log(keyMap["Enter"]); // "Submit"
```

### **Handling Keyboard Events**

```typescript
window.addEventListener("keydown", (event) => {
    console.log(`Key pressed: ${event.key}`);
});
```

---

## **8️⃣ Other Useful Methods**

### **Date Methods**

```typescript
let now = new Date();
console.log(now.toISOString());
console.log(now.getFullYear());
console.log(now.getMonth());
console.log(now.getDate());
```

⏳ **Time Complexity:** O(1)

### **Set Methods**

```typescript
const mySet = new Set<number>();
mySet.add(1);
mySet.has(1);
mySet.delete(1);
```

⏳ **Time Complexity:** O(1)

---

This cheat sheet provides a quick reference to commonly used TypeScript methods, types, async/await, math functions, React hooks, array & map operations, and event handling. 🚀 Happy coding! 🎉

