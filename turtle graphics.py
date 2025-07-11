import turtle

# Create the screen
wind = turtle.Screen()
wind.setup(600, 600)
wind.bgcolor('blue')  # Set background color

# Create a turtle object
my_pen = turtle.Turtle()
my_pen.color('red')           # Set turtle pen color
my_pen.shape('classic')       # Set turtle shape

# Draw a star (5 sides with 144° turns)
for i in range(5):
    my_pen.forward(100)
    my_pen.right(144)

turtle.done()  # Finish the drawing and keep the window open
