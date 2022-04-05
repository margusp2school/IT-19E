map = [
    [12, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 24]
]

start_x = 0
start_y = 0

def saab_liikuda_paremale(map, praegused_kordinaadid):
    print("SIIN TOIMIB SEE")
    print(map[0][0])
    print("SIIN TOIMUS SEE")
    return False 

print(saab_liikuda_paremale(map, [start_x, start_y]))

def print_kaart():
    print(map[0])
    print(map[1])
    print(map[2])
    print(map[3])
    print(map[4])

print_kaart()
