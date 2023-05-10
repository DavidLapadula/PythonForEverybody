counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

# Dict methods
print('annie' in counts)
print(counts.values())
print(counts.get('chuck'))
for key in counts: # for loop will traverse keys by default
    print(key, counts[key])

# how to use maketrans, translate method(s)

txt = "Hello Sam!"
mytable = str.maketrans("S", "P") # will map unicode characters to its replacement. Each item of first arg will be replaced with value from second in the same position
print(txt.translate(mytable)) # will use dict from maketrans to replace first arg with second
