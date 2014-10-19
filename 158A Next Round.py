nk = map(int, raw_input().split(' '))
score = map(int, raw_input().split(' '))

count = 0
for item in score:
	if item > 0 and item >= score[nk[1]-1]:
		count += 1
print count
	
	