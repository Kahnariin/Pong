import turtle


class Paddle(turtle.Turtle):

    def __init__(self, position, color='white'):
        super().__init__()
        self.speed(0)
        self.shape('square') # 20px width and 20px height by standard.
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1) # stretching its width by 5 times while keeping its height.
        self.penup()
        self.goto(position)

    def go_up(self):
        ''' This function shifts up the paddle if its "up" key pressed.'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y) # Keeping x cordinations the same, changing y cordinations according to input.
    
    def go_down(self):
        ''' This function shifts down the paddle if its "down" key pressed.'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y) # Keeping x cordinations the same, changing y cordinations according to input.