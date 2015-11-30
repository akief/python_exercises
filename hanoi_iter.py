from exercises import sum_or_prod

def hanoi(numdiscs):

    """ Solves the Tower of Hanoi problem with numdiscs
        >= 1 discs, using the minimum possible number of 
        moves, and returns that number.

        Prints each move and displays the state of the
        board along the way.
   
    >>>hanoi(4)
    ...printed stuff...
    15
    
    """
    #Executes in O(2^numdiscs - 1) time.

    #setup
    moves = 0
    numrods = 3

    towers = [[0] for rod in range(numrods)]
    for i in range(numdiscs):
    	towers[0].append(numdiscs - i)
    	
    odd = 1-(2*(numdiscs%2))

    #main loop
    print ""
    while True:
    	solved = 0

        #Print state of board
        for tower in range(numrods):
    	    print "Tower " + str(tower) + ": ",
            print towers[tower]
            print ""

        #Move small piece
        for i in range(numrods):
        	if towers[i][-1] == 1:
        		to = i + odd
        		if to < 0:
        			to = numrods-1
        		elif to > numrods-1:
        			to = 0
        		towers[to].append(towers[i].pop())
        		moves += 1
        		print "Moved piece of size " + str(towers[to][-1]) + " from tower " + str(i) + " to tower " + str(to) + "."
        		print "Total moves: " + str(moves)
        		print ""
        		break
        	else:
        		pass

        #Exit if completed
        if sum(towers[numrods-1]) == sum_or_prod(numdiscs):
            for tower in range(numrods):
            	#Print state of board before exiting
                print "Tower " + str(tower) + ": ",
                print towers[tower]
            	print ""	
            print "Completed in " + str(moves) + " move(s)."
            return moves

        #Move larger piece
        for i in range(numrods): 
            if solved == 1:
                break
            else:      	
                if towers[i][-1] > 1:
            	    for j in range(numrods):
            		    if towers[j][-1] > towers[i][-1] or towers[j][-1] == 0:
            		        #Print state of board
            		        for tower in range(numrods):
            		        	print "Tower " + str(tower) + ": ",
            		        	print towers[tower]
            		        	print ""
            		        towers[j].append(towers[i].pop())
            		        moves += 1
            		        print "Moved piece of size " + str(towers[j][-1]) + " from tower " + str(i) + " to tower " + str(j) + "."
            		        print "Total moves: " + str(moves)
            		        print ""
            		        solved = 1
            		        break
        
    #end (not used)
    return towers

#Notes on complexity:
    # 
    #  For this iterative solution, the main determinant
    #  of complexity is the number of times the main loop
    #  must be traversed, i.e. (roughly) the number of
    #  moves / 2, since each loop consists of moving the
    #  small piece and then a larger piece [actually the
    #  game always starts and ends by moving the smaller 
    #  piece, so the total number of moves will be odd]. 
    #
    #  I noticed that each time the game is played, the
    #  first step consists in uncovering the largest stone
    #  and moving it to the rightmost tower to start the
    #  stack there. This seems to occur in 2^numdiscs / 2
    #  moves. 
    #
    #  Also, the second part of the game consists of a
    #  mirror image of the first part:  instead of un-
    #  stacking stones from the first tower, you're
    #  stacking stones on the third tower. And the last
    #  move of the first part = the first move of the
    #  second part, which explains the odd total number
    #  of moves. The game can be thought of as consisting
    #  of two parts, unstacking and restacking, each of
    #  which take 2^numdiscs / 2 moves, with a shared
    #  move in the middle (the -1).
    #
    #  But why that number of moves in each half?
    #
    #  Well, in the course of either building or un-
    #  building a tower of N stones, you need to both
    #  build and unbuild a tower of N-1 stones. (I'm not
    #  sure how to explain why this has to be the case,
    #  it's just something that seems to be true when you
    #  play the game). But of course to do that, you must
    #  build and unbuild a tower of N-2 stones, and so on
    #  until you get to the simplest case, which is simply
    #  moving the smallest stone to "build" and "unbuild"
    #  a tower of one stone.
    #
    #  So the game starts to look recursive. This suggests
    #  a different, and simpler, way of looking at the number
    #  of moves required:  moving a tower of N stones consits
    #  of uncovering the foundation stone, moving that stone,
    #  and then re-covering it. Then, the base case, N = 1,
    #  consists of just moving the foundation stone, since it's
    #  already uncovered and once you've moved it you're done.
    #
    #  We can then represent building a tower of N stones as follows:
    #
    #  [Uncovering] + 1 + [Covering]
    #
    #  The base case is for N = 1:
    #  0 + 1 + 0 = 1
    #
    #  N = 2 is then:
    #  [1] + 1 + [1] = 3
    #
    #  N = 3 is:
    #  [3] + 1 + [3] = 7
    #  ...and so on.
    #
    #  This suggests a recursive implementation, which I'll try next.
    #  The only wrinkle will be figuring out how to tell each recursive
    #  call where to start building the intermediary towers.

