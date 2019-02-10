'''

Any-amount-more-than-8-with-3-and-5

'''

def change(amount):
    
    assert(amount >= 8)
    
    if amount == 8:
        return [3,5]
    if amount == 9:
        return [3,3,3]
    if amount == 10:
        return [5,5]
    
    coins = change(amount - 3)
    coins.append(3)
    
    return coins
    
coins = change(20)
print(coins)
