#SARANSH MOHANTY-2015A1PS0687P
import copy
import random
import sys
import turtle
import time

#Tile array
tiles=[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]

green=1
blue=0
unoccupied=2
count=0
class tile(object):
	def __init__(self,size):
		self.size=size
		#self.color=color
		self.blue_color=[]
		self.green_color=[]
		#self.player=player
		self.goal_test=False
	green=1
	blue=0
	unoccupied=2
	
	def get_column(self):
		occupied=self.green_color+self.blue_color
		available_ind = [0 for j in range(4)]
		for i in range(4):
			m = -1
			for x in occupied:
				if x[0] == i:
					if m < x[1]:
						m = x[1]
			available_ind[i] = m
		return available_ind

	def next_move(self):
		nextmove=[]
		n_move=[]
		nextmove=self.get_column()
		for i in range(4):
			j = nextmove[i]
			if ((i,j+1) in tiles):
				n_move.append((i, j + 1))
		return n_move
	def create_moves(self,posn,player):
		new_tile=tile(self)
		new_tile.blue_color=copy.copy(self.blue_color)
		new_tile.green_color=copy.copy(self.green_color)
		if player is blue:
			new_tile.blue_color.append(posn)
		if player is green:
			new_tile.green_color.append(posn)
		return new_tile

#create all the possible states and pass their parents attributes to their respective nodes
#successor function
		
	def nexttiles(self, Player):
		nextmove = self.next_move()
		next_tiles = []
		for x in nextmove:
			new_tile = self.create_moves(x, Player)
			next_tiles.append(new_tile)
		return next_tiles

#Turtle graphics start here
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
        self.shape("triangle")
        self.pensize(4)
        self.color("green")
        self.penup()
        self.speed(0)

class Agent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
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
 	if P == green:
 		pen = user_pen
 	elif P == blue:
 		pen = agent_pen
 	screen_x = -250 + (x*50)
 	screen_y = 250- (y*50)
 	pen.goto(screen_x, screen_y)
 	pen.stamp()

def markArr(arr, Player):
	for x in arr:
		markPoint(x, Player)

#Scoring function

def utility(tile,p):
	util=0
	t=tile
	score_arr=[]
	possible_posn=[]
	if p is blue:
		comrade=[]
		enemy=[]
		enemy=t.green_color
		comrade=t.blue_color
	if p is green:
		comrade=[]
		enemy=[]
		comrade=t.green_color
		enemy=t.blue_color
	

	nm=[]
	nm=t.blue_color+t.green_color
	for i in nm:
		x,y=i
		
		#3 friends together
		if ((x-1,y) in tiles and (x-1,y) in comrade and (x-2,y) in tiles and (x-2,y) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break
		if ((x+1,y) in tiles and (x+1,y) in comrade and (x+2,y) in tiles and (x+2,y) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break	
		if ((x-1,y) in tiles and (x-1,y) in comrade and (x+1,y) in tiles and (x+1,y) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break
		if ((x,y-1) in tiles and (x,y-1) in comrade and (x,y-2) in tiles and (x,y-2) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break
		if ((x,y-1) in tiles and (x,y-1) in comrade and (x,y+1) in tiles and (x,y+1) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break
		if ((x,y+1) in tiles and (x,y+1) in comrade and (x,y+2) in tiles and (x,y+2) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break

		if ((x+1,y+1) in tiles and (x+1,y+1) in comrade and (x+2,y+2) in tiles and (x+2,y+2) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break

		if ((x-1,y-1) in tiles and (x-1,y-1) in comrade and (x-2,y-2) in tiles and (x-2,y-2) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break
		if ((x+1,y-1) in tiles and (x+1,y-1) in comrade and (x-1,y+1) in tiles and (x-1,y+1) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break
		if ((x+1,y+1) in tiles and (x+1,y+1) in comrade and (x+2,y+2) in tiles and (x+2,y+2) in comrade and (x,y) in tiles and (x,y) in comrade):
			util += 1
			tile.goal_test=True
			break

	return util


def alpha_beta(tile,a,depth,limit,alpha,beta):
	max_depth=limit
	p1=a
	global count
	count +=1
	if (p1 == green):
		p2 = blue
		comrade=tile.green_color
		enemy=tile.blue_color
	elif(p1 == blue):
		p2=green
		comrade=tile.blue_color
		enemy=tile.green_color

	score=utility(tile,p1)-utility(tile,p2)
	if(tile.goal_test == True or (tile.green_color+tile.blue_color==tiles) or depth>=limit):
		return score,[tile],alpha,beta
	else:
		
		depth+=1
		if depth % 2 == 1:
			available_moves=tile.nexttiles(p1)
			possible_next_states=[]
			
			for i in available_moves:
				temp=alpha_beta(i,p1,depth,max_depth,alpha,beta)
				if(temp[0]>beta):
					break
				if(temp[0]>alpha):
					alpha=temp[0]
					#print(alpha)
				possible_next_states.append(temp)
			
			try:
				#print("hi if",depth,score)
				goal=max(possible_next_states,key=lambda x:x[0])
				goal[1].append(tile)
				alpha= -2
				return goal[0], goal[1],alpha,beta
				
			except:
				#print("hi if exc")
				alpha=-2
				return 10,[tile],alpha,beta

			
		elif depth % 2 == 0:
			available_moves=tile.nexttiles(p2)
			possible_next_states=[]
			for i in available_moves:
				temp=alpha_beta(i,p1,depth,max_depth,alpha,beta)
				if(temp[0]<alpha):
					break
				if(temp[0]<beta):
					beta=temp[0]
					
				possible_next_states.append(temp)
			
			try:
				
				goal=min(possible_next_states,key=lambda x:x[0])
				goal[1].append(tile)
				beta=2
				return goal[0],goal[1],alpha,beta

			except:
				beta=2
				return -10,[tile],alpha,beta

initial_tile=tile(4)
current_tile=initial_tile
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Align3")
wn.setup(700,700)
size=(4,4)
tile_pen = Pen()
user_pen = User()
agent_pen = Agent()
draw_floor(size)
Player=blue
start=time.clock()
while(current_tile.goal_test == False):
	limit=10
	if (Player==blue):
		final = alpha_beta(current_tile, blue, 0, limit,-2,2)
		final_arr=final[1]
#checking root node proximity
		try:
			current_tile = final_arr[-2]
		except:
			print ("Humanity lives to die another day")
		markArr(current_tile.blue_color, blue)
		markArr(current_tile.green_color, green)
		print("number of nodes generated= ",count)
		Player = green
	elif (Player == green):
		print("Enter column (0,1,2,3)")
		col = int(raw_input().strip())
		nxt_pos = (col, current_tile.get_column()[col] + 1)
		markPoint(nxt_pos,green)
		next_tile = current_tile.create_moves(nxt_pos, Player)
		Player = blue
		current_tile = next_tile
end=time.clock()
#ended the code execution time
#total time 
time_taken=end-start
#printing various performance and evaluation parameters
print(" the total time taken = ",time_taken)
nodes_ms=count/(1000*time_taken)
print("total nodes per millisecond= ",nodes_ms)
print("Total bits occupied by one node = "+str(sys.getsizeof(tile)))
print("R7 = 0.56")
#***************************************************************THE END****************************************************************
