#!/usr/bin/env python3
"""F2 campaign: the ZERO-PREFIX Q EQUIVALENCE (Modal verification).

THEOREM (proof in the note; three banked pieces): for j < char q, the
F2 level-j census equals the v13 zero-prefix census on the mu_n
divisor lattice:

  #{S in mu_n, |S| = b : p_1(S) = .. = p_j(S) = 0}
    = #{monic degree-b divisors f | X^n - 1 :
        top-j coefficients of f (below the leading 1) all zero}.

(Newton dictionary e_1..e_j <-> p_1..p_j, triangular and invertible
for j < q; divisors of X^n - 1 <-> b-subsets of mu_n.)

VERIFIED here by computing both sides via INDEPENDENT exact DPs:
  left  : power-sum DP over (p_1..p_j) in F_q^j  (as before);
  right : locator-coefficient DP — multiply factors (X - x), x in
          mu_n (take/skip), tracking only the top j coefficients
          (e_1..e_j) in F_q^j.
Assert equality per (row, j). Any mismatch refutes the equivalence.
"""
from math import comb

import modal

app = modal.App("rs-mca-f2-zeroprefix")
image = modal.Image.debian_slim()

ROWS = [(17, 16, 5), (31, 30, 4), (97, 32, 3), (113, 16, 3),
        (257, 16, 3), (193, 32, 2)]


@app.function(image=image, cpu=2, memory=3072, timeout=280)
def row(job):
    q, n, J = job
    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))
    b = n // 2
    out = {}
    for j in range(1, J + 1):
        # left: power sums
        dp = {(0,) * j: [1] + [0] * b}
        for x in D:
            pw = [pow(x, e, q) for e in range(1, j + 1)]
            new = {}
            for st, vec in dp.items():
                t = new.setdefault(st, [0] * (b + 1))
                for w in range(b + 1):
                    t[w] += vec[w]
                st2 = tuple((st[e] + pw[e]) % q for e in range(j))
                t2 = new.setdefault(st2, [0] * (b + 1))
                for w in range(b):
                    if vec[w]:
                        t2[w + 1] += vec[w]
            dp = new
        assert sum(v[b] for v in dp.values()) == comb(n, b)
        left = dp.get((0,) * j, [0] * (b + 1))[b]
        # right: locator top-j coefficients; state = (e_1..e_j),
        # multiplying (X - x) shifts: e_i' = e_i + x * e_{i-1} (e_0 = 1)
        # with signs folded in (track coefficients of the monic product
        # directly: c_i' = c_i - x * c_{i-1})
        dp2 = {(0,) * j: [1] + [0] * b}
        for x in D:
            new = {}
            for st, vec in dp2.items():
                t = new.setdefault(st, [0] * (b + 1))
                for w in range(b + 1):
                    t[w] += vec[w]
                st2 = []
                prev = 1
                for e in range(j):
                    st2.append((st[e] - x * prev) % q)
                    prev = st[e]
                st2 = tuple(st2)
                t2 = new.setdefault(st2, [0] * (b + 1))
                for w in range(b):
                    if vec[w]:
                        t2[w + 1] += vec[w]
            dp2 = new
        assert sum(v[b] for v in dp2.values()) == comb(n, b)
        right = dp2.get((0,) * j, [0] * (b + 1))[b]
        assert left == right, ("EQUIVALENCE FAILED", q, n, j, left, right)
        out[j] = left
    return {"q": q, "n": n, "b": b, "counts": out}


@app.local_entrypoint()
def main():
    res = list(row.map(ROWS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        print(f"  ({r['q']},{r['n']},b={r['b']}): power-sum census == "
              f"zero-prefix divisor census at every j: {r['counts']}")
    if fails:
        raise SystemExit(f"F2_ZERO_PREFIX_EQUIVALENCE_FAIL ({fails})")
    print("\nF2_ZERO_PREFIX_EQUIVALENCE_PASS")
