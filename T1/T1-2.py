import time

start = time.time()
ans = 0
ans = ans + (1 + 999 / 3) * (999 / 3) / 2 * 3
ans = ans + (1 + 999 / 5) * (999 / 5) / 2 * 5
ans = ans - (1 + 999 / 15) * (999 / 15) / 2 * 15
print ans
print "Time: ", time.time() - start