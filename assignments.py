"""
Assignment 1 – String Analyzer
1. Problem Statement
Write a Python program that accepts a sentence from the user and performs the following operations:
1. Count the number of characters.
2. Count the number of words.
3. Convert the sentence into uppercase.
4. Convert the sentence into lowercase.
5. Reverse the sentence.
2. Concepts used
- Strings
- input()
- len()
- split()
- upper()
- lower()
- String slicing
3. Python program
Create string_analyzer.py."""
# String Analyzer
sentence = input("Enter a sentence: ")# Count characters
characters = len(sentence)# Count words
words = len(sentence.split())# Convert to uppercase
uppercase = sentence.upper()# Convert to lowercase
lowercase = sentence.lower()# Reverse the sentence
reversed_sentence = sentence[::-1]# Display result
sprint("\n--- STRING ANALYZER ---")
print("Characters:", characters)
print("Words:", words)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Reversed:", reversed_sentence)


"""
4. Sample output
Enter a sentence: I love Python

--- STRING ANALYZER ---

Characters: 13
Words: 3
Uppercase: I LOVE PYTHON
Lowercase: i love python
Reversed: nohtyP evol I


5. Explanation
Code	Purpose
input()	Accepts a sentence
len(sentence)	Counts characters, including spaces
sentence.split()	Separates the sentence into words
upper()	Converts to uppercase
lower()	Converts to lowercase
[::-1]	Reverses the string

Mentor question: Why are strings immutable in Python?

Answer: Strings are immutable because their contents cannot be modified after creation. Operations such as upper() and replace() produce new strings rather than changing the original string.
"""

"""
#Assignment 2 – Remove Duplicates from a List

1. Problem Statement
Given a list containing duplicate elements, write a Python program to remove duplicate values using a set.
2. Concepts used
- Lists
- Sets
- Type conversion
- set()
- list()
3. Python program
Create remove_duplicates.py.
"""

# Remove Duplicates from a List
numbers = [10, 20, 30, 20, 40, 10, 50]
print("Original List:", numbers)# Convert list into set
unique_numbers = set(numbers)
print("Set without duplicates:", unique_numbers)# Convert set back into list
result = list(unique_numbers)
print("Unique List:", result)



"""
4. Sample output
Original List: [10, 20, 30, 20, 40, 10, 50]

Set without duplicates: {10, 20, 30, 40, 50}

Unique List: [10, 20, 30, 40, 50]


The order of elements in the set and converted list is not guaranteed.
5. Explanation
Step 1:
numbers = [10, 20, 30, 20, 40, 10, 50]



Creates a list with duplicate values.

Step 2:
unique_numbers = set(numbers)



Converts the list into a set. Sets automatically eliminate duplicate elements.

Step 3:
result = list(unique_numbers)



Converts the set back into a list.
6. Alternative: Preserve original order
If your mentor asks you to remove duplicates while preserving the original order, use:
numbers = [10, 20, 30, 20, 40, 10, 50]result = list(dict.fromkeys(numbers))print(result)



Output:
[10, 20, 30, 40, 50]


Mentor question: Why can't we use indexing on a set?

Answer: A set is an unordered collection and does not support positional indexing.
"""

"""
Assignment 3 – Student Information Dictionary
1. Problem Statement
Create a Python dictionary containing student information and display every key and its corresponding value using a loop.

The dictionary should contain:
- Name
- Roll number
- Branch
- Marks
- College
2. Concepts used
- Dictionaries
- Key-value pairs
- Variables
- Loops
- items()
3. Python program
Create student_dictionary.py.
"""
# Student Information Dictionary
student = {    "Name": "Vaishnavi",    "Roll Number": "101",    "Branch": "AIML",    "Marks": 90,    "College": "BVRIT Hyderabad"}# Display student detail
sprint("--- STUDENT INFORMATION ---")
for key, value in student.items():
  print(key, ":", value)


"""
4. Sample output
--- STUDENT INFORMATION ---

Name : Vaishnavi
Roll Number : 101
Branch : AIML
Marks : 90
College : BVRIT Hyderabad


5. Explanation
Step 1 – Dictionary creation
student = {    "Name": "Vaishnavi",    "Roll Number": "101"}



Creates a dictionary containing keys and values.

Step 2 – Dictionary traversal
for key, value in student.items():



The items() method provides each key-value pair.

Step 3 – Display
print(key, ":", value)



Prints the information.
6. Practical extension
Try adding a new key:
student["Year"] = 2



Try updating a value:
student["Marks"] = 95



Try accessing a value:
print(student.get("Branch"))



Output:
AIML


Mentor question: What is the difference between a list and a dictionary?

Answer: A list stores elements accessed using indexes, whereas a dictionary stores key-value pairs accessed using keys.
"""


#Assignment 4 – Safe Calculator

"""
1. Problem Statement
Develop a Python calculator that accepts two numbers and an arithmetic operator from the user.

The calculator should perform:
- Addition
- Subtraction
- Multiplication
- Division
It should also handle invalid inputs and division by zero.
2. Concepts used
- Functions
- Parameters and arguments
- Return statements
- Conditional statements
- Exception handling
- Input/output
3. Python program
Create safe_calculator.py.
"""
# Safe Calculator
def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if b == 0:   
    raise ZeroDivisionError("Cannot divide by zero")    
  return a / b
  try:    # Accept input   
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))    # Perform operation    
    if operator == "+":
    result = add(num1, num2)
  elif operator == "-": 
    result = subtract(num1, num2)
  elif operator == "*": 
    result = multiply(num1, num2)
  elif operator == "/":      
    result = divide(num1, num2)
  else:        
    raise ValueError("Invalid operator")
    print("Result:", result)
except ZeroDivisionError as e:
      print("Error:", e)
except ValueError as e: 
    print("Invalid input:", e)


"""
4. Sample output – Addition
Enter first number: 20
Enter operator (+, -, *, /): +
Enter second number: 10

Result: 30.0


5. Sample output – Division by zero
Enter first number: 20
Enter operator (+, -, *, /): /
Enter second number: 0

Error: Cannot divide by zero


6. Explanation
Function	Purpose
add(a,b)	Adds two numbers
subtract(a,b)	Subtracts two numbers
multiply(a,b)	Multiplies two numbers
divide(a,b)	Divides two numbers

Why use functions?

Instead of writing all arithmetic logic inside one large block, each operation is separated into a reusable function.

Why use try-except?

It prevents invalid numeric inputs and division errors from terminating the program unexpectedly.

Mentor question: Why did you use raise?

Answer: The raise keyword explicitly triggers an exception when an invalid operation is encountered, allowing the exception handler to respond.
"""

#Assignment 5 – Student Performance Management System
"""
Final integrated assignment
This assignment is an improved version of your mini-project in Part 1.
1. Problem Statement
Develop a Python application that accepts student details and marks in five subjects, calculates the student's performance and generates a report.
2. Requirements
1. Accept student name and roll number.
2. Accept marks in five subjects.
3. Store marks in a list.
4. Calculate total and average using functions.
5. Find highest and lowest marks.
6. Assign a grade.
7. Check whether the student passed every subject.
8. Store all details in a dictionary.
9. Handle invalid input.
3. Python program"""

#Create student_management.py.
# Student Performance Management System
# Function to calculate total
def calculate_total(marks):
  return sum(marks)# Function to calculate average
def calculate_average(marks): 
  return sum(marks) / len(marks)# Function to calculate grade
def calculate_grade(average):  
  if average >= 90:     
    return "A"   
  elif average >= 75:  
    return "B"   
  elif average >= 60: 
    return "C"   
  elif average >= 40:  
    return "D"    
  else:       
    return "Fail"# Main function
def main():  
  try:   
    name = input("Enter student name: ")    
    roll = input("Enter roll number: ")  
    marks = []


"""
4. Sample output
Enter student name: Vaishnavi
Enter roll number: 101

Enter subject 1 marks: 80
Enter subject 2 marks: 75
Enter subject 3 marks: 90
Enter subject 4 marks: 65
Enter subject 5 marks: 85

--- FINAL STUDENT REPORT ---

Name : Vaishnavi
Roll Number : 101
Marks : [80.0, 75.0, 90.0, 65.0, 85.0]
Total : 395.0
Average : 79.0
Highest : 90.0
Lowest : 65.0
Grade : B
Result : Pass


5. Explanation of the complete application
Component	Functionality
Input section	Accepts student details
List	Stores subject marks
Loop	Repeats input for five subjects
Functions	Calculate total, average and grade
Conditions	Assign grade and result
Dictionary	Organizes the report
Exception handling	Handles invalid input

6. Important test cases
Don't test only successful inputs. Test these cases too.
Test case	Expected result
All marks between 40 and 100	Pass
One subject mark is 35	Fail
One mark is 110	Invalid marks
One mark is -5	Invalid marks
User enters abc as marks	Invalid numeric input
All marks are 100	Grade A, Pass
All marks are 0	Fail

Important distinction: Grade is based on average marks, whereas pass/fail is based on every subject's individual marks. A student can receive a grade based on the average but still fail an individual subject."""
