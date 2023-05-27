from graphics import Canvas
import random


CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
N_CIRCLES = random.randint(10,  # minimum range
                           20)  # maximum range


def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Make background black to look like space
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "black")
    
    # draw random number of circles
    for i in range(N_CIRCLES):
        draw_circle(canvas)


def draw_circle(my_canvas):
    circle_size = random.randint(2, 30)
    
    random_top_x = random.randint(0, CANVAS_WIDTH - circle_size)
    random_top_y = random.randint(0, CANVAS_HEIGHT - circle_size)
    
    bottom_x = random_top_x + circle_size
    bottom_y = random_top_y + circle_size
    
    color = random_color()
    
    my_canvas.create_oval(
        random_top_x, # top left X
        random_top_y, # top left y
        bottom_x,     # bottom right x
        bottom_y,     # bottom right y
        color         # random
    )        
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ["red", "white", "lightblue", 'yellow', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    color = random.choice(colors)
    return color


if __name__ == '__main__':
    main()
