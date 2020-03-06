#pylint:disable=E1101

# Balloon shooting game by Afrida 2020
# Written in OSX 

import turtle
import random
import os
import math
import time

win = turtle.Screen()
win.title('Simple shooting game')
win.bgpic('war2.gif')
win.setup(800,600)
win.tracer(0)
win.listen()

game_over = False
score = 0
missed = 0

class Cannon(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(2,2)
        self.up()
        self.color('blue')
        self.goto(-360, -260)

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(0.2,0.7)
        self.up()
        self.lt(50)  #left
        self.color('red')
        self.goto(-340, -240)
        self.state = "ready"
        self.speed = 4.5

    def move(self):
        self.fd(10*self.speed)

    def shoot(self):
        os.system("afplay bounce.mp3&")
        self.state = "fire"
        # print(bullet.state)

    def turnleft(self):
        self.left(5)

    def turnright(self):
        self.right(5)

class Balloon(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.shapesize(2,2)
        self.up()
        self.color('green')
        self.goto(220, 250)
        self.speed(6)

    def move(self):
        win.update()
        
        if self.ycor()<200:
            self.up()
            self.goto(self.xcor(), random.randint(-200,290))

        else:
            self.up()
            self.goto(self.xcor(), self.ycor()-5)
        
        
    def hasCollision(self, t2):
        d = math.sqrt(math.pow(t2.xcor()-self.xcor(),2) + math.pow(t2.ycor()-self.ycor(),2))

        if d<20:
            os.system("afplay collision.mp3&")
            return True
        else:
            return False

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__() #circle shape
        self.hideturtle()
        self.up()
        self.color('white')
        self.goto(200,-275)
        self.write('Score: 0', align='left', font=('Courier', 24, 'normal'))
        self.goto(200,-250)
        self.write('Missed: 0', align='left', font=('Courier', 24, 'normal'))

cannon = Cannon()
bullet = Bullet()
balloon = Balloon()
scoreboard = Scoreboard()

win.onkeypress(bullet.turnleft, "Left")
win.onkeypress(bullet.turnright, "Right")
win.onkeypress(bullet.shoot, 'space')

try:
    while not game_over:
        win.update()
        balloon.move()
        
        if bullet.state == 'fire':

            bullet.move()

            if bullet.xcor()<-400 or bullet.xcor()>400 or bullet.ycor()<-300 or bullet.ycor()>300:
                missed += 1
                bullet.state = 'ready'
                bullet.goto(-340, -240)
            
            if balloon.hasCollision(bullet):
                win.tracer(1)
                balloon.hideturtle()
                score += 1                

        if score == 1:
            game_over = True
            print("missed:", missed)
        
    scoreboard.clear()
    scoreboard.goto(0,0)
    scoreboard.write(f'GAME OVER\nScore: {score}\nMissed:{missed}', align='center', font=('Courier', 36, 'bold'))

    win.exitonclick()
    win.mainloop()

except Exception:
    pass