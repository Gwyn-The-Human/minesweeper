       
       
       
       
from ast import Sub


def NewKSearch (OldK, Inferences): #will take self.knowledge as both, and [] as inferences   
    I = []
    checked = []
    for S in OldK:  
        for Sub_S in Inferences: # 1st recursion, checks sets in knowledge for subsets in knowledge:
                                #following recursions: checks new sentences for subsets and sets
            if Sub_S.cells == S.cells:
                continue
            if Sub_S.cells.issubset(S.cells) and {Sub_S,S} not in checked: #checks if x is subset of y, and we havnt already tested if x is subset of y
                checked.add ({Sub_S,S}) #adds to checked 
                InferCells = S.cells-Sub_S.cells
                InferCount = S.count - Sub_S.count
                InferS = Sentence (InferCells,InferCount) #creates new sentences 
                OldK.append (InferS) #adds new sentence to old knowldege 
                I.append(InferS) #adds new sentence to Inferences
            if S.cells.issubset(Sub_S.cells) and {Sub_S,S} not in checked: # same as above by inversed, checks if y is subset of x, but....etc 
                checked.add ({Sub_S,S})
                InferCells = Sub_S.cells-S.cells
                InferCount = Sub_S.count - S.count
                InferS = Sentence (InferCells,InferCount)
                OldK.append (InferS)
                I.append(InferS)
    NewKSearch (OldK, I)
    return OldK


        x = NewKSearch (self.knowledge,self.knowledge)
        self.knowledge = x


def NewKSearch (OldK, Inferences): #will take self.knowledge as both, and [] as inferences   
    I = []
    checked = []
    for S in OldK:  
        for Sub_S in Inferences: # 1st recursion, checks sets in knowledge for subsets in knowledge:
                                #following recursions: checks new sentences for subsets and sets
            if Sub_S.cells == S.cells:
                continue
            if Sub_S.cells.issubset(S.cells) and {Sub_S,S} not in checked: #checks if x is subset of y, and we havnt already tested if x is subset of y
                checked.add ({Sub_S,S}) #adds to checked 
                InferCells = S.cells-Sub_S.cells
                InferCount = S.count - Sub_S.count
                InferS = Sentence (InferCells,InferCount) #creates new sentences 
                OldK.append (InferS) #adds new sentence to old knowldege 
                I.append(InferS) #adds new sentence to Inferences
            if S.cells.issubset(Sub_S.cells) and {Sub_S,S} not in checked: # same as above by inversed, checks if y is subset of x, but....etc 
                checked.add ({Sub_S,S})
                InferCells = Sub_S.cells-S.cells
                InferCount = Sub_S.count - S.count
                InferS = Sentence (InferCells,InferCount)
                OldK.append (InferS)
                I.append(InferS)
    NewKSearch (OldK, I)
    return OldK
