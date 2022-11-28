import itertools
import random
from re import L, S
from typing import Set





class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        x = self.count
        if x == len (self.cells): #if the sentance count is the same as the number of cells, (e.g all are mines)
            return self.cells
        else:
            return set()


    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        if self.count == 0: 
            return self.cells
        else:
            return set()



    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            NewSet = set()
            for c in self.cells: 
                if c == cell: 
                    continue
                NewSet.add (c)
            self.cells = NewSet
            self.count-=1



        
        #######raise NotImplementedError##########

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """

        if cell in self.cells:
            NewSet = set()
            for c in self.cells: 
                if c == cell: 
                    continue
                NewSet.add (c)
            self.cells = NewSet
        
        
        
        #############raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)
     

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)
       




    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        

    #1) 
        self.moves_made.add (cell) 

    #2)        
        self.mark_safe (cell) 
        #count = Minesweeper.nearby_mines (cell) dont need this; its already an argument? 
        
     #3)
        SSet = set() #sentence set
        for i in range(cell[0] - 1, cell[0] + 2):
            if i<0 or i > self.height-1:
                continue
            for j in range(cell[1] - 1, cell[1] + 2):
                if j < 0 or j > self.width-1:  #this and line 233 keep the AI on the board, and not going into -1,-1 , or 9,10 etc. 
                    continue
                if (i, j) == cell:
                    continue
                if (i,j) in self.safes:
                    continue
                if (i,j) in self.mines:
                    count -=1 
                    continue
                CellTuple = (i,j)
                SSet.add(CellTuple) # gives us a set of each of the cell tuples touching the given cell, apart from it. 
        NewS = Sentence (SSet, count) # creates a new sentance containg this new knowledge
    
        #print ("adding sentence " + str (NewS.cells) + "=" + str (NewS.count))
        
 # 4 and 5)   
        self.K2 (NewS)
        print ("KNOWLEDGE IS")
        for x in self.knowledge:
            print (x.cells, x.count)
        
        print ("safes are " + str (self.safes))
        print ("Mines  are " + str (self.mines))
  
    def K2 (self, NewSentence):
        ##for cell in NewSentence.cells: 
            #if cell in safes:
                #############################################################
        self.knowledge.append (NewSentence) # adds newS to knowledge base
        for sentence in self.knowledge: #for each sentence
            for m in sentence.known_mines(): #for each known mine in that sentence                    
                self.mark_mine (m) #mark that mine as such
            for s in sentence.known_safes(): #same for safes 
                self.mark_safe (s)
            if sentence.cells == set():
                self.knowledge.remove (sentence) #removes empty sentences from knowledge
            
        for Set in self.knowledge: #for each sentence in K
            for Subset in self.knowledge: #compared to each other sentence in K
                #add a section here about if its in safes or mines
                if Subset.cells == set() or Set.cells == set(): #if neither sentences have an empty set of cells
                    continue
                if Subset == Set: # and if the two sentenaces are not identical 
                    continue
                if Subset.cells.issubset(Set.cells):
                    #print ("infering from knowledge") 
                    #print (str (Subset) + " Is a subest of " + str (Set))
                    InferCells = Set.cells-Subset.cells
                    InferCount = Set.count - Subset.count
                    print("infering " + str (InferCells) + " = " + str (InferCount))
                    InferS = Sentence (InferCells,InferCount)
                    if InferS in self.knowledge: 
                        pass
                    else: 
                        self.K2(InferS)


    
    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        
        for x in self.safes:
            if x in self.moves_made:
                continue
            else:
                print ("MOVE IS " + str (x))
                return x
                




    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        print ("mines are " + str (self.mines))                                       
        ValidMoves = []
        for i in range(0, self.height):
            for j in range(0, self.width ):
                if (i, j) in self.moves_made:
                    continue
                if (i,j) in self.mines:
                    continue
                ValidMoves.append ((i,j)) # creates a list of all valid moves
        l = len (ValidMoves)
        if l == 1:
            return ValidMoves [0]  # avoid problems with range in last step
        if l == 0:
            return None #if no possible moves 
        move = ValidMoves [random.randint (0,l-1)] # selects a move at a random index in list of possible moves.
        print (move)
        return (move)
        


##to do 
#(cant infer that if space 1 is touching a mine, then all other spaces around it are safe!)
#doesnt seem to be updating infor properly! in final stages i can infer safe but it can't it knows which mines are there, but doesnt update K accordingly! 