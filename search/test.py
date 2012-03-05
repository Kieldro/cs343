from util import PriorityQueue

t = ((1,3), ((2,2), (3,3)))
e =  set()
e.add(t)
print ((1,3), ((2,2), (3,4))) in e

q = PriorityQueue()
q.push('a', 2)
q.push('b', 3)
q.push('c', 4)
q.push('d', 1)
q.push('e', -3)
print q.pop()
print q.pop()
print q.pop()
print q.pop()

def name(a):
	print a
	tup = (1, 2, 3)
	t2 = tup + (4,)

n = name

actions = ['sit', 'stand']
action = 'jump'
n(actions + [action])
actions = actions + [action]
print actions
