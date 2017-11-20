import copy

class node(object):
	def __init__(self, pos, size, dirt):
		self.pos = pos
		self.parent = None
		self.children = []
		self.dimen = size
		self.dirt_arr = dirt

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
		arr = pos_arr
		for p in pos_arr:
			r, s = p
			if (r < 0 or s < 0 or r > n - 1 or s > m - 1):
				arr.remove(p)
		try:
			arr.remove(self.parent.pos)
		except:
			pass

		n_arr = []
		for p in arr:
			n = node(p, self.dimen, copy.copy(self.dirt_arr))
			n_arr.append(n)

		return n_arr


	def addChild(self, n):
		self.children.append(n)
		n.parent = self

def getcorners(size):
	n, m = size
	return [(0,0),(n-1,0),(0,m-1),(n-1,m-1)]
	


dirt = [(1,2),(2,1),(3,2),(4,3)]




def explore(queue):
	while(queue):
		root = queue.pop(0)
		#print queue
		if root.pos in root.dirt_arr:
			root.dirt_arr.remove(root.pos)
			print root.dirt_arr

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


root = node((1,1), (5,5), dirt)
print getcorners(root.dimen)
queue = [root]
last_node = explore(queue)
res_path = tracePath(last_node)
print res_path
