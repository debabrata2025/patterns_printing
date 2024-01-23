#cross pattern
rows = int(input("enter the nujber of rows\n"))

# *   *
#  * *
#   *
#  * *
# *   *

for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i == j or i+j == rows+1:
            print("*", end='')
        else:
            print(" ", end='')
    print()