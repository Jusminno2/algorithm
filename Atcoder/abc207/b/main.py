a, b, c, d = map(int, input().split())
count = 0
red = a
blue = 0

if b > c * d:
    print(-1)
    exit()

if a == 0:
    print(0)
    exit()

if red < blue * d:
    print(red, blue * d)

while red >= blue * d:
    count += 1
    red = red + b
    blue = blue + c

print(count)


