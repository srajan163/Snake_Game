from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5) #it means 10*10 size of object we create
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x,random_y)
