word = raw_input()
def checkUpper(word, index):
    for i in range(index, len(word)):
        if word[i].islower():
            return False
    return True

if checkUpper(word, 0):
    print word.lower()
elif checkUpper(word, 1):
    print word[0].upper() + word[1:].lower()
else:
    print word