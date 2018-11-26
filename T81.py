import time

n = 80
start = time.time()
x = []
for i in range(n):
	x.append(map(int, raw_input().split(',')))
f = [([0] * n) for i in range(n)]
f[0][0] = x[0][0]
for i in range(1, n):
	f[0][i] = f[0][i - 1] + x[0][i]
for i in range(1, n):
	f[i][0] = f[i - 1][0] + x[i][0]
for i in range(1, n):
	for j in range(1, n):
		f[i][j] = min(f[i - 1][j], f[i][j - 1]) + x[i][j]
print f[n - 1][n - 1]
print time.time() - start