x = 0
dx = 1
y = 0
dy = 1
z = 0
dz = 1

while x < 4:
    y = 0
    while y < 4:
        z = 0
        while z < 4:
            print(x, y, z)
            z = z + dz
        y = y + dy
    x = x + dx

