#Check if a number is positive, negative, or zero.

num = int(input("Enter your number : "))

if num == 0:
    print("The number is Zero")
elif num > 0:
    print("The number is Positive")
else:
    print("The number is Negative")
print()

# Check whether a number is even or odd.
n = int(input("enter the number to be checked whether even or odd : "))
if n ==0:
    print("The number is 0 neither even nor odd")
elif n%2 == 0:
    print("The number is even!!")

else:
    print("The number is odd!!")
print()

#Find the greater of two numbers.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a > b :
    print(f"The greater number from {a} and {b} is {a}" )
else:
    print(f"The greater number from {a} and {b} is {b}")
print()

# Find the greatest of three numbers.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a > b and  a > c:
    print(f"The greater number from {a}, {b} and {c} is {a}" )
elif b > a and b > c:
    print(f"The greater number from {a}, {b} and {c} is {b}" )
else:
    print(f"The greater number from {a}, {b} and {c} is {c}" )
print()


#Check if a person is eligible to vote (age ≥ 18).
age = int(input(" Please enter your age : "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")
print()

#Check whether a year is a leap year.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")

elif year % 100 == 0:
    print(f"{year} is not a leap year")

elif year % 4 == 0:
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")

#Check if a character is a vowel or consonant.
c = input("Enter the alphabet: ")

if c in 'aeiouAEIOU':
    print("This is vowel !!")
else:
    print("This is consonant!!")
print()

#Check whether a number is divisible by 5 and 11.
num = int(input("Enter the number : "))

if (num%5 == 0) and (num%11 == 0):
    print("Number divisible by 5 and 11")
else:
    print("Number is not divisible  by 5 and 11")
print()


#Check if a number is a multiple of both 3 and 7.
num = int(input("Enter the number: "))

if (num % 3 == 0) and (num % 7 == 0):
    print("Number is a multiple of both 3 and 7")
else:
    print("Number is not a multiple of both 3 and 7")
print()

# Assign grades based on marks: a. 90–100: A b. 80–89: B c. 70–79: C d. 60–69: D e. Below 60: F
grade = float(input("Enter your grade :"))

if grade >= 90 and grade <= 100:
    print("A grade")
elif grade >=80 and grade < 90:
    print(" B Grade")
elif grade >=70 and grade <= 80:
    print(" C Grade")
elif grade >=60 and grade <= 70:
    print(" D Grade")
else:
    print("Fail")
print()

# Check if a character is uppercase or lowercase
c = input("Enter a character: ")
if c.isupper():
    print("Character is uppercase")
elif c.islower():
    print("Character is lowercase")
else:
    print("It is not an alphabet")
print()

#Check whether the entered alphabet is a vowel using if-elif
c = input("Enter an alphabet: ")

if c == 'a' or c == 'A':
    print("It is a vowel")
elif c == 'e' or c == 'E':
    print("It is a vowel")
elif c == 'i' or c == 'I':
    print("It is a vowel")
elif c == 'o' or c == 'O':
    print("It is a vowel")
elif c == 'u' or c == 'U':
    print("It is a vowel")
else:
    print("It is a consonant")
print()

#Check if three sides can form a triangle
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

#Find the largest among four numbers.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))
if a > b and  a > c and a > d:
    print(f"The greater number from {a}, {b}, {c} and {d} is {a}" )
elif b > a and b > c and b > d:
    print(f"The greater number from {a}, {b}, {c} and {d} is {b}" )
elif c > a and b > c and d > d:
    print(f"The greater number from {a}, {b}, {c} and {d} is {c}" )
else:
    print(f"The greater number from {a}, {b}, {c} and {d} is {d}" )
print()

#Check whether a number is a three-digit number.
num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print("It is a three-digit number")
elif num <= -100 and num >= -999:
    print("It is a three-digit number")
else:
    print("It is not a three-digit number")
print()


#Calculate electricity bill using slab rates.
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity bill =", bill)
print()

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

#Check if a student passes (minimum 35 marks in each subject).
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 35 and science >= 35 and english >= 35:
    print("Student has passed")

else:
    print("Student has failed")
print()

# Find whether a number is within a given range.
num = int(input("Enter a number: "))
lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

if num >= lower_limit and num <= upper_limit:
    print("Number is within the range")

else:
    print("Number is outside the range")

# Build a simple calculator using if-elif-else (+, -, *, /).
a = float(input("Enter first number: "))
operator = input("Enter operator for operations want to be done (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == '+':
    print(" Addition : Result =", a + b)

elif operator == '-':
    print("Substraction : Result =", a - b)

elif operator == '*':
    print("Multiplication : Result =", a * b)

elif operator == '/':
    if b != 0:
        print("Division : Result =", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")
print()


#Check if a year is a century leap year
year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("It is a century leap year")

elif year % 100 == 0:
    print("It is a century year but not a leap year")

else:
    print("It is not a century year")

# Determine the season based on the month number.
month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter Season")

elif month == 3 or month == 4 or month == 5:
    print("Summer Season")

elif month == 6 or month == 7 or month == 8 or month == 9:
    print("Monsoon Season")

elif month == 10 or month == 11:
    print("Post-Monsoon Season")

else:
    print("Invalid month number")
print()

#Find the number of days in a month.
month = (input("Enter month : "))

if month == "february":
    print("February has 28 or 29 days")

elif month == "April"or month == "June" or month == "September" or month == "November":
    print("This month has 30 days")

elif month == "January"or month == "March" or month == "May" or month == "July" or  month == "August" or month == "October" or month == "December":
    print("This month has 31 days")

else:
    print("Invalid month number")

password = input("Enter password: ")

has_digit = False
has_upper = False

for c in password:
    if c.isdigit():
        has_digit = True

    if c.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Password is valid")

else:
    print("Password is invalid")
print()

#Determine ticket price based on age category.
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is free")

elif age <= 12:
    print("Ticket price = ₹50")

elif age < 60:
    print("Ticket price = ₹100")

else:
    print("Ticket price = ₹70")
print()

# Calculate discount based on purchase amount
amount = float(input("Enter purchase amount: "))

if amount < 1000:
    discount = 0

elif amount < 5000:
    discount = amount * 0.10

elif amount < 10000:
    discount = amount * 0.20

else:
    discount = amount * 0.30

final_amount = amount - discount

print("Discount =", discount)
print("Final amount =", final_amount)
print()

#Check if a person is eligible for a driving license (age and eyesight condition).
age = int(input("Enter your age: "))
eyesight = input("Is your eyesight good? (yes/no): ")

if age >= 18 and eyesight == "yes":
    print("You are eligible for a driving license")

else:
    print("You are not eligible for a driving license")
print()

#Create a menu-driven program using if-elif-else with options like: Addition, Subtraction, Multiplication, Division, Exit

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