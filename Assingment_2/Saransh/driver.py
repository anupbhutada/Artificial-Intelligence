import sys
import time
import copy
import turtle

print("1 to get the blank board")
print("Which method do you want to use?")
print("2-minimax 3-alpha beta")
print ("press 4 to get all the statistics(R1-R12)")

c = int(raw_input().strip())
if c == 1:
        class Pen(turtle.Turtle):
            def __init__(self):
                turtle.Turtle.__init__(self)
                self.shape("square")
                self.color("white")
                self.penup()
                self.speed(0)
        tile_pen = Pen()
        def draw_floor(size):
                for y in range(size[1]):
                        for x in range(size[0]):
                                a = (x,y)
                                screen_x = -250 + (x*50)
                                screen_y = 250- (y*50)
                                pen = tile_pen
                                pen.turtlesize(2.2,2.2)
                                pen.goto(screen_x,screen_y)
                                pen.stamp()
        def draw_tile():
                wn = turtle.Screen()
                wn.bgcolor("red")
                wn.title("Empty board")
                wn.setup(700,700)
                size=(4,4)
                draw_floor(size)
		
if c == 1:
        draw_tile()
elif c == 2:
	import align3
elif c == 3:
	import align_ab
elif c == 4:
        Final_stat='''
        R1=7311785
        R2=536 bits
        R3= 16 depth
        R4=3463.26 seconds
        R5=0.00211 nodes per microsecond
        R6=3175939
        R7=0.56
        R8=1107.27
        R9= 3.3*10^9 bits in minimax and in 1.43*10^9 alpha beta
        R10=3463.26 seconds for minimax and1107 seconds for alpha beta
        R11=10
        R12=20
        '''
        print(Final_stat)
else:
	print("invalid input")

