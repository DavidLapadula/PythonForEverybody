pie = 'pie'
piece = pie[1:2] # [:] for the whole string
print(piece)

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:] # strings immutable, so can only add to them
print(new_greeting)

camels = 42
print('I have spotted %d camels.' % camels) 
# for strings, % is a format value where we can interpolate strings with variable values
# different types of format, %d for int, %s for string, etc
