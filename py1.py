def factorial(x):

    if x == 0:

        print('Factorial of 0 is 1')

    elif x < 0:

        print("Factorial doesn't exist")

    else:

        for i in xrange(1, x):

            x *= i

            print(x)

    return 
