# Find the data type of every value in a mixed list.

my_list = [10, "Hello", 3.14, True, [1, 2], (4, 5)]

for value in my_list:
    print(value, "->", type(value))


# Convert a nested list into a tuple of tuples.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = tuple(tuple(row) for row in nested_list)

print(result)

# Remove all duplicate values from a mixed list while preserving the original order.

my_list = [12, "abc", 23, 12, "abc", 55]

result = []
visit = set()

for item in my_list:
    if item not in  visit:
        result.append(item)
        visit.add(item)

print(result)

#Check whether a number is a power of 2 using operators.
n = int(input("Enter a number: "))

if n <= 0:
    print("Not a power of 2")
else:
    while n % 2 == 0:
        n = n // 2

    if n == 1:
        print("Power of 2")
    else:
        print("Not a power of 2")

#Swap two numbers using bitwise XOR.

#Find whether a number is divisible by both 4 and 6 using logical operators.
num = int(input("Enter the number"))

if num % 4 == 0 and num % 6 == 0:
    print("Divisible by both 6 and 4")
elif num % 4==0:
    print("Divisible by 4 only")
elif num % 6==0:
    print("Divisible by 6 only")
else:
    print("Not divisible by 4 and 6")


#Calculate the total electricity bill using different unit rates.
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity bill =", bill)
print()

#Check whether three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides can form a triangle")
else:
    print("The sides cannot form a triangle")
print()

#Determine the type of triangle (Equilateral, Isosceles, Scalene).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")

elif a == b and b == c:
    print("Equilateral triangle")

elif a == b or b == c or a == c:
    print("Isosceles triangle")

else:
    print("Scalene triangle")

print()

#Create a simple ATM menu (Withdraw, Deposit, Balance).
balance = 10000

print("===== ATM MENU =====")
print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Deposit successful")
    print("Updated balance:", balance)

elif choice == 3:
    print("Your balance is:", balance)

else:
    print("Invalid choice")

#Calculate income tax based on income slabs.
income = int(input("Enter your overall income"))

if income <= 400000:
    print("NO Income tax needed to be paid as salary less than 400000")
elif income > 400000 and income <= 800000:
    tax = income * 0.05
    print(f"Total amount of tax need to pay will be {tax} ")
elif income > 800000 and income <= 1200000:
    tax = income * 0.1
    print(f"Total amount of tax need to pay will be {tax} ")
elif income > 1200000 and income <= 1600000:
    tax = income * 0.15
    print(f"Total amount of tax need to pay will be {tax} ")
elif income > 1600000 and income <= 2000000:
    tax = income * 0.2
    print(f"Total amount of tax need to pay will be {tax} ")
elif income > 2000000 and income <= 2400000:
    tax = income * 0.25
    print(f"Total amount of tax need to pay will be {tax} ")
else:
    tax = income * 0.3
    print(f"Total amount of tax need to pay will be {tax} ")
print()

#Create a menu-driven calculator using if-elif.
print("----- Calculator -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition =", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Substraction =", a - b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Multiplication =", a * b)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b != 0:
        print("Division =", a / b)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    print("Thank you!")

else:
    print("Invalid choice")


#Print all prime numbers between 1 and n.

n = int(input("Enter n: "))

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
print()

#Find the factorial of a number using a loop.

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

#Print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

print()

#Check whether a number is an Armstrong number.
n = int(input("Enter a number: "))

original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
print()

#Reverse a number and check if it is a palindrome.
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
print()

#Find the Greatest Common Divisor (GCD) of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD =", a)
print()

#Write a function to check if a string is a palindrome.
def is_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


word = input("Enter a string: ")

print(is_palindrome(word))
print()

# Write a function to count vowels and consonants in a string.
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


text = input("Enter a string: ")

v, c = count_vowels_consonants(text)

print("Vowels =", v)
print("Consonants =", c)
print()

#Create a function to calculate simple and compound interest.
def calculate_interest(p, r, t):
    simple_interest = (p * r * t) / 100

    compound_amount = p * (1 + r / 100) ** t
    compound_interest = compound_amount - p

    return simple_interest, compound_interest


p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

si, ci = calculate_interest(p, r, t)

print("Simple Interest =", si)
print("Compound Interest =", ci)
print()


#Write a function to return all factors of a number.
def find_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


n = int(input("Enter a number: "))

print("Factors =", find_factors(n))
print()

#Write a function to find the second-largest number in a list.
def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    return second


numbers = [10, 5, 20, 8, 15]

print("Second largest =", second_largest(numbers))
print()

 
#Merge two lists without duplicates.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for item in list1:
    if item not in result:
        result.append(item)

for item in list2:
    if item not in result:
        result.append(item)

print("Merged list =", result)
print()

#Find the second-largest and second-smallest elements.
numbers = [10, 5, 20, 8, 15, 3]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

smallest = min(unique)
largest = max(unique)

second_smallest = None
second_largest = None

for num in unique:
    if num != smallest:
        if second_smallest is None or num < second_smallest:
            second_smallest = num

    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

print("Second smallest =", second_smallest)
print("Second largest =", second_largest)
print()


#Rotate a list to the left by k positions.
numbers = [1, 2, 3, 4, 5]

k = int(input("Enter k: "))

for i in range(k):
    first = numbers.pop(0)
    numbers.append(first)

print("Rotated list =", numbers)
print()

#Separate even and odd numbers into two lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers =", even)
print("Odd numbers =", odd)
print()

#Find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for item in list1:
    if item in list2:
        if item not in common:
            common.append(item)

print("Common elements =", common)
print()


#Count the frequency of each element in a tuple.
numbers = (1, 2, 2, 3, 3, 3, 4)

frequency = {}

for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
print()

#Find the union, intersection, and difference of two sets.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B
intersection = A & B
difference = A - B

print("Union =", union)
print("Intersection =", intersection)
print("Difference =", difference)
print()

#Check whether one set is a subset of another.
A = {1, 2}
B = {1, 2, 3, 4}

if A <= B:
    print("A is a subset of B")
else:
    print("A is not a subset of B")

print()

#Count the frequency of words in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency =", frequency)
print()

#Create a dictionary from two lists (keys and values).
keys = ["name", "age", "city"]
values = ["Priyal", 22, "Pune"]

data = {}

for i in range(len(keys)):
    data[keys[i]] = values[i]

print(data)
print()

#Sort a dictionary by its values.
marks = {
    "A": 80,
    "B": 60,
    "C": 90,
    "D": 70
}

sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1]))

print(sorted_marks)
print()


#Read a text file and count the number of lines, words, and characters.
file = open("sample.txt", "w")

file.write(" Hello Python. Python is easy. I am learning Python...")

file.close()

file = open("sample.txt", "r")

lines = file.readlines()

line_count = len(lines)
word_count = 0
character_count = 0

for line in lines:
    word_count += len(line.split())
    character_count += len(line)

file.close()

print("Number of lines =", line_count)
print("Number of words =", word_count)
print("Number of characters =", character_count)




#Copy only the even-numbered lines from one file to another.


#Handle invalid integer input using try-except.
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter an integer.")

print()
#Handle file-not-found errors while reading a file.
try:
    with open("data.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found!")
print()


#Create a random password generator using the random and string modules.
import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated password:", password)

print()




#Use the datetime module to calculate the number of days between two dates.
from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs((d2 - d1).days)

print("Number of days =", difference)
print()


