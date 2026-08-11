#!/usr/bin/env python3
"""The negation-closure excess: mechanism, exact count, and the razor kill.

Source: critical/nodes/rate_half_band_crossing_location/statement.md,
        the negation-closure-excess bullet of the Round-36 R-HRLOW
        addendum (round 36 bank 3; line refs drift with inline markers).
Mechanism text: notes/pilots_20260811/r36_hrlow/f4_close.py:5-21.
Banked rows:    notes/pilots_20260811/r36_hrlow/f4_results.txt:6-24 (scan),
                :26-27 (control), :29-45 (razor closed forms).

Checks
  A. THE MECHANISM, directly: on a negation-closed D with e_1 = x^2 e_0 and
     an even locator S = A u (-A) covering every orbit that T misses, the
     ODD-index rows of the pencil vanish identically, leaving exactly
     ceil(rho/2) conditions on the single unknown gamma;
  B. THE COUNT at rho = 2: the bad even locators are EXACTLY the covering
     ones -- 84 at H1 and 330 at H3, both fields, as SETS not just counts;
  C. THE SUB-COUNT: at H3 the 330 bad locators carry only 329 DISTINCT
     slopes (locator count != slope count -- MISS-2 guard);
  D. THE KILL in miniature: at rho = 3 (H4) the covering count is 165 but
     the bad count is 0, because ceil(3/2) = 2 conditions on one unknown;
  E. THE GENERAL COVERING LAW C(m-off, r/2-off), off = m-(r+1), against all
     six banked cells -- C(m-1, r/2-1) is its off = 1 face;
  F. the razor kill arithmetic and the shape fence r > R/2.

Helpers DUPLICATED; nothing imported.  Stdlib only.
Run: tools/ramguard local -- python3 \
  background/nodes/rate_half_far_ca_negation_closure_excess_fence/verify.py
(RAMGUARD_TIMEOUT 300s)
"""

from itertools import combinations
from math import comb

FAIL = []


def bad(m):
    FAIL.append(m)


def inv(a, q):
    return pow(a % q, q - 2, q)


def make_D(n, q):
    D = []
    for i in range(1, n // 2 + 1):
        D.append(i % q)
        D.append((-i) % q)
    assert len(set(D)) == n
    return D


def make_v(D, q):
    v = {}
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % q
        v[x] = inv(pr, q)
    return v


def syn_of(ev, D, v, q, R):
    y = [0] * R
    for x in D:
        e = ev.get(x, 0) % q
        if not e:
            continue
        c = (e * v[x]) % q
        xp = 1
        for mm in range(R):
            y[mm] = (y[mm] + c * xp) % q
            xp = (xp * x) % q
    return y


def hankel(y, rho, r, q):
    return [[y[i + j] % q for j in range(r + 1)] for i in range(rho)]


def poly_from_roots(roots, q):
    p = [1]
    for a in roots:
        np_ = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            np_[i + 1] = (np_[i + 1] + c) % q
            np_[i] = (np_[i] - c * a) % q
        p = np_
    return p


# cells: tag, n, k, rho ; and the banked covering / bad / distinct counts
CELLS = [
    ("H1", 20, 10, 2, 84, 84, 84),
    ("H3", 24, 12, 2, 330, 330, 329),
    ("H4", 26, 13, 3, 165, 0, 0),
]
FIELDS = [65537, 999983]

odd_rows_zero = 0
scans = 0

for tag, n, k, rho, cov_want, bad_want, dist_want in CELLS:
    R = n - k
    r = R - rho
    a = n - r
    m = n // 2
    if not (4 * rho < R and a > R + 1 and a - 1 > r):
        bad("%s is not razor-faithful" % tag)
    off = m - (r + 1)
    # E. the general covering law, and its off = 1 face
    if comb(m - off, r // 2 - off) != cov_want:
        bad("%s covering law C(m-off, r/2-off) = %d, banked %d"
            % (tag, comb(m - off, r // 2 - off), cov_want))
    if off == 1 and comb(m - 1, r // 2 - 1) != cov_want:
        bad("%s: the off=1 face C(m-1, r/2-1) does not reproduce" % tag)
    if off != 1 and comb(m - 1, r // 2 - 1) == cov_want:
        bad("%s: C(m-1, r/2-1) unexpectedly matches at off = %d" % (tag, off))

    for q in FIELDS:
        D = make_D(n, q)
        v = make_v(D, q)
        pos = [i % q for i in range(1, m + 1)]
        orbits = list(range(1, m + 1))                # orbit i = {+i, -i}
        T = pos[:r + 1]                               # one-sided, meets 1..r+1
        offorbits = set(orbits[r + 1:])
        if len(offorbits) != off:
            bad("%s q=%d: |orbits off T| = %d, want %d"
                % (tag, q, len(offorbits), off))
        e0 = {x: 1 for x in T}
        e1 = {x: (x * x) % q for x in T}
        y0 = syn_of(e0, D, v, q, R)
        y1 = syn_of(e1, D, v, q, R)
        M0 = hankel(y0, rho, r, q)
        M1 = hankel(y1, rho, r, q)

        covering = set()
        badset = set()
        slopes = set()
        for A in combinations(orbits, r // 2):
            S = [i % q for i in A] + [(-i) % q for i in A]
            sig = poly_from_roots(S, q)
            U = [sum(M0[i][j] * sig[j] for j in range(r + 1)) % q
                 for i in range(rho)]
            Wv = [sum(M1[i][j] * sig[j] for j in range(r + 1)) % q
                  for i in range(rho)]
            covers = offorbits <= set(A)
            if covers:
                covering.add(A)
                # A. the mechanism: every ODD-index row vanishes identically
                if any(U[i] or Wv[i] for i in range(1, rho, 2)):
                    bad("%s q=%d: odd rows do not collapse on a covering "
                        "even locator" % (tag, q))
                else:
                    odd_rows_zero += 1
            if all(x == 0 for x in Wv):
                continue
            j0 = next(i for i in range(rho) if Wv[i])
            g = (-U[j0] * inv(Wv[j0], q)) % q
            if all((U[i] + g * Wv[i]) % q == 0 for i in range(rho)):
                badset.add(A)
                slopes.add(g)
        scans += 1
        if len(covering) != cov_want:
            bad("%s q=%d: covering count %d, banked %d"
                % (tag, q, len(covering), cov_want))
        if len(badset) != bad_want:
            bad("%s q=%d: bad even locators %d, banked %d"
                % (tag, q, len(badset), bad_want))
        if len(slopes) != dist_want:
            bad("%s q=%d: distinct slopes %d, banked %d"
                % (tag, q, len(slopes), dist_want))
        if rho == 2 and badset != covering:
            bad("%s q=%d: at rho=2 the bad set is not exactly the covering "
                "set" % (tag, q))
        if rho >= 3 and badset:
            bad("%s q=%d: rho >= 3 left %d bad even locators, want 0"
                % (tag, q, len(badset)))
        # D. the residual-condition count that explains both regimes
        nres = -((-rho) // 2)
        if (nres <= 1) != (bad_want > 0):
            bad("%s: ceil(rho/2) = %d does not explain bad_want = %d"
                % (tag, nres, bad_want))

# ---- E (continued): the law on the three cells the source scanned but this
#      verifier does not rebuild (pure arithmetic against the banked table).
for tag, n, k, rho, cov in (("H6", 30, 15, 3, 715), ("H7", 34, 17, 3, 3003),
                            ("H8", 36, 18, 4, 1365)):
    R = n - k
    r = R - rho
    m = n // 2
    off = m - (r + 1)
    if comb(m - off, r // 2 - off) != cov:
        bad("%s covering law gives %d, banked %d"
            % (tag, comb(m - off, r // 2 - off), cov))

# ---------------------------------------------------------------- F. razor
RHO = 2 ** 34
R40 = 2 ** 40
r_razor = R40 - RHO
if -((-RHO) // 2) != 2 ** 33:
    bad("ceil(rho/2) != 2^33")
if -((-RHO) // 2) - 1 != 8589934591:
    bad("razor surplus != 2^33-1")
if min(M for M in (2 ** i for i in range(41)) if -((-RHO) // M) == 1) != RHO:
    bad("ceil(rho/M) = 1 does not first hold at M = rho")
if r_razor != 1082331758592 or R40 + RHO != 1116691496960:
    bad("razor constants disagree with f4_results.txt:30")

# The shape fence.  "B_ca^far(n-r) <= r+1" is PROVED only at r <= R/2.  BOTH
# the exhibit cells AND the razor row at the crossing offset a = k + 2^34 sit
# at r > R/2, so the proved bound covers NEITHER: at the crossing offset the
# cap must come from the fibre pigeonhole (Statement U), not from that node.
for tag, n, k, rho in (("H1", 20, 10, 2), ("H3", 24, 12, 2)):
    R = n - k
    r = R - rho
    if not r > R / 2:
        bad("%s: exhibit is NOT at r > R/2, so it WOULD contradict the "
            "proved bound" % tag)
if not r_razor > R40 / 2:
    bad("razor row is at r <= R/2 -- then the proved bound would already "
        "cap B_ca^far and Statement U's pigeonhole would be redundant")
# 2r > R at razor is the same inequality that makes the type-2 ledger vacuous.
if not 2 * r_razor > R40:
    bad("2r <= R at razor contradicts the type-2 vacuity-by-sign fence")

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("NEGATION_CLOSURE_EXCESS_FENCE_PASS %d cell-field scans; odd rows "
      "collapse on %d covering even locators; rho=2 bad set == covering set "
      "(84 at H1, 330 at H3 carrying only 329 distinct slopes); rho=3 gives "
      "0 bad from 165 covering; general law C(m-off, r/2-off) reproduces all "
      "six banked cells; razor surplus ceil(rho/2)-1 = %d at M=2"
      % (scans, odd_rows_zero, 2 ** 33 - 1))
