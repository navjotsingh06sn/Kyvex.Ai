'''# printing name and age

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("My name is", name)
print("My age is", age)
'''

''' # adding two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print(sum) 
'''

''' # even or oddnumber
num = int(input("Enter a number: ")) 
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
print("The end")
'''

''' # find the greater number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num2, "is greater than", num1)
'''

''' # printing number from 1 - 10
for i in range(1, 11):
    print(i)
'''

''' # table of a number
num = int(input("Enter a number: "))
for i in range(1, 11):
    # print(num, "x", i, "=", num * i)
    t = num * i
    print(t)
'''

'''
# sum of number from 1 to N
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print(sum)
'''

''' # length of a string
str = input("Enter a string: ")
print(len(str))

'''

''' # reverse a string
str = input("Enter a string: ")
print(str[::-1])
'''

''' # find the largest number in a list
list = [1, 20, 37, 14, 22]
largest = list[0]
for num in list:
    if num > largest:
        largest = num
print("The largest number is:", largest)
'''

''' # create a function to add two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add(a, b):
    return a + b 

print(add(a, b))
'''

# calucalte the total marks and percentage of a student
marks = []    #creates an empty list to store marks
for i in range(5):
    mark = int(input("Enter marks  : "))  
    marks.append(mark)   #add the marks to the list 

total = sum(marks)    #add all the marks in the list to get total marks
percentage = total / 500 * 100  #calucating the percentage based on total marks

print("Total marks:", total)
print("Percentage:", percentage)