"""Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke. 

You can view the result here: https://codeinplace.stanford.edu/cip3/share/eiwqh239ZRrzdxcTs6T9"""

PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes. Enter 'Joke'"

def main():
    user_input = input("What do you want?")
    if user_input=="Joke":
        print (JOKE)
    else: 
        print(SORRY)

if __name__ == "__main__":
    main()
