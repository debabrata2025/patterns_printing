rows = int(input("enter the no of rows\n"))
#     1
#    123
#   12345
#  1234567
# 123456789
for i in range(1, rows+1):
    for j in range(1, (rows-i)+1):
        print(" ", end='')
    for k in range(1, (2*i-1)+1):
        print(k, end='')
    print()

# 123456789
#  1234567
#   12345
#    123
#     1
for i in range(rows, 0, -1):
    for j in range(1, (rows-i)+1):
        print(" ", end='')
    for k in range(1, (2*i-1)+1):
        print(k, end='')
    print()