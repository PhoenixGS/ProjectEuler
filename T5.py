import time

def gcd(x, y):
	if y == 0:
		return x
	return gcd(y, x % y)

start = time.time()
ans = 1
for i in range(1, 21):
	ans = ans * i / gcd(ans, i)
print ans
print time.time() - start