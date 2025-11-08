# print 1 to n using recursion

def print_numbers(n):
    # Base case
    if n == 0:
        return
    
    # Recursive call before printing (for 1 → n)
    print_numbers(n - 1)
    
    # Print after recursive call
    print(n)

# Function call
print_numbers(5)


# Output:
# 1
# 2
# 3
# 4
# 5


# | Step | Function Call      | Action Before Recursive Call | Recursive Call To  | Action After Recursive Call | Output |
# | ---- | ------------------ | ---------------------------- | ------------------ | --------------------------- | ------ |
# | 1    | `print_numbers(5)` | n=5 (not 0) → go recursive   | `print_numbers(4)` | After return → print(5)     | 5      |
# | 2    | `print_numbers(4)` | n=4 (not 0) → go recursive   | `print_numbers(3)` | After return → print(4)     | 4      |
# | 3    | `print_numbers(3)` | n=3 (not 0) → go recursive   | `print_numbers(2)` | After return → print(3)     | 3      |
# | 4    | `print_numbers(2)` | n=2 (not 0) → go recursive   | `print_numbers(1)` | After return → print(2)     | 2      |
# | 5    | `print_numbers(1)` | n=1 (not 0) → go recursive   | `print_numbers(0)` | After return → print(1)     | 1      |
# | 6    | `print_numbers(0)` | Base case → return           | —                  | —                           | —      |


# How to calculate factorial using recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Function call
result = factorial(5)
print("Factorial of 5 is:", result)


#output:
# Factorial of 5 is: 120


# | Step | Function Call  | Base Case Check | Recursive Call | Calculation After Return | Return Value   |
# | ---- | -------------- | --------------- | -------------- | ------------------------ | -------------- |
# | 1    | `factorial(5)` | No              | `factorial(4)` | `5 * factorial(4)`       | `5 * 24 = 120` |
# | 2    | `factorial(4)` | No              | `factorial(3)` | `4 * factorial(3)`       | `4 * 6 = 24`   |
# | 3    | `factorial(3)` | No              | `factorial(2)` | `3 * factorial(2)`       | `3 * 2 = 6`    |
# | 4    | `factorial(2)` | No              | `factorial(1)` | `2 * factorial(1)`       | `2 * 1 = 2`    |
# | 5    | `factorial(1)` | ✅ Yes           | —              | —                        | `1`            |


# concept of recursion
# | Concept            | Meaning                                              |
# | ------------------ | ---------------------------------------------------- |
# | **Recursion**      | Function apne aap ko call karta hai                  |
# | **Base Case**      | Jab condition poori hoti hai aur recursion rukta hai |
# | **Recursive Case** | Jab function firse apne aap ko call karta hai        |


# Recursive stack:
# Simple Definition
# Recursive Stack wo memory structure hoti hai jahan function calls ek ke upar ek store hoti hain jab tak base case nahi milta.

# Soch lo jaise:
# Ek stack of plates — har new recursive call ek nayi plate ke jaisi hai jo upar rakh di jaati hai.
# Jab base case mil jata hai, hum plates ek ek karke wapas nikalte hain (return phase).

# Example — Factorial (3)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))


# step by step track
# | Step | Function Call  | Stack (Top → Bottom)                             | Action                                       |
# | ---- | -------------- | ------------------------------------------------ | -------------------------------------------- |
# | 1    | `factorial(3)` | `factorial(3)`                                   | n=3, base case not met → call `factorial(2)` |
# | 2    | `factorial(2)` | `factorial(2)` → `factorial(3)`                  | n=2, base case not met → call `factorial(1)` |
# | 3    | `factorial(1)` | `factorial(1)` → `factorial(2)` → `factorial(3)` | base case met → return 1                     |
# | 4    | return phase   | pop `factorial(1)` → 1                           | now `factorial(2)` = 2 × 1 = 2               |
# | 5    | return phase   | pop `factorial(2)` → 2                           | now `factorial(3)` = 3 × 2 = 6               |
# | 6    | end            | stack empty                                      | Final answer = 6                             |


# Step 3: Easy Analogy
# Soch lo:
# Tum stair climb kar rahe ho (each stair = ek recursive call).
# Jab top par pahunch jaate ho (base case), tab tum neeche wapas utarte ho (return phase).
# Upar chadhte waqt har step yaad rakhta hai ke kaha se aaye (stack memory me store hota hai).

# summary table :
# | Term                | Meaning                                                    |
# | ------------------- | ---------------------------------------------------------- |
# | **Recursive Stack** | Memory area jahan function calls temporary store hoti hain |
# | **Push (Call)**     | Jab function apne aap ko call karta hai                    |
# | **Pop (Return)**    | Jab function apna result wapas karta hai                   |
# | **Base Case**       | Recursion stop hone ka point                               |
# | **Return Phase**    | Jab result upar walay function ko milta hai                |


# Recursive Tree Kya Hota Hai?
# Recursive Tree ek diagram hota hai jo dikhata hai ke ek recursive function apne aap ko
# kitni baar call karta hai aur kis tarah branch hoti hai.

# Soch lo:
# Jaise ek tree (darakht) hota hai jisme root se branches nikalti hain, waise hi har
# recursive call se new sub-calls (branches) nikalti hain.

# Simple Example — Factorial (3)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

factorial(3)

# Recursive Tree Representation:

# factorial(3)
#     ↓
#     3 * factorial(2)
#             ↓
#             2 * factorial(1)
#                     ↓
#                     1

# Now return phase:
# factorial(1) = 1
# factorial(2) = 2 * 1 = 2
# factorial(3) = 3 * 2 = 6


# 🔹 Step 4: Difference Between Recursive Stack & Recursive Tree
# | Concept             | Meaning                                       | Visualization   | Used For                                                             |
# | ------------------- | --------------------------------------------- | --------------- | -------------------------------------------------------------------- |
# | **Recursive Stack** | Memory flow of function calls (top to bottom) | Linear (1 path) | Execution understanding                                              |
# | **Recursive Tree**  | Function call branching diagram               | Tree shape      | Understanding **how many calls** are made and **call relationships** |

# Step 5: Easy Analogy
# Soch lo:
# Tum recursive stack ko samjho jaise "kaun pehle gaya aur kaun baad me aaya"
# aur recursive tree ko samjho jaise "kaun kis se nikla".


# Q: Recursion ka use karke Python me function likhna hai jo check kare:
# agar n / 2 karne par result 1 ho → return True
# agar 1 nahi ho → return False
# agar 0 ho → return False


def check_divide_by_two(n):
    # Base cases
    if n == 0:
        return False
    if n == 1:
        return True
    
    # Recursive call
    return check_divide_by_two(n / 2)

# Test
print(check_divide_by_two(8))   # True (8→4→2→1)
print(check_divide_by_two(10))  # False (10→5→2.5→1.25→0.625... never exactly 1)
print(check_divide_by_two(0))   # False
print(check_divide_by_two(1))   # True


# 🔹 Step 1: GCD (Greatest Common Divisor) kya hota hai?

# GCD ya HCF (Highest Common Factor) wo sabse bada number hota hai jo dono numbers ko poori tarah divide karta hai (remainder 0 deta hai).

# Example:
# GCD of 20 and 8 →
# Factors of 20 = 1, 2, 4, 5, 10, 20
# Factors of 8 = 1, 2, 4, 8
# 👉 Common factors = 1, 2, 4 →
# GCD = 4


# 🔹 Step 2: Euclidean Algorithm ka Concept
# Euclid ka rule:
# GCD(a, b) = GCD(b, a % b)
# Jab tak b != 0
# aur jab b == 0, tab GCD = a


# 🔸 Example: GCD(48, 18)

# | Step | a  | b  | a % b        | Next Call   |
# | ---- | -- | -- | ------------ | ----------- |
# | 1    | 48 | 18 | 48 % 18 = 12 | GCD(18, 12) |
# | 2    | 18 | 12 | 18 % 12 = 6  | GCD(12, 6)  |
# | 3    | 12 | 6  | 12 % 6 = 0   | GCD(6, 0)   |
# | 4    | 6  | 0  | —            | Return 6 ✅  |

# 👉 Final GCD = 6


# Python Code (Recursive Way):
def gcd(a, b):
    # Base Case
    if b == 0:
        return a
    # Recursive Case
    return gcd(b, a % b)

# Test
print(gcd(48, 18))  # Output: 6
print(gcd(20, 8))   # Output: 4
print(gcd(7, 3))    # Output: 1

#🔹 Step 4: Step-by-Step Trace (for a = 48, b = 18)
# | Function Call | a  | b  | Result               |
# | ------------- | -- | -- | -------------------- |
# | gcd(48, 18)   | 48 | 18 | calls gcd(18, 12)    |
# | gcd(18, 12)   | 18 | 12 | calls gcd(12, 6)     |
# | gcd(12, 6)    | 12 | 6  | calls gcd(6, 0)      |
# | gcd(6, 0)     | 6  | 0  | base case → return 6 |

#✅ Answer = 6

