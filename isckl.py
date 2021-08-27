try:
    text = input('smth')
except EOFError:
    print('why')
except KeyboardInterrupt:
    print('otmena')
else:
    print(text)