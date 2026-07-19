from math import lgamma, log
def lgC(N, m):
    if m < 0 or m > N: return float("-inf")
    return (lgamma(N+1) - lgamma(m+1) - lgamma(N-m+1)) / log(2)
n, k, sigma = 2**41, 2**40, 8592912738
for lgq in (255.9000001, 255.901, 255.91, 255.95, 255.99, 256.0):
    best = (None, -1e18)
    for e in range(1, 41):
        c = 2**e; N = n // c; d = -(-sigma // c)
        if N // 2 + d > N: continue
        f = lgC(N, N//2 + d) - lgq * (d - 1)
        if f > best[1]: best = (e, f)
    print(f"lgq={lgq:>12}: argmax e={best[0]}, log2 F = {best[1]:.3f}")
