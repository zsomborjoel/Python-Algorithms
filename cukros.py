"""
Készíts függvényt, ami megállapítja hogy egy szöveg cukormentes-e. Egy szöveget akkor mondunk cukormentesnek, ha nem olvasható ki belőle az a szó, hogy “cukor”. 
Nem kell, hogy a betűk egymás mellett álljanak, de a sorrendnek helyesnek kell lennie. 
Az is számít, ha pl a szöveg huszadik karaktere a “C”, majd pár karakterrel később jön az “U”, stb.
"""

arr = 'hduiejdcuhcukdwadagfqewqorkryjsjsj'
fin = {}for i in arr:
    if i == 'c':
        fin[i] = 1
    elif i == 'u' and 'c' == ''.join(fin):
        fin[i] = 1
    elif i == 'k' and 'cu' == ''.join(fin):
        fin[i] = 1
    elif i == 'o' and 'cuk' == ''.join(fin):
        fin[i] = 1
    elif i == 'r' and 'cuko' == ''.join(fin):
        fin[i] = 1if ''.join(fin) == 'cukor':
    print('cukros')
else:
    print('nem cukros')
