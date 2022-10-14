letters=['A','K','E','O','T','P','N']
inp=['Arun','Tarun','Kent','Eat','Pot','Net','Peak','peacock','Zebra','Knif','Nato','Toe','Venus','Toke','Ant']
c=0
rl=[]
for word in inp:
    for l in letters:
        if l in word.upper():
            c+=1
        if c==len(word) and word not in rl:
            rl.append(word)
    c=0
print(rl)
        
    
        
        
