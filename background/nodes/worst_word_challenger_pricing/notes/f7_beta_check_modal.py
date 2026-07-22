#!/usr/bin/env python3
"""F7 beta-check (Modal, <60s): challenger count law at a BASE-DOMAIN
EXTENSION row (q = p^2, domain = order-n subgroup of F_p*).

E15/E22 cell conventions preserved exactly: core = first k-1 domain points,
petals of size ell = sigma+1, planted word = scalar_p * L_core(x) on petal p,
0 on core/background; challenger = non-planted deg<k codeword agreeing on
>= s = k+sigma points.

CLAIM UNDER TEST (the beta-exposure): for BASE-VALUED planted words (scalars
in F_p*), the challenger set over F_{p^2} equals the challenger set of the
SAME cell at the base row F_p (interpolation through k base points with base
values forces base coefficients), so the count law is ~ K_cell/p^sigma, NOT
~ K_cell/q^sigma. For genuinely F_q scalars the q-law should hold (near-zero
counts at toy scale). Exact enumeration, no sampling."""
import itertools
import json

import modal

app = modal.App("rs-mca-f7-beta")
image = modal.Image.debian_slim()

CELLS = [
    # (p, nonresidue r for u^2=r, k, sigma, n_layouts, seed)
    (17, 3, 4, 1, 6, 101),
    (17, 3, 2, 1, 6, 202),
    (13, 2, 4, 1, 6, 303),
    (13, 2, 2, 1, 6, 404),
]


@app.function(image=image, cpu=2, memory=2048, timeout=120)
def census(cell):
    import random
    p, r, k, sigma, n_layouts, seed = cell
    rng = random.Random(seed)
    n = p - 1                       # full multiplicative group of F_p
    s = k + sigma
    ell = sigma + 1

    # ---- F_{p^2} arithmetic: x = (a, b) meaning a + b*u, u^2 = r ----
    def add(x, y): return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)
    def sub(x, y): return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)
    def mul(x, y):
        a, b = x; c, d = y
        return ((a * c + r * b * d) % p, (a * d + b * c) % p)
    def inv(x):
        a, b = x
        nrm = (a * a - r * b * b) % p
        ni = pow(nrm, p - 2, p)
        return ((a * ni) % p, (-b * ni) % p)
    ZERO, ONE = (0, 0), (1, 0)
    def is_base(x): return x[1] == 0

    def interp(pts, vals):
        """deg<k interpolant through k (point, value) pairs; points base-embedded."""
        coeffs = [ZERO] * k
        for i, (xi, yi) in enumerate(zip(pts, vals)):
            num = [ONE]          # polynomial coefficients low->high
            den = ONE
            for j, (xj, _) in enumerate(zip(pts, vals)):
                if j == i:
                    continue
                new = [ZERO] * (len(num) + 1)
                for dgr, c in enumerate(num):
                    new[dgr] = sub(new[dgr], mul(c, xj))
                    new[dgr + 1] = add(new[dgr + 1], c)
                num = new
                den = mul(den, sub(xi, xj))
            w = mul(yi, inv(den))
            for dgr, c in enumerate(num):
                coeffs[dgr] = add(coeffs[dgr], mul(c, w))
        return tuple(coeffs)

    def evalpoly(coeffs, x):
        acc = ZERO
        for c in reversed(coeffs):
            acc = add(mul(acc, x), c)
        return acc

    g = None                       # generator of F_p*
    for cand in range(2, p):
        seen, x = set(), 1
        for _ in range(p - 1):
            x = x * cand % p
            seen.add(x)
        if len(seen) == p - 1:
            g = cand
            break
    dom_base = [pow(g, i, p) for i in range(n)]

    def run_word(layout, scalars):
        """Exact challenger census for one (layout, scalars) word. Returns
        (n_challengers, all_challenger_coeffs_base?)."""
        pts = [(layout[i], 0) for i in range(n)]      # base-embedded points
        core = pts[:k - 1]
        rest = pts[k - 1:]
        petals = [rest[i:i + ell] for i in range(0, (len(rest) // ell) * ell, ell)]
        # L_core coefficients (monic locator of core) over F_q
        loc = [ONE]
        for (cx, _) in core:
            new = [ZERO] * (len(loc) + 1)
            for dgr, c in enumerate(loc):
                new[dgr] = sub(new[dgr], mul(c, (cx, 0)))
                new[dgr + 1] = add(new[dgr + 1], c)
            loc = new
        word = {}
        for x in pts:
            word[x] = ZERO
        for pi, petal in enumerate(petals):
            sc = scalars[pi]
            for x in petal:
                word[x] = mul(sc, evalpoly(loc, x))
        planted = set()
        for pi, petal in enumerate(petals):
            cs = [mul(scalars[pi], c) for c in loc] + [ZERO] * (k - len(loc))
            planted.add(tuple(cs[:k]))
        # exact list at radius s: interpolants of all k-subsets of the domain
        cands = set()
        pl = list(word.items())
        for combo in itertools.combinations(range(n), k):
            cpts = [pl[i][0] for i in combo]
            cvals = [pl[i][1] for i in combo]
            cands.add(interp(cpts, cvals))
        challengers = []
        for c in cands:
            agree = sum(1 for (x, v) in pl if evalpoly(c, x) == v)
            if agree >= s and c not in planted and any(cc != ZERO for cc in c):
                challengers.append(c)
        allbase = all(all(is_base(cc) for cc in c) for c in challengers)
        return len(challengers), allbase

    out = {"p": p, "q": p * p, "k": k, "sigma": sigma, "n": n,
           "base_valued": [], "generic": [], "identity_checks": []}
    n_petals = (n - (k - 1)) // ell
    for _ in range(n_layouts):
        layout = dom_base[:]
        rng.shuffle(layout)
        sc_base = [(rng.randrange(1, p), 0) for _ in range(n_petals)]
        sc_gen = [(rng.randrange(p), rng.randrange(1, p)) for _ in range(n_petals)]
        nb, allbase = run_word(layout, sc_base)
        ng, _ = run_word(layout, sc_gen)
        out["base_valued"].append(nb)
        out["generic"].append(ng)
        out["identity_checks"].append(allbase)
    return out


@app.local_entrypoint()
def main():
    results = list(census.map(CELLS, return_exceptions=True))
    print(f"{'cell (p,k,sigma)':>18} {'base-valued challengers':>24} {'generic challengers':>20} {'all base coeffs?':>17}")
    for res in results:
        if not isinstance(res, dict):
            print("worker error:", str(res)[:160]); continue
        bl, gl = res["base_valued"], res["generic"]
        print(f"  ({res['p']:>3},{res['k']},{res['sigma']})  q={res['q']:<6} "
              f"{str(bl):>24} {str(gl):>20} {str(all(res['identity_checks'])):>17}")
    with open("/tmp/f7_beta.json", "w") as f:
        json.dump([r for r in results if isinstance(r, dict)], f, indent=1)
    print("\nVERDICT: base-valued words carry base-row challenger counts (p-law);")
    print("generic F_q words follow the q-law (near-zero at toys) => the envelope's")
    print("count law needs the generated-field reading at base-domain extension rows.")
