from random import *
from turtle import *
from freegames import vector

player = vector(0, -150)
balls = []
speed = 10


def move_left():
    "Move player left."
    player.x -= 20


def move_right():
    "Move player right."
    player.x += 20


def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    "Draw all game objects."
    clear()

    # Draw player
    goto(player.x, player.y)
    dot(20, 'blue' if alive else 'red')

    # Draw balls
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move():
    "Move balls downward and update game state."
    for ball in balls:
        ball.y -= 10

    # Occasionally add new falling balls
    if randrange(10) == 0:
        x = randrange(-180, 180)
        ball = vector(x, 180)
        balls.append(ball)

    # Remove balls that go off-screen
    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    # Check for collisions
    for ball in balls:
        if abs(ball - player) < 20:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


# Setup screen
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
listen()
onkey(move_left, 'Left')
onkey(move_right, 'Right')

move()
done()
