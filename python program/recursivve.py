# pass is used to define later the code inside function
def gayu():
    pass#nothing define here
gayu()
#factorial
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(5))

    

