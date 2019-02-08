'''
Find collocations of N queens on N*N table withou attack each other
'''
allSolutions = 0

def expand(perm, n):
    if(len(perm) == n):
        print(perm)
        global allSolutions
        allSolutions += 1
        # exit()
        
    for k in range(n):
        if(k not in perm):
            perm.append(k)
            if(last_is_suitable(perm)):
                expand(perm, n)
            perm.pop()
            
def last_is_suitable(perm):
    i = len(perm) - 1;
    for j in range(i):
        if(i - j == abs(perm[i] - perm[j])):
            return False
    return True



expand([], 8)
print(allSolutions)

