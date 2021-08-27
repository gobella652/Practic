def podg(text):
    text = text.lower()
    res = ''
    i = 0
    while i < len(text):
        if text[i] != ' ' and text[i] != '.' and text[i] != ',' and text[i] != '!':
            res = res + text[i]
        i += 1
    return res

def reverse(text):
    text = text[::-1]
    return text

def palindrom(text):
    if podg(text) == reverse(podg(text)):
        return True
    else:
        return False

inp = input()
#ar = [1,2,3,4,5]
#ar.remove(ar[3])
#print(ar)
print(palindrom(inp))