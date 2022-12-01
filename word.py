from automathon import NFA

Q = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
sigma = {'0', '1'}
delta = {
          'q1' : {
                  # '0' : {'q2', 'q5'},
                  '1' : {'q1', 'q6'}
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

          'q6' : {
          			'0' : {'q6'},
          			'1' : {'q6'},
          		},
        }
initialState = 'q1'
F = {'q4'}


Qp = {'q1', 'q2', 'q3', 'q4', 'q5'}
sigmamodel = {'r', 'd', 'l', 'u'}
deltap = {
			'q1' : {
					'r' : {'q2'},
					},
			'q2' : {
					'r' : {'q2'},
					'd' : {'q3'},
					},

			'q3' : {
					'd' : {'q3'},
					'l' : {'q4'},
					},
			'q4' : {
					'l' : {'q4'},
					'u' : {'q5'},
					},
			'q5' : {
					'u' : {'q5'},
					''  : {'q1'},
					},
		}
initstatep = 'q1'
Fp = {'q1', 'q5'}



Qw = {'q1','q2','q3','q4','q5','q6','q7','q8', 'q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22'}
deltaw = {
		'q1' : { 
				'':{'q2', 'q8'},
		       },
		       
		'q2' : { 
				'':{'q3', 'q4'},
		       },
		       
		'q3' : { 
				'r':{'q5'},
		       },
		       
		'q4' : { 
				'u':{'q6'},
		       },
		       
		'q5' : { 
				'':{'q7'},
		       },
		       
		'q6' : { 
				'':{'q7'},
		       },
		       
		'q7' : { 
				'':{'q2', 'q8'},
		       },     
		
		'q8' : { 
				'':{'q9', 'q10', 'q11'},
		       },
		       
		'q9' : { 
				'd':{'q12'},
		       },                     

		'q10' : { 
				'l':{'q13'},
		       },
		       
		'q11' : { 
				'':{'q14'},
		       },      

		'q12' : { 
				'':{'q15'},
		       },
		       
		'q13' : { 
				'':{'q15'},
		       },
		       
		'q14' : { 
				'':{'q15'},
		       },
		       
		'q15' : { 
				'':{'q16', 'q22'},
		       },          
		       
		'q16' : { 
				'':{'q17', 'q18'},
		       },
		       
		'q17' : { 
				'r':{'q19'},
		       },
		       
		'q18' : { 
				'u':{'q20'},
		       },
		       
		'q19' : { 
				'':{'q21'},
		       },
		       
		'q20' : { 
				'':{'q21'},
		       },
		       
		'q21' : { 
				'':{'q22', 'q16'},
		       },
		       		       
	}

initstatew = 'q1'
Fw = {'q22'}






Qpw = {'q1','q2','q3','q4','q5','q6','q7','q8', 'q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22'}
sigmamodel = {'r', 'd', 'l', 'u'}
deltapw = {
		'q1' : { 
				'':{'q2', 'q8'},
		       },
		       
		'q2' : { 
				'':{'q3', 'q4'},
		       },
		       
		'q3' : { 
				'l':{'q5'},
		       },
		       
		'q4' : { 
				'd':{'q6'},
		       },
		       
		'q5' : { 
				'':{'q7'},
		       },
		       
		'q6' : { 
				'':{'q7'},
		       },
		       
		'q7' : { 
				'':{'q2', 'q8'},
		       },     
		
		'q8' : { 
				'':{'q9', 'q10', 'q11'},
				},		       
		'q9' : { 
				'u':{'q12'},
		       },                     

		'q10' : { 
				'r':{'q13'},
		       },
		       
		'q11' : { 
				'':{'q14'},
		       },      

		'q12' : { 
				'':{'q15'},
		       },
		       
		'q13' : { 
				'':{'q15'},
		       },
		       
		'q14' : { 
				'':{'q15'},
		       },
		       
		'q15' : { 
				'':{'q16', 'q22'},
				},          
		       
		'q16' : { 
				'':{'q17', 'q18'},
		       },
		       
		'q17' : { 
				'l':{'q19'},
		       },
		       
		'q18' : { 
				'd':{'q20'},
		       },
		       
		'q19' : { 
				'':{'q21'},
		       },
		       
		'q20' : { 
				'':{'q21'},
		       },
		       
		'q21' : { 
				'':{'q22', 'q16'},
		       },
		       
		# 'q22' : { 
		# 		//eta nije dekhe nin borda
		#        },
		       
	}

initstatepw = 'q1'
Fpw = {'q22'}

patrolautomata = NFA(Qp, sigmamodel, deltap, initstatep, Fp)
patrolautomata.view("patrolexpect")

waterautomata = NFA(Qw, sigmamodel, deltaw, initstatew, Fw)
waterautomata.view("waterexpect")

powerautomata = NFA(Qpw, sigmamodel, deltapw, initstatepw, Fpw)
powerautomata.view("powerexpect")

#--------------------------------------------------------------------Model-------------------------------------------------------------#

worlds = {'s', 't', 'u'}
agents = {'a', 'b'}
propositions = {'w', 'p', 'r'}
relation = {
			'a' : {
						'u' : {'u', 's', 't'},
						's' : {'u', 's', 't'},
						't' : {'u', 's', 't'},
				  },
			'b' : {
						'u' : {'u'},
						's' : {'s', 't'},
						't' : {'s', 't'},
				  },
			}

valuation = {
			's' : {'w'},
			'u' : {'p'},
			't' : {'r'},
			}

expect = {
			's' : waterautomata,
			'u' : patrolautomata,
			't' : powerautomata
		}


dronemodel = {
				'worlds' : worlds, 
				'agents' : agents, 
				'propositions' : propositions, 
				'relation' : relation, 
				'valuation' : valuation, 
				'expectation' : expect,

			}



#----------------------------------------------------------------------Input Ends------------------------------------------------------#

# automata = NFA(Q,sigma,delta,initialState,F)
# automata.view("NFA")
# nfatuple = [Q,sigma,delta,initialState,F]

# patrolautomata = NFA(Qp, sigmamodel, deltap, initstatep, Fp)
# patrolautomata.view("patrolexpect")

# waterautomata = NFA(Qw, sigmamodel, deltaw, initstatew, Fw)
# waterautomata.view("waterexpect")

# powerautomata = NFA(Qpw, sigmamodel, deltapw, initstatepw, Fpw)
# powerautomata.view("powerexpect")





#----------------------------------------------------------------Function Starts-------------------------------------------------------#
def nfafinalreach(nfa, start, visited=None):
	if visited is None:
		visited = []
	visited.append(start)
	# print('visited:')
	# print(visited)
	# print(start)
	reach=set()
	transt = nfa.delta[start]
	try:
		for key in transt.keys():
			reach = reach.union(transt[key])    	
		# print('transit:')
		# print(reach)
		for next in reach:
			if not(next in visited):
				nfafinalreach(nfa, next, visited)

	except KeyError:
		# print('transit:')
		# print(reach)
		for next in reach:
			if not(next in visited):
				nfafinalreach(nfa, next, visited)
	return visited


def residue(nfa, letter):
	if nfa == None:
		return None
	if letter == '':
		return nfa
	nfa = nfa.removeEpsilonTransitions()
	# try:
	reachsetinit = nfa.delta[nfa.initialState][letter]
	# print(reachsetinit)
	initstate = 'q' + str(len(nfa.Q) + 1)
	reachset = set()
	for next in reachsetinit:
		if len(nfa.F.intersection(nfafinalreach(nfa,next))) > 0:
			reachset = reachset.union({next})

	if len(reachset) == 0:
		reachset = None

	if not(reachset == None):
		newstatetransit = dict()
		newstatetransit[''] = set()
		for item in reachset:
			newstatetransit[''] = newstatetransit[''].union({item})

		# print(newstatetransit[''])

		nfa.Q = nfa.Q.union({initstate})
		nfa.initialState = initstate
		nfa.delta[initstate] = newstatetransit
		return nfa


def findargs(argstring):
	args = list()
	parencount = 0
	index = 0
	markstartindex = 0
	for c in argstring:
		if c == '(':
			parencount = parencount + 1
		
		if c == ')':
			parencount = parencount - 1

		if parencount == 1 and c == '(':
			markstartindex = index + 1
			
		if parencount == 1 and c == ',':
			args.append(argstring[markstartindex:index])
			markstartindex = index + 1

		if parencount == 0 and index > 0:
			args.append(argstring[markstartindex:index])

		index = index + 1

	return args




def findarginformula(phi):
	args = list()
	if phi[0] == 'A':
		# print('first index mark')
		if phi[0:3] == 'AND':
			argstring = phi[3:len(phi)]
			return findargs(argstring)


		else:
			raise Exception("Syntax Error")
		
	elif phi[0] == 'O':
		# print('O')
		# print('first index mark')
		if phi[0:2] == 'OR':
			argstring = phi[2:len(phi)]
			return findargs(argstring)


		else:
			raise Exception("Syntax Error")

	elif phi[0] == 'N':
		# print('N')
		# print('first index mark')
		if phi[0:3] == 'NOT':
			argstring = phi[3:len(phi)]
			return findargs(argstring)


		else:
			raise Exception("Syntax Error")

	elif phi[0] == 'K':
		# print('K')
		# print('first index mark')
		if phi[0:2] == 'KP':
			argstring = phi[1:len(phi)]
			return findargs(argstring)


		else:
			raise Exception("Syntax Error")

	elif phi[0] == 'D':
		# print('B')
		# print('first index mark')
		if phi[0:3] == 'DIM':
			argstring = phi[3:len(phi)]
			return findargs(argstring)


		else:
			raise Exception("Syntax Error")

	else:
		raise Exception("atom or Syntax Error")







def wordMC(model,phi):
	satworlds = set()
	if phi[0] == 'A':
		arglist = findarginformula(phi)
		for arg in arglist:
			 satworlds = satworlds.intersection(wordMC(model,arg))

		return satworlds

	elif phi[0] == 'O':
		arglist = findarginformula(phi)
		for arg in arglist:
			satworlds = satworlds.union(wordMC(model, arg))

		return satworlds

	elif phi[0] == 'N':
		arglist = findarginformula(phi)
		if len(arglist) > 1:
			raise Exception("Syntax Error")

		# print("formula {}".format(arglist[0]))
		# print("For formula {}, {}".format(arglist[0], wordMC(model, arglist[0])))
		satworlds = model['worlds'].difference(wordMC(model, arglist[0]))
		return satworlds

	elif phi[0] == 'K':
		arglist = findarginformula(phi)
		if len(arglist) > 2:
			raise Exception("Syntax Error")

		# print("formula {}".format(arglist[1]))
		# print("For formula {}, {}".format(arglist[1], wordMC(model, arglist[1])))
		satKworlds = wordMC(model, arglist[1])
		for world in model['worlds']:
			for satworld in satKworlds:
				if satworld in model['relation'][arglist[0]][world]:
					satworlds = satworlds.union({world})

		return satworlds


	elif phi[0] == 'D':
		arglist = findarginformula(phi)
		if len(arglist) > 2:
			raise Exception("Syntax Error")

		modelprime = model
		for c in arglist[0]:
			for world in modelprime['worlds']:
				modelprime['expectation'][world] = residue(modelprime['expectation'][world], c)
				if modelprime['expectation'][world] == None:
					modelprime['worlds'] = modelprime['worlds'].difference({world})
					for agent in modelprime['relation'].keys():
						modelprime['relation'][agent].pop(world)
						for s in modelprime['relation'][agent].keys():
							modelprime['relation'][agent][s] = modelprime['relation'][agent][s].difference({world})

		if len(modelprime['worlds']) > 0:
			return wordMC(modelprime, arglist[1])

		else:
			return {}



	else:
		satworlds = set()
		for world in model['worlds']:
			if phi in model['valuation'][world]:
				satworlds = satworlds.union({world})

		return satworlds




	# except KeyError:
	# 	reachset = None
	# print(reachset)

# residue(nfatuple,'1')


# graph = {'0': ['1', '2'],
#          '1': ['0', '3', '4'],
#          '2': ['0'],
#          '3': ['1', '5'],
#          '4': ['2', '3'],
#          '5' : ['6']}

# dfs(graph, '0')

# print(nfafinalreach(nfatuple, 'q1'))

# nfa = NFA(Q, sigma, delta, initialState, F)
# resnfa = residue(residue(nfa, '0'), '0')
# print(resnfa)
# resauto = NFA(resnfa[0], resnfa[1], resnfa[2], resnfa[3], resnfa[4])
# print(resnfa)
# resnfa.view("resNFA")
# print(resnfa)

# noepautomata = automata.removeEpsilonTransitions()
# noepautomata.view("Epfree")
# print (noepautomata.initialState)


# patrolafterright = residue(patrolautomata, 'r')
# patrolafterright.view("patrolexpectafterrright")

print(wordMC(dronemodel, 'DIM(rrr,NOT(KP(a,NOT(w))))'))

# reswater = residue(waterautomata, 'r')
# reswater.view('reswater')

# noepwater = waterautomata.removeEpsilonTransitions()
# noepwater.view('noepwater')