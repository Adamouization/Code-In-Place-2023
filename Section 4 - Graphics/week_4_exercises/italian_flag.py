from graphics import Canvas


CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw the green part on the left
    canvas.create_rectangle(0,                  # left x
                            0,                  # top y
                            CANVAS_WIDTH /3 ,   # right x
                            CANVAS_HEIGHT,      # bottom y
                            "green")            # color
    
    # draw the red part on the right                        
    canvas.create_rectangle(CANVAS_WIDTH * 0.66,    # left x
                            0,                      # top y
                            CANVAS_WIDTH ,          # right x
                            CANVAS_HEIGHT,          # bottom y
                            "red")                  # color
    
    # No need to draw the white part as the canvas is white by default.
    

if __name__ == '__main__':
    main()
