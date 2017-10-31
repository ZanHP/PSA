# Naloga 1: Nicle
# Žan Hafner Petrovski, 27151071
# matematika, 3. letnik

def naloga(n, m):
    a = st_nizov_modulo(2*n-2,m)
    b = st_nizov_modulo(n-2,m)
    return (a - b)%m


def potenca(matrika, n, m):
    R = [[1,0],[0,1]]
    while n > 0:
        if n & 1:
            R = zmnozi(R, matrika)
            for i in range(2):
                for j in range(2):
                    R[i][j] %= m
        matrika = kvadriraj(matrika)
        for i in range(2):
                for j in range(2):
                    matrika[i][j] %= m
        n >>= 1
    return R

def kvadriraj(M):
    # M je oblike [[a,b],[c,d]]
    a = M[0][0]
    b = M[0][1]
    c = M[1][0]
    d = M[1][1]
    return [[a*a + b*c, a*b + b*d], [a*c + d*c, b*c + d*d]]

def zmnozi(m1,m2):
    r = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                r[i][j] += m1[i][k] * m2[k][j]
    return r

def st_nizov_modulo(n, m):
    if n == 1:
        return 2
    if n == 2:
        return 3
    # m je matrika, ki ustreza rekurzivni zvezi
    M = [[0,1],[1,1]]
    v1 = 2
    v2 = 3
    potencirana = potenca(M, n-2, m)
    c = potencirana[1][0]
    d = potencirana[1][1]
    return c*v1 + d*v2

st_vrstic = int(input().strip())

for _ in range(st_vrstic):
    sez = input().strip().split(" ")
    n = int(sez[0])
    m = int(sez[1])
    print(naloga(n, m))

