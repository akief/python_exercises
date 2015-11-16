from exercises import *

print ""
output = threefive(17)
print "threefive(17): " + str(output)
output = sum_or_prod(9,1)
print "sum_or_prod(9,1): " + str(output)
output = multitable(12)
print "multitable(12): "    
for row in output:
    print row
output = primetest(11)
print "primetest(11): " + str(output)
output = leap_years(2015,4)
print "leap_years(2015,4): " + str(output)
output = return_max(['Steve', 5, 3.24, True])
print ""
print "return_max(['Steve', 5, 3.24, True]): " + str(output)
output = rev(['Steve', 5, 3.24, True])
print "rev(['Steve', 5, 3.24, True]): " + str(output)
output = findin(5, ['Steve', 5, 3.24, True])
print "findin(5, ['Steve', 5, 3.24, True]): " + str(output)
output = findodds(['Steve', 5, 3.24, True])
print "findodds(['Steve', 5, 3.24, True]): " + str(output)
output = totals(['Steve', 5, 3.24, True])
print "totals(['Steve', 5, 3.24, True]): " + str(output)
output = palintest('A man, a plan, a canal...Panama.')
print "palintest('A man, a plan, a canal...Panama.'): " + str(output)
output = combine(['Sam', 'Chloe', 'Scott'],[4, 7, 1200, 3, 2])
print "combine(['Sam', 'Chloe', 'Scott'],[4, 7, 1200, 3, 2]): " + str(output)
output = print_box(['a','list','of','strings'])
print "print_box(['a','list','of','strings']): \n" + str(output)
print ""
output = scrabble_score('SCRABBLE')
print "scrabble_score('SCRABBLE'): " + str(output)
print ""