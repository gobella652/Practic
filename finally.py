import time
try:
    f = open('text.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, ' ')
        time.sleep(10)
except KeyboardInterrupt:
    print('you closed this app')
finally:
    f.close()