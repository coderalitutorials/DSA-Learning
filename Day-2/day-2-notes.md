# 🧠 Time Complexity and Asymptotic Notations

## 1. Time Complexity kya hoti hai?

**Definition (Simple Words me):**  
Time complexity ye batati hai ke **aapka algorithm ya program input ke size ke hisaab se kitna time lega run hone me.** Matlab agar input badhta jaaye to program kitna slow ya fast hota hai — ye uski time complexity se pata chalta hai.

Maan lo tumhara code 1 se `n` tak number print karta hai:

for i in range(n):
    print(i)

Yahan loop **n baar chalega**, matlab agar input `n = 10` hai to 10 baar print hoga. Agar `n = 1000` hai to 1000 baar chalega. To time input ke saath **linearly badhta hai.** 👉 Isliye iski **time complexity = O(n)** hoti hai (isko hum **asymptotic notation** kehte hain, neeche samjhte hain).

Ab maan lo tumhara code fixed operation karta hai:

print("Hello")
print("World")

Chahe input `n = 10` ho ya `n = 1 million`, ye sirf **2 statements** execute karega. To time input par depend hi nahi karta. 👉 Isliye iski **time complexity = O(1)** (constant time).

## ⚙️ 2. Asymptotic Notations kya hoti hain?

Ye **mathematical symbols** hote hain jinke zariye hum algorithm ki performance ko describe karte hain — jaise:  

- Program **fast** hai ya **slow** input badhne par.  
- Kya wo **best case** me tez chalega ya har case me **slow** hoga.  
Ye notations sirf **approximate growth rate** batate hain — exact seconds nahi.

Socho tumhare do algorithms hain:  

- **Algo A:** 2n + 3 steps me kaam karta hai  
- **Algo B:** n² + 5 steps me kaam karta hai  

Agar `n = 5` ho to dono tez chalenge, fark nahi dikhega. Lekin agar `n = 10,000` ho jaaye, to:  

- A → 20,003 steps lega  
- B → 100,005,000 steps 😬  

To A ka growth rate **linear** hai, aur B ka **quadratic**. Yahan hum asymptotic notation se keh dete hain:  

- **A = O(n)**  
- **B = O(n²)**  

Socho ek banda **seedha raste par chal raha hai** (O(n)) aur ek banda **zigzag raste se** (O(n²)). Dono start ek hi jagah se karte hain — chhote raste me dono sath honge, lekin jaise distance badhta jaata hai, **zigzag wala bahut peeche reh jaata hai.** Yahi difference **time complexity** ka hota hai.

### ⚙️ 1. Best Case, Worst Case, Average Case 

Algorithm har baar same time me kaam nahi karta — ye depend karta hai input kaisa hai. Kuch input pe kaam bohot tez hota hai, kuch pe slow, aur normally beech me hota hai.

Isliye hum teen tarah ke “cases” define karte hain:

| Case | Matlab | Kab hota hai |
|------|---------|--------------|
| **Best Case** | Jab algorithm sabse tez chal jaye | Input bilkul ideal ho |
| **Worst Case** | Jab algorithm sabse slow chale | Input sabse bura ho |
| **Average Case** | Jab algorithm normal performance de | Random input ho |

## 🔍 Example 1: Linear Search

Socho tumhare paas ek list hai:

arr = [5, 9, 3, 7, 1]  
target = 7

Aur tum **Linear Search** laga rahe ho (ek ek karke check karte ho).

### 🔹 Best Case

Agar target pehli position par hi mil jaye, jaise:

arr = [7, 9, 3, 5, 1]

To sirf **1 comparison** me mil gaya → ⏱ **O(1)**  
✅ Ye **Best Case** hai.

### 🔹 Worst Case

Agar target last me ho ya bilkul na ho, jaise:

arr = [5, 9, 3, 7, 1]  # last me mila

To poori list check karni padegi → ⏱ **O(n)**  
❌ Ye **Worst Case** hai.

### 🔹 Average Case

Agar target kahin beech me ho, jaise 3rd ya 4th element me mil jaye,  
To on average aadhi list check karni padegi → ⏱ **O(n/2)**  
Par asymptotic notation me constants ignore karte hain → **O(n)**

---

### 💡 Real-Life Analogy

Socho tum ek locker room me apna **bag** dhoondh rahe ho:

- **Best Case:** Bag bilkul pehle locker me hi mil gaya.  
- **Worst Case:** Sab lockers check karne pad gaye, last me mila.  
- **Average Case:** Kahi beech me mil gaya.  

Yahi logic algorithms me lagta hai.

___

## Types of time complexity 

| Complexity | Name         | Example Code Pattern | Growth Rate  |
| ---------- | ------------ | -------------------- | ------------ |
| O(1)       | Constant     | Simple statement     | ⚡ Fastest   |
| O(n)       | Linear       | Single loop          | 🔹 Moderate  |
| O(n²)      | Quadratic    | Nested loops         | 🟡 Slower    |
| O(n³)      | Cubic        | 3-level nested loops | 🔴 Very Slow |
| O(log n)   | Logarithmic  | Binary Search        | ⚙️ Efficient |
| O(n log n) | Linearithmic | Merge/Quick Sort     | ⚖️ Good      |
| O(2ⁿ)      | Exponential  | Recursive Fibonacci  | 🐢 Slowest   |


____

# 🧠 Space Complexity — Complete Explanation

## ⚙️ Definition

**Space Complexity** batata hai ke **algorithm ko chalne ke liye kitni memory (RAM)** chahiye hoti hai.

Jaise Time Complexity measure karti hai “kitna time” lagta hai,  
waise hi Space Complexity measure karti hai “kitni memory” lagti hai.

Space Complexity = **Fixed Space (constant memory)** + **Variable Space (input ke hisaab se memory)**

---

## 🧩 1. Fixed Space (Constant Memory)

Ye wo memory hoti hai jo **hamesha same** rehti hai, chahe input kitna bhi bada ho.

Examples:

- Variables
- Constants
- Simple expressions
- Fixed-size arrays
Example:

```python
a = 10
b = 20
c = a + b 
```


# Recursion and Loop vs Recursion (Detailed Notes)

## 🧩 1. What is Recursion?

**Recursion** ek aisa problem-solving technique hai jisme **function apne aap ko hi call karta hai** — directly ya indirectly — jab tak problem solve na ho jaye.

### 🔹 Simple Words Me

> Recursion is when a big problem is broken into smaller sub-problems of the same type, and each sub-problem is solved using the same logic until we reach a **base condition (stopping point)**.

### 🧠 Real-Life Understanding

Socho tumharay paas **10 nested boxes** hain — ek box ke andar doosra box.  
Tumhe **sabse chhoti box** tak pahunchna hai.

- Tum **ek box kholo**, dekhte ho andar ek aur box hai → tum kehte ho “main is andar wale box ko kholne ja raha hoon.”  
- Phir wohi process repeat hoti rehti hai — **same step har box ke liye**.  
- Jab tum **sabse chhoti box** tak pahunch jaate ho (jisme aur koi box nahi), tum kaam rok dete ho (yeh hai **base case**).  
- Ab tum wapas aate ho har box band karte hue (yeh hoti hai **unwinding of recursion**).

So basically:  
> Har step same logic use karta hai (ek box kholna), jab tak condition poori na ho jaaye (box khatam).  
> Yahi recursion ka **core idea** hai.

### 🧩 Real-World Analogies

- **Russian Matryoshka Dolls** — ek ke andar doosri doll.  
- **Family Tree Traversal** — har child ke child ko same rule se explore karna.  
- **File System** — ek folder ke andar aur folders, har folder ko recursively explore karna.  

---

## ⚙️ 2. How Recursion Works Internally

Recursion computer ke **memory stack (call stack)** par kaam karti hai.

1. Jab ek function apne aap ko call karta hai → system **previous state save** kar leta hai stack me.  
2. Har recursive call ek **naya stack frame** create karti hai.  
3. Jab **base case milta hai** → calls **reverse order me return hoti hain (LIFO — Last In First Out)**.

> Agar base case define na ho, recursion kabhi rukti nahi → **Stack Overflow Error** ho jata hai.

---

## 3. Loop vs Recursion (Deep Comparison)

| **Aspect** | **Loop (Iteration)** | **Recursion** |
|------------|--------------------|---------------|
| **Concept** | Repeats a block of code until a condition is false | Function calls itself until base case is reached |
| **Control Flow** | Uses statements like `for`, `while`, `do-while` | Uses function calls and return statements |
| **Termination Condition** | Loop condition becomes false | Base condition is met |
| **Memory Usage** | Uses single memory block (no extra call stack) | Each call uses new stack frame → high memory |
| **Performance** | Faster, because less overhead | Slower due to multiple function calls |
| **Ease of Understanding** | Easy for simple repetition | Better for problems that are naturally recursive (tree, factorial, etc.) |
| **Example (Conceptually)** | “Repeat this step 10 times.” | “Do the same work on smaller part of data until nothing left.” |
| **Where to Use** | Simple counting, array traversal, etc. | Complex problems: tree traversal, divide-and-conquer algorithms |
| **Risk** | Infinite loop if condition never false | Stack overflow if base case missing |

---

### 💡 Intuitive Difference:

Imagine you are climbing stairs:

- **Loop way:** Tum manually count karte ja rahe ho 1, 2, 3, ... 10 tak.  
- **Recursive way:** Tum kehte ho, “Ek stair chadh jao, baaki stairs chadne ka kaam same logic se handle karo.”  
  Har step tumhare liye ek **new function call** ban jaata hai.

---

## 🧠 4. When to Use Recursion vs Loop

### ✅ Use **Loop** When

- Task simple aur repetitive hai (e.g., printing 1 to 100).  
- Memory optimization important hai.  
- Time complexity ko minimal rakhna ho.  

### ✅ Use **Recursion** When

- Problem naturally **divides into subproblems**.  
- Examples:
  - Tree traversal (left and right child)  
  - Graph traversal (DFS)  
  - Divide & conquer algorithms (Merge Sort, Quick Sort)  
  - Mathematical series (Factorial, Fibonacci)

---

## ⚠️ 5. Common Mistakes in Recursion

1. **Base case define na karna** → Infinite recursion.  
2. **Base case galat define karna** → Wrong output.  
3. **Large input pe stack overflow** → because har call memory consume karti hai.  

---

## 📘 6. Summary in One Line

> **Loop** ek repetitive process hai,  
> **Recursion** ek self-calling process hai — jisme solution milta hai by breaking problem into smaller, similar problems.

