#   *
#   *
# *****
#   *
#   *

rows = int(input("Enter the number of rows: "))
half_row = rows // 2

# Check if the number of rows is even
if rows % 2 == 0:
    print("Not possible for even number of rows.")
else:
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            if i == half_row + 1 or j == half_row + 1:
                print("*", end='')
            else:
                print(" ", end='')
        print()
