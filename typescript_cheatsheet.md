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

## **9️⃣ Promises & Async Handling**

### **Creating a Promise**
```typescript
const myPromise = new Promise<number>((resolve, reject) => {
    setTimeout(() => {
        resolve(42); // Resolve with a value after 1 second
    }, 1000);
});
```

### **Handling a Promise with `.then()`**
```typescript
myPromise.then(value => {
    console.log("Resolved with value:", value);
}).catch(error => {
    console.error("Promise rejected:", error);
});
```

### **Using `async/await` with Promises**
```typescript
async function fetchData(): Promise<void> {
    try {
        const value = await myPromise;
        console.log("Fetched value:", value);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
fetchData();
```

### **Multiple Promises with `Promise.all`**
```typescript
const promise1 = Promise.resolve(10);
const promise2 = new Promise((resolve) => setTimeout(() => resolve(20), 2000));

Promise.all([promise1, promise2]).then(values => {
    console.log("Resolved values:", values); // [10, 20]
});
```

### **Handling the First Resolved Promise with `Promise.race`**
```typescript
const fastPromise = new Promise(resolve => setTimeout(() => resolve("Fast!"), 500));
const slowPromise = new Promise(resolve => setTimeout(() => resolve("Slow!"), 2000));

Promise.race([fastPromise, slowPromise]).then(result => {
    console.log("First resolved:", result); // "Fast!"
});
```

### **Chaining Promises**
```typescript
myPromise
    .then(value => value * 2)
    .then(newValue => console.log("Doubled value:", newValue))
    .catch(error => console.error("Error in chain:", error));
```

⏳ **Time Complexity:** Varies depending on the number of promises and execution time.

### **Looping Through Promises with `for...of` and `Promise.all`**
```typescript
const urls = ["https://api.example.com/1", "https://api.example.com/2"];

async function fetchAllData() {
    for (const url of urls) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            console.log("Data from", url, data);
        } catch (error) {
            console.error("Error fetching", url, error);
        }
    }
}
fetchAllData();
```

### **Looping Through Promises in Parallel with `Promise.all`**
```typescript
async function fetchParallel() {
    try {
        const responses = await Promise.all(urls.map(url => fetch(url)));
        const data = await Promise.all(responses.map(res => res.json()));
        console.log("Fetched all data:", data);
    } catch (error) {
        console.error("Error fetching data", error);
    }
}
fetchParallel();
```

### **Using `forEach` with Promises (Caution)**
```typescript
urls.forEach(async (url) => {
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log("Data from", url, data);
    } catch (error) {
        console.error("Error fetching", url, error);
    }
});
```
⚠ **Warning:** `forEach` does not wait for `await`, so results may be unpredictable.

⏳ **Time Complexity:** O(n) for sequential loops, O(1) for `Promise.all` in parallel execution.

---

## **🔟 React Hooks with TypeScript**

### **useState**
```typescript
const [count, setCount] = useState<number>(0);
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

### **useReducer**
```typescript
type State = { count: number };
type Action = { type: "increment" } | { type: "decrement" };

function reducer(state: State, action: Action): State {
    switch (action.type) {
        case "increment":
            return { count: state.count + 1 };
        case "decrement":
            return { count: state.count - 1 };
        default:
            return state;
    }
}

const [state, dispatch] = useReducer(reducer, { count: 0 });
```

⏳ **Time Complexity:** Hook execution time varies but is generally **O(1)** for setting values, and **O(n)** for dependencies in `useEffect` and `useMemo`.

---

## **1️⃣1️⃣ Understanding `setTimeout`**

### **Basic `setTimeout` Usage**
```typescript
setTimeout(() => {
    console.log("Executed after 2 seconds");
}, 2000);
```
⏳ **Time Complexity:** O(1) (scheduling) but callback execution depends on the delay.

### **Using `setTimeout` with Variables**
```typescript
const timer = setTimeout(() => {
    console.log("This runs once after 3 seconds");
}, 3000);
```

### **Clearing a Timeout**
```typescript
clearTimeout(timer);
```
This prevents the scheduled function from running if it hasn't executed yet.

### **Using `setTimeout` in a Loop**
```typescript
for (let i = 1; i <= 3; i++) {
    setTimeout(() => {
        console.log(`Executed after ${i} second(s)`);
    }, i * 1000);
}
```

### **Using `setTimeout` with Promises**
```typescript
function delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function delayedMessage() {
    await delay(2000);
    console.log("This message appears after 2 seconds");
}

delayedMessage();
```
⏳ **Time Complexity:** O(1) for scheduling, O(n) if used in loops with dependent execution.

---

## **1️⃣2️⃣ Object Functions**

### **Iterating Over Object Properties**

#### **Using `Object.keys()`**
```typescript
const person = { name: "Alice", age: 25, city: "New York" };
Object.keys(person).forEach(key => {
    console.log(`${key}: ${person[key as keyof typeof person]}`);
});
```
⏳ **Time Complexity:** O(n)

#### **Using `Object.values()`**
```typescript
Object.values(person).forEach(value => {
    console.log(value);
});
```
⏳ **Time Complexity:** O(n)

#### **Using `Object.entries()`**
```typescript
Object.entries(person).forEach(([key, value]) => {
    console.log(`${key}: ${value}`);
});
```
⏳ **Time Complexity:** O(n)

### **Checking Object Properties**
```typescript
console.log("name" in person); // true
console.log(person.hasOwnProperty("age")); // true
```
⏳ **Time Complexity:** O(1)

### **Merging Objects**
#### **Using `Object.assign()`**
```typescript
const obj1 = { a: 1 };
const obj2 = { b: 2 };
const merged = Object.assign({}, obj1, obj2);
console.log(merged); // { a: 1, b: 2 }
```
⏳ **Time Complexity:** O(n)

#### **Using Spread Operator (`...`)**
```typescript
const mergedSpread = { ...obj1, ...obj2 };
console.log(mergedSpread); // { a: 1, b: 2 }
```
⏳ **Time Complexity:** O(n)

### **Cloning Objects**
```typescript
const cloned = { ...person };
console.log(cloned);
```
⏳ **Time Complexity:** O(n)

### **Deep Copying an Object**
```typescript
const deepCopy = JSON.parse(JSON.stringify(person));
console.log(deepCopy);
```
⏳ **Time Complexity:** O(n)

### **Freezing & Sealing Objects**
#### **Freezing (`Object.freeze`)**
```typescript
const frozenObj = Object.freeze({ name: "Frozen" });
frozenObj.name = "New"; // Error in strict mode
```
⏳ **Time Complexity:** O(n)

#### **Sealing (`Object.seal`)**
```typescript
const sealedObj = Object.seal({ name: "Sealed" });
sealedObj.name = "Updated"; // Allowed
sealedObj.newProp = "Error"; // Not allowed
```
⏳ **Time Complexity:** O(n)

---

## **1️⃣3️⃣ Set Methods**

### **Creating a Set**
```typescript
const mySet = new Set<number>();
mySet.add(1);
mySet.add(2);
mySet.add(3);
console.log(mySet); // Set { 1, 2, 3 }
```
⏳ **Time Complexity:** O(1) per `.add()` operation

### **Checking for Existence**
```typescript
console.log(mySet.has(2)); // true
console.log(mySet.has(5)); // false
```
⏳ **Time Complexity:** O(1)

### **Deleting an Element**
```typescript
mySet.delete(2);
console.log(mySet); // Set { 1, 3 }
```
⏳ **Time Complexity:** O(1)

### **Clearing the Set**
```typescript
mySet.clear();
console.log(mySet); // Set {}
```
⏳ **Time Complexity:** O(n)

### **Iterating Over a Set**
#### **Using `forEach()`**
```typescript
mySet.forEach(value => {
    console.log(value);
});
```
#### **Using `for...of` Loop**
```typescript
for (const value of mySet) {
    console.log(value);
}
```
⏳ **Time Complexity:** O(n)

### **Converting a Set to an Array**
```typescript
const setArray = [...mySet];
console.log(setArray);
```
⏳ **Time Complexity:** O(n)

### **Performing Set Operations**
#### **Union**
```typescript
const setA = new Set([1, 2, 3]);
const setB = new Set([3, 4, 5]);
const unionSet = new Set([...setA, ...setB]);
console.log(unionSet); // Set { 1, 2, 3, 4, 5 }
```
⏳ **Time Complexity:** O(n)

#### **Intersection**
```typescript
const intersectionSet = new Set([...setA].filter(x => setB.has(x)));
console.log(intersectionSet); // Set { 3 }
```
⏳ **Time Complexity:** O(n)

#### **Difference**
```typescript
const differenceSet = new Set([...setA].filter(x => !setB.has(x)));
console.log(differenceSet); // Set { 1, 2 }
```
⏳ **Time Complexity:** O(n)

---
