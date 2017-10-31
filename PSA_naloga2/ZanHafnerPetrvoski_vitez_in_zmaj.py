# Naloga 1: Nicle
# Žan Hafner Petrovski, 27151071
# matematika, 3. letnik

smeri = {"gor", "dol", "levo", "desno"}
zasedeno = {"#", "V", "Z", False}
matrika = []
vitez = (-1,-1)
zmaj = (-1,-1)

def je(matrika, i, j):
    # vrne matrika[i][j], če je (i,j) v matriki, sicer False
    if i < 0 or j < 0:
        return False
    try:
        return matrika[i][j]
    except IndexError:
        return False

def mozni_premiki(polozaj, matrika):
    i, j = polozaj
    mozni = []
    if je(matrika,i-1,j) not in zasedeno:
        mozni.append((-1,0))
    if je(matrika,i+1,j) not in zasedeno:
        mozni.append((+1,0))
    if je(matrika,i,j-1) not in zasedeno:
        mozni.append((0,-1))
    if je(matrika,i,j+1) not in zasedeno:
        mozni.append((0,+1))
    return mozni

def napadalni_polozaji(matrika):
    # vrne slovar položajev z vrednostmi napada, če pridemo do tega položaja
    polozaji = {}
    i,j = zmaj

    if je(matrika,i-1,j) not in zasedeno:
        polozaji[(i-1,j)] = 1
        k = 0
        #levo
        while je(matrika,i-1,j-k) not in zasedeno:
            polozaji[(i-1,j-k)] = k+1
            k += 1
        k = 0
        #dol
        while je(matrika,i-1-k,j) not in zasedeno:
            polozaji[(i-1-k,j)] = k+1
            k += 1
        k = 0
        #desno
        while je(matrika,i-1,j+k) not in zasedeno:
            polozaji[(i-1,j+k)] = k+1
            k += 1

    if je(matrika,i+1,j) not in zasedeno:
        polozaji[(i + 1, j)] = 1
        k = 0
        # levo
        while je(matrika,i+1,j-k) not in zasedeno:
            polozaji[(i + 1, j - k)] = k + 1
            k += 1
        k = 0
        # gor
        while je(matrika,i+1+k,j) not in zasedeno:
            polozaji[(i + 1 + k, j)] = k + 1
            k += 1
        k = 0
        # desno
        while je(matrika,i+1,j+k) not in zasedeno:
            polozaji[(i + 1, j + k)] = k + 1
            k += 1

    if je(matrika,i,j-1) not in zasedeno:
        polozaji[(i, j-1)] = 1
        k = 0
        # levo
        while je(matrika,i,j-1-k) not in zasedeno:
            polozaji[(i, j-1 - k)] = k + 1
            k += 1
        k = 0
        # gor
        while je(matrika,i+k,j-1) not in zasedeno:
            polozaji[(i+k, j - 1)] = k + 1
            k += 1
        k = 0
        # dol
        while je(matrika,i-k,j-1) not in zasedeno:
            polozaji[(i-k, j - 1)] = k + 1
            k += 1

    if je(matrika,i,j+1) not in zasedeno:
        polozaji[(i, j + 1)] = 1
        k = 0
        # desno
        while je(matrika,i,j+1+k) not in zasedeno:
            polozaji[(i, j + 1 + k)] = k + 1
            k += 1
        k = 0
        #gor
        while je(matrika,i+k,j+1) not in zasedeno:
            polozaji[(i+k, j + 1)] = k + 1
            k += 1
        k = 0
        # dol
        while je(matrika,i-k,j+1) not in zasedeno:
            polozaji[(i - k, j + 1)] = k + 1
            k += 1
    print(polozaji)
    return polozaji


def razdalje(L, matrika):
    # matriko spremeni tako, da pike zamenja z oddaljenostjo polja od začetnega položaja viteza
    mat = [vrstica[:] for vrstica in matrika]
    mat = floodfill(mat, vitez, L)
    print(mat)


def floodfill(matrika, polozaj, L, n=0, drugic=False):
    print("N:",n)
    if n == 0 or n > L:
        if drugic:
            print("mm:", matrika)
            return matrika
    mozni = mozni_premiki(polozaj, matrika)
    i,j = polozaj
    if matrika[i][j] == '.':
        matrika[i][j] = 1
    for premik in mozni:
        a,b = premik
        floodfill(matrika, (i+a,j+b), L, n+1, True)
    print("n:",n, matrika)


def najboljsi_napad(L, M=matrika):
    if L == 0:
        global vitez
        i,j = vitez
        napadi = napadalni_polozaji(matrika)
        return napadalni_polozaji(matrika)[(i,j)]
    # for premik in mozni_premiki(vitez, matrika):
    #     i,j = vitez
    #     a,b = premik
    #     spr_matrika = matrika[:][:]
    #     spr_matrika[i][j], spr_matrika[i+a][j+b] = ".", "V"
    #     vitez = (i+a,j+b)
    #     najboljsi_napad(L-1, spr_matrika)

st_testov = int(input().strip())
presledek = input()

for st in range(st_testov):
    sez = input().strip().split(" ")
    w = int(sez[0])
    h = int(sez[1])
    L = int(sez[2])

    matrika = [[] for _ in range(h)]
    vitez = (-1,-1) #zacetni polozaj viteza
    zmaj = (-1,-1)

    for i in range(h):
        vrstica = input().strip()
        for j in range(w):
            znak = vrstica[j]
            matrika[i].append(znak)
            if znak == 'V':
                vitez = (i,j)
            if znak == 'Z':
                zmaj = (i,j)

    #print(matrika, "vitez:", vitez)
    print(razdalje(L,matrika))
    #print(najboljsi_napad(L, matrika))
    if st < st_testov - 1:
        presledek = input()
