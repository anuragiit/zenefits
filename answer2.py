from itertools import permutations
l=list()
n=int(input())
for i in range(n):
    a=input()
    l.append(a)
string=input()
l=permutations(string)
l=tuple(sorted(l))
inp=tuple(string)
print(l.index(inp)+1)
    
