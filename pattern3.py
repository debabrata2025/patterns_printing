rows = int(input("enter the number of rows\n"))

#     *
#    ***
#   *****
#  *******
# *********

for i in range(1, rows+1):
    #space printing
    for j in range(1,(rows-i)+1):
        print(" ", end='')
    #star printing
    for k in range(1,(2*i-1)+1):
        print("*", end='')
    print(" ")

#revers
print("------------1.space-count-and-star(2i-1)-----------------------------")

# *********
#  *******
#   *****
#    ***
#     *

for m in range(rows, 0, -1):
    for n in range(1, (rows-m)+1):
        print(" ", end='')
    for o in range(1,(2*m-1)+1):
        print("*", end='')
    print(" ")



