#Anup Bhutada 2015A1PS0524P
from logic import *

class Predicate(object):
	def __init__(self, predicate, *args):
		self.name = predicate
		self.args = map(expr, args)
		self.arg_ind = None

	def __repr__(self):
		if len(self.args) == 0: # Constant or proposition with arity 0
			return str(self.op)
		elif len(self.args) >= 0:
			st = ''
			for i in range(len(self.args)):
				st = st + ' ' + str(self.sym[i]) + '(' + str(self.args[i]) + ')' 
			return st + ' ' + '%s(%s)' % (self.name, (', ').join(map(repr, self.args)))


def fol(s):
	s = s.replace(',', ' ').replace('(', ' ').replace(')', ' ')
	arr = s.split(' ')
	arr = [a for a in arr if a != '']
	#print arr
	c = 0
	predicate = arr[c]
	c += 1
	rem = ''
	for x in arr[c:]:
		rem = rem + x
	args = []
	for a in rem:
		if is_symbol(a):
			args.append(a)

	return Predicate(predicate, *args)


class KBase(object):
	def __init__(self):
		self.facts = []
		self.sentences = []

	def addsentence(self, clause):
		self.sentences.append(clause)

	def makeFact(self, clause):
		self.facts.append(clause)


class FOL(object):
	def __init__(self, sym, ante, cons, args):
		self.sym = sym
		self.antecedent = fol(ante)
		self.consequent = fol(cons)
		self.args = map(Args, args)		#will def the arg to be a variable if it is one of [x,y,z] and a const otherwise

def listliterals(clause):
	antecedents = [clause]
	all_sym = False
	while(not all_sym):
		all_sym = True
		for c in antecedents:
			if not is_symbol(c.op):
				all_sym = False
				antecedents.remove(c)
				antecedents = antecedents + c.args
	return antecedents


def forwardChaining(KBase, query):
	KBChanged = True
	while(KBChanged):
		KBChanged = False
		for clause in KBase.sentences:
			antecedents = listliterals(clause.args[0])
			for c in antecedents:
				for fact in KBase.facts:
					if c.op == fact.op:
						sub = unify(c, fact, {})
						#print sub
						#print c, fact
						try:
							n_c = subst(sub, clause)
							if not n_c in KBase.sentences:
								KBase.addsentence(n_c)
								KBChanged = True
						except:
							pass

			if set(antecedents).issubset(KBase.facts):
				if not clause.args[1] in KBase.facts:
					KBase.makeFact(clause.args[1])
					KBChanged = True

			for fact in KBase.facts:
				if query.op == fact.op:
					return unify(query, fact, {})
	return "No substitution possible"


def backwardChaining(KBase, query):
	subt_dict = {}
	for fact in KBase.facts:
		if query.op == fact.op:
			return unify(query, fact, subt_dict)
		else:
			for sent in KBase.sentences:
				if (query.op == sent.args[1].op) and (unify(query, sent.args[1], {}) is not None):
					#print unify(query, sent.args[1], {})
					subt_dict = unify(query, sent.args[1], subt_dict)
					antecedents = listliterals(sent.args[0])
					for c in antecedents:
						subt_dict.update(backwardChaining(KBase, c))
	return subt_dict

filename1 = 'predicates1.txt'

f1 = open(filename1, 'r')
facts = []
sentences = []
marker = None
for line in f1:
	#print line
	#print marker
	if line == "$facts\n":
		marker = 'facts'
		continue
	if line == "$sentences\n":
		marker = 'sentences'
		continue
	if marker == 'facts':
		facts.append(expr(line))
		#print expr(line)
	elif marker == 'sentences':
		sentences.append(expr(line))

k1 = KBase()
k1.facts = facts
k1.sentences = sentences

print "KB1"
print "Assassinate(x,Caeser)", forwardChaining(k1, expr("Assassinate(x,Caeser)")), "forwardChaining"
print "Assassinate(x,Caeser)", backwardChaining(k1, expr("Assassinate(x,Caeser)")), "backwardChaining"
print "Isruler(x)", forwardChaining(k1, expr("Isruler(x)")), "forwardChaining"
print "Isruler(x)", backwardChaining(k1, expr("Isruler(x)")), "backwardChaining"
print "IsnotLoyal(x, Caeser)", forwardChaining(k1, expr("Isnotloyal(x, Caeser)")), "forwardChaining"
print "IsnotLoyal(x, Caeser)", backwardChaining(k1, expr("Isnotloyal(x, Caeser)")), "backwardChaining"
print "Hate(x, Caeser)", forwardChaining(k1, expr("Hate(x, Caeser)")), "forwardChaining"
print "Hate(x, Caeser)", backwardChaining(k1, expr("Hate(x, Caeser)")), "backwardChaining"
print "Erupt_volcano(x)", forwardChaining(k1, expr("Erupt_volcano(x)")), "forwardChaining"
print "Erupt_volcano(x)", backwardChaining(k1, expr("Erupt_volcano(x)")), "backwardChaining"

filename3 = 'predicates3.txt'
f1 = open(filename3, 'r')
facts = []
sentences = []
marker = None
for line in f1:
	#print line
	#print marker
	if line == "$facts\n":
		marker = 'facts'
		continue
	if line == "$sentences\n":
		marker = 'sentences'
		continue
	if marker == 'facts':
		facts.append(expr(line))
		#print expr(line)
	elif marker == 'sentences':
		sentences.append(expr(line))

k3 = KBase()
k3.facts = facts
k3.sentences = sentences
print "KB3"
print "Interested(x, Shopping)", forwardChaining(k3, expr("Interested(x, Shopping)")), "forwardChaining"
print "Interested(x, Shopping)", backwardChaining(k3, expr("Interested(x, Shopping)")), "backwardChaining"
