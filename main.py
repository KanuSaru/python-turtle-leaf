import turtle

# Setup
screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("black") # Background color
screen.title("Turtle: Leaf Pattern")

t = turtle.Turtle()
t.speed(10) # Drawing speed, the fastest is 0
t.pensize(4)
t.color("white") # Leaf color

# Functions, the set values correspond to the pattern 1 in the example outputs
def leaf():
    t.circle(100, 100)
    t.left(80) # Angle between leaves
    t.circle(100, 100)
    
# The magic
for i in range(9): # This can be n leaves
    leaf()
    
turtle.exitonclick()