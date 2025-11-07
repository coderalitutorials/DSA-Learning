# Q NO :1 
# Given an integer n, return a string array answer (1-indexed) where:

# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# - answer[i] == "Fizz" if i is divisible by 3.
# - answer[i] == "Buzz" if i is divisible by 5.
# - answer[i] == i (as a string) if none of the above conditions are true.

def fizzBuzz(n):
    answer = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    
    return answer

print(fizzBuzz(5))


# """
# 🧮 Question: Count Odd Numbers in an Interval Range

# Given two non-negative integers low and high.
# Return the count of odd numbers between low and high (inclusive).
# """

def countOdds(low, high):
    # Formula-based solution (no loop needed)
    return (high + 1) // 2 - (low // 2)


# Example usage:
print(countOdds(3, 7))  # Output: 3


# 🔍 Example Dry Run
# For low = 3, high = 7:

# (high + 1)//2 = (7 + 1)//2 = 4
# (low)//2 = 3//2 = 1
# count = 4 - 1 = 3 ✅


# """
# 🧮 Question: How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find how many numbers in the array are smaller than it.
# Return the answer in an array.
# """

def smallerNumbersThanCurrent(nums):
    result = []

    # Outer loop -> for each element
    for i in range(len(nums)):
        count = 0
        # Inner loop -> compare with every other element
        for j in range(len(nums)):
            if nums[j] < nums[i] and j != i:
                count += 1
        result.append(count)
    
    return result


# Example usage:
print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))


# | i                   | nums[i] | j | nums[j] | Condition (nums[j] < nums[i]?) | Count (after check) |
# | ------------------- | ------- | - | ------- | ------------------------------ | ------------------- |
# | 0                   | 8       | 0 | 8       | ❌ (equal, skip)                | 0                   |
# | 0                   | 8       | 1 | 1       | ✅ (1 < 8)                      | 1                   |
# | 0                   | 8       | 2 | 2       | ✅ (2 < 8)                      | 2                   |
# | 0                   | 8       | 3 | 2       | ✅ (2 < 8)                      | 3                   |
# | 0                   | 8       | 4 | 3       | ✅ (3 < 8)                      | 4                   |
# | **→ result[0] = 4** |         |   |         |                                |                     |
# | 1                   | 1       | 0 | 8       | ❌ (8 > 1)                      | 0                   |
# | 1                   | 1       | 1 | 1       | ❌ (same index)                 | 0                   |
# | 1                   | 1       | 2 | 2       | ❌ (2 > 1)                      | 0                   |
# | 1                   | 1       | 3 | 2       | ❌ (2 > 1)                      | 0                   |
# | 1                   | 1       | 4 | 3       | ❌ (3 > 1)                      | 0                   |
# | **→ result[1] = 0** |         |   |         |                                |                     |
# | 2                   | 2       | 0 | 8       | ❌ (8 > 2)                      | 0                   |
# | 2                   | 2       | 1 | 1       | ✅ (1 < 2)                      | 1                   |
# | 2                   | 2       | 2 | 2       | ❌ (same index)                 | 1                   |
# | 2                   | 2       | 3 | 2       | ❌ (equal)                      | 1                   |
# | 2                   | 2       | 4 | 3       | ❌ (3 > 2)                      | 1                   |
# | **→ result[2] = 1** |         |   |         |                                |                     |
# | 3                   | 2       | 0 | 8       | ❌                              | 0                   |
# | 3                   | 2       | 1 | 1       | ✅                              | 1                   |
# | 3                   | 2       | 2 | 2       | ❌                              | 1                   |
# | 3                   | 2       | 3 | 2       | ❌                              | 1                   |
# | 3                   | 2       | 4 | 3       | ❌                              | 1                   |
# | **→ result[3] = 1** |         |   |         |                                |                     |
# | 4                   | 3       | 0 | 8       | ❌                              | 0                   |
# | 4                   | 3       | 1 | 1       | ✅                              | 1                   |
# | 4                   | 3       | 2 | 2       | ✅                              | 2                   |
# | 4                   | 3       | 3 | 2       | ✅                              | 3                   |
# | 4                   | 3       | 4 | 3       | ❌                              | 3                   |
# | **→ result[4] = 3** |         |   |         |                                |                     |

# output
# [4, 0, 1, 1, 3]


# 🧠 Samjho kya ho raha hai:

# Outer loop i → fix karta hai current number.

# Inner loop j → us current number se compare karta hai sabke sath.

# Jab bhi koi nums[j] < nums[i] milta hai, count badhta hai.

# Har i ke end me count result list me append hota hai.



# """
# 🧮 Question: Count Digits That Divide a Number

# Given an integer num, return the number of digits in num that divide num.
# An integer val divides num if num % val == 0.
# """

def countDigits(num):
    count = 0
    for digit in str(num):          # convert number to string to access each digit
        val = int(digit)            # convert back to integer
        if val != 0 and num % val == 0:  # skip 0 to avoid division error
            count += 1
    return count


# Example usage:
print(countDigits(1248))   # Output: 4
print(countDigits(121))    # Output: 2
print(countDigits(1012))   # Output: 3

# | Step                 | Action                  | Example |
# | -------------------- | ----------------------- | ------- |
# | Convert num → string | "1248"                  |         |
# | Loop each digit      | '1', '2', '4', '8'      |         |
# | Check divisibility   | 1248 % digit == 0       |         |
# | Skip digit = 0       | avoid ZeroDivisionError |         |
# | Count valid digits   | add 1 for each divider  |         |

num= 1012
# | Digit | num % digit | Divides? | Count |
# | ----- | ----------- | -------- | ----- |
# | 1     | 0           | ✅        | 1     |
# | 0     | ❌ skip      | —        | 1     |
# | 1     | 0           | ✅        | 2     |
# | 2     | 0           | ✅        | 3     |


# """
# 🧮 Question: Palindrome Number

# Given an integer x, return True if x is a palindrome, and False otherwise.
# """

def isPalindrome(x):
    # Negative numbers are never palindromes
    if x < 0:
        return False
    
    # Convert to string and compare with its reverse
    return str(x) == str(x)[::-1]


# Example usage:
print(isPalindrome(121))   # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))    # False
print(isPalindrome(1331))  # True


# """
# 🧮 Question: Subtract the Product and Sum of Digits of an Integer

# Given an integer n, return the difference between the product of its digits and the sum of its digits.
# """

def subtractProductAndSum(n):
    product = 1
    sum_digits = 0
    
    while n > 0:
        digit = n % 10
        product *= digit
        sum_digits += digit
        n //= 10  # remove last digit
    
    return product - sum_digits


# Example usage:
print(subtractProductAndSum(234))  # Output: 15
print(subtractProductAndSum(4421)) # Output: 21


#Dry run example
# | Step                           | n            | digit | product     | sum_digits |
# | ------------------------------ | ------------ | ----- | ----------- | ---------- |
# | Start                          | 234          | -     | 1           | 0          |
# | 1                              | 234 % 10 = 4 | 4     | 1 × 4 = 4   | 0 + 4 = 4  |
# | 2                              | 23 % 10 = 3  | 3     | 4 × 3 = 12  | 4 + 3 = 7  |
# | 3                              | 2 % 10 = 2   | 2     | 12 × 2 = 24 | 7 + 2 = 9  |
# | End                            | —            | —     | 24          | 9          |
# | **Difference = 24 - 9 = 15 ✅** |              |       |             |            |


# """
# 🧮 Question: Kids With the Greatest Number of Candies

# For each kid, return True if giving all extraCandies to them
# makes them have the greatest number of candies among all.
# """

def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)   # step 1
    result = []

    # step 2: loop through each kid
    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    return result


# Example usage:
print(kidsWithCandies([2, 3, 5, 1, 3], 3))
# Output: [True, True, True, False, True]


# 🔹 Step 3: Har bachay pe sochna manually (logic forming)
# Soch lo tum check kar rahe ho ek ek bachay ko:

# | Kid | Current | + ExtraCandies | Total | Compare with max (5) | Result |
# | --- | ------- | -------------- | ----- | -------------------- | ------ |
# | A   | 2       | 3              | 5     | 5 ≥ 5 ✅              | True   |
# | B   | 3       | 3              | 6     | 6 ≥ 5 ✅              | True   |
# | C   | 5       | 3              | 8     | 8 ≥ 5 ✅              | True   |
# | D   | 1       | 3              | 4     | 4 ≥ 5 ❌              | False  |
# | E   | 3       | 3              | 6     | 6 ≥ 5 ✅              | True   |
