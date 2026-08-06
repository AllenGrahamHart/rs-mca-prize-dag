#!/usr/bin/env python3
"""Round 20 -- THE TAIL-COUNT CRITERION: verifier.

Usage:  tools/ramguard local -- python3 notes/pilots_20260806/tail_count/verify_tail.py STAGE [STAGE...]

Stages: ctrl ident dist thr prof t2 tr   (or 'all')

Fail-closed: every check goes through CHK(); any FAIL sets the exit code to
1 and the final line reports the tally.  No stage silently skips work: an
unreachable cell must be declared UNREACHED explicitly.
"""

import math
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tc_lib as T                                            # noqa: E402

NPASS = [0]
NFAIL = [0]


def CHK(name, cond, detail=""):
    ok = bool(cond)
    if ok:
        NPASS[0] += 1
    else:
        NFAIL[0] += 1
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  | " + detail) if detail else ""))
    return ok


def head(s):
    print("\n" + "=" * 72 + "\n%s\n" % s + "=" * 72)


# the pre-registered FAMILY A rows (PREREG.md section C)
G = [(17, 2), (113, 1), (241, 1), (97, 2), (353, 2), (673, 2)]
SMALL = [(17, 2), (113, 1), (241, 1), (97, 2)]      # exact-census reachable


# ---------------------------------------------------------------------------
# CTRL -- licensing controls
# ---------------------------------------------------------------------------

def stage_ctrl():
    head("CTRL -- licensing controls (a failure VOIDS the pilot)")
    banked = {17: Fraction(5, 4), 97: None}
    for p, R in SMALL:
        row = T.Row(p, R)
        num, den, W = T.ternary_mass_exact(row)
        Z_exact = Fraction(num, den)
        # independent route: Z_1 = p^{-R} sum_u P(u)
        lt = T.log2_local_table(p)
        tot = 0.0
        for u in T.enumerate_tuples(p, R):
            vals = row.values(u)
            s = 0.0
            for c in vals:
                s += lt[c]
            tot += 2.0 ** s
        Z_char = tot / p ** R
        rel = abs(Z_char - float(Z_exact)) / float(Z_exact)
        CHK("CTRL-1 %s: character form == exact ternary census" % row.tag(),
            rel < 5e-12, "Z_1=%.9f (census %.9f) rel=%.2e"
            % (Z_char, float(Z_exact), rel))
        if p == 17:
            CHK("CTRL-2 G1 reproduces banked Z_1 = 1.25",
                Z_exact == Fraction(5, 4), "got %s" % Z_exact)
        if p == 97:
            CHK("CTRL-2 G4 reproduces banked Z_1 = 9.387207",
                abs(float(Z_exact) - 9.387207) < 5e-7, "got %.6f"
                % float(Z_exact))
        # grid legality
        CHK("CTRL-3 %s: S = 2^{v2(p-1)-1}, 2S a 2-power, 0 not in Lambda"
            % row.tag(),
            row.S == 1 << (T.v2(p - 1) - 1) and 0 not in row.Lam
            and (2 * row.S) & (2 * row.S - 1) == 0,
            "S=%d Lambda=%s" % (row.S, row.Lam[:4]))
    _ = banked


# ---------------------------------------------------------------------------
# IDENT -- P1 (the telescoping) and P4(i) (the c=1 endpoint)
# ---------------------------------------------------------------------------

def stage_ident():
    head("IDENT -- P1: Prop 10 telescopes to log2 P = S - cost")
    for p, R in SMALL:
        row = T.Row(p, R)
        S = row.S
        lt = T.log2_local_table(p)
        dt = T.cost_table(p)
        # log2|2 sin(pi c/p)| for c != 0
        Lsin = [None] + [math.log2(2.0 * abs(math.sin(math.pi * c / p)))
                         for c in range(1, p)]
        inv2 = pow(2, p - 2, p)
        worst_p10 = 0.0
        worst_tel = 0.0
        worst_dlt = 0.0
        for u in T.enumerate_tuples(p, R):
            vals = row.values(u)
            n = [0] * p
            for c in vals:
                n[c] += 1
            direct = sum(lt[c] for c in vals)
            # Prop 10 RHS
            acc = 0.0
            for c in range(1, p):
                acc += (n[c * inv2 % p] - n[c]) * Lsin[c]
            p10 = -S + 2 * n[0] + 2.0 * acc
            # telescoped form
            tel = S - sum(dt[c] for c in vals)
            worst_p10 = max(worst_p10, abs(p10 - direct))
            worst_tel = max(worst_tel, abs(tel - direct))
        # the per-value telescoping algebra: L(2c) - L(c) = log2|2cos(pi c/p)|
        for c in range(1, p):
            lhs = Lsin[2 * c % p] - Lsin[c]
            rhs = math.log2(2.0 * abs(math.cos(math.pi * c / p)))
            worst_dlt = max(worst_dlt, abs(lhs - rhs))
        CHK("P1a %s: Prop 10 RHS == log2 P (all %d tuples)"
            % (row.tag(), p ** R), worst_p10 < 1e-9, "max err %.2e" % worst_p10)
        CHK("P1b %s: S - cost(u) == log2 P (all tuples)" % row.tag(),
            worst_tel < 1e-9, "max err %.2e" % worst_tel)
        CHK("P1c %s: L(2c)-L(c) == log2|2cos(pi c/p)| = 1 - d(c)/2, all c!=0"
            % row.tag(), worst_dlt < 1e-12, "max err %.2e" % worst_dlt)
        # sum_{c!=0} log2|cos(pi c/p)| = -(p-1)
        ssum = sum(math.log2(abs(math.cos(math.pi * c / p)))
                   for c in range(1, p))
        CHK("P1d p=%d: prod_{c!=0}|cos(pi c/p)| = 2^{-(p-1)}" % p,
            abs(ssum + (p - 1)) < 1e-9, "sum=%.10f vs %d" % (ssum, -(p - 1)))

    head("IDENT -- P4(i): |U_1| = 1  (only u=0 attains P = 2^S)")
    for p, R in SMALL:
        row = T.Row(p, R)
        lt = T.log2_local_table(p)
        best, arg = -1e18, None
        nmax = 0
        for u in T.enumerate_tuples(p, R):
            v = sum(lt[c] for c in row.values(u))
            if v > best + 1e-12:
                best, arg, nmax = v, u, 1
            elif abs(v - best) <= 1e-12:
                nmax += 1
        CHK("P4i %s: argmax P is u=0 alone, max log2 P = S" % row.tag(),
            arg == tuple([0] * R) and nmax == 1
            and abs(best - row.S) < 1e-9,
            "argmax=%s count=%d max=%.6f S=%d" % (arg, nmax, best, row.S))


# ---------------------------------------------------------------------------
# DIST -- P2: the exact value-distribution facts
# ---------------------------------------------------------------------------

def stage_dist():
    head("DIST -- P2: marginals, R-wise independence, exact moments")
    for p, R in SMALL:
        row = T.Row(p, R)
        S, P_ = row.S, p ** R
        # (i) each coordinate marginal is EXACTLY uniform (integer check)
        marg = [[0] * p for _ in range(S)]
        energy_tot = 0
        allvals = []
        for u in T.enumerate_tuples(p, R):
            vals = row.values(u)
            allvals.append(vals)
            n = [0] * p
            for s, c in enumerate(vals):
                marg[s][c] += 1
                n[c] += 1
            energy_tot += sum(x * x for x in n)
        okm = all(marg[s][c] == P_ // p for s in range(S) for c in range(p))
        CHK("P2i %s: every coordinate marginal is exactly uniform (p^{R-1})"
            % row.tag(), okm, "p^{R-1}=%d" % (P_ // p))
        # (ii) R-wise independence: every R distinct coordinates joint-uniform
        import itertools
        combos = list(itertools.combinations(range(S), R))
        if len(combos) > 200:
            combos = combos[:200]
        okj = True
        for cmb in combos:
            tab = {}
            for vals in allvals:
                k = tuple(vals[s] for s in cmb)
                tab[k] = tab.get(k, 0) + 1
            if len(tab) != p ** R or any(v != 1 for v in tab.values()):
                okj = False
                break
        CHK("P2ii %s: every R-subset of coordinates is jointly uniform (MDS)"
            % row.tag(), okj, "%d R-subsets tested" % len(combos))
        # (iii) E_u[log2 P] = -S(1-2/p) exactly
        dt = T.cost_table(p)
        mean = sum(S - sum(dt[c] for c in vals) for vals in allvals) / P_
        pred = -S * (1.0 - 2.0 / p)
        CHK("P2iii %s: E_u[log2 P] = -S(1-2/p)" % row.tag(),
            abs(mean - pred) < 1e-9, "measured %.10f predicted %.10f"
            % (mean, pred))
        # (iv) E_u[sum_c n_c^2] = S + S(S-1)/p exactly (INTEGER identity)
        lhs = Fraction(energy_tot, P_)
        rhs = Fraction(S) + Fraction(S * (S - 1), p)
        CHK("P2iv %s: E_u[sum_c n_c^2] = S + S(S-1)/p EXACTLY" % row.tag(),
            lhs == rhs, "%s == %s" % (lhs, rhs))
        # (v) variance additivity for R >= 2
        if R >= 2:
            var = sum((S - sum(dt[c] for c in vals) - mean) ** 2
                      for vals in allvals) / P_
            mu = sum(dt) / p
            vard = sum((x - mu) ** 2 for x in dt) / p
            CHK("P2v %s: Var_u[log2 P] = S Var(d) (R>=2 => pairwise indep)"
                % row.tag(), abs(var - S * vard) < 1e-7,
                "measured %.9f predicted %.9f" % (var, S * vard))


import stages2                                                 # noqa: E402
import t2_stage                                                # noqa: E402

STAGES = {"ctrl": stage_ctrl, "ident": stage_ident, "dist": stage_dist,
          "thr": lambda: stages2.stage_thr(CHK, head),
          "tr": lambda: stages2.stage_tr(CHK, head),
          "prof": lambda: stages2.stage_prof(CHK, head),
          "t2": lambda: t2_stage.run(CHK, head)}


def main():
    args = sys.argv[1:] or ["all"]
    names = list(STAGES) if args == ["all"] else args
    for nm in names:
        if nm not in STAGES:
            print("unknown stage %r" % nm)
            sys.exit(2)
        STAGES[nm]()
    print("\n" + "-" * 72)
    print("TOTAL: %d PASS, %d FAIL" % (NPASS[0], NFAIL[0]))
    sys.exit(1 if NFAIL[0] else 0)


if __name__ == "__main__":
    main()
