import random 

seq = []

for i in range(10):
    seq.append(random.randrange(100))

maxNum = seq[0]
temp = 0

for num in seq:
    if num > maxNum:
        maxNum = num
    else:
        continue

print(seq)
print("Max number is: " + str(maxNum))
