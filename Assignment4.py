# ============================================================
# 1. Check Whether a Number is Even or Odd
# ============================================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 2. Find the Largest of Three Numbers
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# ============================================================
# 3. Check Whether a Number is Prime
# ============================================================

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")


# ============================================================
# 4. Fibonacci Series up to n Terms
# ============================================================

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# ============================================================
# 5. Factorial of a Number Using Loop
# ============================================================

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# ============================================================
# 6. Reverse a String Without Using [::-1]
# ============================================================

text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)


# ============================================================
# 7. Check Whether a String is a Palindrome
# ============================================================

text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# ============================================================
# 8. Count Number of Vowels and Consonants
# ============================================================

text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text.lower():

    if char in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# ============================================================
# 9. Find Sum of All Elements in a List
# ============================================================

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Sum:", total)


# ============================================================
# 10. Find Largest and Smallest Without max() or min()
# ============================================================

numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# ============================================================
# 11. Remove Duplicate Elements from a List
# ============================================================

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:

    if num not in unique:
        unique.append(num)

print("After removing duplicates:", unique)


# ============================================================
# 12. Count How Many Times Each Element Appears Using Dictionary
# ============================================================

numbers = [10, 20, 10, 30, 20, 10]

count = {}

for num in numbers:

    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print("Element frequency:", count)


# ============================================================
# 13. Find the Second-Largest Number in a List
# ============================================================

numbers = [10, 50, 30, 40, 20]

largest = numbers[0]
second = None

for num in numbers:

    if num > largest:
        second = largest
        largest = num

    elif num != largest and (second is None or num > second):
        second = num

print("Second largest:", second)


# ============================================================
# 14. Sort a List Without sort() or sorted()
# ============================================================

numbers = [50, 20, 40, 10, 30]

for i in range(len(numbers)):

    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# ============================================================
# 15. Function to Return Only Even Numbers
# ============================================================

def even_numbers(numbers):

    result = []

    for num in numbers:

        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 2, 3, 4, 5, 6, 8]

print("Even numbers:", even_numbers(numbers))


# ============================================================
# 16. Find Frequency of Each Character in a String
# ============================================================

text = input("Enter a string: ")

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)


# ============================================================
# 17. Check Whether Two Strings are Anagrams
# ============================================================

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")


# ============================================================
# 18. Find All Duplicate Values in a List
# ============================================================

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

duplicates = []

for num in numbers:

    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values:", duplicates)


# ============================================================
# 19. Find the Longest Word in a Sentence
# ============================================================

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:

    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# ============================================================
# 20. Student Marks Program
# ============================================================

marks = []

for i in range(5):

    mark = float(input(f"Enter marks for subject {i + 1}: "))

    marks.append(mark)


total = sum(marks)

percentage = total / 5


if percentage >= 90:
    grade = "A"

elif percentage >= 80:
    grade = "B"

elif percentage >= 70:
    grade = "C"

elif percentage >= 60:
    grade = "D"

elif percentage >= 50:
    grade = "E"

else:
    grade = "F"


if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"


print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)