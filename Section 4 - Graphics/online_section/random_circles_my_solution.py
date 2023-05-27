import random

from graphics import Canvas


# Define constants
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300


def main():
    print('Random Circles')
    
    # Create canvas to draw on
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Get number of circles to draw
    num_circles = random.randint(20, 50)
    
    # Draw num_circles on the canvas
    for i in range(num_circles):
        draw_random_circles(canvas)
    
    
def draw_random_circles(canvas):
    # Get a random color
    color = get_random_color()
    
    # Get a random size for the circle
    size = random.randint(20, 60)
    
    # Get circle position
    x, y = get_circle_position(size)
    
    # Draw the circles
    canvas.create_oval(x,           # left_x
                       y,           # top_y
                       x + size,    # right_x
                       y + size,    # bottom_y
                       color)       # color


def get_random_color():
    """
    This is a function to use to get a random color for each circle. 
    We have defined this for you and there is no need to edit code in this function, 
    but feel free to read it over if you are interested. 
    """
    colors = [
        'blue', 
        'purple', 
        'salmon', 
        'lightblue', 
        'cyan', 
        'forestgreen',
        'Magenta'
    ]
    return random.choice(colors)
    

def get_circle_position(size):
    # Get initial random X and Y locations to draw on
    rand_x = random.randint(0, CANVAS_WIDTH - size)
    rand_y = random.randint(0, CANVAS_HEIGHT - size)
    
    # If the initial x/y locations of the circles are too close to the edge of the canvas
    # and will cause the circle to outside the canvas' boundary,
    # then re-calculate valid coordinates until they are within the canvas' edges
    while rand_x + size > CANVAS_WIDTH:
        rand_x = random.randint(0, CANVAS_WIDTH - size)
    while rand_y + size > CANVAS_HEIGHT:
        rand_y = random.randint(0, CANVAS_WIDTH - size)
    
    # Return the random x and y coordinates to draw on 
    return rand_x, rand_y


if __name__ == '__main__':
    main()
