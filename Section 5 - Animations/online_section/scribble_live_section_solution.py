import time

from graphics import Canvas


CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    while True:
        x, y = get_mouse(canvas)
        draw_circle(canvas, x, y)
        time.sleep(DELAY)


def get_mouse(canvas):
    x = canvas.get_mouse_x()
    y = canvas.get_mouse_y()
    print("x = " + str(x))
    print("y = " + str(y))
    print()
    return x, y


def draw_circle(canvas, x, y):
    left_x = x
    top_y = y
    right_x = x + CIRCLE_SIZE
    bottom_y = y + CIRCLE_SIZE
    circle = canvas.create_oval(left_x, top_y, right_x, bottom_y, "salmon")
    

if __name__ == "__main__":
    main()
