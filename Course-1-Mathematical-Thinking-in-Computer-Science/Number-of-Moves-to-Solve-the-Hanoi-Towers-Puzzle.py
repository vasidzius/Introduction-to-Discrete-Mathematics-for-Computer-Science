'''

Number-of-Moves-to-Solve-the-Hanoi-Towers-Puzzle

The number of moves required to solve the Hanoi Towers puzzle for n=1n=1
and n=2n=2 discs is equal to 1 and 3, respectively. Implement the recursive
solution for the Hanoi Towers (described in the lectures) and count the
number of moves for n=6 discs.

'''

def hanoi(n):
    
    assert(n > 0)
    
    if n == 1:
        return 1

    # return 2*hanoi(n - 1) + 1
    return 2**n - 1

n = 6
print(hanoi(n))
