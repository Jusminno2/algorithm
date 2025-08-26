x, y = map(int, input().split())

month = x + y

if month <= 12:
    print(month)
else:
    print(month-12)
