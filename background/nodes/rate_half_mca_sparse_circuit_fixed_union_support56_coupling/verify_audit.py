#!/usr/bin/env python3
"""Independent direct arithmetic audit of the support-5/6 charge."""

from math import comb


K, m, u, g = 83, 67555, 29, 6
R, N = K - u - g, m - u
w5, w6 = 15 * comb(m - 5, 6), 10 * comb(m - 6, 5)
pieces = []
for i in range(4):
    L = comb(u, i) * R * comb(N, 4 - i) // (5 - i)
    A = comb(u, i) * R * comb(N, 5 - i)
    lam = (6 - i) * w5 - (N - R - 4 + i) * w6
    pieces.append((w6 * A + max(lam, 0) * L) // (6 - i))
pieces.append(w5 * (comb(u, 4) * R + comb(u, 5)))
pieces.append(w6 * (comb(u, 4) * R * N // 2 + comb(u, 5) * R + comb(u, 6)))
assert sum(pieces) == 16499018112619081218909046137784886320200565035
assert R == 48 and N == 67526
assert N >= R + 4
print({"independent_pieces": len(pieces), "weighted_cap": sum(pieces)})
