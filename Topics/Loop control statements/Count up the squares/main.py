Loop = True
numList = []
sqList = []
ans = 0

while Loop == True:
    num = int(input())
    numList.append(num)
    if sum(numList) == 0:
        Loop = False

for nums in numList:
    sqList.append(nums**2)

print(sum(sqList))
