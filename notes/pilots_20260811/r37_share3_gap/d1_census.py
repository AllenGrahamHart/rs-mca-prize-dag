"""D1 -- THE FULL CONSTANT-NORM CENSUS (round 37).

Derived reductions used here (registered as R4.1/R4.3 in PREREG.md):

(1) FIELD WINDOW.  mu_64 <= F_q^* forces q = 1 mod 64.  In 97 <= q <= 690
    the admissible PRIME fields are exactly {193,257,449,577,641}; no
    prime power helps (31^2 = 961 > 690).  So the window is FIVE fields,
    not a dense one.

(2) THE FULL CONSTANT-NORM FAMILY IS ONE mu_64-ORBIT.  A constant-norm
    pencil is a line C1 + s*Delta with Delta having ZERO CONSTANT TERM,
    i.e. Delta = X(d1 X + d2); every member then has the same e3 (root
    product).  Scaling x -> u x (u in mu_64) maps mu_64 to itself and
    sends e3 -> u^3 e3; gcd(3,64)=1 so u -> u^3 is a BIJECTION of mu_64
    and the action is TRANSITIVE on the 64 values of e3.  Hence the full
    family is exhaustively enumerable from the SINGLE slice e3 = 1,
    which holds exactly 41664/64 = 651 split cubics.  This makes the
    FULL family (not a sub-family) exhaustive at every field.

(3) DISJOINTNESS IS ALMOST FREE.  Two distinct members C, C + s*Delta of
    a constant-norm line share a root r iff s*r(d1 r + d2) = 0 with
    r in mu_64, i.e. r = r0 := -d2/d1 (0 is not in mu_64).  So a
    constant-norm pencil has AT MOST ONE repeated root value r0 over the
    whole line, and the maximum pairwise-disjoint sub-family is
    (#members avoiding r0) + (1 if any member contains r0).

Writes d1_census_results.txt (versioned per run via argv tag) and
appends to d1_census_ckpt.txt.  Stdlib only.  No imports of banked code.
"""
import sys
import time

DIR = "notes/pilots_20260811/r37_share3_gap/"
TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
FIELDS = [193, 257, 449, 577, 641]
if len(sys.argv) > 2:
    FIELDS = [int(x) for x in sys.argv[2].split(",")]

OUT = []
T0 = time.time()


def p(s=""):
    OUT.append(str(s))


def flush():
    # versioned per run: never a blind "w" that a rerun of a DIFFERENT
    # run erases (the round-36 loss).
    with open(DIR + "d1_census_results_%s.txt" % TAG, "w") as f:
        f.write("\n".join(OUT) + "\n")


def mu(q, n):
    """the n-th roots of unity in F_q as a sorted list; requires n | q-1."""
    assert (q - 1) % n == 0
    for g in range(2, q):
        h = pow(g, (q - 1) // n, q)
        seen = set()
        x = 1
        for _ in range(n):
            seen.add(x)
            x = x * h % q
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError("no generator")


def census(q):
    """Exhaustive census of the FULL constant-norm family at q."""
    D = mu(q, 64)
    pos = {x: i for i, x in enumerate(D)}
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)

    # --- the e3 = 1 slice: every 3-subset of mu_64 with product 1 ---
    pts = []          # (e1, e2, (i,j,k) indices into D)
    for ii in range(64):
        a = D[ii]
        for jj in range(ii + 1, 64):
            b = D[jj]
            ab = a * b % q
            c = inv[ab]
            kk = pos[c]
            if kk <= jj:
                continue                     # canonical ii<jj<kk
            e1 = (a + b + c) % q
            e2 = (ab + c * (a + b)) % q
            pts.append((e1, e2, (ii, jj, kk)))
    n = len(pts)

    # --- every line in the (e1,e2) plane through >= 2 of the points ---
    lines = {}
    for s in range(n):
        x1, y1, _ = pts[s]
        for t in range(s + 1, n):
            x2, y2, _ = pts[t]
            A = (y1 - y2) % q
            B = (x2 - x1) % q
            if A:
                v = inv[A]
                A2, B2 = 1, B * v % q
            else:
                A2, B2 = 0, 1
                v = inv[B]
            C2 = (-(A2 * x1 + B2 * y1)) % q
            key = (A2, B2, C2)
            e = lines.get(key)
            if e is None:
                lines[key] = {s, t}
            else:
                e.add(s)
                e.add(t)

    hist = {}
    best = 0
    best_key = None
    for key, mem in lines.items():
        k = len(mem)
        hist[k] = hist.get(k, 0) + 1
        if k > best:
            best, best_key = k, key
    # points on NO line with another point are singletons; count them
    on = set()
    for mem in lines.values():
        on |= mem
    hist[1] = hist.get(1, 0) + (n - len(on))

    # --- disjointness (reduction 3) on the large lines ---
    disj = {}
    bigs = []
    for key, mem in lines.items():
        if len(mem) < 6:
            continue
        mem = sorted(mem)
        cnt = {}
        for s in mem:
            for r in pts[s][2]:
                cnt[r] = cnt.get(r, 0) + 1
        rep = [r for r, c in cnt.items() if c > 1]
        assert len(rep) <= 1, (q, key, rep)     # reduction (3), CHECKED
        if rep:
            k = sum(1 for s in mem if rep[0] not in pts[s][2]) + 1
        else:
            k = len(mem)
        disj[k] = disj.get(k, 0) + 1
        if k >= 8:
            bigs.append((k, key, mem, rep))
    return D, pts, n, hist, best, disj, bigs, inv


p("=== D1  FULL CONSTANT-NORM CENSUS, EXHAUSTIVE, round 37 ===")
p("R4.1 : q = 1 mod 64 admits EXACTLY {193,257,449,577,641} in [97,690].")
p("R4.3 : the full family is ONE mu_64-orbit; the e3=1 slice (651 cubics)")
p("       is exhaustive for the WHOLE family, counts x64 by transitivity.")
p("reduction (3): a constant-norm line has AT MOST ONE repeated root r0.")
p()
flush()

for q in FIELDS:
    t1 = time.time()
    D, pts, n, hist, best, disj, bigs, inv = census(q)
    dt = time.time() - t1
    p("--- q = %d   (e3=1 slice: %d split cubics; predicted 651)" % (q, n))
    p("    wall %.1f s" % dt)
    p("    LINE-SIZE HISTOGRAM (exhaustive over ALL lines in the slice):")
    p("      %s" % {k: hist[k] for k in sorted(hist)})
    p("    MAX collinear split cubics (raw)          = %d   (need 8)" % best)
    p("    MAX-DISJOINT histogram on lines of size>=6: %s"
      % {k: disj[k] for k in sorted(disj)})
    md = max(disj) if disj else 0
    p("    MAX DISJOINT COMPLETE FIBRES              = %d   (need 8)" % md)
    p("    number of >=8-fibre constant-norm pencils in the slice = %d"
      % len(bigs))
    p("    ... over the whole family (x64 orbit)                  = %d"
      % (64 * len(bigs)))
    if bigs:
        bigs.sort(reverse=True)
        k, key, mem, rep = bigs[0]
        p("    BEST PENCIL  line key (A,B,C) with A*e1+B*e2+C=0 : %s" % (key,))
        p("      members (indices into mu_64, e3=1):")
        for s in mem:
            p("        %s" % (pts[s][2],))
        p("      repeated root value r0 : %s" % (rep,))
        # fibre parameters t_i = w(x) = line parameter s_T
        # Delta direction: (de1, de2) along the line; C_T = C1 + s*Delta
        x1, y1, _ = pts[mem[0]]
        # direction vector of the line A*e1+B*e2+C=0 is (-B, A)
        A2, B2, C2 = key
        de1, de2 = (-B2) % q, A2 % q
        params = []
        for s in mem:
            x, y, _ = pts[s]
            if de1:
                sv = (x - x1) * inv[de1] % q if de1 else 0
            else:
                sv = (y - y1) * inv[de2] % q
            params.append(sv)
        p("      fibre parameters t_i (line coordinate) : %s" % (params,))
    p()
    flush()
    with open(DIR + "d1_census_ckpt.txt", "a") as f:
        f.write("tag=%s q=%d n=%d maxline=%d maxdisj=%d big=%d wall=%.1f\n"
                % (TAG, q, n, best, max(disj) if disj else 0, len(bigs), dt))

p("total wall %.1f s" % (time.time() - T0))
flush()
print("\n".join(OUT))
