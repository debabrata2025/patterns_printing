rows = int(input("enter number of rows\n"))
# ********
# **    **
# * *  * *
# *  **  *
# *  **  *
# * *  * *
# **    **
# ********
for i in range(1, rows+1):
    for j in range(1, rows+1):
        if i == 1 or i == rows or j == 1 or j == rows or i == j or i+j == rows+1:
            print("*", end='')
        else:
            print(" ", end='')
    print()