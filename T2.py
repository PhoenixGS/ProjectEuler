import time

start = time.time()
ans = 0
x = 2
y = 8
ans = ans + x + y
while (x + 4 * y <= 4000000):
    t = y
    y = x + 4 * y
    x = t
    ans = ans + y
print ans
print "Time:", time.time() - start
