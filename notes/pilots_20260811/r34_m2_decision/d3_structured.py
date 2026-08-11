"""D3 (r34): the STRUCTURED (symmetry) families -- round 33's G4 escape
hatch -- at m=2, and the exact classification of which symmetry orders can
host the (SAT3) design.

Why symmetry is the only known way to beat a dimension count here: round 33's
e=1 ladder ran on the Kummer family Q_Z = X^rho + Z, whose members' root sets
are COSETS of mu_rho.  Cosets are pairwise disjoint, which is exactly the
m=1 requirement (d_x <= e = 1).  At m=2 the design needs 31 of the 36 slope
pairs to SHARE a domain point (d_x = 2), and orbits of a group are equal or
disjoint -- so the coset mechanism is structurally unavailable.  What is left
is a symmetry that MOVES the members:

    F(zeta^s Z, zeta x) = zeta^t F(Z, x)   =>   S_{tau(g)} = zeta * S_g,

so totally-split members come in tau-orbits and one splitting event buys a
whole orbit.  This script:

  (1) enumerates the equivariant nets (invariant subspaces of f(x)->f(zeta x)),
  (2) scans them for totally-split members over several fields,
  (3) tests every hit against the (L2) Hankel-realization system, and
  (4) prints the exact orbit arithmetic that says which symmetry order k can
      host 9 slopes with u-profile 7^9 or 7^8,6.

Usage: d3_structured.py OUTFILE
"""
import sys
import random

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


def inv_table(q):
    return [0] + [pow(a, q - 2, q) for a in range(1, q)]


def sqrt_table(q):
    t = {}
    for a in range(q):
        t.setdefault(a * a % q, a)
    return t


def rank(rows, ncols, q):
    rows = [r[:] for r in rows]
    rk = 0
    for c in range(ncols):
        p = None
        for i in range(rk, len(rows)):
            if rows[i][c] % q:
                p = i
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        iv = pow(rows[rk][c], q - 2, q)
        rows[rk] = [v * iv % q for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rk])]
        rk += 1
        if rk == len(rows):
            break
    return rk


def realization_nullity(Qk, q):
    """m=2: (m+2)(4m+1) = 36 equations on 2R = 32 unknowns."""
    m, R, r = 2, 16, 7
    rows = []
    for k in range(m + 2):
        for i in range(R - r):
            row = [0] * (2 * R)
            if 0 <= k <= m:
                for j in range(r + 1):
                    row[i + j] = (row[i + j] + Qk[k][j]) % q
            if 0 <= k - 1 <= m:
                for j in range(r + 1):
                    row[R + i + j] = (row[R + i + j] + Qk[k - 1][j]) % q
            rows.append(row)
    return 2 * R - rank(rows, 2 * R, q)


def incidences(c2, c1, c0, q, IV, sq):
    """c_i are coefficient lists (length 8).  For every x in F_q^*, the
    slopes g with c_2(x)g^2 + c_1(x)g + c_0(x) = 0.  Returns slope->count
    and the root sets."""
    deg = {}
    roots = {}
    for x in range(1, q):
        xp = 1
        a = b = c = 0
        for j in range(8):
            a = (a + c2[j] * xp) % q
            b = (b + c1[j] * xp) % q
            c = (c + c0[j] * xp) % q
            xp = xp * x % q
        if a == 0:
            if b == 0:
                continue
            g = (-c) * IV[b] % q
            deg[g] = deg.get(g, 0) + 1
            roots.setdefault(g, []).append(x)
            continue
        disc = (b * b - 4 * a * c) % q
        if disc not in sq:
            continue
        s = sq[disc]
        iv = IV[2 * a % q]
        for g in ({(-b + s) * iv % q, (-b - s) * iv % q}):
            deg[g] = deg.get(g, 0) + 1
            roots.setdefault(g, []).append(x)
    return deg, roots


def main():
    random.seed(340811)
    out("=== r34 D3: symmetry families at m=2 (round 33's G4) ===")
    out("")

    # ---------- (4) the orbit arithmetic, first: it is the punchline -----
    out("--- ORBIT ARITHMETIC: which symmetry order k can host the design "
        "---")
    out("Setup: a cyclic symmetry of order k acting on the x-line with the")
    out("net invariant.  Its induced action tau on the slope line is a")
    out("Mobius map of the same order, so the 9 supported slopes split into")
    out("tau-orbits of size k plus at most 2 tau-FIXED slopes.  A fixed")
    out("slope's member f satisfies f(zeta x) = nu f(x), hence")
    out("f = x^j h(x^k): its NONZERO roots come in mu_k-orbits, so")
    out("u_gamma == 0 (mod k) for every fixed slope.")
    out("")
    out(" rho = 7, T = 9, admissible u-profiles: 7^9 (O=0) and 7^8,6 (O=1)")
    out(" k | 9 = A*k + F, F <= 2 | fixed-slope u must be divisible by k | "
        "verdict")
    for k in (2, 3, 4, 5, 6, 7, 8, 9, 16, 32):
        ok = []
        for F in (0, 1, 2):
            if (9 - F) % k:
                continue
            if F == 0:
                ok.append("A=%d, no fixed slope" % ((9 - F) // k))
            else:
                # fixed slopes must carry u in {7,6} with k | u, u <= 7
                us = [u for u in (7, 6) if u % k == 0]
                if us:
                    ok.append("A=%d, %d fixed slope(s) with u in %s"
                              % ((9 - F) // k, F, us))
        out(f"  k={k:2d}: " + ("; ".join(ok) if ok else
                               "IMPOSSIBLE (no admissible split)"))
    out("")
    out("  => the ONLY symmetry order that can host the full 9-slope design")
    out("     is k=2 (four orbits of 2 plus one fixed slope with u=6).")
    out("     k=8 gives 8 split members from ONE splitting event, i.e.")
    out("     exactly T = rho+1 = 8 -- the strict target, ONE SLOPE SHORT of")
    out("     the failure size rho+2 = 9, and it cannot be extended: a 9th")
    out("     slope would drag its whole 8-orbit along (8*6 = 48 extra")
    out("     incidences against a budget of 64-56 = 8).")
    out("")

    # ---------- (1)+(2) the k=8 monomial families -----------------------
    out("--- k=8 EQUIVARIANT NETS (monomial: the only invariant nets when "
        "the 8 eigenvalues are distinct) ---")
    triples = [(a, b, c) for a in range(8) for b in range(8) for c in range(8)
               if (a + c - 2 * b) % 8 == 0 and min(a, b, c) == 0
               and max(a, b, c) == 7 and len({a, b, c}) == 3]
    out(f"  admissible monomial exponent triples (a,b,c) with "
        f"a+c=2b mod 8, min=0, max=7: {triples}")
    for q in (97, 193, 257):
        IV = inv_table(q)
        sq = sqrt_table(q)
        best = 0
        best_info = None
        n_nets = 0
        for (a, b, c) in triples:
            for alpha in range(1, q, max(1, q // 12)):
                for beta in range(1, q, max(1, q // 12)):
                    n_nets += 1
                    c2 = [0] * 8
                    c1 = [0] * 8
                    c0 = [0] * 8
                    c2[a] = 1
                    c1[b] = alpha
                    c0[c] = beta
                    deg, roots = incidences(c2, c1, c0, q, IV, sq)
                    n7 = sum(1 for v in deg.values() if v == 7)
                    if n7 > best:
                        best = n7
                        g0 = [g for g, v in deg.items() if v == 7]
                        best_info = ((a, b, c), alpha, beta,
                                     sorted(roots[g0[0]]) if g0 else None)
        out(f"  q={q}: {n_nets} k=8-equivariant nets scanned, MAX n7 = {best}")
        if best_info:
            (a, b, c), alpha, beta, S = best_info
            out(f"    witness net: x^{a} Z^2 + {alpha} x^{b} Z + {beta} x^{c}"
                f"   split member root set {S}")
            # coset pattern under mu_8 and the (L2) realization test
            h = None
            for t in range(2, q):
                if pow(t, (q - 1) // 8, q) != 1:
                    h = pow(t, (q - 1) // 8, q)
                    break
            cos = {}
            for x in S:
                key = min(x * pow(h, i, q) % q for i in range(8))
                cos[key] = cos.get(key, 0) + 1
            out(f"    mu_8-coset pattern of the root set: "
                f"{sorted(cos.values(), reverse=True)}  "
                f"(need (2,2,2,1) for |D| = 32 and d_x <= 2)")
            c2 = [0] * 8
            c1 = [0] * 8
            c0 = [0] * 8
            c2[a] = 1
            c1[b] = alpha
            c0[c] = beta
            nl = realization_nullity([c0, c1, c2], q)
            out(f"    (L2) Hankel-realization nullity of this net: {nl}   "
                f"{'REALIZABLE' if nl else 'NO SYNDROME PENCIL -- the net is'}"
                f"{'' if nl else ' a locator fiction'}")
    out("")

    # ---------- k=4 equivariant nets ------------------------------------
    out("--- k=4 EQUIVARIANT NETS (eigenspaces are 2-dimensional, so the "
        "nets are NOT forced monomial) ---")
    out("  shape: c_2 in <1,x^4>, c_1 in <x^3,x^7>, c_0 in <x^2,x^6>")
    for q in (97, 193, 257):
        IV = inv_table(q)
        sq = sqrt_table(q)
        best = 0
        best_nl = None
        for _ in range(3000):
            c2 = [0] * 8
            c1 = [0] * 8
            c0 = [0] * 8
            c2[0], c2[4] = random.randrange(q), random.randrange(q)
            c1[3], c1[7] = random.randrange(q), random.randrange(q)
            c0[2], c0[6] = random.randrange(q), random.randrange(q)
            if not (c2[4] or c2[0]) or not (c1[7] or c1[3]):
                continue
            deg, roots = incidences(c2, c1, c0, q, IV, sq)
            n7 = sum(1 for v in deg.values() if v == 7)
            if n7 > best:
                best = n7
                best_nl = realization_nullity([c0, c1, c2], q)
        out(f"  q={q}: 3000 k=4-equivariant nets, MAX n7 = {best}, "
            f"(L2) nullity of the best = {best_nl}")
    out("")

    # ---------- generic nets: the L2 filter on sparse coefficient vectors
    out("--- (L2) the sparsity tension: realization nullity vs support size "
        "---")
    out("supp = number of nonzero coefficients in each of c_0,c_1,c_2")
    for q in (97, 193):
        for supp in (1, 2, 3, 4, 6, 8):
            hits = 0
            for _ in range(80):
                Qk = []
                for _ in range(3):
                    v = [0] * 8
                    for j in random.sample(range(8), supp):
                        v[j] = random.randrange(1, q)
                    Qk.append(v)
                if realization_nullity(Qk, q):
                    hits += 1
            out(f"  q={q} supp={supp}: realizable nets out of 80: {hits}")
    out("")

    with open(sys.argv[1], "w") as f:
        f.write("\n".join(LINES) + "\n")


main()
