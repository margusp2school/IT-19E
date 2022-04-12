map = [
    [12, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 24]
]

VABA_TEE = 0
SEIN = 1

start_x = 0
start_y = 0

def saab_liikuda_paremale(kaart, praegused_kordinaadid):
    print(kaart[1][3] == VABA_TEE)
    return False  

def saab_liikuda_vasakule(kaart, praegused_kordinaadid):
    print(kaart[0][0] == VABA_TEE)
    return False  

def print_kaart(kaart):
    print(kaart[0])
    print(kaart[1])
    print(kaart[2])
    print(kaart[3])
    print(kaart[4])

print_kaart(map)

print(saab_liikuda_paremale(map, [2, 1]))
# print(saab_liikuda_paremale(map, [1, 1]))

# TEHA FUNKTSIOONID LIIKUMISEKS
# Googeldada: "python random.choice"
# valida suvaline vaba tee liikumiseks
# https://github.com/margusp2school/IT-19E