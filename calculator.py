def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
def exponential(a,b):
    return a**b
def floordivision(a,b):
    return a//b
def calculate(a,b,c):
    match c:
       case 1:print("sum= ",addition(a,b))
       case 2:print("diff= ",subtraction(a,b))
       case 3:print("product= ",multiplication(a,b))
       case 4:print("division= ",division(a,b))
       case 5:print("remainder= ",modulus(a,b))
       case 6:print("exponent= ",exponential(a,b))
       case 7:print("quotient= ",floordivision(a,b)) 
       case _:print("invalid choice")
print("menu\n1.add\n2.sub\n3.mul\n4.div\n5.mod\n6.expo\n7")
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter choice from the menu"))
calculate(a,b,c)