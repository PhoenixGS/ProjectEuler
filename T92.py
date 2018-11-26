import time

f = [0] * 10000000
f[1] = 1
f[89] = 2

def calc(x):
	if (f[x]):
		return f[x]
	c = 0
	t = x
	while t:
		c = c + (t % 10) * (t % 10)
		t = t / 10
	f[x] = calc(c)
	return f[x]

start = time.time()
for i in range(1, 10000000):
	if f[i] == 0:
		calc(i)
ans = 0
for i in range(1, 10000000):
	ans += (f[i] == 2)
print ans
print time.time() - start