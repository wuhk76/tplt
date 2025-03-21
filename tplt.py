import math
import numpy as np
import matplotlib.pyplot as plt

class Turtle:

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.d = 0.0
        self.p = 0

    def up(self):
        self.p = 0

    def down(self):
        self.p = 1

    def goto(self , x , y , color = 'k'):
        if self.p == 1:
            a = [self.x , x]
            b = [self.y , y]
            plt.plot(a , b , color = color)
            self.x = float(x)
            self.y = float(y)
        else:
            self.x = float(x)
            self.y = float(y)

    def right(self , a):
        self.d -= float(a * math.pi / 180)

    def left(self , a):
        self.d += float(a * math.pi / 180)

    def setheading(self , a):
        self.d = float(a * math.pi / 180)

    def forward(self , d , color='k'):
        if self.p == 1:
            x = [self.x , self.x + d * math.cos(self.d)]
            y = [self.y , self.y + d * math.sin(self.d)]
            self.x += d * math.cos(self.d)
            self.y += d * math.sin(self.d)
            plt.plot(x , y , color = color)
        else:
            self.x += d * math.cos(self.d)
            self.y += d * math.sin(self.d)

    def back(self , d , color = 'k'):
        if self.p == 1:
            x = [self.x , self.x - d * math.cos(self.d)]
            y = [self.y , self.y - d * math.sin(self.d)]
            plt.plot(x , y , color = color)
            self.x -= d * math.cos(self.d)
            self.y -= d * math.sin(self.d)
        else:
            self.x -= d * math.cos(self.d)
            self.y -= d * math.sin(self.d)

    def circle(self , r , color = 'k'):
        if self.p == 1:
            t = np.linspace(0 , 2 * math.pi , 100 + 100 * int(round(r)))
            x = self.x + r * np.cos(t)
            y = self.y + r * np.sin(t)
            plt.plot(x , y, color = color)

    def home(self , color = 'k'):
        if self.p == 1:
            x = [self.x , 0]
            y = [self.y , 0]
            plt.plot(x , y , color = color)
            self.x = 0.0
            self.y = 0.0
        else:
            self.x = 0.0
            self.y = 0.0

    def locate(self):
        return((self.x , self.y , (self.d * (180 / math.pi))))

tplt = Turtle()