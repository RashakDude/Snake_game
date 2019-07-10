import turtle
import time
import random

delay = 0.15

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake game by Rajat")
wn.bgcolor("white")
wn.setup(width=700, height=700)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.color("blue")
pen.hideturtle()
pen.goto(0,310)
pen.write("Score : 0  High Score: 0", align="center", font=("Courier", 24, "normal"))



def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")


while True:
    wn.update()

    if head.xcor()>320 or head.xcor()<-320 or head.ycor()>280 or head.ycor()<-320:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(500,500)

        segments = []
        x = random.randint(-330,330)
        y = random.randint(-330,290)
        food.goto(x,y)

        score = 0
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        delay = 0.15


    if head.distance(food) < 20:
        x = random.randint(-330,330)
        y = random.randint(-330,290)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        delay -= 0.003

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    for index in range((len(segments)-1),0,-1):
                       x = segments[index-1].xcor()
                       y = segments[index-1].ycor()
                       segments[index].goto(x,y)

    if len(segments) > 0:
                       x = head.xcor()
                       y = head.ycor()
                       segments[0].goto(x,y)
            
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(500,500)

            segments = []
            x = random.randint(-330,330)
            y = random.randint(-330,290)
            food.goto(x,y)

            score = 0
            delay = 0.15
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    time.sleep(delay)
    

wn.mainloop()
