#Stacy Alme
#alme0056

class Random:


	def __init__(self,seed): 

		self.seed = seed
		self.seed = self.next()
		#print self.seed

	def next(self): 

		self.seed =  (16807*self.seed)%(2147483648-1)
		return self.seed

 	def choose(self, objects): 
				
 	    return objects[self.next()%len(objects)]



class Grammar: 


	def __init__(self,seed): 

		self.randomnumber = Random(seed);
		self.rules = {}


	def rule(self,left,rights): 

		for key in self.rules:
			if key==left:	  
				raise RuntimeError('cannot have two rules with the same name')
			
		self.rules[left]=rights
	

	def generate(self):   

		for key in self.rules:
			if key=='Start':
				# print "keys"
				# print self.rules[key][0]
				return self.generating(self.rules[key][0])
				
		raise RuntimeError('No START rule to begin the program')


	def generating(self,right):

		astring = ''

		for i in range(len(right)):
			if right[i] in self.rules:
				# print right[i]
				newelements = self.rules[right[i]]
				selectelement = self.randomnumber.choose(newelements)
				# print selectelement
				astring += self.generating(selectelement)
				# print astring
			else:
				astring += str(right[i])+ ' '

		return astring


G = Grammar(100)
G.rule('Noun',   (('apple',), ('puppy',), ('dog',), ('girl',)))
G.rule('Verb',   (('bit',), ('ate',), ('kissed',)))
G.rule('Phrase', (('the', 'Noun', 'Verb', 'the', 'Noun'),))
G.rule('Story',  (('Phrase',), ('Phrase', 'and', 'Story')))
G.rule('Start',  (('Story', '.'),))


print G.generate()

S = Grammar(2235)
S.rule('Noun',   (('person',), ('geek',), ('engineer',), ('puppy',)))
S.rule('Verb',   (('running',), ('yogaing',), ('was',)))
S.rule('Phrase', (('the', 'Noun', 'Verb', 'the', 'Noun',),('the','Noun','Verb','and','Noun','Verb','Noun')))
S.rule('Story',  (('Phrase',), ('Phrase', 'and', 'Story')))
S.rule('Start',  (('Story', '.'),))

print S.generate()

P = Grammar(1324234)
P.rule('Noun',   (('coolest',), ('coleslaw',), ('engineer',), ('zombie',)))
P.rule('Verb',   (('running',), ('high-fiving',), ('was',),('eating')))
P.rule('Phrase', (('the', 'Noun', 'Verb', 'the', 'Noun',),))
P.rule('Story',  (('Phrase',), ('Phrase', 'and', 'Story')))
P.rule('Start',  (('Story', '.'),))

print P.generate()