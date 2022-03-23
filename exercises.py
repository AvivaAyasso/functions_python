def sum_number(a, b):
    print(a+b)


def sum_number(a, b):
    pretty_print(a+b)

#call function

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

# #call function
# s = sum_number(5, 1)
# print(s)




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

#cllas_exercises
#1
def evenorodd(x=int(input("enter number"))):
    if x%2==0:
        return 0
    else:
        return 1
#2

def nfun(n):
    total=0
    count=0
    for i in range(n):
        n=int(input("enter number"))
        total =total+n
        count=count+1
    return (total/count)

print(nfun(3))

#3
def leng(x):
    while x!=-999:
        b=str(x)
        return len(b)

print(leng(9087))

#4
def change(c):
    x=c//20
    coins= c-(x*20)
    y=coins//10
    coinsof5=c-(x*20+y*10)
    b=(coinsof5//5)
    coinsof1= c-(x*20+y*10+b*5)
    n=coinsof1//1
    return ("notes of 20=",x,"coins of 10=",y,"coins of 5=",b,"coins of 1=", n)

print(change(76))

#5
def power(x,y):
    return (x**y)

print(power(4,2))

#6
def dis10(x,y):
    afterdis=x-(x*y)/100
    return afterdis

def price(x):
    if x>1000:
        y=int(input("enter dis"))
        return dis10(x, y)
    else:
        return x - (x*10)/100

print(price(1300))




#9
def menu(c,d):
    x=input("a-	the biggest devider\nb-	the smallest divider"
            "\nc-	the result of pow(a,b)\nd-	the result of sqrt(a)-sqrt(b)]\ne-	exit\nchoose one:")


print(menu(10,13))


#11
def pri(id):
    print("give customer", id, "special treat")


def books(id,value,bills,years):
    if value>8000 and bills==1 or years>5:
        return pri(id)
    if bills==1 or bills==1 and years>5:
        return pri(id)
    else:
        print("sorry no dis")

#12
def hello():
    name = input("enter a name")
    print("hello", name)

hello()

#13
def mul_nymber(a, b):
    c = a* b
    print(c)

mul_nymber(2, 3)

def mul_nymber(a, b):
    c = a* b
    return c

h= mul_nymber(2, 3)
#to print i will add "print(h)

#14
def looplist(x):
    for i in range(x):
        yield i

print(list(looplist(10)))

cllas_exercises

1
def avg():
    sum = 0
    count = 0
    num = input("enter anumber")
    while num != "q":
        count =+ 1
        sum = int(num)
        num = input("enter anumber")
    print(sum/count)

avg()

#2
def palindrom(st):
    start = 0
    end = len(st) - 1
    for i in range(len(st)//2):
        if st[start] != st[end]:
            print("not palindrom")
            return
        else:
            start += 1
            end -= 1
    print("palindrom")
#
palindrom("aviva")

3
def holenumber():



#6
def count_number(ls):
    newls=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in ls:
        newls[i] +=1
    return newls

my = [1, 1, 3, 3, 3, 4, 9, 8, 9]
print(count_number(my))

#quiz
#1
num = int(input("enter a number"))
count = 1
a = 1
while a <= num:
    count *= a
    print(a, count)
    a += 1

#2
num = input("enter 6 numbers:")
even = 0
odd = 0
for i in (num):
    a = int(i)
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, "even numbers")
print(odd, "odd numbers")