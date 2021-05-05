#  Snake Game created by GeekDoge  #
import turtle
import time
import random

# GAME SCREEN
window = turtle.Screen()  # Create a window screen object
window.title("Blue")    # Title of screen set to blue
window.bgcolor("white")  # Background color set to blue
window.setup(width=670, height=750) # Height and width set to 600
window.tracer(0)        # Allows animation to run. Speed set to zero.

# BORDER
border = turtle.Turtle()
border.color("black")
border.penup()
border.setposition(-320, -340)
border.pendown()
border.pensize(20)
for line in range(4):
    border.forward(640)
    border.left(90)
border.hideturtle()


# SNAKE HEAD OBJECT
head = turtle.Turtle()    # Create a head object
head.speed(0)           # Set speed of head to zero
head.shape("square")    # Set shape of head as Square
head.color("black")     # Set color as Black
head.penup()            # penup() function restricts the head object to draw lines.
head.goto(0, -60)         # Start position of head
head.direction = "stop" # Starting state of head

# FOOD OBJECT
food=turtle.Turtle()    # Create a food object
food.speed(0)           # Set food speed to zero
food.shape("circle")    # Set food shape
food.color("red")       # set food color
food.penup()            # Again same. Not needed here though
food.goto(0, 100)       # Location of first food object.

# BODY

body = []       # List of body objects

# TEXTBOX FOR SCORING

box = turtle.Turtle()   # Create turtle object
box.speed(0)            # Allows animation
box.color("black")      # text color
box.penup()
box.hideturtle()        # Box should be hidden
box.goto(0, 325)        # Box position at top of the screen
box.write("SCORE: 0   HIGH SCORE: 0", align="center")

# SCORING
score = 0       # Variable store current score
high_score = 0  # variable stores high score

# GAME OVER MESSAGE
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("red")
game_over.penup()
game_over.goto(0, 0)
game_over.hideturtle()

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()     # Retrieve y coordinate of head using ycord function
        head.sety(y+20)     # update y position by +20 pixels i.e UP
    if head.direction == "down":
        y = head.ycor()     # Retrieve y coordinate of head using ycord function
        head.sety(y-20)     # update y position by -20 pixels i.e DOWN
    if head.direction == "left":
        x = head.xcor()     # Retrieve x coordinate of head using xcord function
        head.setx(x-20)     # update x position by -20 pixels i.e LEFT
    if head.direction == "right":
        x = head.xcor()     # Retrieve x coordinate of head using xcord function
        head.setx(x+20)     # update x position by +20 pixels i.e RIGHT
# set directions
def go_up():
    # If condition to restrict the movement of snake in opposite direction.
    # i.e. snake cannot directly change direction from up to down or left to right.
    if head.direction != "down":
        head.direction = "up"   # Change direction to up
def go_down():
    if head.direction != "up":
        head.direction = "down" # Change direction to down
def go_left():
    if head.direction != "right":
        head.direction = "left"  # Change direction to left
def go_right():
    if head.direction != "left":
        head.direction = "right"  # Change direction to right

# Keyboard Inputs
window.listen()     # Reads keyboard input

# Set w, W, and up arrow key for up
window.onkeypress(go_up, "w")
window.onkeypress(go_up, "W")
window.onkeypress(go_up, "Up")

# Set s, S, and down arrow key for down
window.onkeypress(go_down, "s")
window.onkeypress(go_down, "S")
window.onkeypress(go_down, "Down")

# Set a, A, and left arrow key for left
window.onkeypress(go_left, "a")
window.onkeypress(go_left, "A")
window.onkeypress(go_left, "Left")

# Set d, D, and right arrow key for right
window.onkeypress(go_right, "d")
window.onkeypress(go_right, "D")
window.onkeypress(go_right, "Right")

# Make an infinite loop that will keep running the move function and keep updating
# the screen with delay of 0.1 sec.
while True:
    window.update()    # Keeps updating the screen.
    # Eating food
    if head.distance(food)<20:
        x = random.randint(-14, 14)     # Random integer for x position of next food object
        y = random.randint(-15, 12)     # Random integer for y position of next food object
        x=x*20                          # So that the position is always a multiple of 10
        y=y*20
        food.goto(x, y)         # update food position.

        increase_body = turtle.Turtle() # New body object
        increase_body.speed(0)
        increase_body.shape("square")
        increase_body.color("grey")
        increase_body.penup()
        body.append(increase_body)      # Body object added to body list

        score += 5

        if score>high_score:
            high_score = score
        box.clear()
        box.write("SCORE: {}   HIGH SCORE: {}".format(score, high_score), align="center")

    # Attaching body to head by changing position of every body object to the preceding one as the
    # snake moves. Doing so in reverse order i.e. moving last body object to a position of body object
    # one before it and so on with all the individual body objects.
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
    # Move first body object to the head position
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)  # Setting head coordinates to first body segment.

    # COLLISION CHECK WITH SCREEN BORDER
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>275 or head.ycor()<-315:
        game_over.write("GAME OVER\n SCORE: {}".format(score), align = "center", font = ("", 12, "normal"))
        time.sleep(1)       # delay of 1 sec
        game_over.clear()
        head.goto(0, -60)     # restarts the game by putting head at initial position.
        head.direction = "stop"

        # Hide body objects out of screen
        for index in body:
            index.goto(1000, 1000)

        # Clear body list
        body.clear()
        score = 0  # reset score to zero when collides with wall.
        # Create new box object with updated value of score = 0 and highscore.
        box.clear()
        box.write("SCORE: {}   HIGH SCORE: {}".format(score, high_score), align="center")



    move()

    # COLLISION WITH ITSELF
    for index in body:
        if index.distance(head) < 20:
            game_over.write("GAME OVER\n Score: {}".format(score), align="center", font=("", 16, "normal"))
            time.sleep(1)
            game_over.clear()
            head.goto(0, -60)
            head.direction = "stop"

            # Hide body objects out of screen
            for index in body:
                index.goto(1000, 1000)

            # Clear body list
            body.clear()

            score = 0   # Reset score to zero when self collision
            # Create new box object with updated value of score = 0 and highscore.
            box.clear()
            box.write("SCORE: {}   HIGH SCORE: {}".format(score, high_score), align="center")

    time.sleep(0.1)     # delay of 0.1 sec
