"""ES-G-LANES main analysis: L1 (true |Z_w|), L2 (global balance per lane per
admissible (p,delta,e)), L3 (strata / binding stratum), L5 (u2c pin check).

FAIL-CLOSED: every pre-registered prediction P1..P6 is asserted; a violated
prediction prints FIRED/REFUTED explicitly and the script exits nonzero only
on an internal inconsistency (a prediction firing is a RESULT, not an error).
"""
import sys
import math
from fractions import Fraction
from esg_lib import (closure_size_fast, closure_size_brute, mult_order,
                     p_classes, balance, log2_binom, log2_bracket,
                     BAND_ROWS, N, DELTA_PMIN, ADMISSIBLE_DE)

M = 41
HALF = 1 << (M - 2)
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


# --------------------------------------------------------------------------
def iroot(x, k):
    """floor(x ** (1/k)) exactly."""
    if x < 0:
        raise ValueError
    hi = 1 << ((x.bit_length() + k - 1) // k + 1)
    lo = 0
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# the eight p-classes mod 2^41 with ord | 4, labelled
CLASSES = []
for eps in (1, -1):
    for j in range(4):
        g = (eps * (1 + j * HALF)) % N
        CLASSES.append((g, mult_order(g, N), eps, j))
CLASSES.sort(key=lambda t: (t[1], t[0]))


def pmin_for_class(g):
    """smallest possible prime p in the residue class g mod 2^41 -- we only
    need a rigorous LOWER bound on p, and p = g (mod 2^41) with p odd prime
    gives p >= g whenever g > 1 (p = g is the smallest representative)."""
    return g if g > 1 else N + 1


def pmax_for_e(e):
    """largest integer p with p^e < 2^256."""
    return iroot((1 << 256) - 1, e)


# ==========================================================================
say("=" * 78)
say("L1 -- TRUE p-CYCLOTOMIC CLOSURE SIZE |Z_w| AT THE CROSSING ROW n = 2^41")
say("=" * 78)
say("")
say("The eight residue classes of p mod 2^41 with ord_n(p) | 4 (all admissible")
say("characteristics lie in one of them; ord in {1,2,4} is PROVED, see PROOFS).")
say("")
say(f"{'p mod 2^41':>16} {'delta':>5} {'eps':>4} {'j':>2} | "
    + " ".join(f"|Z_w|/(w-1) @ w=2^{v}" for v in (34, 39)))
ratios = {}
for (g, delta, eps, j) in CLASSES:
    row = []
    for v in (34, 39):
        w = 1 << v
        z = closure_size_fast(M, w - 1, g)
        row.append(Fraction(z, w - 1))
        ratios[(g, v)] = (z, Fraction(z, w - 1))
    say(f"{g:>16} {delta:>5} {eps:>4} {j:>2} | " +
        "  ".join(f"{str(r):>18}" for r in row))

say("")
say("Exact |Z_w| for every class and every structural w = 2^v, v = 34..39:")
say("")
hdr = f"{'p mod 2^41':>16} {'d':>2} " + " ".join(f"{'w=2^%d' % v:>22}" for v in range(34, 40))
say(hdr)
ZW = {}
for (g, delta, eps, j) in CLASSES:
    cells = []
    for v in range(34, 40):
        w = 1 << v
        z = closure_size_fast(M, w - 1, g)
        ZW[(g, v)] = z
        cells.append(f"{z:>22}")
    say(f"{g:>16} {delta:>2} " + " ".join(cells))

say("")
say("Ratios |Z_w|/(w-1) are w-INDEPENDENT across v = 34..39 for every class:")
for (g, delta, eps, j) in CLASSES:
    rs = {Fraction(ZW[(g, v)], (1 << v) - 1) for v in range(34, 40)}
    say(f"   p={g:>16}  delta={delta}  ratios={sorted(map(str, rs))}")

# ---- P1
say("")
distinct = sorted({Fraction(ZW[(g, 34)], (1 << 34) - 1) for (g, d, e, j) in CLASSES})
say(f"(P1) distinct |Z_w|/(w-1) values at w=2^34: {[str(x) for x in distinct]}")
P1_ok = [str(x) for x in distinct] == ['1', '3/2', '2', '11/4', '3']
say(f"(P1) predicted {{1, 3/2, 2, 11/4, 3}} -> {'HOLDS' if P1_ok else 'REFUTED'}")
max_d4 = max(Fraction(ZW[(g, 34)], (1 << 34) - 1)
             for (g, d, e, j) in CLASSES if d == 4)
say(f"(P1 corollary) max ratio at delta=4 is {max_d4} < 4 = delta  -> "
    f"the round-15 bracket TOP delta*(w-1) is NOT ATTAINED at delta=4: "
    f"{'HOLDS' if max_d4 < 4 else 'REFUTED'}")

# ==========================================================================
say("")
say("=" * 78)
say("L2 -- GLOBAL BALANCE  |Z_w| * log2 p >= n  AT THE CROSSING ROW")
say("=" * 78)
say("")
say("Admissible (delta,e): delta | e, e <= 6, v_2(e) <= 2, e*log2 p < 256,")
say("p >= 2^(41-log2 delta) - 1.  For each class+e, p ranges over")
say("[p_min(class), floor((2^256-1)^(1/e))].")
say("")
say(f"{'p class':>16} {'d':>2} {'e':>2} {'log2 p range':>28} "
    f"{'w':>6} {'thr log2 p*':>16} {'VERDICT':>9}")
crossing_rows = []
for v in (34, 35, 36, 37, 38, 39):
    w = 1 << v
    for (g, delta, eps, j) in CLASSES:
        z = ZW[(g, v)]
        thr = Fraction(N, z)          # required log2 p
        for (dd, e) in ADMISSIBLE_DE:
            if dd != delta:
                continue
            plo = pmin_for_class(g)
            phi = pmax_for_e(e)
            if plo > phi:
                continue
            verdict, mlo, mhi = balance(z, plo, phi, N)
            lo_b = log2_bracket(plo)[0]
            hi_b = log2_bracket(phi)[1]
            crossing_rows.append((v, g, delta, e, plo, phi, z, thr, verdict))
            if v in (34, 35, 36):
                say(f"{g:>16} {delta:>2} {e:>2} "
                    f"[{float(lo_b):>10.5f},{float(hi_b):>11.5f}] "
                    f"{'2^%d' % v:>6} {float(thr):>16.7f} {verdict:>9}")

say("")
say("Summary over the WHOLE structural bracket w = 2^34..2^39:")
for v in range(34, 40):
    nev = sum(1 for r in crossing_rows if r[0] == v and r[8] == "NEVER")
    flp = sum(1 for r in crossing_rows if r[0] == v and r[8] == "FLIPS")
    alw = sum(1 for r in crossing_rows if r[0] == v and r[8] == "ALWAYS")
    say(f"   w=2^{v}: ALWAYS sub-balance {alw:>2} classes, FLIPS {flp:>2}, "
        f"NEVER (above balance for every admissible p) {nev:>2}")

# ---- P2: exhibit an explicit admissible ABOVE-balance row
say("")
say("(P2) explicit admissible official rate-1/2 rows ABOVE global balance at w=2^34")
exhibits = []
for e in (6, 5, 4, 3, 2):
    c = 1
    while c <= 4000 and len(exhibits) < 3:
        p = c * N + 1                      # p = 1 mod 2^41  => delta = 1
        if p ** e < (1 << 256) and is_prime(p):
            z = ZW[(1, 34)]
            v_, mlo, _ = balance(z, p, p, N)
            q = p ** e
            Bstar = q >> 128
            if v_ == "NEVER":
                exhibits.append((p, e, q, Bstar, z, mlo))
        c += 1
    if exhibits:
        break
for (p, e, q, Bstar, z, mlo) in exhibits:
    lq = float(log2_bracket(q)[0])
    lp = float(log2_bracket(p)[0])
    say(f"   p = {p} (prime, p = 1 mod 2^41), e = {e}, q = p^e")
    say(f"     log2 p = {lp:.6f}, log2 q = {lq:.6f} < 256, 2^41 | q-1, k=2^40")
    say(f"     B* = floor(q/2^128) = {Bstar}  (log2 B* = {float(log2_bracket(Bstar)[0]):.3f})")
    say(f"     |Z_w| = {z}, |Z_w|*log2 p - n = {float(mlo):.6e}  -> ABOVE GLOBAL BALANCE")
P2_fired = len(exhibits) > 0
say(f"(P2) prediction FIRES: {P2_fired}")

# the structural MC-3 count at each w, versus B*
say("")
say("Which w the crossing lane can actually use: structural count S(v) = C(2^(41-v), 2^(40-v)-1)/2^(41-v)")
for v in range(34, 40):
    Nv = 1 << (41 - v)
    mv = (1 << (40 - v)) - 1
    S = log2_binom(Nv, mv) - (41 - v)
    say(f"   w=2^{v}: log2 S = {S:>10.4f}   (needs log2 B* >= this, i.e. log2 q >= {128+S:.4f})")

# ==========================================================================
say("")
say("=" * 78)
say("L3 -- STRATUM DECOMPOSITION (C4-a) AND THE BINDING STRATUM")
say("=" * 78)
say("")
say("Stratum a: T a union of mu_{2^a}-cosets  =>  only the conditions with")
say("2^a | s survive, and they are the prefix window of the n/2^a instance:")
say("   n_a = 2^(41-a),  W_a = floor((w-1)/2^a) = 2^(v-a) - 1,")
say("   |Z^(a)| = |closure of {1..W_a} under *p in Z/n_a|,   a = 0 .. v-1.")
say("Global balance at stratum a:  |Z^(a)| * log2 p >= n_a.")
say("")
binding = {}
for v in (34, 35, 36, 39):
    w = 1 << v
    say(f"--- crossing w = 2^{v} (M = 2^{v}, strata a = 0..{v-1})")
    say(f"{'p class':>16} {'d':>2} | {'a':>3} {'n_a':>12} {'|Z^(a)|':>14} "
        f"{'req log2 p':>14}   {'binding?':>8}")
    for (g, delta, eps, j) in CLASSES:
        worst_a, worst_thr, worst_z = None, Fraction(0), None
        rowsa = []
        for a in range(0, v):
            ma = M - a
            na = 1 << ma
            Wa = (1 << (v - a)) - 1
            ga = g % na
            za = closure_size_fast(ma, Wa, ga)
            thr = Fraction(na, za)
            rowsa.append((a, na, za, thr))
            if thr > worst_thr:
                worst_a, worst_thr, worst_z = a, thr, za
        binding[(v, g)] = (worst_a, worst_thr, worst_z)
        for (a, na, za, thr) in rowsa:
            if a in (0, 1, v - 2, v - 1) or a == worst_a:
                mark = "<== BIND" if a == worst_a else ""
                say(f"{g:>16} {delta:>2} | {a:>3} {na:>12} {za:>14} "
                    f"{float(thr):>14.6f}   {mark:>8}")
        say("")

say("The binding stratum is the DEEPEST one (a = v-1) for every class:")
allbind = all(binding[(v, g)][0] == v - 1 for v in (34, 35, 36, 39)
              for (g, d, e, j) in CLASSES)
say(f"   uniform-deepest: {allbind}")
say("")
say("Required log2 p at the deepest stratum a = v-1  (n_a = 2^(42-v), one")
say("surviving condition s = 2^(v-1), so |Z^(a)| = 1 if p = 1 mod 2^(42-v),")
say("else 2):")
say("")
say("NOTE (self-caught): the verdict column below MUST use the certified")
say("comparator, never a float compare -- log2(2^128 - 1) rounds to 128.0 in")
say("float64 and silently flips the boundary cases.  See PROOFS.md CATCH-A.")
say("")
say("Scope: the crossing lane's OPEN branch is B* >= 3, i.e. q >= 3*2^128")
say("(node statement: branches B* in {1,2} are a COMPLETE determination), so")
say("p >= ceil((3*2^128)^(1/e)).  Both scopes reported.")
say("")
say(f"{'w':>7} {'p class':>16} {'d':>2} {'e':>2} {'n_a':>8} {'|Z|':>4} "
    f"{'req log2 p':>12} {'log2 p range':>26} {'a=0':>7} {'DEEPEST':>8} {'ALL STRATA':>11}")
P4_fired = {}          # (v, g, e) -> True if the deepest stratum can never hold
ALLSTRAT = {}          # (v, g, e) -> verdict over all strata a = 0..v-1
Q_BSTAR3 = 3 * (1 << 128)
for v in (34, 35, 36, 37, 38, 39):
    for (g, delta, eps, j) in CLASSES:
        for (dd, e) in ADMISSIBLE_DE:
            if dd != delta:
                continue
            phi = pmax_for_e(e)
            plo = max(pmin_for_class(g), iroot(Q_BSTAR3 - 1, e) + 1)
            if plo > phi:
                continue                       # (class,e) inadmissible at B*>=3
            # deepest stratum
            a = v - 1
            ma, na = M - a, 1 << (M - a)
            za = closure_size_fast(ma, (1 << (v - a)) - 1, g % na)
            thr = Fraction(na, za)
            vd, mlo, mhi = balance(za, plo, phi, na)
            P4_fired[(v, g, e)] = (vd == "NEVER")
            # every stratum
            worst = "ALWAYS"
            for aa in range(0, v):
                mm, nn = M - aa, 1 << (M - aa)
                zz = closure_size_fast(mm, (1 << (v - aa)) - 1, g % nn)
                vv, _, _ = balance(zz, plo, phi, nn)
                if vv == "NEVER":
                    worst = "NEVER"
                    break
                if vv == "FLIPS":
                    worst = "FLIPS"
            ALLSTRAT[(v, g, e)] = worst
            z0 = closure_size_fast(M, (1 << v) - 1, g)
            v0, _, _ = balance(z0, plo, phi, N)
            if v <= 36:
                say(f"{'2^%d' % v:>7} {g:>16} {delta:>2} {e:>2} {na:>8} {za:>4} "
                    f"{float(thr):>12.4f} "
                    f"[{float(log2_bracket(plo)[0]):>8.5f},{float(log2_bracket(phi)[1]):>9.5f}] "
                    f"{v0:>7} {vd:>8} {worst:>11}")
say("")
for v in range(34, 40):
    keys = [k for k in P4_fired if k[0] == v]
    nf = sum(1 for k in keys if P4_fired[k])
    nn_ = sum(1 for k in keys if ALLSTRAT[k] == "NEVER")
    na_ = sum(1 for k in keys if ALLSTRAT[k] == "ALWAYS")
    say(f"   w=2^{v}: deepest stratum NEVER holds for {nf}/{len(keys)} (class,e) pairs; "
        f"stratum-uniform: ALWAYS {na_}, NEVER {nn_}, FLIPS {len(keys)-na_-nn_}")
# non-vacuity of every stratum: r' = 2^40 - 2^v must be divisible by 2^a
for v in range(34, 40):
    for a in range(0, v):
        assert ((1 << 40) - (1 << v)) % (1 << a) == 0, (v, a)
say("")
say("Non-vacuity: r' = 2^40 - 2^v is divisible by 2^a for every stratum")
say("a = 0..v-1 and every v = 34..39, so every stratum has candidate members")
say("(a union of mu_{2^a}-cosets of the right size exists).  CHECKED.")
P4_all34 = all(P4_fired[k] for k in P4_fired if k[0] == 34)
say(f"(P4) at w=2^34 the deepest stratum NEVER holds, for EVERY admissible "
    f"(p-class, e): {P4_all34}")

# ==========================================================================
say("")
say("=" * 78)
say("L2/L4 -- THE BAND ROWS (full-rank + syzygy), c = 2d generic F_q-forms")
say("=" * 78)
say("")
say("Band-proper depth = ceil(h/2) <= d <= h-2 (WIRING.md:59).")
say("Global balance:  2d * log2 q >= n = 2^41,  q < 2^256, q >= 2^209 (pin).")
say("")
say(f"{'rate':>6} {'d':>12} {'2d':>12} {'req log2 q':>18} {'q>=2^209..<2^256':>18}")
band_verdicts = {}
for rate, (k, h, dlo, dhi) in BAND_ROWS.items():
    for d in (dlo, (dlo + dhi) // 2, dhi):
        c = 2 * d
        thr = Fraction(N, c)
        verdict, mlo, mhi = balance(c, 1 << 209, (1 << 256) - 1, N)
        band_verdicts[(rate, d)] = verdict
        say(f"{rate:>6} {d:>12} {c:>12} {float(thr):>18.9f} {verdict:>18}")
say("")
say("Exact depth threshold d* = n / (2 log2 q) at three field sizes:")
for lq in (209, 250, 255.9, 256):
    dstar = N / (2 * lq)
    say(f"   log2 q = {lq:>6}: d* = {dstar:>18.2f}  (= 2^{math.log2(dstar):.6f})")
say("")
for rate, (k, h, dlo, dhi) in BAND_ROWS.items():
    say(f"   rate {rate}: band-proper d in [{dlo}, {dhi}] = [2^{math.log2(dlo):.6f}, 2^{math.log2(dhi):.6f}]")
say("")
# P3: rate 1/16 always above balance
k, h, dlo, dhi = BAND_ROWS["1/16"]
c_max = 2 * dhi
v16, m16lo, m16hi = balance(c_max, 1 << 209, (1 << 256) - 1, N)
say(f"(P3) rate 1/16, LARGEST depth d = {dhi}, c = 2d = {c_max}:")
say(f"     verdict over q in [2^209, 2^256) : {v16}")
say(f"     even at q -> 2^256:  2d*256 = {c_max*256} vs n = {N}; "
    f"deficit = {N - c_max*256} bits")
P3_fired = (v16 == "NEVER") and (c_max * 256 < N)
say(f"(P3) rate-1/16 band row is ABOVE global balance at EVERY admissible "
    f"(q,d): {'FIRES' if P3_fired else 'REFUTED'}")
say("")
k4, h4, dlo4, dhi4 = BAND_ROWS["1/4"]
say(f"(rates 1/4, 1/8) LOWEST depth d = {dlo4}, c = 2d = {2*dlo4}:")
thr_lo = Fraction(N, 2 * dlo4)
say(f"     required log2 q = {float(thr_lo):.9f}  (admissible window width to 256: "
    f"{256 - float(thr_lo):.3e} bits)")
v4, _, _ = balance(2 * dlo4, 1 << 209, (1 << 256) - 1, N)
say(f"     verdict over q in [2^209, 2^256): {v4}")
say(f"     at the banked pin log2 q = 209 the above-balance zone is "
    f"d in [{dlo4}, {int(N/(2*209))}]  "
    f"({100.0*(N/(2*209)-dlo4)/(dhi4-dlo4):.1f}% of the band-proper range)")
say(f"     at the convention log2 q = 250 the above-balance zone is "
    f"d in [{dlo4}, {int(N/(2*250))}]  "
    f"({100.0*(N/(2*250)-dlo4)/(dhi4-dlo4):.1f}% of the band-proper range)")

# syzygy: rank bracket
say("")
say("Syzygy node (rank J_d < 2d): depth ceil((2h+2)/3) <= d <= h-2, and")
say("(SL2-ABN) dim K_d <= 3d-2h-ell, so rank J_d in [2h-d+ell, 2d].  Both ends:")
say("")
say(f"{'rate':>6} {'d_lo':>12} {'d_hi':>12} {'c=2d @d_lo':>12} "
    f"{'c=rank_min@d_lo':>16} {'verdict(2d)':>12} {'verdict(rank_min)':>18}")
for rate, (k, h, dlo, dhi) in BAND_ROWS.items():
    sd_lo = -(-(2 * h + 2) // 3)
    sd_hi = h - 2
    for d in (sd_lo, sd_hi):
        c_nom = 2 * d
        c_min = 2 * h - d           # ell = 0, worst admissible rank deficit
        vn, _, _ = balance(c_nom, 1 << 209, (1 << 256) - 1, N)
        vm, _, _ = balance(max(c_min, 1), 1 << 209, (1 << 256) - 1, N)
        say(f"{rate:>6} {sd_lo:>12} {sd_hi:>12} {c_nom:>12} {c_min:>16} "
            f"{vn:>12} {vm:>18}")

# ==========================================================================
say("")
say("=" * 78)
say("L5 -- u2c PIN CHECK: the five round-16 witnesses vs the GLOBAL boundary")
say("=" * 78)
say("")
say("u2c falsifier (node.json:10) requires sub-balance q^t >= 2^n.  For the")
say("(ES) object that reads p^{|Z_w|} >= 2^n with n = 32 at the witness rows.")
say("")
WIT = [(6, 4, 7, 4, 10, -8.284), (6, 3, 47, 2, 4, -2.429),
       (6, 4, 17, 2, 5, -0.648), (5, 2, 23, 4, 4, -0.475),
       (5, 2, 463, 2, 2, -0.090)]
say(f"{'r\'':>3} {'w':>3} {'p':>5} {'d':>2} {'|Z_w|':>6} {'Lam(per-wt)':>12} "
    f"{'log2 p^|Z|':>12} {'n=32':>5} {'GLOBAL':>10}")
P5_ok = True
for (rp, wv, p, delta, zw, lam) in WIT:
    z = closure_size_brute(32, wv - 1, p)
    assert z == zw, (p, z, zw)
    val = p ** z
    lg = float(log2_bracket(val)[0])
    sub = val >= (1 << 32)
    if sub:
        P5_ok = False
    lam_chk = log2_binom(32, rp) - z * float(log2_bracket(p)[0])
    say(f"{rp:>3} {wv:>3} {p:>5} {delta:>2} {z:>6} {lam_chk:>12.3f} "
        f"{lg:>12.3f} {32:>5} {'ABOVE' if not sub else 'SUB(!)':>10}")
    assert abs(lam_chk - lam) < 5e-3, (p, lam_chk, lam)
say("")
say(f"(P5) all five witnesses ABOVE the global boundary (hence excluded by the")
say(f"     u2c pre-registered falsifier): {'HOLDS' if P5_ok else 'REFUTED'}")

# ==========================================================================
say("")
say("=" * 78)
say("PREDICTION LEDGER")
say("=" * 78)
say("Exact |Z_w| closed forms at w = 2^v (v <= 37, before the orbit-merge):")
say("   delta=1  (p = 1 mod 2^41)              : |Z_w| = w-1")
say("   delta=2  (p = 2^40+1)                  : |Z_w| = 3*2^(v-1) - 1")
say("   delta=2  (p = -1 or 2^40-1)            : |Z_w| = 2(w-1)")
say("   delta=4  (p = +-1 mod 2^39, eps=+1)    : |Z_w| = 11*2^(v-2) - 1")
say("   delta=4  (p = +-1 mod 2^39, eps=-1)    : |Z_w| = 6*2^(v-1) - 2")
say("   (at w = 2^38, 2^39 the eps=-1 delta=4 classes MERGE orbits and drop to 2(w-1))")
say("")
led = [("P1 |Z_w| ratio set exactly {1,3/2,2,11/4,3}", "REFUTED AS STATED" if not P1_ok else "HOLDS"),
       ("P1c delta=4 bracket top not attained", "HOLDS" if max_d4 < 4 else "REFUTED"),
       ("P2 admissible crossing row above global balance", "FIRES" if P2_fired else "did not fire"),
       ("P3 rate-1/16 band above balance everywhere", "FIRES" if P3_fired else "did not fire"),
       ("P4 deepest stratum unpayable at w=2^34", "FIRES" if P4_all34 else "did not fire"),
       ("P5 u2c falsifier excludes all five witnesses", "HOLDS" if P5_ok else "REFUTED")]
for a, b in led:
    say(f"   {a:<52} {b}")

with open("esg_analysis.log", "w") as fh:
    fh.write("\n".join(OUT) + "\n")

# internal consistency assertions (fail-closed).  A REFUTED prediction is a
# result, not an error; only an internal inconsistency aborts.
assert all(closure_size_fast(M, (1 << v) - 1, g) == ZW[(g, v)]
           for (g, d, e, j) in CLASSES for v in range(34, 40)), "L1 unstable"
assert P5_ok, "u2c falsifier does NOT exclude the witnesses -- L5 inconsistent"
print()
print("ANALYSIS COMPLETE (log written to esg_analysis.log)")
