'''

Largest-Amount-that-Cannot-Be-Paid-with-5-and-7-Coins

Imagine we have only 5- and 7-coins. One can prove that any large 
enough integer amount can be paid using only such coins. Yet clearly we 
cannot pay any of numbers 1, 2, 3, 4, 6, 8, 9 with our coins. 
What is the maximum amount that cannot be paid?

'''

def change(amount):
    
    # assert(amount >= 5 
    #         and amount != 9
    #         and amount != 11
    #         and amount != 13
    #         and amount != 16
    #         and amount != 18
    #         )
    
    if(amount < 5):
        return ['X']
    
    if amount == 5:
        return [5]
    
    if amount == 7:
        return [7]
        
    if amount == 10:
        return [5,5]
        
    if amount == 12:
        return [5,7]
    
    if amount == 12:
        return [5,7]
        
    if(amount % 5 == 0):
        coins = change(amount - 5)
        coins.append(5)
    else:
        coins = change(amount - 7)
    coins.append(7)
    return coins
    
result = []
for i in range(1000):
    result.append(change(i))
    
count = 0
for i in result:
    if('X' in i):
        print(count, i)
    count += 1
    
