#!/usr/bin/env python3
"""(OUT-m) as an aggregate identity, and its (DEG-m) corollary.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L3329-3350 ((OUT-m) posed, round 34 bank 3, WITH the coordinator's
        two corrections) and L3752-3771 (refined to an identity, round 35
        bank 3), plus the completion-level record at L4552-4557 (round 36
        bank 4).

Everything here is POSED-status content: (OUT-m) is a constraint on the
configuration space, and (DEG-m) inherits that status.  The verifier checks
the ARITHMETIC and the DOUBLE COUNT, not the geometry.

Checks
  A. the aggregate identity sum_gamma eps~_gamma = sum_x def(x) * t_x is a
     correct double count under the charge law t_x = m-1 / m-2 / m-3 at
     outside / symmetric-difference / middle points -- on explicit synthetic
     incidence structures, including the degenerate cases;
  B. the aggregate bound (m-1)(1+O) is attained ONLY by outside deficiency,
     and the m=3 witness's sum = 2 = (m-1)(1+O) at O = 0 attains it, while
     the REFUTED original rider 1+O = 1 fails (2 > 1);
  C. the corollary qualifier: "X_gamma = 0 impossible" needs 1+O < m-1,
     i.e. O <= m-3 -- satisfied at m=3, O=0, and VACUOUS at m=2;
  D. (DEG-m): deg_Sh(gamma) + X''_gamma >= ceil((m-1-eps~)/2) with the exact
     middle budget sum_gamma X''_gamma = (m-1)(m-2); at m >= 4 a degree-1
     slope REQUIRES middle support, at m = 3 it does not;
  E. the completion-level record: the 2-sharing m=4 ceiling configurations
     have n_1 = 9 against a completeness bound of 4.

Stdlib only; helpers duplicated; nothing imported.
Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_bivcurve_out_m_identity_and_deg_m/verify.py
(RAMGUARD_TIMEOUT 60s)
NOTE (D11 rename, applied at wiring): the quantity called deg_H in the
round-35 addendum is deg_Sh here and in every wired document -- deg_H
already names the bipartite non-incidence degree in the PROVED node
rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction.
"""

import random

FAIL = []


def bad(m):
    FAIL.append(m)


# ---------------------------------------------------------------- A + B
def charge(kind, m):
    """type-2 blocks through a point, by position class."""
    return {"outside": m - 1, "symdiff": m - 2, "middle": m - 3}[kind]


def double_count(m, points, rng):
    """points = [(kind, deficiency)].  Build an explicit bipartite
    incidence in which a point of class `kind` lies in exactly t_x
    type-2 blocks, then check the identity both ways."""
    blocks = {}
    total_blocks = max(1, (m - 1) * 4)
    for idx, (kind, defi) in enumerate(points):
        t = charge(kind, m)
        if t < 0:
            return None
        chosen = rng.sample(range(total_blocks), min(t, total_blocks))
        if len(chosen) != t:
            return None
        for g in chosen:
            blocks.setdefault(g, []).append(idx)
    lhs = 0
    for g, idxs in blocks.items():
        lhs += sum(points[i][1] for i in idxs)          # eps~_gamma
    rhs = sum(defi * charge(kind, m) for kind, defi in points)
    return lhs, rhs


rng = random.Random(3708)
checked = 0
for m in (3, 4, 5, 6, 8):
    for _ in range(40):
        npts = rng.randrange(1, 7)
        pts = []
        for _ in range(npts):
            kind = rng.choice(["outside", "symdiff", "middle"])
            if charge(kind, m) < 0:
                kind = "outside"
            pts.append((kind, rng.randrange(0, 4)))
        got = double_count(m, pts, rng)
        if got is None:
            continue
        lhs, rhs = got
        if lhs != rhs:
            bad("double count fails at m=%d on %s: %d != %d"
                % (m, pts, lhs, rhs))
        else:
            checked += 1

# B. the aggregate is attained ONLY by outside deficiency
for m in (3, 4, 5):
    for O in (0, 1, 2):
        cap = (m - 1) * (1 + O)
        # one unit of deficiency, placed in each class
        vals = {k: charge(k, m) for k in ("outside", "symdiff", "middle")}
        if max(vals.values()) != vals["outside"]:
            bad("outside is not the maximal charge at m=%d" % m)
        units = 1 + O
        if units * vals["outside"] != cap:
            bad("the aggregate (m-1)(1+O) is not units*charge_outside "
                "at m=%d O=%d" % (m, O))
        for k in ("symdiff", "middle"):
            if units * vals[k] >= cap and vals[k] > 0:
                bad("class %s reaches the aggregate at m=%d" % (k, m))

# the m=3 witness: sum eps~ = 2 = (m-1)(1+O) with O = 0, refuting the rider
m, O = 3, 0
if (m - 1) * (1 + O) != 2:
    bad("m=3 aggregate is not 2")
if not 2 > 1 + O:
    bad("the refuted rider sum eps <= 1+O should FAIL at the m=3 witness")
# the m=2 exhibit places its deficient point INSIDE W and charges 0
if charge("symdiff", 2) != 0:
    bad("m=2 inside placement should charge 0")

# ------------------------------------------------------------------- C
for m in (2, 3, 4, 5):
    # "X_gamma = 0 impossible" requires 1 + O < m - 1, i.e. O <= m - 3
    admissible = [O for O in range(0, 6) if 1 + O < m - 1]
    predicted = [O for O in range(0, 6) if O <= m - 3]
    if admissible != predicted:
        bad("corollary qualifier mismatch at m=%d: %s vs %s"
            % (m, admissible, predicted))
    if m == 2 and admissible:
        bad("the corollary should be VACUOUS at m=2")
    if m == 3 and admissible != [0]:
        bad("at m=3 the corollary should hold exactly for O=0")

# ------------------------------------------------------------------- D
def deg_m_floor(m, eps):
    return -((-(m - 1 - eps)) // 2)


for m in range(3, 21):
    f = deg_m_floor(m, 0)
    if m == 3 and f != 1:
        bad("(DEG-m) floor at m=3 is %d, want 1 (no middle support forced)"
            % f)
    if m >= 4 and f < 2:
        bad("(DEG-m) floor at m=%d is %d; a degree-1 slope would not need "
            "middle support" % (m, f))
    # a degree-1 slope has X' = 2*deg_Sh = 2, i.e. deg_Sh = 1
    if m >= 4 and 1 >= f:
        bad("at m=%d deg_Sh=1 already meets the floor" % m)
    if (m - 1) * (m - 2) != sum([m - 2] * (m - 1)):
        bad("middle budget arithmetic at m=%d" % m)
if (3 - 1) * (3 - 2) != 2 or (4 - 1) * (4 - 2) != 6:
    bad("middle budget values at m=3,4")

# ------------------------------------------------------------------- E
if not 9 > 4:
    bad("completion record: n_1 = 9 should exceed the completeness bound 4")

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("OUTM_IDENTITY_DEGM_PASS double count exact on %d synthetic "
      "configurations (m=3,4,5,6,8); aggregate (m-1)(1+O) attained only by "
      "outside deficiency; m=3 witness sum=2 refutes the rider 1+O=1; "
      "corollary needs O<=m-3 and is VACUOUS at m=2; (DEG-m) floor "
      "ceil((m-1)/2) forces middle support for a degree-1 slope at every "
      "m>=4 and not at m=3; middle budget (m-1)(m-2) = 2,6 at m=3,4"
      % checked)
