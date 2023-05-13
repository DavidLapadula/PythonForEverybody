import re

# caret to only search the start of a string
caret1 = 'from another galaxy'
caret2 = 'a galaxy from the milky way'

print(re.search('from', caret1))
print(re.search('from', caret2))
print(re.search('^from', caret1))
print(re.search('^from', caret2)) # false
print('-------------------------')

# period as wildcard to match any character
wildcard1 = 'this'
wildcard2 = 't22s'
wildcard3 = 'From:john@'
wildcard4 = 'From:doe@'
wildcard5 = 'hello'

print(re.search('t..s', wildcard1))
print(re.search('t..s', wildcard2))
print(re.search('^From:.+@', wildcard3))
print(re.search('h.+l', wildcard5)) # greedy, matches longest possible 'hell'
print(re.search('h.+?l', wildcard5)) # lazy, matches shortest possible 'hel'
# * = 0 or more, + = 1 or more. Applies to single character immediately to the left. Lazy requires using '?'
print('-------------------------')

# matches a string with regex
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM mike@>>'
lst = re.findall('\S+@\S+', s) # \S for any non-white space character
lst2 = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', s) # [] means acceptable characters
print(lst)
print(lst2)
print('-------------------------')

# search and extract
s2 = 'X-DSPAM-Confidence: 0.8475'
lst3 = re.findall('^X\S*: [0-9.]+', s2) # ^ to match beginning of the line. Inside square brackets, period IS NOT wildcard
print(lst3)
print('-------------------------')

# parentheses. Usually mean ignore part of the string inside them. BUT with findall(), they mean match the WHOLE string, but only extract the part inside the parentheses
s3 = 'X-DSPAM-Confidence: 0.6178'
lst4 = re.findall('^X\S*: ([0-9.]+)', s3)
print(lst4)
print('-------------------------')

# Escape character, match the actual character and ignore what is represented in regex
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x) # dollar sign actually means end of line
print(y)
print('-------------------------')
