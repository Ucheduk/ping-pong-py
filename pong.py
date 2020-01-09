# A Basic Ping Pong Ball Game

import turtle as t
import os

wn = t.Screen()
wn.title("Ping Pong by @DukStack")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(2)

# Score
score_a = 0
score_b = 0

# Paddle A
pad_a = t.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = t.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('white')
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = -0.05

# Pen
pen = t.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} | Player B: {}".format(str(score_a), str(score_b)), align="center", font=("Courier", 16, "normal"))

# Pause pen
pause_pen = t.Turtle()
pause_pen.speed(0)
pause_pen.color('white')
pause_pen.penup()
pause_pen.hideturtle()
pause_pen.goto(0, 0)

# Paddle A Functions
def pad_a_up():
  y = pad_a.ycor()
  y += 20
  pad_a.sety(y)

def pad_a_down():
  y = pad_a.ycor()
  y -= 20
  pad_a.sety(y)


# Paddle B Functions
def pad_b_up():
  y = pad_b.ycor()
  y += 20
  pad_b.sety(y)

def pad_b_down():
  y = pad_b.ycor()
  y -= 20
  pad_b.sety(y)

def do_nothing():
  pass

pause = False

# Pause game
def pause_game():
  global pause
  pause = not(pause)

# Keyboard binding
wn.listen()
wn.onkeypress(pause_game, 'Escape')


# Main game loop
while True:
  wn.update()


  if pause != True:

    pause_pen.clear()

    # Move the left and right paddle
    wn.onkeypress(pad_a_up, 'w')
    wn.onkeypress(pad_a_down, 's')
    wn.onkeypress(pad_b_up, 'Up')
    wn.onkeypress(pad_b_down, 'Down')

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      os.system('aplay bounce.wav&') # afplay for Mac | aplay for Linux | winsound.PlaySound('bounce.wav', winsound.SND_ASYNC) for windows 

    if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      os.system('aplay bounce.wav&')

    if ball.xcor() > 390:
      ball.goto(0, 0)
      ball.dx *= -1
      score_a += 1
      pen.clear()
      pen.write("Player A: {} | Player B: {}".format(str(score_a), str(score_b)), align="center", font=("Courier", 16, "normal"))
      

    if ball.xcor() < -390:
      ball.goto(0, 0)
      ball.dx *= -1
      score_b += 1
      pen.clear()
      pen.write("Player A: {} | Player B: {}".format(str(score_a), str(score_b)), align="center", font=("Courier", 16, "normal"))


    # Ball Paddle colliding
    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50):
      ball.setx(330)
      ball.dx *= -1
      os.system('aplay bounce.wav&')

    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50):
      ball.setx(-330)
      ball.dx *= -1
      os.system('aplay bounce.wav&')

  else:
    # Disable the left and right paddle and pause game
    wn.onkeypress(do_nothing, 'w')
    wn.onkeypress(do_nothing, 's')
    wn.onkeypress(do_nothing, 'Up')
    wn.onkeypress(do_nothing, 'Down')
    pause_pen.write("Game Paused", align="center", font=("Courier", 14, "normal"))
