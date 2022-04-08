from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() # will allow us to inherit from the other class
        self.shape("circle") # creates the shape of the food
        self.penup() # makes sure that the moving object that you've created does not draw anything on the window
        self.shapesize(stretch_len= 0.5, stretch_wid =0.5) # The size of food
        self.color("blue") # color of food
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # This is so that the food will randomly move around within the grid
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # This allows us to be have to have the food move around