#!/usr/bin/env python3
"""F3 shallow-instance exponent ladder (Modal): exact T(n,h,q) censuses.

T(n,h,q) = #unordered pairs of disjoint h-subsets of mu_n with equal
e_1..e_{h-1} (= constant-shift divisor pairs of X^n - 1 = the top
shift-pair stratum = F3's trades). Bucket census by exact signature:
cost C(n,h), independent of q. Intersecting equal-signature pairs are
impossible (equal locators force equal sets), so T = sum_sig C(k_sig,2).

Measured per row: T, toral/nontoral split, max fiber (vs the proved n/h
cap), #colliding classes, dilation-orbit count of trades. Regimes:
q ~ n^2 (F3's floor boundary) and q ~ n^3. At h = 2, T = additive-energy
collisions of mu_n: the known law T <= C n^{5/2} (Heath-Brown-Konyagin,
n <= q^{2/3}) is the validation gate; exponents alpha(h) for h >= 3 are
the data-driven targets."""
import itertools
import json

import modal

app = modal.App("rs-mca-f3-ladder")
image = modal.Image.debian_slim()


def jobs():
    out = []
    for h, ns in ((2, (16, 32, 64, 128, 256, 512)),
                  (3, (16, 32, 64, 128, 192)),
                  (4, (16, 24, 32, 48, 64, 96)),
                  (5, (16, 24, 32, 48, 64))):
        for n in ns:
            for reg in (2, 3):
                out.append((n, h, reg))
    return out


@app.function(image=image, cpu=4, memory=6144, timeout=280)
def census(job):
    n, h, reg = job

    def is_prime(m):
        if m < 2:
            return False
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if m % a == 0:
                return m == a
        d, r = m - 1, 0
        while d % 2 == 0:
            d //= 2; r += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(r - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    q = ((n ** reg) // n) * n + 1
    while not (is_prime(q) and q > n ** reg):
        q += n
    # generator of mu_n
    g = None
    for c in range(2, q):
        x, ok = pow(c, (q - 1) // n, q), True
        if x == 1:
            continue
        y, order = x, 1
        while y != 1:
            y = y * x % q
            order += 1
        if order == n:
            g = x
            break
    D = [pow(g, i, q) for i in range(n)]

    # pass 1: signature -> count
    counts = {}
    for P in itertools.combinations(range(n), h):
        coeffs = [1] + [0] * (h - 1)
        for a in P:
            root = D[a]
            for j in range(h - 1, 0, -1):
                coeffs[j] = (coeffs[j] - root * coeffs[j - 1]) % q
            # note: we only track e_1..e_{h-1}; drop e_h
        sig = tuple(coeffs[1:])
        counts[sig] = counts.get(sig, 0) + 1
    colliding = {s for s, k in counts.items() if k >= 2}
    T = sum(k * (k - 1) // 2 for k in counts.values())
    mx = max(counts.values())

    # pass 2: collect members of colliding classes for structure stats
    toral = 0
    orbit_reps = set()
    if colliding:
        members = {}
        for P in itertools.combinations(range(n), h):
            coeffs = [1] + [0] * (h - 1)
            for a in P:
                root = D[a]
                for j in range(h - 1, 0, -1):
                    coeffs[j] = (coeffs[j] - root * coeffs[j - 1]) % q
            sig = tuple(coeffs[1:])
            if sig in colliding:
                members.setdefault(sig, []).append(P)

        def is_coset(P):
            if n % h:
                return False
            step = n // h
            r0 = P[0] % step
            return all(x % step == r0 for x in P) and len(set(P)) == h

        for sig, mem in members.items():
            for i in range(len(mem)):
                for j in range(i + 1, len(mem)):
                    A, B = mem[i], mem[j]
                    if set(A) & set(B):
                        continue
                    if is_coset(A) and is_coset(B):
                        toral += 1
                    # dilation orbit representative of the unordered pair:
                    key = min(tuple(sorted(((a + s) % n for a in A + B)))
                              for s in range(n))
                    orbit_reps.add(key)
    return {"n": n, "h": h, "q": q, "regime": reg, "T": T,
            "toral": toral, "nontoral": T - toral, "max_fiber": mx,
            "n_colliding_classes": len(colliding),
            "n_dilation_orbits": len(orbit_reps),
            "n3": n ** 3, "hbk_n52": round(n ** 2.5, 0)}


@app.local_entrypoint()
def main():
    import math
    res = [r for r in census.map(jobs(), return_exceptions=True)]
    ok = [r for r in res if isinstance(r, dict)]
    errs = len(res) - len(ok)
    print(f"{'(n,h)':>10} {'q':>10} {'reg':>4} {'T':>9} {'nontoral':>9} {'maxfib':>7} "
          f"{'orbits':>7} {'n^2.5':>10} {'n^3':>10}")
    for r in sorted(ok, key=lambda r: (r['h'], r['regime'], r['n'])):
        print(f"  ({r['n']},{r['h']})".rjust(10) + f" {r['q']:>10} {r['regime']:>4} "
              f"{r['T']:>9} {r['nontoral']:>9} {r['max_fiber']:>7} "
              f"{r['n_dilation_orbits']:>7} {int(r['hbk_n52']):>10} {r['n3']:>10}")
    # exponent fits per (h, regime) on rows with T >= 4
    print("\nalpha(h) log-log fits (rows with T >= 4):")
    for h in (2, 3, 4, 5):
        for reg in (2, 3):
            pts = [(math.log(r['n']), math.log(r['T']))
                   for r in ok if r['h'] == h and r['regime'] == reg and r['T'] >= 4]
            if len(pts) >= 3:
                xs, ys = zip(*pts)
                mx_, my = sum(xs)/len(xs), sum(ys)/len(ys)
                slope = sum((x-mx_)*(y-my) for x, y in pts) / sum((x-mx_)**2 for x in xs)
                print(f"  h={h} regime q~n^{reg}: alpha = {slope:.2f} ({len(pts)} pts)")
    if errs:
        print(f"\n{errs} worker errors/timeouts")
    with open("/tmp/f3_ladder.json", "w") as f:
        json.dump(ok, f, indent=1)
