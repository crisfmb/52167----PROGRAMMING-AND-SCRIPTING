# Cristina Borges, 09-Feb-18

def collatz(num): # Condition while input number was different then 1
    while num != 1:
        print(num)
        if num % 2 == 0: # Check if the number is an even or odd.
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        print(num)
        print('Done :-)')

def main():
    num = int(input('Input an integer: ')) # enter a number
    collatz(num)

main()
