N, M = map(int, input().split())

for x in range(0,N+1):
	z = (M-x*2)-3*(N-x)
	y = N-x-z
	if y >= 0 and z >= 0:
		print (x,y,z)
		exit()

print(-1, -1, -1)
