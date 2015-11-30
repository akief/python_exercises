def bin_search(array, num):

    """ Binary search:  Returns True if num is in array, False otherwise

        >>>bin_search([-1, 2, 5, 9, 15, 16, 18, 19, 20, 25, 35], 6)
        False

        >>> bin_search(range(10),7)
        True
    """
    #Executes in O(log_2 of n) time, where n = len(array)

    extrabit = len(array)%2
    left = array[:(((len(array)-extrabit)/2)+extrabit)]
    right = array[len(left):]
    if left == []:
    	return False
    else:
        mid = left[-1]
        if mid == num:
    	    return True
        else:   	
        	if len(array)>1:
        		rightleft = {True: right, False: left}
        		return bin_search(rightleft[mid < num], num)
        	else:
        	    return False


#Notes on complexity:
    #
    #          1    1
    #         /    /
    #        3----2      
    #       /      \
    # 11----6---3   1----X
    #  \             \
    #   5             0
    #
    #  Each time binary search is called, it in effect divides the
    #  (ordered) list of remaining possibilities in half by asking
    #  whether the query is >= its midpoint. 
    #
    #  Call the last choice in the series C(0), and any previous choice C(i),
    #  where i increases as distance from C(0) in the decision tree increases. 
    #  C(0) decides between 2 possibilities, so set C(0) = 2.
    #  Then any choice in the series working backward, C(i), decides between
    #  C(i-1) * 2 possibilities (for example the second-to-last choice C(1) decides
    #  between C(0)*2 = 2*2 = 4 possibilities, the third-to last C(1)*2 = 4*2 = 8, etc). 
    #
    #  So the algorithm must be run X times, where X = the number such that C(X) = n,
    #  the number of elements in the list. Since each C adds a factor of 2 to the number
    #  of possibilities explored, it should take log_2(n) choices to explore all possibilities.  
    #
    #  Assuming the non-recursive operations in bin_search execute in constant time, the maximum 
    #  running time for binary search is then O(log_2 of n). 
    #
    #  How about average running time? The chances that the search will happen to hit on the 
    #  right number on each iteration are 1/p, where p is the number of remaining possibilities.
    #  This chance gets greater with each iteration until it is 0.5 when the last choice is made.
    #  Thus, as the list length grows, the chances of the algorithm hitting on the right answer
    #  early on decrease. I *think* this means that the algorithm is most likely to find the
    #  answer only on the last choice, so that the average runtime = the maximum runtime.
    #
    #  Note:  in my implementation at least, if the query is not in the list, the algorithm is 
    #  called an extra time. This is because, once the program narrows the list down to a single 
    #  closest value via the search routine, bin_search must be called again to decide whether 
    #  that value is the query. The "base case" for the recursion is when the input list has only 
    #  1 element, but evaluating this case can yield two possible results. Since this adds at most 
    #  a single iteration, I treat it as a constant and do not add it to the total time cost.