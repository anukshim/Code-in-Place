"""The starter code for this program prints out a single random number in the range 1 to 100, inclusive.

Modify this program so that instead of printing one random number, it prints 10. 

You can view the result here: https://codeinplace.stanford.edu/cip3/share/coKP4Czt9PgxYJmzdDKm"""

import random

def main():
   for i in range (10): 
       value = random.randint(1, 100)
       print(value)

if __name__ == '__main__':
    main()
