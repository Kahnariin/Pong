import turtle


class Ball(turtle.Turtle):
    
    def __init__(self, posx, posy, color="white"):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.color(color)
        self.penup()
        self.goto(posx, posy)
        
        # Delta x/y of the ball. This means ball can move 2px per frame for each direction.
        self.dx = 2
        self.dy = 2



    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        '''If the ball hits the top or bottom surfaces,
        then the sign of delta-y is changed and it results in a reflection.'''
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1
        elif self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1
        elif self.xcor() > 390:
            self.goto(0, 0)
            self.dx *= -1
        elif self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1
            

