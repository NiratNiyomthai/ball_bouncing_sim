# 8 Player Pong

An endless 8 player pong game with two teams and a point counter.
Contains 10 balls.
Recommended to play with friends. Post-game effects may include anger and violence.
There will be a notification for every 10 points a side scores.

# HOW TO RUN
Download pong.py and run it in an editor.
The editor will need to be able to run Python and you must be connected to the internet.


# CONTROLS

Blue side

Up - Down

W - S 

E - D 

R - F 

T - G 


Red side

Up - Down

I - K 

O - L 

P - : 

[ - ' 

# VIDEO DEMO

https://youtu.be/W3MBuugvs_A


# UML DIAGRAM


![Screenshot 2024-12-16 170303](https://github.com/user-attachments/assets/599dce8b-f210-494b-8c61-190f0a24cb23)






# HOW TO MODIFY
Amount of balls: 

Line 117-118
~~~
def create_balls(self):
        for _ in range(10):
 ~~~       
Modify the value in range.

Paddle Speed:

Line 24-28
~~~
def move(self):
        if self.moving_up and self.paddle.ycor() < 290:
            self.paddle.sety(self.paddle.ycor() + 0.5)
        if self.moving_down and self.paddle.ycor() > -290:
            self.paddle.sety(self.paddle.ycor() - 0.5)
~~~
Modify the value in self.paddle.set; 0.5 is the default. Too high of a value and the paddles will teleport from the top to bottom.
          
Keybinds:

Line 104-115
~~~
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
~~~
Modify the letters for each paddle to the desired key. The first one will be up, the second will be down.



Sophistication level: 80
Have fun!
