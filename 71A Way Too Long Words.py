n = int(raw_input())
for i in range(n):
    word = raw_input()
    if len(word) <= 10:
        print word
    else:
        print word[0] + str(len(word)-2) + word[len(word)-1]