rows = int(input("enter the number of rows\n"))
# *
# **
# ***
# ****
# *****

for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*", end='')
    print(" ")

print("-------both-loop-is-dependent-on-ith-value----------")
# reverse

# *****
# ****
# ***
# **
# *
for k in range(rows,0,-1):
    for l in range(1,k+1):
        print("*", end='')
    print(" ")