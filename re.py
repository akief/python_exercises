def factorial(n):
    """
    Factorial function.

    >>> fact(5)
    120
    >>> fact(6)
    720
    """
    if n <= 1:
        return 1

    else:
        return factorial(n-1)*n

def reverse_rec(s):
    """
    Reverse a string, recursively.
    """
    
    if len(s) == 1:
    	return s
    else:
    	return s[-1] + reverse_rec(s[:-1])

def list_mult(l, n):
    """
    Repeat the list l as many times as n.

    >>> list_mult([1, 2, 3], 2)
    [1, 2, 3, 1, 2, 3]
    >>> list_mult([1, 2], 3)
    [1, 2, 1, 2, 1, 2]
    """
    
    if n == 0:
    	return []
    else:
    	return l+list_mult(l,n-1)

def flatten(lst):
    """Take a deeply nested list and flatten it to a single level.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([[1], [2, 3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten([1, [2, 3], [[4], [5, [6]]]])
    [1, 2, 3, 4, 5, 6]
    """
    
    flattened = []

    for ele in lst:
        if type(ele) is list:
            flattened += flatten(ele)
        else:
        	flattened += [ele]

    return flattened

def flatten_dict(d):
    """Flatten a nested dictionary, using a period to separate nested keys.

    Only works if nested keys are all strings.

    >>> flatten_dict({'a': 1, 'b': {'foo': 2, 'bar': 3}})
    {'a': 1, 'b.foo': 2, 'b.bar': 3}
    """

    f = {}

    for key in d:
        if type(d[key]) is dict:
        	val = d[key].copy()
        	for ele in val.keys():
        		val[key+"."+ele] = val.pop(ele)
        	f.update(flatten_dict(val))
        else:
            f.update({key: d[key]})

    return f



