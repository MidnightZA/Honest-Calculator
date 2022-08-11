out = []
# seq, x = input().splitlines()
seq = input()
x = input()
seq = seq.split(' ')

for i in range(0,len(seq)):
    if seq[i] == x:
        out.append(str(i))
if x not in seq:
    print('not found')

print(' '.join(out))