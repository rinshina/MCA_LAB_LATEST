
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


import operations
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print(a,'+',b,'=',operations.add(a,b))
print(a,'-',b,'=',operations.sub(a,b))
print(a,'*',b,'=',operations.mul(a,b))
print(a,'/',b,'=',operations.div(a,b))
