

## Verifica daca un an este bisect

## 1. Sunt divizibil cu 400
## 2. Sunt divizibil cu 4 dar nu cu 100

def este_bisect(an):
    if  an % 400 == 0  or  (an % 4 == 0 and an % 100 != 0):
        return True
    else:
        return False
