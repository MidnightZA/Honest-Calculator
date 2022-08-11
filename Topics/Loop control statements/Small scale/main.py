numList = []
while True:
    num = input()
    if num == '.':
        break
    else:
        fNum = float(num)
        numList.append(fNum)
print(min(numList))
