""" You can access the code here: https://codeinplace.stanford.edu/cip3/share/46Yu1TlKyaqmxOxZvFSy"""

import random

def main():
    print("Khansole Academy")
    num1= random.randint(10,99)
    num2= random.randint(10,99)
    sum=num1+num2
    print ("What is " + str(num1) + "+" + str(num2))
    answer=int(input("Your answer:"))
    if answer==sum:
        print("You are correct. Good Job!")
    else:
        print("Sorry. This is incorrect. The expected answer is "  +  str(sum) )
    
    
if __name__ == '__main__':
    main()
