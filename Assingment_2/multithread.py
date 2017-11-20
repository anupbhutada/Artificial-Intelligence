import threading
import copy
import turtle
import random
import sys
import matplotlib.pyplot as plt
import time

class state(object):
	def __init__(self, size):
		self.redpos = []
		self.bluepos = []
		#self.children = None
		#self.parent = None
		self.dimen = size
		self.goal = False

	def __str__(self):
		return str(self.maxindarr)

	def maxindarr(self):
		all_pos = self.redpos + self.bluepos
		max_ind_arr = [0 for j in range(self.dimen[0])]
		for i in range(self.dimen[0]):
			m = -1
			for x in all_pos:
				if x[0] == i:
					if m < x[1]:
						m = x[1]
			max_ind_arr[i] = m
		return max_ind_arr

	def nextpos(self):
		max_ind_arr = self.maxindarr()
		next_pos = []
		for j in range(self.dimen[0]):
			m = max_ind_arr[j]
			if m < self.dimen[1]-1:
				next_pos.append((j, m + 1))
		return next_pos

	def createChild(self, pos, Player):
		new_state = state(self.dimen)
		new_state.redpos = copy.copy(self.redpos)
		new_state.bluepos = copy.copy(self.bluepos)
		if Player == RED:
			new_state.redpos.append(pos)
		elif Player == BLUE:
			new_state.bluepos.append(pos)
		return new_state

	def nextStates(self, Player):
		next_pos = self.nextpos()
		next_states = []
		for x in next_pos:
			new_state = self.createChild(x, Player)
			next_states.append(new_state)
		return next_states

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
class User(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.pensize(4)
        self.color("red")
        self.penup()
        self.speed(0)

class Agent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.pensize(4)
        self.color("blue")
        self.penup()
        self.speed(4)

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

def markPoint(pos, Player):
 	x, y = pos
 	P = Player
 	if P == RED:
 		pen = user_pen
 	elif P == BLUE:
 		pen = agent_pen
 	screen_x = -250 + (x*50)
 	screen_y = 250- (y*50)
 	pen.goto(screen_x, screen_y)
 	pen.stamp()

def markArr(arr, Player):
	for x in arr:
		markPoint(x, Player)

#RED is the user and BLUE is the intelligent agent
BLUE = 0
RED = 1
Player = BLUE

def getSurPos(pos, size):
	m, n = size
	x, y = pos
	pos1 = (x+1, y)
	pos2 = (x, y+1)
	pos3 = (x+1,y-1)
	pos4 = (x+1,y+1)
	pos5 = (x-1, y)
	pos6 = (x, y-1)
	pos7 = (x-1,y+1)
	pos8 = (x-1,y-1)
	pos_arr = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8]
	pos_dic = {}
	for i in range(len(pos_arr)):
		pos_dic.update({i: pos_arr[i]})
	arr = pos_dic.items()
	for p in arr:
		r, s = p[1]
		if (r < 0 or s < 0 or r > m - 1 or s > n - 1):
			#print'P: ' + str(p)
			del pos_dic[p[0]]
	return pos_dic

def score(state, Player):
	#state.goal = False
	token = 0
	score = 0
	P = Player
	if P == RED:
		filled_pos = state.redpos
	elif P == BLUE:
		filled_pos = state.bluepos

	for pos in filled_pos:
		#print pos
		#if pos not in checked_pos:
		x, y = pos
		pos_dic = getSurPos((x,y), state.dimen)
		#print pos_dic
		arr = pos_dic.items()
		pos_ind = []
		for p in arr:
			if p[1] in filled_pos:
				#score += 1
				pos_ind.append(p[0])
		#defining goal states
		for i in pos_ind:
			'''
			pos = pos_dic[i]
			new_pos_dic = getSurPos(pos, state.dimen)
			try:
				if new_pos_dic[i] in filled_pos:
					state.goal = True
					score += 50
					#print 'i', i, pos_dic[i]
			except:
				pass
			'''
			if i-4 in pos_ind:
				state.goal = True
				score += 50
				token = 1
				#print score, filled_pos, 'break'
				break
		
		if token == 1:
			break
				#print 'i-4', i-4, pos_dic[i]
	return score

def alpha_beta(state, Player, a, b, depth, max_depth):
	global N
	N += 1
	P = Player
	d = depth
	turn = P
	if P == RED:
		OP = BLUE
		filled_pos = state.redpos
	elif P == BLUE:
		OP = RED
		filled_pos = state.bluepos

	s = score(state, P) - score(state, OP)
	#print s
	if state.goal == True or d >= max_depth:
		#print d, s, filled_pos
		return s, [state], a, b

	else:
		d += 1
		buff = []
		#nxt = state.nextStates(Player)
		if d % 2 == 1:
			nxt = state.nextStates(P)
			for st in nxt:
				val = alpha_beta(st, P, a, b, d, max_depth)
				if (len(val[1]) <= 1) and (val[1][0].goal != True) and (d != max_depth):
					#print 'lol1', d, val[1][0].goal
					continue
				a = val[2]
				b = val[3]
				if val[0] > b:
					#print '1',b, val[0]
					return s, [state], a, b
				else:
					buff.append(val)
				a = max(a,val[0])
			#buff = [alpha_beta(st, P, d, max_depth) for st in nxt]
			a=-100
			try:
				req = max(buff, key = lambda x : x[0])
				#if req[0] <= b:
				#	b = req[0]
				req[1].append(state)
				#print req[0]
				return req[0], req[1], a, b
			except:
				return 100, [state], a, b
					
		elif d % 2 == 0:
			nxt = state.nextStates(OP)

			for st in nxt:
				val = alpha_beta(st, P, a, b, d, max_depth)
				if (len(val[1]) <= 1) and (val[1][0].goal != True) and (d != max_depth):
					#print 'lol0', d, val[1][0].goal
					continue
				a = val[2]
				b = val[3]
				if val[0] < a:
					#print '0',a, val[0]
					return s, [state], a, b
				else:
					buff.append(val)
				b = min(val[0],b)
			#buff = [alpha_beta(st, P, d, max_depth) for st in nxt]
			b=100
			try:
				req = min(buff, key = lambda x : x[0])
				#if req[0] >= a:
				#	a = req[0]
				req[1].append(state)
				#print req[0]
				return req[0], req[1], a ,b
			except:
				return -100, [state], a, b
				
#Execution of the program
size = (4,4)
a = -100
b = 100
init_state = state(size)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Align3")
wn.setup(700,700)

def onTextClick(event):
    x, y = event.x, event.y
    print('x={}, y={}'.format(x, y))    
    if (x >= 600 and x <= 800) and (  y >= 280 and y <= 300):
        turtle.onscreenclick(lambda x, y: turtle.bgcolor('red'))
        
canvas = turtle.getcanvas()
canvas.bind('<Button-1>', onTextClick)  

tile_pen = Pen()
user_pen = User()
agent_pen = Agent()
draw_floor(size)

N = 0

def run_game():
	res = alpha_beta(init_state, BLUE, a, b, 0, max_depth)
	res_arr = res[1]
	#print res_arr
	try:
		init_state = res_arr[-2]
	except:
		print "You Lost"
		markArr(init_state.bluepos, BLUE)
		markArr(init_state.redpos, RED)
		print init_state.redpos ,init_state.bluepos
		return 0

def get_input():
	print 'hi'
	col = int(raw_input().strip())
	nxt_pos = (col, init_state.maxindarr()[col] + 1)
	markPoint(nxt_pos, RED)
	nxt_state = init_state.createChild(nxt_pos, Player)
	Player = BLUE
	init_state = nxt_state
	return 0

t1 = threading.Thread(target = 'run_game')
t2 = threading.Thread(target = 'get_input')

while(init_state.goal != True):
	if Player == BLUE:
		max_depth = 10
		t1.start()
		t1.join()
		Player = RED
	elif Player == RED:
		t2.start()
		t2.join()		
print 'No. of nodes explored =', N
