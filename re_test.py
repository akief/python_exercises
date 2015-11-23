from re import *

print ""
output = factorial(5)
print "factorial(5): " + str(output)
output = factorial(6)
print "factorial(5): " + str(output)
print ""
output = reverse_rec("This string will be all but illegible backward.")
print "reverse_rec('This string will be all but illegible backward.'): " + str(output)
print ""
output = list_mult([1, 2, 3], 2)
print "list_mult([1, 2, 3], 2): " + str(output)
output = list_mult([1, 2], 3)
print "list_mult([1, 2], 3): " + str(output)
print ""
output = flatten([1, 2, 3])
print "flatten([1, 2, 3]): " + str(output)
output = flatten([[1], [2, 3], [4, 5, 6]])
print "flatten([[1], [2, 3], [4, 5, 6]]): " + str(output)
output = flatten([1, [2, 3], [[4], [5, [6]]]])
print "flatten([1, [2, 3], [[4], [5, [6]]]]): " + str(output)
print ""
output = flatten_dict({'a': 1, 'b': {'foo': 2, 'bar': 3}})
print "flatten_dict({'a': 1, 'b': {'foo': 2, 'bar': 3}): " + str(output)
print ""

