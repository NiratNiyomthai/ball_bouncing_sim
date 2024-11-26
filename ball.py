import turtle

# Constants
canvas_width = 600
canvas_height = 400
ball_radius = 10
paddle_width = 10
paddle_height = 80
paddle_speed = 20

# Paddle properties
paddle2_x = canvas_width // 2 - 20  # Align paddle near the right vertical wall
paddle2_y = 0  # Initial position of the paddle

# Set up the screen
screen = turtle.Screen()
screen.setup(canvas_width + 50, canvas_height + 50)
screen.tracer(0)

# Draw the second paddle
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.shapesize(stretch_wid=paddle_height / 20, stretch_len=paddle_width / 20)
paddle2.color("green")
paddle2.penup()
paddle2.goto(paddle2_x, paddle2_y)

# Functions to control paddle 2
def move_paddle2_up():
    global paddle2_y
    if paddle2_y + paddle_height / 2 < canvas_height // 2:  # Check upper boundary
        paddle2_y += paddle_speed
        paddle2.sety(paddle2_y)

def move_paddle2_down():
    global paddle2_y
    if paddle2_y - paddle_height / 2 > -canvas_height // 2:  # Check lower boundary
        paddle2_y -= paddle_speed
        paddle2.sety(paddle2_y)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_paddle2_up, "w")
screen.onkeypress(move_paddle2_down, "x")

# Draw a sample ball for testing
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball_speed_x = 2
ball_speed_y = 2

# Ball movement logic
def move_ball():
    global ball_speed_x, ball_speed_y

    x, y = ball.position()
    # Update position
    x += ball_speed_x
    y += ball_speed_y

    # Bounce off walls
    if x + ball_radius > canvas_width // 2 or x - ball_radius < -canvas_width // 2:
        ball_speed_x *= -1
    if y + ball_radius > canvas_height // 2 or y - ball_radius < -canvas_height // 2:
        ball_speed_y *= -1

    # Bounce off paddle 2
    if (paddle2_x - paddle_width / 2 < x < paddle2_x + paddle_width / 2) and \
       (paddle2_y - paddle_height / 2 < y < paddle2_y + paddle_height / 2):
        ball_speed_x *= -1

    ball.goto(x, y)

# Main game loop
def game_loop():
    move_ball()
    screen.update()
    screen.ontimer(game_loop, 20)

# Start the game loop
game_loop()
screen.mainloop()
