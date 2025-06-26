print("Hello World")

print("    /|")
print("   /_|")
print("  /__|")
print(" /___|")

print("There once was a man named George,")
print("he was 70 years old.")
print("He really liked the name George")
print("but didn't like being 70.")

# String Manipulation
name = "John" #string
age = "35" #string
isMale = True #bool

print("There once was a man named " + name + ",")
print("he was " + age + " years old.")
name = "Mike"
print("He really liked the name " + name)
print("but didn't like being " + age + ".")

print("Girrafe\nGiraffe\nGiraffe") # \n is used to create a new line

phrase = "Giraffe Academy"
print(phrase + " is cool") # Concatenation
print(phrase.lower()) # Lowercase
print(phrase.upper()) # Uppercase
print(phrase.isupper()) # Check if all characters are uppercase
print(phrase.islower()) # Check if all characters are lowercase
print(len(phrase)) # Length of the string
print(phrase[0]) # Accessing the first character
print(phrase.index("G")) # Find the index of the first occurrence of "G"
print(phrase.replace("Giraffe", "Elephant")) # Replace "Giraffe" with "Elephant"

# Number Manipulation
print(5 + 3) # Addition
print(5 - 3) # Subtraction
print(5 * 3) # Multiplication
print(5 / 3) # Division
print(5 % 3) # Modulus (remainder)
print(5 ** 3) # Exponentiation (5 raised to the power of 3)
print(abs(-5)) # Absolute value
print(pow(5, 3)) # Power function (5 raised to the power of 3)
print(max(5, 3)) # Maximum of two numbers
print(min(5, 3)) # Minimum of two numbers
print(round(5.7)) # Round to the nearest integer
print(round(5.4)) # Round to the nearest integer

print(str(5) + " is a string now") # Convert number to string

from math import *
print(floor(3.7))  # Round down to the nearest integer
print(ceil(3.7))   # Round up to the nearest integer
print(sqrt(36))    # Square root of 36

# Getting User Input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!" + " You are " + age + " years old.")

#Simple Calculator
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print("Result: " + str(result))

# Simple Mad Libs Game
print("Welcome to the Mad Libs Game!")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
print("Here is your story:")
print(f"The {adjective} {noun} decided to {verb} in the park. It was a fun day!")

#List Manipulation
fruits = ["apple", "banana", "cherry", "strawberry"]
print(fruits)  # Print the list
print(fruits[0])  # Access the first element
print(fruits[1:3])  # Access a slice of the list
print(fruits[-1])  # Access the last element
fruits.append("orange")  # Add an element to the end
fruits.remove("banana")  # Remove an element
fruits.pop()  # Remove the last element
fruits.insert(1, "kiwi")  # Insert an element at a specific index
print(fruits)  # Print the modified list
exotic_fruits = ["mango", "pineapple", "papaya"]
fruits.extend(exotic_fruits)  # Extend the list with another list
print(fruits)  # Print the extended list

fruits.sort() # Sort the list in ascending order
fruits.reverse()  # Reverse the order of the list

fruits_copy = fruits.copy()  # Create a copy of the list

# Tuple Manipulation
# Tuples are immutable lists
fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple)  # Print the tuple
print(fruits_tuple[0])  # Access the first element
print(fruits_tuple[1:3])  # Access a slice of the tuple

# Dictionary Manipulation
# Dictionaries are key-value pairs
print("Welcome to the Dictionary Manipulation!")
student = {
    "name": "John",
    "age": 20,
    "is_student": True
}
print(student)  # Print the dictionary
print(student["name"])  # Access a value by key
print(student.get("age"))  # Access a value using the get method
student["age"] = 21  # Update a value
print(student)  # Print the updated dictionary
student["grade"] = "A"  # Add a new key-value pair
print(student)  # Print the dictionary with the new key-value pair

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")  # Print each key-value pair

# Nested Dictionary
nested_dict = {
    "student1": {
        "name": "Alice",
        "age": 22
    },
    "student2": {
        "name": "Bob",
        "age": 23
    }
}
print(nested_dict)  # Print the nested dictionary
# Accessing nested dictionary values
print(nested_dict["student1"]["name"])  # Accessing Alice's name
print(nested_dict["student2"]["age"])  # Accessing Bob's age

# Functions
def greet(name):
    """Function to greet a person."""
    print(f"Hello, {name}!")

greet("Alice")  # Call the function with an argument

# Function with default parameters
def greet_with_default(name="Guest"):
    """Function to greet a person with a default name."""
    print(f"Hello, {name}!")
greet_with_default()  # Call the function without an argument
greet_with_default("Bob")  # Call the function with an argument

# Function with multiple parameters
def introduce(name, age):
    """Function to introduce a person."""
    print(f"My name is {name} and I am {age} years old.")

introduce("Charlie", 30)  # Call the function with two arguments

# Function with return value
def add_numbers(num1, num2):
    """Function to add two numbers."""
    return num1 + num2
result = add_numbers(5, 3)  # Call the function and store the result
print(f"The sum is: {result}")  # Print the result

# Function with variable number of arguments
def calculate_average(*args):
    """Function to calculate the average of any number of arguments."""
    if len(args) == 0:
        return 0
    return sum(args) / len(args)
average = calculate_average(10, 20, 30, 40, 50)  # Call the function with multiple arguments
print(f"The average is: {average}")  # Print the average

# If Statements
def check_age(age):
    """Function to check if a person is an adult."""
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")
check_age(20)  # Call the function with an age greater than 18
check_age(16)  # Call the function with an age less than 18

def check_even_odd(number):
    """Function to check if a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

check_even_odd(10)  # Call the function with an even number
check_even_odd(7)  # Call the function with an odd numberg

# Simple Rock, Paper, Scissors Game
import random
print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(choices)
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

