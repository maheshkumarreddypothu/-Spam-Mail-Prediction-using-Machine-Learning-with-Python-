#Setting the window screen for the game
import turtle
window=turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Score
score_a=0
score_b=0

#Left Paddle
paddle_L=turtle.Turtle()
paddle_L.speed(0)
paddle_L.shape("square")
paddle_L.color("blue")
paddle_L.penup()
paddle_L.goto(-350,0)
paddle_L.shapesize(stretch_wid=5,stretch_len=1)

#Right paddle
paddle_R=turtle.Turtle()
paddle_R.speed(0)
paddle_R.shape("square")
paddle_R.color("red")
paddle_R.penup()
paddle_R.goto(350,0)
paddle_R.shapesize(stretch_wid=5,stretch_len=1)

#The Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
# ball.goto(0,0)
ball.dx=0.07
# ball.dy=0.07
ball.dy=-0.07

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0, Player B: 0",align="center",font=("courier",24,"normal"))

#Moving the paddles
#Moving the Left paddle up and down
def paddle_L_up():
    y=paddle_L.ycor()
    y=y+20
    paddle_L.sety(y)
def paddle_L_down():
    y=paddle_L.ycor()
    y=y-20
    paddle_L.sety(y)
#Moving the right paddle up and down
def paddle_R_up():
    y=paddle_R.ycor()
    y=y+20
    paddle_R.sety(y)
def paddle_R_down():
    y=paddle_R.ycor()
    y=y-20
    paddle_R.sety(y)

#Keyboard binding
window.listen()
window.onkeypress(paddle_L_up,"w")
window.onkeypress(paddle_L_down,"s")
window.onkeypress(paddle_R_up,"u")
window.onkeypress(paddle_R_down,"d")

while True:
    window.update()
    newx=ball.xcor()+ball.dx
    newy=ball.ycor()+ball.dy
    ball.setx(newx)
    ball.sety(newy)
    #Border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=ball.dy*-1
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy=ball.dy*-1
    if ball.xcor()>350:
        score_a=score_a+1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx=ball.dx*-1
    elif ball.xcor()<-350:
        score_b=score_b+1
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a,score_b), align="center", font=("courier",24,"normal"))
        ball.goto(0,0)
        ball.dx=ball.dx*-1
    if (-350 < ball.xcor()<-340) and ball.ycor()<paddle_L.ycor()+50 and ball.ycor()>paddle_L.ycor()-50:
        ball.dx=ball.dx * -1
    if (350 > ball.xcor() > 340) and ball.ycor() < paddle_R.ycor() + 50 and ball.ycor() > paddle_R.ycor() - 50:
        ball.dx = ball.dx * -1

