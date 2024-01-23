#sqare pattern

# ****
# ****
# ****
# ****

rows = int(input("enter the number of rows\n"))

for i in range(1, rows+1):
    for j in range(1, rows+1):
        print("*", end='')
    print()

#hollow
# ****
# *  *
# *  *
# ****

for k in range(1, rows+1):
    for l in range(1, rows+1):
        if k == 1 or k == rows or l == 1 or l == rows:
            print("*", end='')
        else:
            print(" ", end='')
    print(" ")