"""
4. Desenvolva uma função que determine se um número é primo ou não. Retorne true se for primo e 
false se não for.
"""

def prim(num):
    if num < 0:
        return None
    if num == 1:
        return True
    if num == 2:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
        else:
            return True
        
print(prim(2))