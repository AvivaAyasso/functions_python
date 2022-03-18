#How to work with functions
#1
def pretty_print(num):
    print('****************************')
    print('the number is')
    print(num)
    print('****************************')

def sum_number(a, b):
    pretty_print(a+b)

#call function
sum_number(5, 1)

#2
def sum_number(a, b):
    if a * b > 10:
        print('a & b is bigger than 10')
    else:
        print('a & b is lower than 10')

#call function
sum_number(5, 7)

#3
def sum_number(a, b):
    pretty_print(a+b)

def sub_number(a, b):
    pretty_print(a-b)

def div_number (a, b):
    pretty_print(a/b)

def mul_number(a,b):
    pretty_print(a*b)

#call function
mul_number(6,7)
div_number(6, 7)
sub_number(6, 7)
sum_number(6, 7)



#3A
def sum_number(a, b):
    z = a + b
    return z

#call function
s = sum_number(5, 1)
print(s)

#4
def sum_number(a, b):
    c = a + b
    return c

def sub_number(a, b):
    c = a - b
    return c

def div_number (a, b):
    c = a / b
    return c

def mul_number(a,b):
    c = a * b
    return c

#call function
s = sum_number(5, 1)
print(s)


num = input("What calculation operation would you like to perform:\nto join press 1\nto subtraction Press 2\nto division press 3\nto double tap 4\n")
if num == "1":
    print("enter 2 number")
    a = int(input("enter first number"))
    b = int(input("enter secand number"))
    pretty_print(sum_number(a, b))
if num == "2":
    print("enter 2 number")
    a = int(input("enter first number"))
    b = int(input("enter secand number"))
    pretty_print(sub_number(a, b))
if num == "3":
    print("enter 2 number")
    a = int(input("enter first number"))
    b = int(input("enter secand number"))
    pretty_print(div_number(a, b))
if num == "4":
    pretty_print(print("enter 2 number"))
    a = int(input("enter first number"))
    b = int(input("enter secand number"))
    mul_number(a, b)