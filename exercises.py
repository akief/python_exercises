#ELEMENTARY EXERCISES

#5
def threefive(num):

    """ Returns the sum of all positive multiples of 3 and 5
        up to and including the input (num).

    >>>threefive(17)
    60                                                   """

    sumsofar = 0
    while (num > 0):
        if (num%5 == 0 or num%3 == 0):
            sumsofar += num
        num -= 1

    return sumsofar

#6
def sum_or_prod(num, mode=0):

    """ Returns either the sum or product of numbers from 1 to
        the input (num).

        Set mode to 0 for sum (default); set mode to 1 for product.

    >>>sum_or_prod(9,1)
    362880                                                      """

    if (mode == 0):
        sumsofar = 0
        while (num > 0):
            sumsofar += num
            num -= 1

        return sumsofar

    elif (mode == 1):
        prodsofar = 1
        while (num > 0):
            prodsofar = prodsofar * num
            num -= 1

        return prodsofar

    elif ((mode != 0) and (mode != 1)):
        print "no:  mode must be 0(sum) or 1(product)"

#7

def multitable(num):

    nums = [x+1 for x in range(num)]
    table = [[str(x) + "*" + str(y) + "= " + str(x*y) for y in nums] for x in nums]

    return table

#8 (modified)
def primetest(num):

    """ Returns True if input is a prime number,
        False otherwise.

    >>>primetest(11):
    True                                     """

    bnum = num

    while (bnum > 2):
        bnum -= 1
        if (num%bnum==0):
            return False

    if (bnum == 2):
        if (num!=4):
            return True

    elif (bnum==1):
        return False


#10
def leap_years(year, N=20):

    """ Returns a list of the next N leap years, starting
        from a specified year. Default N is 20.

    >>>leap_years(2015,4)
    [2016, 2020, 2024, 2028]                          """

    num_years = 0
    leaps = []

    while (num_years < N):

        if (year%4==0):
            if (year%100==0):
                if (year%400==0):
                    leaps += [year]
                    num_years +=1
            else:
                leaps += [year]
                num_years += 1
        year += 1

    return leaps





#LIST EXERCISES

#1
def return_max(array):

    """ Returns largest element in a list.
        For string elements, size = string length.
        For numbers, size = magnitude.
        For Boolean, size = 0 (False) or 1 (True).
        If there is no unique largest element, the first element in the list with the maximum size is returned.
    
    >>>return_max(['Steve', 5, 3.24, True])
    'Steve'                                                                                                 """
    
    longest = None
    max_length = 0
    length = 0
  
    for item in array:
        if (type(item) is str):
            length = len(item)
        elif (type(item) is int or type(item) is float or type(item) is bool):
            length = item * 1
        
        if (length > max_length):
            longest = item
            max_length = length

    return longest

#2
def rev(array):

    """ Reverses the order of the elements in a list.
    
    >>>rev(['Steve', 5, 3.24, True])
    [True, 3.24, 5, 'Steve']                      """
  
    rev = []

    for item in array:
        rev = [item] + rev  

    return rev

#3
def findin(sought, array):

    """ Checks for the presence of an element in a list.
        Returns Boolean value True if the item is present,
        False otherwise.
    
    >>>findin(5, ['Steve', 5, 3.24, True])
    True                                               """
  
    isin = False

    for item in array:
        if (sought == item):
            isin = True
            break  

    return isin

#4
def findodds(array):

    """ Returns the odd elements of a list (assuming
        that the first index is 1).
    
    >>>findodds(['Steve', 5, 3.24, True])
    ['Steve', 3.24]                              """
  
    odds = []
    ind = 1

    for item in array:
        if (ind%2 > 0):
            odds += [item]
        ind += 1

    return odds

#5
def totals(array):

    """ Returns an array containing the running totals 
        of numerical elements in a list as each item is added.

    >>>totals(['Steve', 5, 3.24, True])
    [5, 8.24, 9.24]                                        """

    nums = [x for x in array if type(x) is not str]
    totals = [nums[0]]

    for i in range(1,len(nums)):
        totals += [nums[i] + totals[i-1]]
 
    return totals

#6
def palintest(string):

    """ Returns True if input is a palindrome, False otherwise.

    >>>palintest('A man, a plan, a canal...Panama.')
    True                                                    """

    punct = [" ", ".", ",", ";", "'", "?", "!", "(", ")", "[", "]", "{", "}", "$", "-", "/"]
    for thing in punct:
        string = string.replace(thing,"")
    string = string.lower()

    extrabit = len(string)%2
    midpoint = ((len(string)-extrabit)/2)+extrabit 
    firsthalf = string[:midpoint]
    secondhalf = string[midpoint-extrabit:]
    revsec = ""

    for i in range(len(secondhalf)-1, -1, -1):
        revsec += secondhalf[i]
    if (firsthalf == revsec):  # Could just reverse the whole thing instead but that involves
        return True            # more loop iterations. Which is more efficient?
    else:
        return False



#10
def combine(array1,array2):
    """ Takes two arrays as input and returns a new array composed
        by taking elements alternately from the two arrays.
        If the arrays are of unequal length, unpaired elements of the
        longer array are appended at the end.

    >>>combine(['Sam', 'Chloe', 'Scott'],[4, 7, 1200, 3, 2])
    ['Sam', 4, 'Chloe', 7, 'Scott', 1200, 3, 2]                   """

    longer = max(array1,array2,key=len)
    shorter = min(array1,array2,key=len)

    newarr = []
    for i in range(len(shorter)):
        newarr += [array1[i],array2[i]]
    newarr += longer[len(shorter):]

    return newarr



#18
def print_box(strings):
    """ Returns a message printed in a box.
    
    >>>print_box(['a','list','of','strings'])
    ***********
    * a       *
    * list    *
    * of      *
    * strings *
    ***********                          """

    maxlength = len(max(strings, key=len))

    boxstring =  "*" * (maxlength + 4) + "\n"
    for i in strings:
        boxstring += "* " + i + (" " * ((maxlength - len(i)) + 1)) + "*" + "\n"
    boxstring += "*" * (maxlength + 4)

    return boxstring





#DICT EXERCISE
def scrabble_score(string):
    """ Returns the Scrabble score for a word.

    >>>scrabble_score('SCRABBLE')
    14                                     """

    score = 0
    scores = {'A': 1, 'B': 3, 'C': 3, 'D': 1, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
    string = string.upper()
    for c in string:
        score += scores[c]

    return score




