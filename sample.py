# check num odd or even
"""count=0
while count<3:
    number = int(input("enter number: "))
    count = count + 1
    if number%2==0:
        print("Even")
    else:
        print("Odd")"""

#max num

"""num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
if num1>num2:
    print(f'The maximun num is : {num1}')
else:
    print(f'The maximun num is : {num2}')
"""

#prime num check

"""def prime(num):
    if num<1:
        print("Not valid")
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input("enter num: "))
if prime(num):
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')"""


#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

"""def find(num):
        for q in num:
            i=[]
            if q%2==0:
                i.append(q)
                print(q)

find(range(1000,3001))    """


#Question:
"""Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3   """

"""def cal(letter,digits):
    print(len(letter.strip(" ")))
    print(len(digits))

cal("hello world","123")
"""


rows = 20

# Create a for loop to iterate over the rows
for i in range(1, rows + 1):
    # Create a nested for loop to iterate over the columns
    for j in range(1, i + 1):
        # Print the current number
        print(j, end=" ")

    # Print a new line at the end of each row
    print()

# w3 resources - online python practise

""" Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*     """

rows=6
for i in range(rows+1):     # 1 2 3 4 5 6
    for j in range(1,i):    # (1,1)  (1,2)  (1,3)  (1,4)  (1,5)  (1,6)
        print("*",end=" ")
    print()
for i in range(rows-1,0,-1):   #5 4 3 2
    for j in range(1,i):    # (1,5) (1,4) (1,3) (1,2)
        print("*",end=" ")
    print()



"""Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999"""



row=9
for i in range(1,row+1):  # 1 2 3 4 5 6 7 8 9
    for j in range(0,i):    # (0,1) (0,2) (0,3).....
        print(i,end=" ")
    print()      # helps to move the next line after printing the num

"""Write a Python program to create the multiplication table (from 1 to 10) of a number.
Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 """

num=int(input("enter a num: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

"""Write a Python program to find the median of three values.
Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0 
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)"""

import datetime
time=datetime.datetime.now()
print(time)

"""Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20"""
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=num1+num2
if num3>=15 and num<=20:
    print

