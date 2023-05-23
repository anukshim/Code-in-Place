""" Write a program to draw a simple flag of Indonesia 
You can view the result here: https://codeinplace.stanford.edu/cip3/share/n62Fe5SPLvaeea330MDG 
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0,0,450,150,"red")
    

if __name__ == '__main__':
    main()
