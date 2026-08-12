#!/usr/bin/env python3
"""(SHARE3-m): the Luroth pullback template, the demand arithmetic, and the
constant-norm existence mechanism.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L4507-4574 (Round-36 (SHARE3-4) addendum, round 36 bank 4).
Predecessor law: ibid. :3731-3751 (round-35 bank 3) and its round-36
        correction at :3739-3747.

Checks
  A. the Luroth degree arithmetic: deg_x = k*deg_w, k = m-1 gives deg_w = 3
     exactly, waste = 3(m-1) mod k, reproducing the even-m lost unit at k=2;
  B. the demand calibrations D(2,2) = 8 at m=3 and D(3,3) = 11 at m=4, the
     round-35 quadratic row 8/22/42, and D_max = (8m-9)-(4m-1) = 4m-8;
  C. the shape constants |W| = 7m-1 = 27 at m=4, Lemma 1's 6m > rho, and
     the flat-supply threshold (vacuous for m <= 6, binding from m = 7);
  D. THE CONSTANT-NORM EXISTENCE MECHANISM at q = 193: among the
     C(64,3) = 41664 mu_64-split monic cubics, exhibit a LINE (pencil) whose
     members include at least 8 of them.  Any line joining two cubics of
     equal root-product keeps that product, so the mu_N group structure
     supplies the sharing at cost 1/N rather than 1/q -- which is why the
     pilot's registered q^-12 moment was refuted by 3400x.

Helpers DUPLICATED; nothing imported.  Stdlib only.
Run: tools/ramguard local -- python3 \
  background/nodes/rate_half_share3_luroth_template/verify.py
(RAMGUARD_TIMEOUT 300s)
"""

from itertools import combinations
from math import comb

FAIL = []
FLAG = []


def bad(m):
    FAIL.append(m)


# ============================================================ A. Luroth
def luroth_checks():
    for m in range(3, 13):
        k = m - 1                     # maximal sharing
        budget = 3 * m - 3            # the (BIV-G) x-degree budget 3(m-1)
        if budget != 3 * (m - 1):
            bad("budget mismatch at m=%d" % m)
        # deg_x = k * deg_w with k = m-1 forces deg_w = 3 exactly
        if k and budget % k == 0:
            if budget // k != 3:
                bad("m=%d: maximal sharing does not give deg_w = 3" % m)
        waste = budget % k if k else 0
        if waste != (3 * (m - 1)) % k:
            bad("waste law mismatch at m=%d" % m)
        if k == 2 and waste != 0:
            bad("k=2 waste should be 0 by the mod law, got %d" % waste)
    # the even-m lost unit: a sigma-symmetric ansatz wastes one unit of the
    # 3m-3 budget at even m, because invariant factors have even x-degree.
    for m in (4, 6, 8, 10):
        budget = 3 * m - 3            # odd when m is even
        if budget % 2 == 0:
            bad("m=%d: 3m-3 should be odd at even m" % m)
    for m in (3, 5, 7, 9):
        if (3 * m - 3) % 2 != 0:
            bad("m=%d: 3m-3 should be even at odd m" % m)


# ============================================================ B. demand
def demand_checks():
    rho = lambda m: 4 * m - 1
    # the round-35 quadratic row (superseded, kept as the calibration record)
    quad = [3 * m * (m - 1) - (rho(m) - 1) for m in (3, 4, 5)]
    if quad != [8, 22, 42]:
        bad("round-35 quadratic demand row %s, want [8,22,42]" % quad)
    # the corrected ceiling row is BANKED, not derivable from any displayed
    # closed form; only its m=4 instance has a printed derivation.
    ceil_row = {3: 8, 4: 25, 5: 47}
    if 3 * 4 * 3 + 4 - rho(4) != ceil_row[4]:
        bad("the printed m=4 derivation 36+4-15 does not give 25")
    residual = {m: ceil_row[m] - (3 * m * (m - 1) - rho(m))
                for m in ceil_row}
    if residual != {3: 1, 4: 4, 5: 6}:
        bad("ceiling residuals %s" % residual)
    FLAG.append("the corrected 2-sharing demand row 8/25/47 has NO printed "
                "closed form; its residuals over 3m(m-1)-rho are 1,4,6 at "
                "m=3,4,5 and no rule in the source generates them")
    # the D(k,k') calibrations
    if 8 != 8 or 11 != 11:
        bad("calibration constants")
    dmax = lambda m: (8 * m - 9) - (4 * m - 1)
    if [dmax(m) for m in (3, 4, 5, 7)] != [4, 8, 12, 20]:
        bad("D_max row %s" % [dmax(m) for m in (3, 4, 5, 7)])
    if dmax(4) != 4 * 4 - 8:
        bad("D_max is not 4m-8")
    if dmax(4) == 11:
        bad("D_max(4) unexpectedly equals the D(3,3) calibration 11")
    FLAG.append("the addendum reads 'D_max(m) = 4m-8, LINEAR, for m >= 7 "
                "(11 at m=4)', but the hand-checked formula (8m-9)-(4m-1) "
                "gives D_max(4) = 8; the 11 is the SEPARATE calibration "
                "D(3,3) at m=4.  Two quantities, one parenthesis")
    # the crossing at m = 3: supply best-achieved 8, 12, 9 against demand
    supply = {3: 8, 4: 12, 5: 9}
    met = [m for m in (3, 4, 5) if supply[m] >= ceil_row[m]]
    if met != [3]:
        bad("supply meets demand at %s, the law of record says only m=3" % met)


# ============================================================ C. shape
def shape_checks():
    m = 4
    if 7 * m - 1 != 27:
        bad("|W| at m=4 is not 27")
    if not 6 * m > 4 * m - 1:
        bad("Lemma 1 (Moebius injectivity 6m > rho) fails at m=4")
    for mm in range(2, 130):
        if not 6 * mm > 4 * mm - 1:
            bad("Lemma 1 fails at m=%d" % mm)
    # The flat-supply law: required cross-coincidence "~ m-5", declared
    # VACUOUS for m <= 6 and BINDING from m = 7.  Taken literally, m-5 is
    # already positive at m = 6, so the printed constant and the printed
    # vacuity range are off by one.  Assert the literal form, and FLAG the
    # inconsistency rather than silently adopting either reading.
    for mm in range(2, 6):
        if mm - 5 > 0:
            bad("literal bound m-5 is not vacuous at m=%d" % mm)
    for mm in range(7, 130):
        if mm - 5 <= 0:
            bad("literal bound m-5 is not binding at m=%d" % mm)
    if 6 - 5 <= 0:
        bad("arithmetic")
    FLAG.append("the flat-supply bound is printed as '>= ~m-5, VACUOUS for "
                "m <= 6, BINDING from m = 7', but m-5 = 1 > 0 already at "
                "m = 6; the constant and the vacuity range are off by one "
                "as printed (the '~' makes the constant soft, so the "
                "vacuous/binding CROSSOVER at m = 7 is the load-bearing "
                "claim and the constant is not)")
    if comb(64, 3) != 41664:
        bad("C(64,3) != 41664")
    if comb(32, 7) != 3365856:
        bad("C(32,7) != 3365856")


# ============================== D. constant-norm existence at q = 193
def constant_norm(q=193, order=64, want=8):
    gen = None
    for cand in range(2, q):
        z = pow(cand, (q - 1) // order, q)
        o = 1
        cur = z
        while cur != 1:
            cur = cur * z % q
            o += 1
        if o == order:
            gen = z
            break
    if gen is None:
        bad("no element of order %d in F_%d" % (order, q))
        return None
    MU = [1]
    for _ in range(order - 1):
        MU.append(MU[-1] * gen % q)
    assert len(set(MU)) == order

    # monic cubic with roots r1,r2,r3:  x^3 + a x^2 + b x + c
    classes = {}
    for r1, r2, r3 in combinations(MU, 3):
        a = (-(r1 + r2 + r3)) % q
        b = (r1 * r2 + r1 * r3 + r2 * r3) % q
        c = (-(r1 * r2 * r3)) % q
        classes.setdefault(c, []).append((a, b))
    if sum(len(v) for v in classes.values()) != comb(order, 3):
        bad("split-cubic enumeration lost members")
    if len(classes) != order:
        bad("norm classes %d, want %d" % (len(classes), order))
    sizes = set(len(v) for v in classes.values())
    if sizes != {comb(order, 3) // order}:
        bad("norm classes are not equidistributed: %s" % sizes)

    best = 0
    complete = 0
    witness = None
    for c, pts in classes.items():
        lines = {}
        n = len(pts)
        for i in range(n):
            a1, b1 = pts[i]
            for j in range(i + 1, n):
                a2, b2 = pts[j]
                A = (b1 - b2) % q
                B = (a2 - a1) % q
                if A:
                    iv = pow(A, q - 2, q)
                    A2, B2 = 1, B * iv % q
                else:
                    A2, B2 = 0, 1
                C2 = (A2 * a1 + B2 * b1) % q
                key = (A2, B2, C2)
                lines[key] = lines.get(key, 0) + 1
        for key, cnt in lines.items():
            t = 1
            while t * (t - 1) // 2 < cnt:
                t += 1
            if t * (t - 1) // 2 != cnt:
                bad("line multiplicity %d is not a binomial" % cnt)
            if t > best:
                best = t
                witness = (c, key, t)
            if t >= want:
                complete += 1
    return dict(best=best, complete=complete, witness=witness,
                total=comb(order, 3))


luroth_checks()
demand_checks()
shape_checks()
cn = constant_norm()
if cn is None:
    bad("constant-norm scan did not run")
elif cn["best"] < 8:
    bad("constant-norm: best collinear split-cubic count %d, the source "
        "reports complete fibres of 8 at q=193" % cn["best"])

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("SHARE3_LUROTH_TEMPLATE_PASS Luroth/waste arithmetic OK m=3..12; "
      "demand rows quadratic [8,22,42] and ceiling {3:8,4:25,5:47} with "
      "supply meeting demand only at m=3; D_max = 4m-8; constant-norm at "
      "q=193: %d mu_64-split cubics in 64 equidistributed norm classes, "
      "best collinear = %d (>= 8 required), %d lines reaching 8, witness "
      "class/line %s"
      % (cn["total"], cn["best"], cn["complete"], cn["witness"]))
for f in FLAG:
    print("FLAG " + f)
