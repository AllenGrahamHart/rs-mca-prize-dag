"""D3 (r35) -- THE MULTIPLICATIVE-DOMAIN PUSH, and the D2 quantifier addendum.

SUBTRACTION FIRST (CATCH-24A, run before writing any of this up):
  * the factor-degree dichotomy IS A PROVED NODE --
    background/nodes/rate_half_ca_hankel_endpoint_rational_branch_exclusion/
    statement.md:24-42  (CPR3) unique component with r=4e-1, (CPR4) every
    other component balanced r_i=4e_i, (CPR5) e_(i*)>=ceil((3m+1)/4) and
    sum_(i!=i*) e_i <= floor((m-1)/4), "cannot split into m rational moving
    root branches".
  * the norm identity IS A PROVED NODE --
    background/nodes/rate_half_ca_hankel_endpoint_norm_factorization/
    statement.md:36-45 (ENF2) J*R = H^rho*S, deg J = O, deg S = 1+O, with
    R(U,V) = prod_(x in D) Q(U,V;x); and statement.md:93-98 (ENF6) the
    two-sided weight identity.
  * gcd(4m-1,16m) = 1, hence coset/subgroup-structured supports are
    obstructed, IS A PROVED NODE --
    background/nodes/rate_half_type2_fr_quartic_coset_biform_lift_obstruction/
    proof.md:66-72 (9).
So [A] below is a VERIFICATION of banked results from a cheaper direction,
not a new statement.  The new object is the quantified gate in [C]: the
number of degree-rho divisors of x^N-1 is C(16m,4m-1), a q-INDEPENDENT count,
against an ambient q^rho.

 [A] profile rescan with the per-factor constraint (closed form + brute force
     control), against the banked (CPR3)-(CPR5)
 [B] the m=1 EXACT count of layer-A-consistent (Q,Gamma) over F_17
 [C] the first-moment count at m>=2, calibrated against [B]
 [D] D2 ADDENDUM: EVERY 16-subset of the m=3 witness's W, exhaustively
"""

import math
import sys
from itertools import combinations

HERE = "notes/pilots_20260811/r35_rout_layer_a"
sys.path.insert(0, HERE)
import biv_core                                                        # noqa
import m3_phi                                                          # noqa
sys.modules.setdefault("biv_core", biv_core)
sys.modules.setdefault("m3_phi", m3_phi)
from biv_core import PackedRank, poly_from_roots, mu_N                 # noqa

src = open(HERE + "/m3_build_bank34.py").read()
exec(compile(src.split("\nfor q in (97, 193):")[0],
             "m3_build_bank34.py [head]", "exec"))                     # noqa

OUTL = []


def P(s=""):
    print(s)
    OUTL.append(s)


P("=" * 78)
P("D3 [r35] -- MULTIPLICATIVE-DOMAIN PUSH  (see the subtraction in the header)")
P("=" * 78)

# --------------------------------------------------------------- [A]
P("")
P("[A] PROFILE RESCAN, per-factor form.  From the incidence side:")
P("      sum_j d_j = rho,  sum_j m_j = m,  and for EVERY irreducible factor")
P("      T*d_j - N*m_j <= Drop_j + Extra_j,  sum_j (Drop_j+Extra_j) = O <= m-1.")
P("    Writing d_j = 4m_j-1+s_j, the excess of factor j is")
P("      max(0, 4m_j - T + T*s_j) = 0 (s_j=0), 4m_j (s_j=1), 4m_j+T(s_j-1) ...")
P("    and sum_j s_j = rho - (4m - t) = t-1, so the CHEAPEST assignment puts")
P("    one unit on every factor except the largest:")
P("      minimal total excess = 4(m - max_j m_j)  <=  m-1.")
P("    i.e. exactly (CPR3)+(CPR4)+(CPR5): ONE factor with d = 4m_j - 1, all")
P("    others balanced d = 4m_j, and sum of the others' m_j <= floor((m-1)/4).")
P("")


def parts(n, cap=None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, cap), 0, -1):
        for rest in parts(n - k, k):
            yield (k,) + rest


def survives_closed(prof, m):
    return 4 * (m - max(prof)) <= m - 1


def _assign(left, t):
    if t == 1:
        yield (left,)
        return
    for k in range(left + 1):
        for rest in _assign(left - k, t - 1):
            yield (k,) + rest


def survives_brute(prof, m):
    """brute force over every d-assignment (control on the closed form)."""
    T, N, rho = 4 * m + 1, 16 * m, 4 * m - 1
    t = len(prof)
    for assign in _assign(rho - t, t):
        d = [1 + s for s in assign]
        if sum(max(0, T * dj - N * mj) for dj, mj in zip(d, prof)) <= m - 1:
            return True
    return False


def survives_anchor1(prof, m):
    """anchor 1's aggregate form (r34 REPORT.md:336-338)."""
    T, N, rho = 4 * m + 1, 16 * m, 4 * m - 1
    t = len(prof)
    best = -1
    for assign in _assign(rho - t, t):
        d = [1 + s for s in assign]
        best = max(best, sum(min(T * dj, N * mj)
                             for dj, mj in zip(d, prof)))
    return best >= T * rho - (m - 1)


P("       m  #profiles  survivors  brute-force agrees  anchor1 agrees  "
  "ceil((3m+1)/4)  min m_(i*)")
for m in (1, 2, 3, 4, 5, 6, 7, 8):
    pr = list(parts(m))
    sc = [p for p in pr if survives_closed(p, m)]
    sb = [p for p in pr if survives_brute(p, m)]
    sa = [p for p in pr if survives_anchor1(p, m)]
    P("    %4d %10d %10d %19s %15s %15d %11d"
      % (m, len(pr), len(sc), sc == sb, sc == sa, -(-(3 * m + 1) // 4),
         min(max(p) for p in sc)))
P("    survivors: %s"
  % {m: [p for p in parts(m) if survives_closed(p, m)] for m in (2, 3, 4, 5, 8)})
P("    large m (closed form only):")
for m in (16, 40):
    pr = list(parts(m))
    sc = [p for p in pr if survives_closed(p, m)]
    P("       m=%3d : %8d profiles, %5d survivors, min dominant m_(i*) = %d"
      " (banked ceil((3m+1)/4) = %d)"
      % (m, len(pr), len(sc), min(max(p) for p in sc), -(-(3 * m + 1) // 4)))
# closed-form survivor count: choosing the dominant part M = m-k leaves a
# partition of k <= floor((m-1)/4) whose parts are automatically <= M, so
#   #survivors(m) = sum_{k=0}^{floor((m-1)/4)} p(k).
PK = [1] + [0] * 400
for part in range(1, 401):
    for s in range(part, 401):
        PK[s] += PK[s - part]
P("    closed-form survivor count  sum_{k<=floor((m-1)/4)} p(k) :  %s"
  % {m: sum(PK[k] for k in range((m - 1) // 4 + 1))
     for m in (4, 8, 16, 40, 100, 1024)})
P("    (the enumerated counts above agree: 1,2,7,97 at m=4,8,16,40)")

# --------------------------------------------------------------- [B]
P("")
P("[B] m=1 EXACT COUNT of layer-A-consistent (Q, Gamma) over F_17.")
P("    Q(Z,x) = q_0(x) + Z q_1(x), deg_x <= rho = 3: the kernel family is a")
P("    LINE in P^3.  A slope is usable iff Q(gamma,.) is a squarefree cubic")
P("    SPLIT OVER D (RNC statement.md:48-50), i.e. one of the C(16,3) = 560")
P("    degree-3 divisors of x^16-1.  Need T = rho+2 = 5 of them with")
P("    d_x <= m = 1, i.e. PAIRWISE DISJOINT supports covering 15 of the 16.")
q = 17
Dl = sorted(mu_N(q, 16))
spec = {}
for S in combinations(Dl, 3):
    spec[tuple(poly_from_roots(list(S), q))] = frozenset(S)
pts = list(spec)
lines = {}
for i in range(len(pts)):
    p = pts[i]
    for j in range(i + 1, len(pts)):
        r = pts[j]
        on = [p, r]
        for t in range(1, q):
            v = tuple((p[k] + t * r[k]) % q for k in range(4))
            if v[3] == 0:
                continue
            iv = pow(v[3], q - 2, q)
            v = tuple(x * iv % q for x in v)
            if v in spec and v not in on:
                on.append(v)
        if len(on) >= 5:
            lines[frozenset(on)] = len(on)
sizes = {}
good, exemplar = 0, None
for L in lines:
    sizes[len(L)] = sizes.get(len(L), 0) + 1
    for sub in combinations(sorted(L), 5):
        bl = [spec[s] for s in sub]
        if len(set().union(*bl)) == 15:
            good += 1
            if exemplar is None:
                exemplar = [sorted(b) for b in bl]
P("    special points (C(16,3)) : %d ; lines carrying >= 5 of them : %d ;"
  " sizes %s" % (len(pts), len(lines), dict(sorted(sizes.items()))))
P("    admissible (Q,Gamma) configurations (T=5 disjoint blocks) : %d" % good)
if exemplar:
    P("    exemplar blocks : %s" % exemplar)

# --------------------------------------------------------------- [C]
P("")
P("[C] THE FIRST-MOMENT COUNT (heuristic; graded as such -- R3(b))")
P("    E = #{(Q up to scale and PGL_2, Gamma) : every Q(gamma,.) splits over D}")
P("    log2 E = [(m+1)(rho+1)-1-3] log2 q + log2 C(q+1,T)")
P("             + T [ log2 C(16m,4m-1) - rho log2 q ]")
P("    The multiplicative domain enters ONLY through C(16m,4m-1), which is")
P("    q-INDEPENDENT, against an ambient q^rho.  That is the whole gate.")
P("")


def logE(m, lq, qq=None):
    rho, N, T = 4 * m - 1, 16 * m, 4 * m + 1
    dim = (m + 1) * (rho + 1) - 1 - 3
    lcNr = (math.lgamma(N + 1) - math.lgamma(rho + 1)
            - math.lgamma(N - rho + 1)) / math.log(2)
    if qq is not None and qq + 1 >= T:
        lcq = (math.lgamma(qq + 2) - math.lgamma(T + 1)
               - math.lgamma(qq + 2 - T)) / math.log(2)
    else:
        lcq = T * lq - math.lgamma(T + 1) / math.log(2)
    return dim * lq + lcq + T * (lcNr - rho * lq), lcNr


P("       m        q   unknowns   T   log2 C(N,rho)      log2 E")
for (m, qq) in ((1, 17), (1, 97), (2, 97), (2, 193), (3, 97), (3, 193),
                (4, 193), (4, 257), (5, 401), (6, 193)):
    v, lc = logE(m, math.log2(qq), qq)
    P("    %4d %8d %10d %4d %15.2f %11.2f"
      % (m, qq, (m + 1) * (4 * m), 4 * m + 1, lc, v))
P("")
P("    official scale (q ~ 2^167):")
for m in (2, 4, 16, 1024, 2 ** 20):
    v, lc = logE(m, 167.0)
    P("       m = %-9d log2 E = %-14.6g   (log2 E)/m^2 = %.3f"
      % (m, v, v / (m * m)))

# --------------------------------------------------------------- [D]
P("")
P("[D] D2 ADDENDUM -- 'the binding sub-system is ANY 16 points of W' made a")
P("    QUANTIFIER claim (CATCH-24C): ALL C(20,16) = 4845 subsets, both fields.")
m3, rho3, N3 = 3, 11, 48


def la_nullity(inc, mm, rr, qq):
    ncols = (mm + 1) * (rr + 1)
    pr = PackedRank(ncols, qq)
    for gam, x in inc:
        gp = [pow(gam, i, qq) for i in range(mm + 1)]
        xp = [pow(x, t, qq) for t in range(rr + 1)]
        pr.add_row([gp[i] * xp[t] % qq for i in range(mm + 1)
                    for t in range(rr + 1)])
    return ncols - pr.rank


for qq in (97, 193):
    cfg = build(qq, 340000 + qq)                                        # noqa
    if cfg is None:
        P("    q=%d BUILD FAILED" % qq)
        continue
    bl, Wset = cfg["blocks"], cfg["Wset"]
    keys = sorted(bl)
    sl = [cfg["g"] if k == "g" else cfg["h"] if k == "h" else int(k[1:])
          for k in keys]
    Amap = {x: [s for k, s in zip(keys, sl) if x in bl[k]] for x in Wset}
    hist = {}
    for sub in combinations(sorted(Wset), 16):
        inc = [(s, x) for x in sub for s in Amap[x]]
        n = la_nullity(inc, m3, rho3, qq)
        hist[n] = hist.get(n, 0) + 1
    P("    q=%3d : nullity over ALL %d 16-subsets of W : %s   (48 conditions"
      " on 48 unknowns each)" % (qq, sum(hist.values()), dict(sorted(hist.items()))))
P("    gcd(rho,N) = gcd(%d,%d) = %d -> no block is a union of cosets of a"
  " nontrivial subgroup of mu_N" % (rho3, N3, math.gcd(rho3, N3)))
P("    (banked: coset_biform_lift_obstruction proof.md:66-72 eq (9))")
P("")
P("=== END d3_mult ===")
open(HERE + "/d3_mult_results.txt", "w").write("\n".join(OUTL) + "\n")
