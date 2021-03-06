#ANUP BHUTADA 2015A1PS0524P
import copy
import turtle
import random
import sys
import time

#defining the state
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
	#successor function
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
#declaring the first player
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
			del pos_dic[p[0]]
	return pos_dic

#Utility Function
def score(state, Player):

	token = 0
	score = 0
	P = Player
	if P == RED:
		filled_pos = state.redpos
	elif P == BLUE:
		filled_pos = state.bluepos

	for pos in filled_pos:
		x, y = pos
		pos_dic = getSurPos((x,y), state.dimen)
		#print pos_dic
		arr = pos_dic.items()
		pos_ind = []
		for p in arr:
			if p[1] in filled_pos:
				pos_ind.append(p[0])
		
		#defining goal states
		for i in pos_ind:

			if i-4 in pos_ind:
				state.goal = True
				score += 50
				token = 1
				break
		
		if token == 1:
			break

	return score

#defining minmax function; when depth is odd:max will be executed; when depth is even: min will be executed
def MinMax(state, Player, depth, max_depth):
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
		return s, [state]

	elif state.goal == False:
		d += 1
		#nxt = state.nextStates(Player)
		if d % 2 == 1:
			nxt = state.nextStates(P)
			if not (nxt):
				return 100, [state]
			buff = [MinMax(st, P, d, max_depth) for st in nxt]
			req = max(buff, key = lambda x : x[0])
			req[1].append(state)
			#print req[0]
			return(req[0], req[1])
		elif d % 2 == 0:
			nxt = state.nextStates(OP)
			if not (nxt):
				return -100, [state]
			buff = [MinMax(st, P, d, max_depth) for st in nxt]
			req = min(buff, key = lambda x : x[0])
			req[1].append(state)
			#print req[0]
			return(req[0], req[1])

#Execution of the program
size = (4,4)
init_state = state(size)

#setting up the GUI
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Align3")
wn.setup(700,700)

tile_pen = Pen()
user_pen = User()
agent_pen = Agent()
draw_floor(size)
#initialise Nunber of nodes explored
N = 0
t0 = time.time()
while(init_state.goal != True):
	if Player == BLUE:
		max_depth = 16
		res_arr = MinMax(init_state, BLUE, 0, max_depth)[1]
		#print res_arr
		try:
			init_state = res_arr[-2]
		except:
			print "You Lost"
		markArr(init_state.bluepos, BLUE)
		markArr(init_state.redpos, RED)
		print init_state.redpos ,init_state.bluepos
		Player = RED
		print 'No. of nodes explored =', N
	elif Player == RED:
		print 'hi'
		col = int(raw_input().strip())
		nxt_pos = (col, init_state.maxindarr()[col] + 1)
		markPoint(nxt_pos, RED)
		nxt_state = init_state.createChild(nxt_pos, Player)
		Player = BLUE
		init_state = nxt_state

t1 = time.time()
time = t1-t0
mem = sys.getsizeof(state)
print 'Time taken for playing the game =', time,'seconds'
print 'No. of nodes explored in the entire program =', N
print 'Number of nodes explored in mocrosecond =', (N/(time*1000000))
print 'Memory occupied by one node =', mem, 'bits'
