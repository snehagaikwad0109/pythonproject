a=int(input("Enter a number"))
def fact(x):
    if x<2:
        return 1
    else:
        return x*(fact(x-1))
b=fact(a)
print("Factorial of",a, "is:",b)