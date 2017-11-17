import time
import math

def max(x, y):
    if x > y:
        return x
    return y

start = time.time()
ans = 1
x = int(input())
for i in range(2, int(math.sqrt(x) + 1)):
    if x % i == 0:
        ans = max(ans, i)
    while x % i == 0:
        x = x / i
ans = max(ans, x)
print ans
print "Time:", time.time() - start