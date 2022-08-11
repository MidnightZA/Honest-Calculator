guests = ''
guest_list = []

while guests !='.':
    guests = input()
    if guests == '.':
        pass
    else:
        guest_list.append(guests)
print(guest_list)
print(len(guest_list))
