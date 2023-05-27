import atexit
import time

from graphics import Canvas


# Constants
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 15
DELAY = 0.01


def main():
    """
    Program entry point
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    is_started_drawing = False
    is_keep_drawing = True
    while is_keep_drawing: # can end program by clickling "stop"
        # Get mouse X/Y coordinates
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        
        # If mouse coordinates within canvas, then draw the circles
        if is_mouse_within_canvas(x, y):
            canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, color="blue")
            is_started_drawing = True
        # else:
        #     is_keep_drawing = False
        
        print(not is_mouse_within_canvas(x, y))
        print(is_started_drawing)
        print("--")
        if not is_mouse_within_canvas(x, y) and is_started_drawing:
            is_keep_drawing = False
        
        # Wait before laying more ink
        time.sleep(DELAY)
        
    
  
  
def is_mouse_within_canvas(x, y):
    """
    Calculates if the mouse is on the canvas or not.
    Returns a boolean True if it is, else returns False.
    """
    if x > 0 and x < CANVAS_WIDTH and y > 0 and y < CANVAS_HEIGHT:
        return True
    return False
    

if __name__ == "__main__":
    main()
