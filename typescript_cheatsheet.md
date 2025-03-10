# **TypeScript Cheat Sheet**
Cheat sheet built with CHATGPT :o

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

### **Basic Iteration**

```typescript
const numbers: number[] = [1, 2, 3, 4, 5];
numbers.forEach(num => console.log(num)); // O(n)
```

### **Using `for...of` Loop**

```typescript
for (const num of numbers) {
    console.log(num);
} // O(n)
```

### **Using `for...in` Loop (Enumerating Indexes)**

```typescript
for (const index in numbers) {
    console.log(index, numbers[index]);
} // O(n)
```

### **Mapping Elements**

```typescript
const squared = numbers.map(n => n * n);
console.log(squared); // [1, 4, 9, 16, 25] // O(n)
```

### **Filtering Elements**

```typescript
const evens = numbers.filter(n => n % 2 === 0);
console.log(evens); // [2, 4] // O(n)
```

### **Reducing an Array**

```typescript
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // 15 // O(n)
```

### **Looping Through a 2D Array (Row by Row)**

```typescript
const matrix: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
for (const row of matrix) {
    for (const value of row) {
        console.log(value);
    }
} // O(n * m)
```

### **Looping Through a 2D Array with Indexes**

```typescript
for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
        console.log(`Element at [${i}][${j}]:`, matrix[i][j]);
    }
} // O(n * m)
```

### **Looping with `entries()` (Index & Value Pairing)**

```typescript
for (const [index, value] of numbers.entries()) {
    console.log(`Index: ${index}, Value: ${value}`);
} // O(n)
```

⏳ **Time Complexity:** All array iterations are **O(n)**, except **nested loops over 2D arrays, which are O(n × m)**.

---

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

## **6️⃣ JSON Methods**
### **Converting an Object to a JSON String (`JSON.stringify`)**
```typescript
const user = { name: "Alice", age: 25 };
const jsonString = JSON.stringify(user);
console.log(jsonString); // '{"name":"Alice","age":25}'
```
🔹 **What it does:** Converts a JavaScript object into a JSON string.
🔹 **When to use:** When storing objects in local storage, sending data over APIs, or logging structured data.

### **Parsing a JSON String into an Object (`JSON.parse`)**
```typescript
const parsedObject = JSON.parse(jsonString);
console.log(parsedObject.name); // "Alice"
```
🔹 **What it does:** Converts a JSON string into a JavaScript object.
🔹 **When to use:** When reading data from APIs, local storage, or other JSON-based sources.

### **Handling Errors with `try/catch`**
```typescript
try {
    const data = JSON.parse('{ "name": "Alice" }');
    console.log(data.name);
} catch (error) {
    console.error("Invalid JSON format", error);
}
```
🔹 **What it does:** Catches syntax errors when parsing an invalid JSON string.
🔹 **When to use:** When handling dynamic JSON data from APIs or user input.

### **Formatting JSON with Indentation**
```typescript
const formattedJSON = JSON.stringify(user, null, 2);
console.log(formattedJSON);
```
🔹 **What it does:** Pretty-prints JSON with indentation.
🔹 **When to use:** When logging JSON or generating human-readable JSON files.

### **Filtering Keys While Stringifying (`replacer` Function)**
```typescript
const filteredJSON = JSON.stringify(user, ["name"]);
console.log(filteredJSON); // '{"name":"Alice"}'
```
🔹 **What it does:** Includes only specific keys while converting to JSON.
🔹 **When to use:** When stripping sensitive data before sending it over an API.

### **Modifying Values While Parsing (`reviver` Function)**
```typescript
const modifiedObject = JSON.parse('{ "age": "25" }', (key, value) =>
    key === "age" ? Number(value) : value
);
console.log(modifiedObject.age); // 25 (as a number)
```
🔹 **What it does:** Modifies parsed values dynamically.
🔹 **When to use:** When transforming data types while parsing JSON.

⏳ **Time Complexity:** `JSON.stringify()` and `JSON.parse()` have a time complexity of **O(n)**, where `n` is the size of the object.

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

React hooks allow functional components to manage state and lifecycle events.

### **useState - Manage Component State**
```typescript
const [count, setCount] = useState<number>(0);
setCount(count + 1);
```
🔹 **What it does:** Manages local component state.
🔹 **When to use:** When you need a stateful value that changes over time.

### **useEffect - Side Effects & Lifecycle Events**
```typescript
useEffect(() => {
    console.log("Component mounted");
    return () => console.log("Component unmounted");
}, []);
```
🔹 **What it does:** Runs side effects (fetching data, subscriptions, etc.) after rendering.
🔹 **When to use:** When you need to run code on mount, unmount, or dependency updates.

### **onMount - Equivalent to `useEffect(() => {}, [])`**
(Only applicable in frameworks like Svelte, not React.)
```typescript
useEffect(() => {
    console.log("Component mounted");
}, []);
```
🔹 **What it does:** Runs once when the component mounts.
🔹 **When to use:** When you need setup logic only once.

### **useRef - Reference DOM Elements & Persist Values**
```typescript
const inputRef = useRef<HTMLInputElement>(null);
useEffect(() => inputRef.current?.focus(), []);
```
🔹 **What it does:** Stores a reference to a DOM element or value across renders without re-triggering renders.
🔹 **When to use:** When you need to interact with DOM elements directly.

### **useContext - Consume Context Values**
```typescript
const theme = useContext(ThemeContext);
```
🔹 **What it does:** Provides access to values from a React context.
🔹 **When to use:** When multiple components need access to shared state without prop drilling.

### **useMemo - Optimize Expensive Calculations**
```typescript
const computedValue = useMemo(() => heavyComputation(), [dependency]);
```
🔹 **What it does:** Caches computed values and only recalculates when dependencies change.
🔹 **When to use:** When an expensive calculation shouldn't run on every render.

### **useCallback - Optimize Function References**
```typescript
const memoizedFunction = useCallback(() => console.log("Called!"), []);
```
🔹 **What it does:** Caches function references to prevent unnecessary re-renders.
🔹 **When to use:** When passing functions as props to prevent child components from re-rendering.

### **useReducer - Manage Complex State Logic**
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
🔹 **What it does:** Manages state transitions based on dispatched actions.
🔹 **When to use:** When state logic is complex or depends on previous state values.

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

## **1️⃣5️⃣ Local Storage Methods**

### **Setting an Item in Local Storage**
```typescript
localStorage.setItem("username", "Alice");
```
🔹 **What it does:** Stores a key-value pair in local storage.
🔹 **When to use:** When persisting user settings, authentication tokens, or small data across sessions.

### **Getting an Item from Local Storage**
```typescript
const username = localStorage.getItem("username");
console.log(username); // "Alice"
```
🔹 **What it does:** Retrieves a value stored in local storage.
🔹 **When to use:** When reading saved user preferences or authentication state.

### **Removing an Item from Local Storage**
```typescript
localStorage.removeItem("username");
```
🔹 **What it does:** Deletes a specific key from local storage.
🔹 **When to use:** When logging out a user or clearing specific settings.

### **Clearing All Local Storage Data**
```typescript
localStorage.clear();
```
🔹 **What it does:** Removes all stored key-value pairs.
🔹 **When to use:** When resetting app settings or logging out all users.

### **Storing Objects in Local Storage**
```typescript
const user = { name: "Alice", age: 25 };
localStorage.setItem("user", JSON.stringify(user));
```
🔹 **What it does:** Stores objects as strings in local storage.
🔹 **When to use:** When saving structured data like user profiles or app settings.

### **Retrieving and Parsing Objects from Local Storage**
```typescript
const storedUser = localStorage.getItem("user");
const userObject = storedUser ? JSON.parse(storedUser) : null;
console.log(userObject); // { name: "Alice", age: 25 }
```
🔹 **What it does:** Retrieves and parses stored JSON data.
🔹 **When to use:** When reading structured data previously saved in local storage.

### **Checking if a Key Exists in Local Storage**
```typescript
if (localStorage.getItem("username")) {
    console.log("Username exists in storage");
}
```
🔹 **What it does:** Checks whether a key is present in local storage.
🔹 **When to use:** When conditionally handling stored values.

⏳ **Time Complexity:** All local storage operations are **O(1)** because they operate on a key-value store.

---

## **1️⃣7️⃣ Fetch API & HTTP Requests**

### **Basic Fetch Request**
```typescript
fetch("https://api.example.com/data")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Fetch error:", error));
```
🔹 **What it does:** Sends a GET request to the specified URL and parses the JSON response.
🔹 **When to use:** When fetching data from an API.

### **Using `async/await` with Fetch**
```typescript
async function fetchData() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Fetch error:", error);
    }
}
fetchData();
```
🔹 **What it does:** Fetches data using `async/await` for better readability.
🔹 **When to use:** When handling API requests inside async functions.

### **Making a POST Request**
```typescript
async function postData(url: string, payload: object) {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });
        const data = await response.json();
        console.log("Response:", data);
    } catch (error) {
        console.error("Error posting data:", error);
    }
}

postData("https://api.example.com/data", { name: "Alice", age: 25 });
```
🔹 **What it does:** Sends a POST request with a JSON payload.
🔹 **When to use:** When submitting data to a server.

### **Handling Fetch Errors**
```typescript
async function safeFetch(url: string) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Fetch failed:", error);
    }
}
```
🔹 **What it does:** Checks if the response is successful before parsing.
🔹 **When to use:** When handling potential HTTP errors.

### **Using `AbortController` to Cancel Requests**
```typescript
const controller = new AbortController();
const signal = controller.signal;

fetch("https://api.example.com/data", { signal })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Fetch error:", error));

// Cancel the request
controller.abort();
```
🔹 **What it does:** Allows canceling a fetch request before completion.
🔹 **When to use:** When handling timeouts or user-triggered cancellations.

### **Setting Request Timeouts**
```typescript
async function fetchWithTimeout(url: string, timeout = 5000) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), timeout);
    try {
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        return await response.json();
    } catch (error) {
        console.error("Request timed out or failed:", error);
    }
}
fetchWithTimeout("https://api.example.com/data", 3000);
```
🔹 **What it does:** Aborts the request if it takes longer than the given timeout.
🔹 **When to use:** When limiting API request durations to prevent hanging operations.

⏳ **Time Complexity:** Fetch operations depend on network conditions, but parsing and handling JSON are **O(n)**.

---


