"""D1 (r35_rout_layer_a) -- IS Rout BOUNDED?  The scaled Rout census.

Machinery: notes/pilots_20260811/rh_psi_degree/d3_psi.py lines 1-497, copied
into this directory as d3_psi_bank1.py BEFORE use and exec'd here without a
single edit (the driver below the '# ROUND-33 DRIVER' marker is NOT exec'd;
this file replaces it).  Every h_gamma quantity below is computed by the same
formulas as bank 1's driver (d3_tail.py:125-136), re-typed here so that the
identity checks (JDEC)/(DEGSUM)/(Rin = n+X-ov) act as a positive control on my
re-implementation.

NEW HERE (the mandate's D1):
  * the FULL Rout histogram, not just its max, per (where, a) cell;
  * the running max of Rout against sample size  (the sample-artifact test);
  * a NULL MODEL run in the same loop: for each measured slope, one uniformly
    random polynomial of the SAME cofactor degree Dg = Dh - Rin_m, whose
    F_q-roots outside W are counted the same way.  If Rout is 'free', the two
    histograms agree.
  * violation counters for  ROUTB : Rout <= d-m
                            NSA   : Rin_m + Rout <= d-m      [(NS-m)]
                            NSW   : Rin_m <= d-m             [(NS-W-m)]
                            CLO   : (d-Dh)+(n-ov)+Rout+nonsplit >= m  [closure]
    each restricted to the cells where the hypothesis d >= m holds.

usage:  d1_rout.py m q seconds a1,a2,...
"""

import random
import sys
import time

SRC = "notes/pilots_20260811/r35_rout_layer_a/d3_psi_bank1.py"
MARK = "# ROUND-33 DRIVER"

M = int(sys.argv[1])
QQ = int(sys.argv[2])
BUDGET = float(sys.argv[3])
ALIST = [int(t) for t in sys.argv[4].split(",")]

src = open(SRC).read()
head = src.split(MARK)[0]
sys.argv = ["machinery", str(M), str(QQ), "60", "20"]
exec(compile(head, SRC + " [lines 1..497]", "exec"))          # noqa

m, q = M, QQ
FOURM2 = 4 * m + 2
Dset = set(D)                                                  # noqa: F821
T0 = time.time()

OUTL = []


def P(s=""):
    OUTL.append(s)


def poly_eval(c, x):
    r = 0
    for v in reversed(c):
        r = (r * x + v) % q
    return r


def interp_coeffs(nodes, vals):
    n = len(nodes)
    dd = vals[:]
    for k in range(1, n):
        for i in range(n - 1, k - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * inv(nodes[i] - nodes[i - k]) % q   # noqa
    coeffs = [0] * n
    basis = [1] + [0] * (n - 1)
    deg = 0
    for i in range(n):
        if dd[i]:
            for t in range(deg + 1):
                coeffs[t] = (coeffs[t] + dd[i] * basis[t]) % q
        if i < n - 1:
            new = [0] * n
            for t in range(deg + 1):
                new[t + 1] = (new[t + 1] + basis[t]) % q
                new[t] = (new[t] - basis[t] * nodes[i]) % q
            basis = new
            deg += 1
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def divide_out(c, r):
    n = len(c)
    b = [0] * (n - 1)
    b[n - 2] = c[n - 1]
    for i in range(n - 2, 0, -1):
        b[i - 1] = (c[i] + r * b[i]) % q
    return b


def split_roots(c):
    mult = {}
    cur = c[:]
    for x in range(q):
        while len(cur) > 1 and poly_eval(cur, x) == 0:
            cur = divide_out(cur, x)
            mult[x] = mult.get(x, 0) + 1
    return mult, len(cur) - 1


ST = {}          # (where,a) -> dict of counters
GLOB = dict(slopes=0, rin_ok=0, rin_bad=0, jdec_ok=0, jdec_bad=0,
            degsum_ok=0, degsum_bad=0, simple_ok=0, simple_bad=0,
            clo_ok=0, clo_bad=0, growth=[], maxrout=0, nullhist={},
            routhist={}, routD=0, routtot=0, nullD=0, nulltot=0)


def cell(where, a):
    return ST.setdefault((where, a), dict(
        n=0, rout=[0] * 40, maxrout=0, maxnull=0, null=[0] * 40,
        routb_bad=0, nsa_bad=0, nsw_bad=0, clo_bad=0, sumrout=0,
        sumnull=0, sumns=0, sumX=0, maxX=0, dh_eq_d=0))


def measure(where, Wsorted, recs):
    Wset = set(Wsorted)
    a = len(Wsorted)
    dcap = a - FOURM2
    if dcap < 0:
        return
    C = cell(where, a)
    sp = {x: sigma_prime(Wsorted, x) for x in Wsorted}          # noqa
    for rc in recs:
        if rc["typ"] != 2:
            continue
        S, z, v = rc["S"], rc["z"], rc["v"]
        X = len(S & Wset)
        o = rho - len(S)                                        # noqa
        n = a - len(z)
        ov = sum(1 for x in Wsorted if x in S and x not in z)
        cancel = sum(1 for x in Wsorted if x in S and x in z
                     and z[x] == v.get(x, 0))
        j = rc["j"]
        hv = []
        for x in Wsorted:
            Qx = 1
            for s in S:
                Qx = Qx * (x - s) % q
            hv.append(z.get(x, 0) * Qx % q * sp[x] % q)
        Dh = newton_degree(Wsorted, hv)                          # noqa
        Rin = sum(1 for t in hv if t == 0)
        coeffs = interp_coeffs(Wsorted, hv)
        mult, nonsplit = split_roots(coeffs)
        Rin_m = sum(k for x, k in mult.items() if x in Wset)
        Rout = sum(k for x, k in mult.items() if x not in Wset)
        RoutD = sum(k for x, k in mult.items() if x not in Wset and x in Dset)
        # ---- controls (bank 1's identities; a failure kills my re-impl)
        GLOB["slopes"] += 1
        GLOB["rin_ok" if Rin == n + X - ov else "rin_bad"] += 1
        GLOB["jdec_ok" if dcap - Rin == o + j + cancel else "jdec_bad"] += 1
        GLOB["degsum_ok" if Dh == Rin_m + Rout + nonsplit
             else "degsum_bad"] += 1
        GLOB["simple_ok" if Rin_m == Rin else "simple_bad"] += 1
        # ---- the exact closure criterion (rearrangement of the two above)
        clo = (dcap - Dh) + (n - ov) + Rout + nonsplit >= m
        GLOB["clo_ok" if clo == (X <= dcap - m) else "clo_bad"] += 1
        # ---- NULL: a uniform poly of the same cofactor degree
        Dg = Dh - Rin_m
        if Dg > 0:
            rc2 = [random.randrange(q) for _ in range(Dg)] + [
                random.randrange(1, q)]
            mult2, _ = split_roots(rc2)
            Rnull = sum(k for x, k in mult2.items() if x not in Wset)
            RnullD = sum(k for x, k in mult2.items()
                         if x not in Wset and x in Dset)
        else:
            Rnull, RnullD = 0, 0
        # ---- record
        C["n"] += 1
        C["rout"][min(Rout, 39)] += 1
        C["null"][min(Rnull, 39)] += 1
        C["sumrout"] += Rout
        C["sumnull"] += Rnull
        C["sumns"] += nonsplit
        C["sumX"] += X
        C["maxX"] = max(C["maxX"], X)
        C["maxrout"] = max(C["maxrout"], Rout)
        C["maxnull"] = max(C["maxnull"], Rnull)
        C["dh_eq_d"] += (Dh == dcap)
        GLOB["routhist"][Rout] = GLOB["routhist"].get(Rout, 0) + 1
        GLOB["nullhist"][Rnull] = GLOB["nullhist"].get(Rnull, 0) + 1
        GLOB["routD"] += RoutD
        GLOB["routtot"] += Rout
        GLOB["nullD"] += RnullD
        GLOB["nulltot"] += Rnull
        if Rout > GLOB["maxrout"]:
            GLOB["maxrout"] = Rout
            GLOB["growth"].append((GLOB["slopes"], Rout, a, where, dcap))
        if Rout > dcap - m:
            C["routb_bad"] += 1
        if Rin_m + Rout > dcap - m:
            C["nsa_bad"] += 1
        if Rin_m > dcap - m:
            C["nsw_bad"] += 1
        if not clo:
            C["clo_bad"] += 1


random.seed(20260811 + m * 1000 + q)
P("=" * 78)
P("D1 (r35) SCALED Rout CENSUS   m=%d q=%d rho=%d N=%d  budget=%.0fs"
  % (m, q, rho, N, BUDGET))                                     # noqa
P("  a values planted: %s ;  a* = 7m-1 = %d ; 2rho = %d ; 4m+2 = %d"
  % (ALIST, 7 * m - 1, 2 * rho, FOURM2))                        # noqa
P("  d = a-(4m+2) ; the ledger needs X <= d-m ; (NS-m) needs Rin_m+Rout <= d-m")
P("=" * 78)

pencils = 0
rounds = 0
while time.time() - T0 < BUDGET:
    rounds += 1
    for a in ALIST:
        if time.time() - T0 > BUDGET:
            break
        lo = max(1, R1 - a)                                     # noqa
        for p in range(lo, rho + 1):                            # noqa
            if time.time() - T0 > BUDGET:
                break
            b = build_modeB(a, p)                               # noqa
            if b is None:
                continue
            W0, recs0 = analyse(b[0], b[1])                     # noqa
            if len(W0) != a:
                continue
            pencils += 1
            measure("planted", W0, recs0)
            out = canonical_pass(recs0)                         # noqa
            if out is not None:
                astar, Wc, recsc, vg, vh = out
                measure("canon", Wc, recsc)

P("")
P("  pencils built = %d   (sweeps over the a-list: %d)" % (pencils, rounds))
P("")
P("--- CONTROLS (bank 1's identities on MY re-implementation) ---")
P("  type-2 slopes measured         : %d" % GLOB["slopes"])
P("  Rin = n + X - ov               : OK %d  BAD %d"
  % (GLOB["rin_ok"], GLOB["rin_bad"]))
P("  (JDEC) d - Rin = o + j + cancel: OK %d  BAD %d"
  % (GLOB["jdec_ok"], GLOB["jdec_bad"]))
P("  (DEGSUM) Dh = Rin_m+Rout+nonsp : OK %d  BAD %d"
  % (GLOB["degsum_ok"], GLOB["degsum_bad"]))
P("  every W-root of h simple       : OK %d  BAD %d"
  % (GLOB["simple_ok"], GLOB["simple_bad"]))
P("  (CLO) <=> closure X <= d-m     : OK %d  BAD %d"
  % (GLOB["clo_ok"], GLOB["clo_bad"]))
P("")
P("--- PER-CELL  (violations counted only where the stated bound bites) ---")
P("  where     a   d  d-m  slopes  meanRout maxRout | meanNULL maxNULL |"
  " Rout>d-m  NSA_bad  NSW_bad  maxX")
for key in sorted(ST):
    C = ST[key]
    a = key[1]
    dcap = a - FOURM2
    if C["n"] == 0:
        continue
    P("  %-8s %3d %3d %4d %7d %9.3f %7d | %8.3f %7d | %8d %8d %8d %5d"
      % (key[0], a, dcap, dcap - m, C["n"], C["sumrout"] / C["n"],
         C["maxrout"], C["sumnull"] / C["n"], C["maxnull"],
         C["routb_bad"], C["nsa_bad"], C["nsw_bad"], C["maxX"]))
P("")
P("--- Rout HISTOGRAM  vs  THE NULL (uniform poly of the same cofactor deg) ---")
ks = sorted(set(GLOB["routhist"]) | set(GLOB["nullhist"]))
P("  Rout value :  %s" % "  ".join("%5d" % k for k in ks))
P("  measured   :  %s" % "  ".join("%5d" % GLOB["routhist"].get(k, 0)
                                   for k in ks))
P("  null model :  %s" % "  ".join("%5d" % GLOB["nullhist"].get(k, 0)
                                   for k in ks))
tot = sum(GLOB["routhist"].values())
mn = sum(k * v for k, v in GLOB["routhist"].items()) / max(tot, 1)
mnn = sum(k * v for k, v in GLOB["nullhist"].items()) / max(tot, 1)
P("  mean measured = %.4f ; mean null = %.4f ; slopes = %d" % (mn, mnn, tot))
P("  roots that land in D\\W : measured %d/%d ; null %d/%d ; (N-a)/(q-a) ~ %.3f"
  % (GLOB["routD"], GLOB["routtot"], GLOB["nullD"], GLOB["nulltot"],
     (N - ALIST[0]) / float(q - ALIST[0])))                     # noqa
P("")
P("--- GROWTH OF max Rout WITH SAMPLE SIZE (the sample-artifact test) ---")
P("  new record at slope #, value, a, where, d")
for g in GLOB["growth"]:
    P("    %7d   Rout = %2d   a=%2d  %-8s d=%d" % g)
P("")
P("=== END d1_rout m=%d q=%d ===" % (m, q))

open("notes/pilots_20260811/r35_rout_layer_a/d1_rout_results_m%d_q%d.txt"
     % (m, q), "w").write("\n".join(OUTL) + "\n")
sys.stdout.write("\n".join(OUTL) + "\n")
