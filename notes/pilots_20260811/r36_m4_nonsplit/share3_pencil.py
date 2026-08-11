"""D1/D2: does a 3-sharing pencil exist on mu_64, and does it obey the
registered q^-12 threshold (R2.1/R2.2)?

INSTRUMENT (R1.6, derived before searching).  A k=3 sharing pattern is a
LINE in P^3 = P(binary cubics) meeting the 41664 monic cubics with all
three roots in mu_64.  All those cubics are monic, so the monic members
of a pencil form an AFFINE line in A^3 = {(c2,c1,c0)}.  For a fixed base
triple T1 we project every disjoint triple T to the direction
(C_T - C_T1) normalised in P^2; triples collinear with C_T1 land in the
same bucket.  The scan over a fixed T1 is EXHAUSTIVE over all lines
through C_T1 (R2.3) -- it is not a truncated search.

Writes share3_pencil_results.txt and share3_pencil_ckpt.txt in this
directory only.  Stdlib only.
"""
import random
import sys
import time
from math import comb

DIR = "notes/pilots_20260811/r36_m4_nonsplit/"
OUT = []
T0 = time.time()
DEADLINE = 250.0


def p(s=""):
    OUT.append(str(s))


def flush():
    with open(DIR + "share3_pencil_results.txt", "w") as f:
        f.write("\n".join(OUT) + "\n")


def mu(q, n):
    """the n-th roots of unity in F_q, as a list; requires n | q-1."""
    assert (q - 1) % n == 0
    for g in range(2, q):
        h = pow(g, (q - 1) // n, q)
        seen = set()
        x = 1
        for _ in range(n):
            seen.add(x)
            x = x * h % q
        if len(seen) == n:
            return sorted(seen), h
    raise RuntimeError("no generator")


def build(q, N=64):
    D, _ = mu(q, N)
    idx = list(range(N))
    trips = []
    c2s = []
    c1s = []
    c0s = []
    for i in range(N):
        a = D[i]
        for j in range(i + 1, N):
            b = D[j]
            ab = a * b % q
            apb = (a + b) % q
            for k in range(j + 1, N):
                c = D[k]
                # (X-a)(X-b)(X-c) = X^3 - e1 X^2 + e2 X - e3
                e1 = (apb + c) % q
                e2 = (ab + c * apb) % q
                e3 = ab * c % q
                trips.append((i, j, k))
                c2s.append((-e1) % q)
                c1s.append(e2)
                c0s.append((-e3) % q)
    return D, trips, c2s, c1s, c0s


def scan(q, D, trips, c2s, c1s, c0s, inv, base_idx):
    """Exhaustive over all lines through C_{trips[base_idx]}.
    Returns (best_bucket_size, best_key, members)."""
    i0, j0, k0 = trips[base_idx]
    b2, b1, b0 = c2s[base_idx], c1s[base_idx], c0s[base_idx]
    buckets = {}
    for t in range(len(trips)):
        i, j, k = trips[t]
        if i == i0 or i == j0 or i == k0:
            continue
        if j == i0 or j == j0 or j == k0:
            continue
        if k == i0 or k == j0 or k == k0:
            continue
        d2 = (c2s[t] - b2) % q
        d1 = (c1s[t] - b1) % q
        d0 = (c0s[t] - b0) % q
        if d2:
            v = inv[d2]
            key = (0, d1 * v % q, d0 * v % q)
        elif d1:
            v = inv[d1]
            key = (1, 0, d0 * v % q)
        elif d0:
            key = (2, 0, 0)
        else:
            continue
        e = buckets.get(key)
        if e is None:
            buckets[key] = [t]
        else:
            e.append(t)
    best = 0
    bk = None
    hist = {}
    for key, mem in buckets.items():
        n = len(mem)
        hist[n] = hist.get(n, 0) + 1
        if n > best:
            best, bk = n, key
    return best, bk, buckets, hist


def verify_pencil(q, D, trips, base_idx, members):
    """Independent second field-check: build w = -C1/Delta and histogram
    w on mu_64; a value of multiplicity exactly 3 is a complete fibre."""
    def coef(t):
        return (1, c2s[t], c1s[t], c0s[t])
    C1 = coef(base_idx)
    C2 = coef(members[0])
    d = tuple((C2[i] - C1[i]) % q for i in range(4))     # d[0] == 0
    vals = {}
    for x in D:
        cv = (((x + C1[1]) * x + C1[2]) * x + C1[3]) % q
        dv = ((d[1] * x + d[2]) * x + d[3]) % q
        if dv == 0:
            key = "inf" if cv else "base"
        else:
            key = (-cv * pow(dv, q - 2, q)) % q
        vals.setdefault(key, []).append(x)
    fibres = [v for v in vals.values() if len(v) == 3]
    return d, fibres, sorted(len(v) for v in vals.values())


# ---------------- predicted first moments (R2.1) ----------------
def predicted(q, j):
    """E[# of j-subsets of the 41664 split cubics collinear with a FIXED
    one] = N_j' * q^-2(j-1),  N_j' = prod_{i<j} C(61-3i,3) / j!."""
    n = 1
    for i in range(j):
        n *= comb(61 - 3 * i, 3)
    for i in range(2, j + 1):
        n //= i
    return n / float(q) ** (2 * (j - 1))


FIELDS = [(193, 400), (257, 400), (449, 800), (577, 800)]
if len(sys.argv) > 1:
    FIELDS = [f for f in FIELDS if str(f[0]) in sys.argv[1].split(",")]

p("=== D1/D2  3-SHARING PENCIL SEARCH ON mu_64  (R1.6 instrument) ===")
p("target: a line in P^3 carrying 8 disjoint mu_64-split cubics")
p("        = a degree-3 map w with 8 complete fibres inside mu_64")
p("registered prediction (R2.1): EXISTS at q=193,257 ; ABSENT at 449,577")
p()
p("PREDICTED E[# of j-subsets collinear with a FIXED base triple]:")
p("  q      j=2       j=3       j=4       j=5       j=6       j=7       j=8")
for q, _ in FIELDS:
    p("  %-5d %s" % (q, " ".join("%9.3g" % predicted(q, j)
                                 for j in range(2, 9))))
p()
flush()

WITNESS = None
for q, NBASE in FIELDS:
    if time.time() - T0 > DEADLINE:
        p("!! DEADLINE reached before q=%d -- ZERO DRAWS, NOT a measurement" % q)
        break
    t1 = time.time()
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    D, trips, c2s, c1s, c0s = build(q)
    random.seed(1000 + q)
    bases = random.sample(range(len(trips)), NBASE)
    agg = {}
    best_overall = 0
    best_rec = None
    done = 0
    for bi in bases:
        if time.time() - T0 > DEADLINE:
            break
        best, bk, buckets, hist = scan(q, D, trips, c2s, c1s, c0s, inv, bi)
        for n, c in hist.items():
            agg[n] = agg.get(n, 0) + c
        done += 1
        if best > best_overall:
            best_overall = best
            best_rec = (bi, bk, list(buckets[bk]))
    dt = time.time() - t1
    p("--- q = %d : |mu_64| = %d, |Sigma| = %d, base triples scanned = %d"
      % (q, len(D), len(trips), done))
    p("    (each scan EXHAUSTIVE over every line through its base triple)")
    p("    wall %.1f s" % dt)
    p("    MAX collinear split cubics found (incl. base) = %d   (need 8)"
      % (best_overall + 1))
    p("    observed bucket histogram, MEAN per base triple vs PREDICTED:")
    p("      j (=bucket+1)   observed mean    predicted E")
    for n in sorted(agg):
        if n >= 2:
            p("      %2d              %12.5g   %12.5g"
              % (n + 1, agg[n] / float(done), predicted(q, n)))
    tail = sum(c for n, c in agg.items() if n >= 7)
    p("    total >=8-point lines seen across the sample : %d of %d bases ;"
      " predicted per-base rate %.4g" % (tail, done, predicted(q, 7)))
    p("    VERDICT q=%d : %s"
      % (q, "3-SHARING PENCIL FOUND" if best_overall + 1 >= 8
         else "no 8-point line in this sample (ceiling %d)" % (best_overall + 1)))
    if best_rec and best_overall + 1 >= 8:
        bi, bk, mem = best_rec
        d, fibres, mult = verify_pencil(q, D, trips, bi, mem)
        p("    WITNESS PENCIL  base triple %s" % (trips[bi],))
        p("      C1 = X^3 + %d X^2 + %d X + %d" % (c2s[bi], c1s[bi], c0s[bi]))
        p("      Delta = %d X^2 + %d X + %d" % (d[1], d[2], d[3]))
        p("      collinear triples (indices into mu_64):")
        p("        %s" % (trips[bi],))
        for t in mem:
            p("        %s" % (trips[t],))
        p("      INDEPENDENT CHECK w = -C1/Delta on mu_64:")
        p("        complete (multiplicity-3) fibres = %d" % len(fibres))
        p("        fibre-size multiset = %s" % mult)
        allpts = set()
        ok = True
        for f in fibres:
            for x in f:
                if x in allpts:
                    ok = False
                allpts.add(x)
        p("        fibres pairwise disjoint : %s ; points covered %d of 64"
          % (ok, len(allpts)))
        if WITNESS is None and len(fibres) >= 8:
            WITNESS = (q, d, (c2s[bi], c1s[bi], c0s[bi]), fibres)
    p()
    flush()
    with open(DIR + "share3_pencil_ckpt.txt", "a") as f:
        f.write("q=%d bases=%d max=%d wall=%.1f\n"
                % (q, done, best_overall + 1, dt))

if WITNESS:
    q, d, c1, fibres = WITNESS
    p("=== WITNESS EXPORT (for the arithmetic layer) ===")
    p("q = %d" % q)
    p("C1 = %s" % (c1,))
    p("Delta = %s" % (d,))
    p("fibres = %s" % ([sorted(f) for f in fibres],))
p()
p("total wall %.1f s" % (time.time() - T0))
flush()
print("\n".join(OUT))
