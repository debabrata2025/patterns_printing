# 1
# 12
# 123
# 1234
# 12345

rows = int(input("enter no of rows:\n"))

# 1234
# 123
# 12
# 1

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end='')
    print()

# reverse
for k in range(rows,0,-1):
    for l in range(1,k+1):
        print(l, end='')
    print()
