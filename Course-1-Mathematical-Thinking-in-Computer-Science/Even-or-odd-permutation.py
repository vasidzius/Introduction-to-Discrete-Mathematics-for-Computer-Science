'''

Even-or-odd-permutation
http://code.activestate.com/recipes/578227-generate-the-parity-or-sign-of-a-permutation/

'''

import itertools as it

def is_permutation(p):
    
    return (set(p) == set(range(len(p))))

def perm_parity(lst):
    '''\
    Given a permutation of the digits 0..N in order as a list, 
    returns its parity (or sign): +1 for even parity; -1 for odd.
    '''
    parity = 1
    for i in range(0,len(lst)-1):
        if lst[i] != i:
            parity *= -1
            mn = min(range(i,len(lst)), key=lst.__getitem__)
            lst[i],lst[mn] = lst[mn],lst[i]
    return parity  
    
def is_even_permutation(p):
    is_used = []
    # cycles = []
    parity = 1
    for i in range(len(p)):
        if (i not in is_used):
            is_used.append(i)
            # cycle = [i]
            pointer = p[i]
            while(pointer != i):
                parity *= -1
                # cycle.append(pointer)
                is_used.append(pointer)
                pointer = p[pointer]
            # cycles.append(cycle)
    # print(cycles, parity)
    return True if parity==1 else False
    
    
    
    
for p in it.permutations(range(7)):
        l = list(p)
        parity_not_mine = perm_parity(l)
        # print("%2i %r" % (parity_not_mine, p))
        print(is_even_permutation(p))
        

