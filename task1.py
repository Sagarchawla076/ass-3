
def factorial(a):
    if(a==0):
        return 1
    return a*factorial(a-1)

output = factorial(5)
print(output)