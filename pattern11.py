rows = int(input("enter the no of rows\n"))
#     1
#    222
#   33333
#  4444444
# 555555555
for i in range(1, rows+1):
    for j in range(1, (rows-i)+1):
        print(" ", end='')
    for k in range(1, (2*i-1)+1):
        print(i, end='')
    print()

# reverse
# 555555555
#  4444444
#   33333
#    222
#     1
for l in range(rows,0,-1):
    for m in range(1, (rows-l)+1):
        print(" ", end='')
    for n in range(1, (2*l-1)+1):
        print(l, end='')
    print()