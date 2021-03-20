# odd numbers

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# 0 to 100 in 10's

for i in range(0, 110, 10):
    print(i, end=' ')
print()

# 20 to 1

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# n stars

n = int(input("Number of stars: "))
for i in range(1, n+1, 1):
    print('*', end='')
print()

# n stars (part 2)

n = int(input("Number of stars: "))
for i in range(1, n+1, 1):
    for c in range(1, i+1, 1):
        print('*', end='')
    print()
print()