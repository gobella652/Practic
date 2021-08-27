text = '''text
            text
        text'''
f = open('text.txt', 'w')
f.write(text)
f.close()
f = open('text.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()


n = open(file='n.txt')
r = n.read()
print(r)
n.close()