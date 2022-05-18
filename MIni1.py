defconvert(string):

returnlist(string)





classStringClass: #string class created

def__init__(self, string):

self.string= string



deflength(self):

returnlen(self.string) #get the length





defpairs(string):

res= []

res= [[i,j] for i in string for j instring]

fori in res:

print(f"({i[0]},{i[1]})", end =' ')





defprintpairs(string):

var= []

ans= pairs(string)

returnans





classPairsPossible(StringClass):

pass





inp= input("Enter the string\n")

ans= StringClass(inp)

print(convert(inp))

print(ans.length()) #print length

ans1= PairsPossible(inp) #no. of possible pairs

print(pairs(inp)) # pairs
