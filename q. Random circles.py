"""Write a program that draws circles at random positions with random colors on the canvas. 
You are provided with the constants N_CIRCLES (the number of circles to draw),
 CANVAS_WIDTH and CANVAS_HEIGHT (the width and height of the canvas, respectively),
 and CIRCLE_SIZE (which is both the width and height of the circle)

You can view the result here: https://codeinplace.stanford.edu/cip3/share/oZPqzpZrkmotdXUOHsvz
"""
from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 40
N_CIRCLES = 40

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)
        
def draw_random_circle(canvas):
    x = random.randint(0, CANVAS_WIDTH-CIRCLE_SIZE)
    y = random.randint(0, CANVAS_HEIGHT-CIRCLE_SIZE)
    color = random_color()
    canvas.create_oval(x, y, x+CIRCLE_SIZE, y+ CIRCLE_SIZE, color)
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
