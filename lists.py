newList = [1, '1', [2, '3']] # mixed types
newList[0] = 'new' # mutable
print('1' in newList) # in operator for list containing

print([1, 2, 3] + [4, 5,6]) # concatenate
print([1, 2, 3] * 2) # multiply

newList2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(newList2[1:2])
print(newList2[:2]) # omit first, start at beginning
print(newList2[2:]) # omit last, end at finish

a = [1, 2, 3]
b = [1, 2, 3]
# a is b is false because two object with lists. equal but not identical

a = [1, 2, 3]
b = a
# b is a is true because aliasing is used for reference types

stringList = ['1', '2', '3']
noAlias = stringList[:] # will make a new list and not use reference type


