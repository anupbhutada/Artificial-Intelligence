import turtle
import random
from vacuum_cleaner import *
import sys
import matplotlib.pyplot as plt
import time




class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
class PenDirt(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

class DirtTracer(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.pensize(4)
        self.color("blue")
        self.penup()
        self.speed(4)



n = 10
p = 0.2



def draw_floor(size,dirt):
    for y in range(size[1]):
        for x in range(size[0]):
            a = (x,y)
            screen_x = -250 + (x*50)
            screen_y = 250- (y*50)
            
            if a not in dirt:
                pen.turtlesize(2.2,2.2)
                pen.goto(screen_x,screen_y)
                pen.stamp()
            elif a in dirt:
                dirty.turtlesize(2.2,2.2)
                dirty.goto(screen_x,screen_y)
                dirty.stamp()

def trace_path(path,initial_pos):
    x,y = initial_pos

    
    screen_x = -250 + (x*50)
    screen_y = 250- (y*50)
    trace.goto(screen_x,screen_y)
    trace.stamp()
    trace.color('red')
    

    for pos in path:
        x,y = pos
        screen_x = -250 + (x*50)
        screen_y = 250- (y*50)
        trace.pendown()
        trace.goto(screen_x,screen_y)

path = res_path


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Floor")
wn.setup(700,700)
sys.setrecursionlimit(1000)

pen = Pen()
dirty = PenDirt()
trace = DirtTracer()
draw_floor(root.dimen, dirt)
trace_path(path,root.pos)

#print(agent.state)

#print(agent.path[::-1])
#print(agent.num_nodes)

time_arr1 = []
for i in range(3,21):
    
    dirt_a = genDirt((i,i), i*i//2)
    t0 = time.clock()
    root = node(init_pos, (i,i), dirt_a)
    perm = 200000
    while(True):
        root.children = []
        queue = [root]
        last_node = explore(queue,perm)
        if last_node != None:
            break
        elif last_node == None:
            #print str(perm) + ' exceeded'
            perm += 200000
    #print i
    t1 = time.clock()

    ti = float(t1-t0)
    time_arr1.append(ti)

print 'Done'

#print t3.time_arr1


plt.figure(1)
plt.subplot(211)
plot1 = plt.plot(range(3,21),time_arr1)
plt.setp(plot1, color = 'r',linewidth = 2.0)
plt.show()

plt.subplot(212)
plot2 = plt.plot(range(3,21),time_arr2)
plt.setp(plot2, color = 'r',linewidth = 2.0)
plt.show()


