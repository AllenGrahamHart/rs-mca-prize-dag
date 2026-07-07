#!/usr/bin/env python3
"""F3 IDENTIFICATION machine check (Modal): F3 trades == top shift-pair
stratum sp_{h-1}(h; mu_n), including the toral/pullback split.

Both counters in one script: (a) F3's own signature census (functions
copied verbatim from experiments/u1_x4_active_core_budget_probe.py);
(b) the fleet's joint (|S|,|T|,prefix-difference) DP counting ordered
disjoint pairs with equal power sums p_1..p_{h-1} (Newton-equivalent to
equal e_1..e_{h-1} for h-1 < p), plus a coset-pair count for the toral
column. Identification predicts: DP_ordered == 2 * census_unordered and
DP_toral_ordered == 2 * census_toral, on every row."""
import itertools
import json

import modal

app = modal.App("rs-mca-f3-ident")
image = modal.Image.debian_slim().pip_install("numpy")

ROWS = [(16, 3, 17), (16, 3, 97), (16, 4, 17), (16, 4, 97),
        (32, 4, 97), (32, 5, 193)]


@app.function(image=image, cpu=2, memory=4096, timeout=240)
def check(row):
    import numpy as np
    n, h, p = row

    def mu_gen(p_, n_):
        for c in range(2, p_):
            seen, x = set(), 1
            ok = True
            for _ in range(p_ - 1):
                x = x * c % p_
                seen.add(x)
            if len(seen) == p_ - 1:
                return pow(c, (p_ - 1) // n_, p_)
    zeta = mu_gen(p, n)
    powers = [pow(zeta, a, p) for a in range(n)]

    # --- (a) F3's census, verbatim logic ---
    def elementary_signature(exps):
        coeffs = [1] + [0] * h
        for a in exps:
            root = powers[a]
            for j in range(h, 0, -1):
                coeffs[j] = (coeffs[j] - root * coeffs[j - 1]) % p
        first = tuple(((-coeffs[j]) % p if j & 1 else coeffs[j])
                      for j in range(1, h))
        last = (-coeffs[h]) % p if h & 1 else coeffs[h]
        return first, last

    def is_coset(exps):
        if n % h:
            return False
        step = n // h
        base = sorted(e % step for e in exps)
        return base == [base[0]] * h and len({e for e in exps}) == h

    buckets = {}
    for exps in itertools.combinations(range(n), h):
        sig, last = elementary_signature(exps)
        buckets.setdefault(sig, []).append((exps, last))
    unordered = toral = nontoral = 0
    for entries in buckets.values():
        for i, (L, ll) in enumerate(entries):
            Ls = set(L)
            for R_, rl in entries[i + 1:]:
                if Ls & set(R_):
                    continue
                if ll == rl:
                    continue
                unordered += 1
                if is_coset(L) and is_coset(R_):
                    toral += 1
                else:
                    nontoral += 1

    # --- (b) the fleet DP: ordered disjoint pairs, equal p_1..p_{h-1} ---
    w = h - 1
    D = sorted(powers)
    dp = np.zeros((h + 1, h + 1) + (p,) * w, dtype=np.int64)
    dp[(0, 0) + (0,) * w] = 1
    for x in D:
        v = [pow(x, j, p) for j in range(1, w + 1)]
        vneg = [(-s) % p for s in v]
        def ndroll(a, sh):
            for ax, s in enumerate(sh):
                a = np.roll(a, s, axis=ax)
            return a
        add_S = np.stack([np.stack([ndroll(dp[a, b], v)
                                    for b in range(h + 1)]) for a in range(h)])
        add_T = np.stack([np.stack([ndroll(dp[a, b], vneg)
                                    for b in range(h)]) for a in range(h + 1)])
        dp[1:, :] += add_S
        dp[:, 1:] += add_T
    dp_ordered = int(dp[(h, h) + (0,) * w])
    # toral (coset-pair) ordered count, direct enumeration (cosets are few)
    toral_ordered = 0
    if n % h == 0:
        step = n // h
        cosets = [tuple(range(r, n, step)) for r in range(step)]
        for L, R_ in itertools.permutations(cosets, 2):
            sL, lL = elementary_signature(L)
            sR, lR = elementary_signature(R_)
            if sL == sR and lL != lR and not set(L) & set(R_):
                toral_ordered += 1
    ident_ok = (dp_ordered == 2 * unordered) and (toral_ordered == 2 * toral)
    return {"n": n, "h": h, "p": p, "census_unordered": unordered,
            "census_toral": toral, "census_nontoral": nontoral,
            "dp_ordered": dp_ordered, "toral_ordered": toral_ordered,
            "IDENTIFICATION_OK": ident_ok}


@app.local_entrypoint()
def main():
    out = list(check.map(ROWS, return_exceptions=True))
    print(f"{'(n,h,p)':>12} {'census unord/toral':>19} {'DP ordered':>11} {'2x check':>9}")
    for r in out:
        if not isinstance(r, dict):
            print("worker error:", str(r)[:130]); continue
        print(f"  ({r['n']},{r['h']},{r['p']})".rjust(12) +
              f" {r['census_unordered']:>10}/{r['census_toral']:<7} {r['dp_ordered']:>11} "
              f"{'OK' if r['IDENTIFICATION_OK'] else 'MISMATCH':>9}")
    with open("/tmp/f3_ident.json", "w") as f:
        json.dump([r for r in out if isinstance(r, dict)], f, indent=1)
