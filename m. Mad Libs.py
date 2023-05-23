"""
Uses constants to tell a mad libs story.

You can view the result here: https://codeinplace.stanford.edu/cip3/share/pzkxF7r5oc0VwfJEv1G0
"""

# Fun fact: 6174 is known as Kaprekar's constant,
# and it's a pretty mysterious number :)

WIZARD = 'Karel'
NUMBER_OF_FRUIT = 6174
FRUIT = 'mangoes'

def main():
    print("There once was a wizard by the name of " + WIZARD + " who loved to eat " + FRUIT + ".")
    print(WIZARD + " always kept a stash of " + str(NUMBER_OF_FRUIT) + " " + FRUIT + " in their house...")

if __name__ == '__main__':
    main()
