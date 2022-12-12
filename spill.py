import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Skjerm oppsettet
skjerm = turtle.Screen()
skjerm.title("Snake Spill")
skjerm.bgcolor("green")
skjerm.setup(width=600, height=600)
skjerm.tracer(0) # Turns off the screen updates

# Slange hodeaa
hode = turtle.Turtle()
hode.speed(0)
hode.shape("square")
hode.color("black")
hode.penup()
hode.goto(0,0)
hode.direction = "stop"

# Slange maten
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Bevegelse Funksjoner
def go_up():
    if hode.direction != "doskjerm":
        hode.direction = "up"

def go_doskjerm():
    if hode.direction != "up":
        hode.direction = "doskjerm"

def go_left():
    if hode.direction != "right":
        hode.direction = "left"

def go_right():
    if hode.direction != "left":
        hode.direction = "right"

def move():
    if hode.direction == "up":
        y = hode.ycor()
        hode.sety(y + 20)

    if hode.direction == "doskjerm":
        y = hode.ycor()
        hode.sety(y - 20)

    if hode.direction == "left":
        x = hode.xcor()
        hode.setx(x - 20)

    if hode.direction == "right":
        x = hode.xcor()
        hode.setx(x + 20)

# Keyboard knapper
skjerm.listen()
skjerm.onkeypress(go_up, "w")
skjerm.onkeypress(go_doskjerm, "s")
skjerm.onkeypress(go_left, "a")
skjerm.onkeypress(go_right, "d")

# Spill looop
while True:
    skjerm.update()

    # Sjekker om den kræsjer med grensen
    if hode.xcor()>290 or hode.xcor()<-290 or hode.ycor()>290 or hode.ycor()<-290:
        time.sleep(1)
        hode.goto(0,0)
        hode.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Fjerner de andre slange segmentene
        segments.clear()

        # Resetter scoren
        score = 0

        # Tiden det tar å resette scoren
        delay = 0.2

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Sjekker for at jeg treffer maten
    if hode.distance(food) < 20:
        # Putter maten et tilfeldig sted
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Legger til en slange segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Øker Skoren
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the hode is
    if len(segments) > 0:
        x = hode.xcor()
        y = hode.ycor()
        segments[0].goto(x,y)

    move()    

    # Sjekker om hode kolliderer med kroppen
    for segment in segments:
        if segment.distance(hode) < 20:
            time.sleep(1)
            hode.goto(0,0)
            hode.direction = "stop"
        
            # Skjuler segmentene
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Fjerner de andre segmentene
            segments.clear()

            # Resetter scoren
            score = 0

            # Tiden det tar for å
            delay = 5
        
            # Oppdaterer skoren
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

skjerm.mainloop()