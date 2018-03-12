# Cristina Borges 12-Mar-18

# A function called factorial that takes a single argument and returns factorial


def factorial(number):
    result = 1

    for number in range(number, 0, -1):
        result *= number

    return result

print ('The factorial of', 5, 'is', factorial(5))
print ('The factorial of', 7, 'is', factorial(7))
print ('The factorial of', 10, 'is', factorial(10))