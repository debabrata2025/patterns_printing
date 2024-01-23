rows = int(input("enter no of rows\n"))
#     1
#    12
#   123
#  1234
# 12345
for i in range(1, rows+1):
    #for space
    for j in range(1, (rows-i)+1):
        print(" ", end='')
    for k in range(1, i+1):
        print(k, end='')
    print()

# 12345
#  1234
#   123
#    12
#     1

for l in range(rows, 0, -1):
    #for space
    for m in range(1, (rows-l)+1):
        print(" ", end='')
    for n in range(1, l+1):
        print(n, end='')
    print()