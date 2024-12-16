import turtle
import random

class Paddle:
    def __init__(self, x_position, y_position, up_key, down_key, color, screen):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=2, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_position, y_position)
        self.moving_up = False
        self.moving_down = False
        self.up_key = up_key
        self.down_key = down_key

        # Keybindings for this paddle
        screen.onkeypress(self.start_move_up, self.up_key)
        screen.onkeyrelease(self.stop_move_up, self.up_key)
        screen.onkeypress(self.start_move_down, self.down_key)
        screen.onkeyrelease(self.stop_move_down, self.down_key)

    def move(self):
        if self.moving_up and self.paddle.ycor() < 290:
            self.paddle.sety(self.paddle.ycor() + 0.5)
        if self.moving_down and self.paddle.ycor() > -290:
            self.paddle.sety(self.paddle.ycor() - 0.5)

    def start_move_up(self):
        self.moving_up = True

    def stop_move_up(self):
        self.moving_up = False

    def start_move_down(self):
        self.moving_down = True

    def stop_move_down(self):
        self.moving_down = False

    def ycor(self):
        return self.paddle.ycor()

    def xcor(self):
        return self.paddle.xcor()

class Ball:
    def __init__(self, x_start, y_start, dx, dy):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(x_start, y_start)
        self.ball.dx = dx
        self.ball.dy = dy

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_y(self):
        self.ball.dy *= -1

    def bounce_x(self):
        self.ball.dx *= -1

    def reset_position(self):
        self.ball.goto(0, 0)
        self.bounce_x()

    def xcor(self):
        return self.ball.xcor()

    def ycor(self):
        return self.ball.ycor()

    def setx(self, x):
        self.ball.setx(x)

    def sety(self, y):
        self.ball.sety(y)

class PongGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("8-Player Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.paddles = []
        self.balls = []
        self.left_score = 0
        self.right_score = 0
        self.score_display = self.create_score_display()

        self.create_paddles()
        self.create_balls()

        self.screen.listen()

    def create_paddles(self):
        # Left paddles (blue)
        self.paddles.append(Paddle(-350, 200, "w", "s", "blue", self.screen))
        self.paddles.append(Paddle(-350, 100, "e", "d", "blue", self.screen))
        self.paddles.append(Paddle(-350, 0, "r", "f", "blue", self.screen))
        self.paddles.append(Paddle(-350, -100, "t", "g", "blue", self.screen))

        # Right paddles (red)
        self.paddles.append(Paddle(350, 200, "i", "k", "red", self.screen))
        self.paddles.append(Paddle(350, 100, "o", "l", "red", self.screen))
        self.paddles.append(Paddle(350, 0, "p", ";", "red", self.screen))
        self.paddles.append(Paddle(350, -100, "[", "'", "red", self.screen))

    def create_balls(self):
        for _ in range(10):
            x_start = random.randint(-100, 100)
            y_start = random.randint(-100, 100)
            dx = random.choice([-0.15, 0.15])
            dy = random.choice([-0.15, 0.15])
            ball = Ball(x_start, y_start, dx, dy)
            self.balls.append(ball)

    def create_score_display(self):
        score_display = turtle.Turtle()
        score_display.speed(0)
        score_display.color("white")
        score_display.penup()
        score_display.hideturtle()
        score_display.goto(0, 260)
        score_display.write("Blue: 0  Red: 0", align="center", font=("Courier", 24, "normal"))
        return score_display

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Blue: {self.left_score}  Red: {self.right_score}",
                                 align="center", font=("Courier", 24, "normal"))

    def display_special_text(self, side):
        special_text = turtle.Turtle()
        special_text.speed(0)
        special_text.color("yellow")
        special_text.penup()
        special_text.hideturtle()
        special_text.goto(0, 0)
        special_text.write(f"{side} Team achieved 10 Points!", align="center", font=("Courier", 24, "bold"))
        self.screen.update()
        self.screen.ontimer(special_text.clear, 1000)

    def play(self):
        while True:
            self.screen.update()

            # Move paddles
            for paddle in self.paddles:
                paddle.move()

            # Move balls
            for ball in self.balls:
                ball.move()

                # Ball collision with top wall
                if ball.ycor() > 290:
                    ball.sety(290)
                    ball.bounce_y()

                # Ball collision with bottom wall
                if ball.ycor() < -290:
                    ball.sety(-290)
                    ball.bounce_y()

                # Ball collision with paddles
                for paddle in self.paddles:
                    if abs(ball.xcor() - paddle.xcor()) < 10 and \
                            (paddle.ycor() - 30 < ball.ycor() < paddle.ycor() + 30):
                        ball.bounce_x()

                # Ball out of bounds (right side)
                if ball.xcor() > 390:
                    self.left_score += 1
                    self.update_score()
                    ball.reset_position()
                    if self.left_score % 10 == 0:
                        self.display_special_text("Blue")

                # Ball out of bounds (left side)
                if ball.xcor() < -390:
                    self.right_score += 1
                    self.update_score()
                    ball.reset_position()
                    if self.right_score % 10 == 0:
                        self.display_special_text("Red")

# Run the game
if __name__ == "__main__":
    game = PongGame()
    game.play()
