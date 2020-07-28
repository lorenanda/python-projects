# From "Automate the boring stuff wih python"
# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1. Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    n = input("Enter a number: ")
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print("You have to enter an integer.")