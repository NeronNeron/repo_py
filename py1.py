def factorial(x):
    if x == 0:
        print('Factorial of 0 is 1')
    elif x < 0:
        print("Factorial doesn't exist")
    else:

        for i in xrange(1, x+1): 
            x *= i
            print(x)
    print("here is change")
    return 
#remove blank lines



