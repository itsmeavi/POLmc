from automathon import NFA


Q = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
sigma = {'0', '1'}
delta = {
          'q1' : {
                  # '0' : {'q1'},
                  '1' : {'q1', 'q2'}
                  },
          'q2' : {
                  '0' : {'q6'},
                  '' : {'q3'}
                  },
          'q3' : {
                  '1' : {'q4'},
                  },
          'q4' : {
                  '0' : {'q4'},
                  '1' : {'q4'},
                  },
          'q5' : {
          		  '0' : {'q4'},
          		  '1' : {'q3'},
          		 },
        }
initialState = 'q1'
F = {'q4'}

automata = NFA(Q,sigma,delta,initialState,F)
automata.view("NFA")
nfatuple = (Q,sigma,delta,initialState,F)
# print (automata)

def dfs(graph, start, visited=None):
	if visited is None:
		visited = []
	visited.append(start)

	print(start)

	for next in graph[start]:
		try:
			if not(next in visited):
				dfs(graph, next, visited)

		except KeyError:
			continue
	return visited


def nfafinalreach(nfatuple, start, visited=None):
	if visited is None:
		visited = []
	visited.append(start)
	# print('visited:')
	# print(visited)
	# print(start)
	reach=set()
	transt = nfatuple[2][start]
	try:
		for key in transt.keys():
			reach = reach.union(transt[key])    	
		# print('transit:')
		# print(reach)
		for next in reach:
			if not(next in visited):
				nfafinalreach(nfatuple, next, visited)

	except KeyError:
		# print('transit:')
		# print(reach)
		for next in reach:
			if not(next in visited):
				nfafinalreach(nfatuple, next, visited)
	return visited


def residue(nfatuple, letter):
	try:
		reachsetinit = nfatuple[2][nfatuple[3]][letter]
		initstate = 'q' + str(len(nfatuple[0]) + 1)
		reachset = set()
		for next in reachsetinit:
			if len(nfatuple[4].intersection(nfafinalreach(nfatuple,next))) > 0:
				reachset = reachset.union({next})

		if len(reachset) == 0:
			return None


	except KeyError:
		reachset = None
	print(reachset)

# residue(nfatuple,'1')


# graph = {'0': ['1', '2'],
#          '1': ['0', '3', '4'],
#          '2': ['0'],
#          '3': ['1', '5'],
#          '4': ['2', '3'],
#          '5' : ['6']}

# dfs(graph, '0')

# print(nfafinalreach(nfatuple, 'q1'))


residue(nfatuple, '0')