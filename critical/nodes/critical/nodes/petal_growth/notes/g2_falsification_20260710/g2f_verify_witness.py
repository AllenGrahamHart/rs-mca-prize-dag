#!/usr/bin/env python3
"""g2f_verify_witness: minimal, self-contained re-verification of a fixed-M
hybrid witness against SOL_TARGET_2's ORIGINAL (fixed-M) conjecture text.

Everything is recomputed from scratch (no shared library): field arithmetic,
the sunflower word, the codeword by direct Lagrange interpolation, the
agreement set, the staircase test at M, and the order-M-subgroup stabilizer.

WITNESS 1 (n=8):
  p=17, n=8, M=4, k=3, sigma=1, layout=fiber_pairs, scalars=geometric.
WITNESS 2 (n=16, found by grid B; filled from its JSON):
  see CLI args.
"""
import sys
from itertools import combinations


def check_witness(p, n, M, k, sigma, layout_pairs, scalar_seq, verbose=True):
    # --- domain: order-n subgroup of F_p^*
    assert (p - 1) % n == 0
    g = 2
    while True:
        fs = []
        v, d = p - 1, 2
        while d * d <= v:
            if v % d == 0:
                fs.append(d)
                while v % d == 0:
                    v //= d
            d += 1
        if v > 1:
            fs.append(v)
        if all(pow(g, (p - 1) // f, p) != 1 for f in fs):
            break
        g += 1
    g0 = pow(g, (p - 1) // n, p)
    dom = [pow(g0, j, p) for j in range(n)]
    assert len(set(dom)) == n

    # --- sunflower word: fiber_pairs layout (exponent order j, j+n/2 pairs)
    ell = sigma + 1
    assert ell == 2
    order = []
    for j in range(n // 2):
        order.extend([j, j + n // 2])
    core = sorted(order[: k - 1])
    rest = order[k - 1 :]
    t = len(rest) // ell
    petals = [sorted(rest[i * ell : (i + 1) * ell]) for i in range(t)]
    # core locator
    loc = [1]
    for j in core:
        r = dom[j]
        new = [0] * (len(loc) + 1)
        for i, c in enumerate(loc):
            new[i] = (new[i] - r * c) % p
            new[i + 1] = (new[i + 1] + c) % p
        loc = new
    def ev(poly, x):
        v = 0
        for c in reversed(poly):
            v = (v * x + c) % p
        return v
    values = [0] * n
    for c_i, petal in zip(scalar_seq, petals):
        for j in petal:
            values[j] = c_i * ev(loc, dom[j]) % p

    # --- search: all codewords (deg < k) agreeing on >= k+sigma points,
    #     found via all (k+sigma)-subsets + Lagrange on first k, then filter
    #     to fixed-M hybrids in the band.
    s = k + sigma
    found = {}
    for idxs in combinations(range(n), s):
        xs = [dom[j] for j in idxs]
        ys = [values[j] for j in idxs]
        # Lagrange through first k
        poly = [0] * k
        for i in range(k):
            num = [1]
            den = 1
            for j2 in range(k):
                if j2 == i:
                    continue
                r = xs[j2]
                new = [0] * (len(num) + 1)
                for d2, c in enumerate(num):
                    new[d2] = (new[d2] - r * c) % p
                    new[d2 + 1] = (new[d2 + 1] + c) % p
                num = new
                den = den * (xs[i] - xs[j2]) % p
            coef = ys[i] * pow(den, -1, p) % p
            for d2, c in enumerate(num):
                poly[d2] = (poly[d2] + coef * c) % p
        if any(ev(poly, x) != y for x, y in zip(xs, ys)):
            continue
        key = tuple(poly)
        if key in found:
            continue
        S = frozenset(j for j in range(n) if ev(poly, dom[j]) == values[j])
        if len(S) >= s:
            found[key] = S

    hybrids = []
    for poly, S in found.items():
        size = len(S)
        if not (s <= size <= s + M - 1):
            continue                       # top defect band of the fixed-M form
        # staircase at M: S minus full M-fibers has size < M ?
        step = n // M
        covered = 0
        nfull = 0
        for r in range(step):
            fiber = {r + step * i for i in range(M)}
            if fiber <= S:
                covered += M
                nfull += 1
        residual = size - covered
        stair_lax = residual < M            # tail-only allowed
        stair_strict = stair_lax and nfull >= 1
        # stabilizer under order-M subgroup: shifts by multiples of n/M
        stab = [a for a in range(0, n, step)
                if all(((x + a) % n) in S for x in S)]
        primitive = (len(stab) == 1)
        if (not stair_lax) and (not primitive):
            hybrids.append((poly, sorted(S), size, residual, nfull, stab))
        if verbose and (not stair_strict) and (not primitive):
            pass
    return hybrids, petals, values, dom


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "w2":
        # witness cell from grid B (n=16): args p k sigma scalars-mode geometric
        p, n, M, k, sigma = 97, 16, 4, 6, 1
        # geometric scalars: 1,5,25,... mod p, t petals
        t = (n - (k - 1)) // 2
        scal = []
        v = 1
        for _ in range(t):
            scal.append(v)
            v = v * 5 % p
        hyb, petals, values, dom = check_witness(p, n, M, k, sigma, None, scal)
    else:
        p, n, M, k, sigma = 17, 8, 4, 3, 1
        t = (n - (k - 1)) // 2
        scal = []
        v = 1
        for _ in range(t):
            scal.append(v)
            v = v * 5 % p
        hyb, petals, values, dom = check_witness(p, n, M, k, sigma, None, scal)
    print(f"p={p} n={n} M={M} k={k} sigma={sigma} scalars={scal}")
    print(f"petals (exponent indices): {petals}")
    print(f"word values (by exponent index): {values}")
    if not hyb:
        print("NO in-band fixed-M hybrid found -> witness NOT confirmed")
        sys.exit(1)
    for poly, S, size, residual, nfull, stab in hyb:
        print(f"HYBRID CONFIRMED: codeword coeffs {poly} agreement-set(exponents) {S} "
              f"size {size} in band [{k+sigma},{k+sigma+M-1}]; residual@M={residual} >= M={M} "
              f"(full {M}-fibers inside: {nfull}) -> NOT staircase at M (any reading); "
              f"order-{M}-subgroup stabilizer shifts {stab} -> NONTRIVIAL")
    sys.exit(0)
