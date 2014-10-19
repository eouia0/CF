N = 20
dic = {0: ".", 1: "!", 2: "X", 3: "#"}
cases = int(raw_input())

for case in range(cases):
    days = int(raw_input())
    D = map(int, raw_input().split())
    dna = [[0] * N for i in range(N)]
    for i in range(N):
        line = raw_input().split()
        for j in range(N):
            dna[i][j] = int(line[j])

    for day in range(days):
        new = [[0] * N for i in range(N)]
        for i in range(N):
            for j in range(N):
                left = dna[max(i-1, 0)][j]
                right = dna[min(i+1, N-1)][j]
                up = dna[i][max(j-1, 0)]
                down = dna[i][min(j+1, N-1)]
                new[i][j] = dna[i][j] + D[left+right+up+down]
        for i in range(N):
            for j in range(N):
                dna[i][j] = new[i][j]
                
                
    for i in range(N):
        line = ""
        for j in range(N):
            line += dic[new[i][j]]
        print line
    
    print "\n"