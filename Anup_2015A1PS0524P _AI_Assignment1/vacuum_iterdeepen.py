import copy
import random
from collections import defaultdict

class node(object):
	def __init__(self, pos, size, dirt):
		self.pos = pos
		self.parent = None
		self.dimen = size
		self.dirt_arr = dirt
		self.state = (pos,len(dirt))

	def __str__(self):
		return str(self.pos)

	def childNodes(self):
		x, y = self.pos
		n, m = self.dimen
		pos1 = (x+1, y)
		pos2 = (x, y+1)
		pos3 = (x-1, y)
		pos4 = (x, y-1)
		pos_arr = [pos1, pos2, pos3, pos4]
		arr = copy.copy(pos_arr)
		for p in pos_arr:
			r, s = p
			if (r < 0 or s < 0 or r > n - 1 or s > m - 1):
				#print'P: ' + str(p)
				arr.remove(p)

		n_arr = []
		for p in arr:
			n = node(p, self.dimen, copy.copy(self.dirt_arr))
			n_arr.append(n)

		return n_arr


	def addChild(self, n):
		n.parent = self

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

v_states = defaultdict(bool)


def deepen(nod,d,rec_d):
	#print 'hi'
	#print nod.pos
	if nod.pos in nod.dirt_arr:
			nod.dirt_arr.remove(nod.pos)
			#print nod.dirt_arr

	if ((not (nod.dirt_arr)) and (nod.pos in getcorners(nod.dimen))):
		print 'yay'
		res_nod = nod
		return nod, res_nod


	if (d >= rec_d):
		return nod, 0

	else:
		t = 0
		#print d
		#print nod.pos
		children = nod.childNodes()
		arr = children
		for n in children:
			if v_states[n.state] == True:
				arr.remove(n)
				#print n.pos
				continue
			else:
				v_states[n.state] = True
		#print arr
		if arr:
			for n in arr:
				t = deepen(n, d+1,rec_d)
				#print t
				nod.addChild(t[0])
				#print t[0].pos
				#print t[0].pos
				if t[1] != 0:
					break
			else:
				#print 'khaali'
				i = random.randint(0,len(children)-1)
				#print len(children)
				n = children[i]
				#print n.pos
				t = deepen(n, d+1, rec_d)
				#print t
				nod.addChild(t[0])

		return nod, t[1]


def iterDeepen(nod):
	rec_d = 100
	while(True):
		d = 0
		res = deepen(nod,d,rec_d)
		if res[1] == 0:
			#print str(rec_d) + 'exceeded'
			rec_d += 1

		elif res[1] != 0:
			#print res[1]
			break

	return res[1]


#dirt = [(1,2),(2,1),(3,2),(4,3),(5,4),(5,3),(6,7)]


def explore(queue):
	while(queue):
		root = queue.pop(0)
		#print queue((not (nod.dirt_arr)) and (root.pos in getcorners(nod.dimen)))
		if root.pos in root.dirt_arr:
			root.dirt_arr.remove(root.pos)
			#print root.dirt_arr

		if (not (root.dirt_arr)) and (root.pos in getcorners(root.dimen)):
			break

		else:
			arr = root.childNodes()
			for nod in arr:
				root.addChild(nod)
				#print nod.dirt_arr
			queue = queue + arr

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
init_pos = (1,1)
dirt = genDirt(size,50)
root = node(init_pos, size, dirt)
#print getcorners(root.dimen)
queue = [root]
last_node = iterDeepen(root)
res_path = tracePath(last_node)
print res_path
cost = len(res_path)*2 + len(dirt)
print 'cost: ' + str(cost)
