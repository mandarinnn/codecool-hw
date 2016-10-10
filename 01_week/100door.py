number = 100
doors = [False] * number

for i in range(len(doors)):
    for j in range(i, len(doors), i + 1):
        doors[j] = not doors[j]

print("The following doors are open: ")

for k in range(len(doors)):
    if doors[k] == True:
        print(k + 1, end=' ')

print()

