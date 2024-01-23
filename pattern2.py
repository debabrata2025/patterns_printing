rows = int(input("enter the value of rows\n"))

#     *
#    **
#   ***
#  ****
# *****

for i in range(1,rows+1):
    #for space printing
    for j in range(1, (rows-i)+1):
        print(" ", end='')
    #for star printing
    for k in range(1,i+1):
        print("*", end='')
    print(" ")
print("---------------loop-is-divided-in-2-part1-space--part2-star-------------------")
#reverse

# *****
#  ****
#   ***
#    **
#     *

for m in range(rows, 0,-1):
    # for space printing
    for l in range(1, (rows-m)+1):
        print(" ", end='')
    # for star printing
    for n in range(1, m+1):
        print("*", end='')
    print(" ")
