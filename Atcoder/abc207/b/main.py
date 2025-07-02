a, b, c, d = map(int, input().split())
ans = -1
diff = c*d - b
if 0 < diff:
    ans = (a + diff -1) // diff
print(ans)

