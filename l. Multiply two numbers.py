"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second

You can view the result here: https://codeinplace.stanford.edu/cip3/share/qTRvjOwiEMoqQn8zRzbz
"""

def main():
    print("This program multiplies two numbers.")

    num1= int(input("Enter first number: "))

    num2=int(input("Enter second number: "))

    Multiply=num1*num2

    print (str(Multiply))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
