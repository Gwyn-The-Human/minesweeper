       NewK = []
        for Set in self.knowledge: #for each sentance in K
            #print ("TEST SENTENCE " + str (Set.cells) + str (Set.count))
            for Subset in self.knowledge: 
                if Subset.cells == set() or Set.cells == set():
                    continue
                #print ("comparing " + str(Subset.cells) + " to " + str( Set.cells))
                if Subset.cells == Set.cells:
                    continue
                if Subset.cells.issubset(Set.cells):
                    print ("infering from knowledge") 
                    print (str (Subset) + " Is a subest of " + str (Set))
                    InferCells = Set.cells-Subset.cells
                    InferCount = Set.count - Subset.count
                    InferS = Sentence (InferCells,InferCount)
                    print ("adding new Knowledge" + str (InferS.cells) + str (InferS.count))
                    NewK.append (InferS) #creats a list of new sentences 
                    return self.AddK2 (InferS)





                    

    #4)  

    
        NewMines = NewS.known_mines () #if count = len cells; returns cells
        print ("Newmines are " + str (NewMines))
            print ("marking NewMines") 
        for m in NewMines:                   #all other sentances have already been checked presumably, so can just check the newest one NewK
            self.mark_mine (m)              #removes all known mines from sentances and adjust counts accordingly
            print ("just marked as mine:" + str (m) )
            print (self.mines)
       
         

#do i need all know mines in her somewhere? why dont i just add the sentence to knowledge, and then update recursivly until there are no more new min

        NewSafes = NewS.known_safes() 
        #print (" the New safes are " + str(NewSafes))
        for s in NewSafes:
            self.mark_safe(s) 
       
               
    
    #5) 



    ####################
 