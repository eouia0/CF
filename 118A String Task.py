vowel = ["A", "O", "Y", "E", "U", "I"]
vowel = set(vowel)

word = raw_input()
sol = ""
for string in word:
    if string.upper() not in vowel:
        sol = sol + "." + string.lower()
print sol