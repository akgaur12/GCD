def gcd(a, b):
    g = a if a<b else b
    while g>=1:
        if a%g==0 and b%g==0:
            return g
    g -= 1

    
print(gcd(6, 0))
