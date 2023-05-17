import socket
import urllib.request, urllib.parse, urllib.error
import re
import ssl

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) #512 character chunks
    if len(data) < 1: 
        break
    print(data.decode(), end='')

mysock.close()

print('--------------------')

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # second param of get is what to be returned if key does not exist
print(counts)

print('---------------------')

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() # read will return as bytes instead of http response
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()


print('---------------------')

# Ignore ssl req's
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())

# Beautiful soup can also be used to parse flawed html, and will give you access to the elements on the page
    