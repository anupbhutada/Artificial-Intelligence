import copy
import operator
import random
from collections import defaultdict
import sys

class node(object):
	def __init__(self, pos, size, dirt):
		self.pos = pos
		self.parent = None
		self.children = []
		self.dimen = size
		self.dirt_arr = dirt
		self.state = (pos, len(dirt))
		
	def __str__(self):
		return str(self.pos)


	def childNodes(self):
		x, y = self.pos
		n, m = self.dimen
		pos1 = (x+1, y)
		pos2 = (x, y+1)
		pos3 = (x-1, y)
		pos4 = (x, y-1)
		pos_dic = {'r' : pos1, 'd': pos2, 'l': pos3, 'u': pos4}

		arr = pos_dic.items()
		for mo,p in pos_dic.items():
			r, s = p
			if (r < 0 or s < 0 or r > n - 1 or s > m - 1):
				arr.remove((mo,p))
		
		n_dic = {}
		for p in arr:
			n = node(p[1], self.dimen, copy.copy(self.dirt_arr))
			n_dic.update({p[0]: n})

		return n_dic


	def addChild(self, n):
		self.children.append(n)
		n.parent = self

def observPos(pos, dirt_arr):
	x, y = pos
	pos1 = (x+1, y)
	pos2 = (x, y+1)
	pos3 = (x-1, y)
	pos4 = (x, y-1)
	pos5 = (x+1,y-1)
	pos6 = (x+1,y+1)
	pos7 = (x-1,y+1)
	pos8 = (x-1,y-1)
	
	arr1 = [pos1,pos2,pos3,pos4]
	arr2 = [[pos5,pos6],[pos6,pos7],[pos7,pos8],[pos8,pos5]]
	scores = {'r': 0, 'd': 0, 'l': 0, 'u': 0}
	keys = ['r','d','l','u']
	for i in range(4):
		if arr1[i] in dirt_arr:
			scores[keys[i]] += 3
		for p in arr2[i]:
			if p in dirt_arr:
				#print(p)
				scores[keys[i]] += 1
	return scores

def getcorners(size):
	n, m = size
	return [(0,0),(n-1,0),(0,m-1),(n-1,m-1)]
		
def genDirt(size, p):
	dirt_arr = []
	n, m = size
	arr = random.sample(range(0,n*m), k = p)
	for x in arr:
		dirt = (x%n,x//m)
		dirt_arr.append(dirt)

	return dirt_arr

#dirt = [(1,2),(2,1),(3,2),(4,3),(9,7),(6,5),(5,8),(5,8)]
num_nodes = 0

def explore(queue, perm):
	global num_nodes
	v_states = {}
	v_states = defaultdict(bool)
	check = True
	flag = False
	while(queue):
		if len(queue) >= perm:
			check = False
		root = queue.pop(0)
		num_nodes += 1
		#print queue
		#print root.pos
		if root.pos in root.dirt_arr:
			root.dirt_arr.remove(root.pos)
			#print root.dirt_arr

		if v_states[root.state] == True:
			#print 'hi'
			#print root.pos
			continue
		else:
			v_states[root.state] = True
		#print len(v_states.items())


		if (not (root.dirt_arr)) and (root.pos in getcorners(root.dimen)):
			flag = True
			break
		
		else:
			dic = observPos(root.pos, root.dirt_arr)
			#print dic
			arr = dic.items()
			random.shuffle(arr)
			_,val = max(arr, key=lambda x : x[1])
			#print key
			keys = []
			for x in arr:
				if val == x[1]:
					keys.append(x[0])

			child_dic = root.childNodes()

			for key in keys:
				if key in child_dic.keys():
					child  = child_dic[key]
					#print key
					root.addChild(child)
					#print child.depth
					#print nod.dirt_arr
					if check:
						queue.append(child)
				'''
				else:
					child = child_dic.values()[random.randint(0,len(child_dic.items())-1)]
					#print child_dic.keys()[random.randint(0,len(child_dic.items())-1)]
					
		
			root.addChild(child)
				#print nod.dirt_arr
			if check:
				queue.append(child)

			'''
	if flag == True:
		return root


def tracePath(nod):
	path = []
	while(nod.parent != None):
		path.append(nod.pos)
		#print path
		nod = nod.parent
		#print nod.pos
	path.append(nod.pos)
	return path[::-1]

size = (10,10)
init_pos = (0,0)
dirt = genDirt(size,20)
root = node(init_pos, size, dirt)
#print getcorners(root.dimen)
queue = [root]
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


res_path = tracePath(last_node)
print 'Path for heuristic 2(improved):'
print res_path

cost = len(res_path)*2 + len(dirt)
print 'cost: ' + str(cost)

print 'Num of nodes explored'
print num_nodes

print 'Depth at which goal state is reached:'
print len(res_path)

print 'Memory Utilised by one node :'
print str(sys.getsizeof(node)/8) + ' Bytes'