"""
Write a customizable version of the classic "hello world!" program in main.py which, instead of saying "hello world!",
 prompts the user for their name and then says hello to them! 

You can view the result here: https://codeinplace.stanford.edu/cip3/share/iEnX6lwKI1Yo5M5IGfuC"""

def main():
    name= input("What is your name?")
    print ("Hello"+ str(name))

if __name__ == '__main__':
    main()
