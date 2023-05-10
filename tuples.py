t1 = ('a',) # need comma to distinguish from string. parentheses with comma will always be a tuple
t = tuple('lupins') # will be broken into components parts
t2 = t[1:3] # slice
t3 = t[0] # index

m = [ 'have', 'fun' ]
(x, y) = m # left hand assignment for tuples, corresponding to place. can do a, b = b, a to swap the values BUT right side expressions evaluated first


d = {'a':10, 'b':1, 'c':22}
t4 = list(d.items()) # will return eack k/v as a tuple

for key, val in list(d.items()): # items returns list of tuples, so can have two iterators
    print(val, key)
    print(key, val) # can use this technique to make a tuple in reverse order, to sort by the original 'value'

# composite keys
directory = {}
first = 'first'
last = 'last'
number = 123
directory[last,first] = number # can now traverse keys, which are themselves tuples

# list comprehension
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [ int(x) for x in list_of_ints_in_strings ] # bracket syntax, use one line for loop to make list from existing list
print(sum(list_of_ints))