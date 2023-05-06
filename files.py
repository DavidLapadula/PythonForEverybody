exampleTxtHandle = open('example.txt')

for line in exampleTxtHandle:
    print('test: ' + line)

exampleTxtHandle2 = open('example.txt').read()

print(len(exampleTxtHandle2))

exampleTxtHandle3 = open('example.txt')

for line in exampleTxtHandle3:
    line = line.rstrip()
    if line.find('final') == -1: continue
    print('Yes ' + line)

fname = input('enter the file name')

try:
    fhand = open(fname)
except: 
    print('file cannot be opened')
    exit()

fout = open('output.txt', 'w')
fout.write('hello world')
fout.close()

print(repr('1 2\t 3\n 4')) #preferable to print as will show all characters
