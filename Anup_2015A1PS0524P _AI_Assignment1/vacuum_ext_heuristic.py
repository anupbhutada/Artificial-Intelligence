import math
import copy
'''
def dirt_generator():
	p=random.randrange(0,100,1)
	while(p>=0):
		dirt=[]
        arr=[(a.random.randrange(0,100,1)),(b.random.randrange(0,100,1))]
        dirty +=arr
        p -=1
	return dirty
'''
#dirt_arr=dirt_generator(p)
tile_size=10
tile_posn=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,9),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]
#tile_posn=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,9),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9)]
class state(object):
	def __init__(self,posn,tile_size,dirt_arr,extendedlist):
		self.posn=posn
		self.dirt_arr=dirt_arr
		self.prev_move=None
		self.next_move=[]
		self.extendedlist=extendedlist
		#is_dirty=False
	def all_moves(self):
		possible_tiles=[]
		x,y=self.posn
		possible_tiles.append((x,y+1))
		possible_tiles.append((x,y-1))
		possible_tiles.append((x+1,y))
		possible_tiles.append((x-1,y))
		available_moves=[]
		for a in possible_tiles:
			x,y=a
			if (0<=x and x<4 and y <4 and 0<=y):
				temp=state(a,4,copy.copy(self.dirt_arr),copy.copy(self.extendedlist))
				available_moves.append(temp)
		return available_moves
	
	def add_next_state(self,node):
		#for x in available_moves:
		self.next_move.append(node)
		node.prev_move=self
		node.extendedlist.append(self)
		return node
			
dirt_arr=[(1,2),(1,3),(2,2)]
current_posn=(0,0)
initial_state=state(current_posn,10,dirt_arr,[])
initial_state.prev_move=None
resting_places=[]
def rest(tile_size):
	return [(0,0),(tile_size-1,tile_size-1),(tile_size-1,0),(0,tile_size-1)]
resting_places=rest(10)
'''
goal_state=[]
goal_state.append(state(resting_places[0],4,[],tile_posn))
goal_state.append(state(resting_places[1],4,[],tile_posn))
goal_state.append(state(resting_places[2],4,[],tile_posn))
goal_state.append(state(resting_places[2],4,[],tile_posn))
'''
queue=[initial_state]

def in_tile((x,y)):
		if(0<=x and x<tile_size and 0<=y and y<tile_size):
		return True
	else:
		return False
def check_dirt_and_move(state n):
	x,y=n.posn
	b=[]
	b=current_state.extendedlist
	b.append(current_state.posn)
	for i in n.next_move:
		if i.posn in dirt_arr:
			next_state=i
			current_state.dirt_arr.remove(i.posn)
			current_state.extendedlist=b
			return state(i.posn,tile_size,current_state.dirt_arr,b)
			break
		elif (in_tile(x+1,y) and (x+1,y) in dirt_arr):
			Dirt_arr=[]
			current_state.dirt_arr.remove((x+1,y))
			next_state=state((x+1,y),tile_size,current_state.dirt_arr,b)
			return next_state
			break
		elif (in_tile(x-1,y) and (x-1,y) in dirt_arr):
			Dirt_arr=[]
			current_state.dirt_arr.remove((x-1,y))
			next_state=state((x-1,y),tile_size,current_state.dirt_arr,b)
			return next_state
			break
		elif (in_tile(x,y-1) and (x,y-1) in dirt_arr):
			Dirt_arr=[]
			current_state.dirt_arr.remove((x,y-1))
			next_state=state((x,y-1),tile_size,current_state.dirt_arr,b)
			return next_state
			break
		elif (in_tile(x,y+1) and (x,y+1) in dirt_arr):
			Dirt_arr=[]
			current_state.dirt_arr.remove((x,y+1))
			next_state=state((x,y+1),tile_size,current_state.dirt_arr,b)
			return next_state
			break
		else:
			current_state=current_state.next_move(0)
			return current_state
			break


def explore_moves(queue):
	while(queue):
		brs=[]
		bfs=[]
		current_state = queue.pop(0)
		if current_state.posn in current_state.dirt_arr:
			current_state.dirt_arr.remove(current_state.posn)
		if (not current_state.dirt_arr) and (current_state.posn in resting_places) or (current_state.extendedlist==tile_posn):
			break
		else:

			brs = current_state.all_moves()
			n=check_dirt_and_move(current_state)
			current_state.add_next_state(n)			
			'''
			for a in brs:
				x,y=a.posn

				current_state.add_next_state(a)
			'''
			queue.append(n)

		
		
	return current_state

def find_path(current_state):
	q=[]
	while(current_state.prev_move != None):
		q.append(current_state.posn)
		current_state = current_state.prev_move
	q.append(current_state.posn)
	return q[::-1]
path=[]

last_node=explore_moves(queue)
traverse_cost=2*len(path)
Tiles=[]
path=find_path(last_node)
#def dirt_generator(p):
#cost=traverse_cost+cost_cleaning
#print cost
print(path)
