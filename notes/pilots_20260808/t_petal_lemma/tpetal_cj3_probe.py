#!/usr/bin/env python3
"""BONUS PROBE (clearly labelled: a probe, not a claim).

Two questions the main pilot raised.

(A) The FPC5 large-source node names a SECOND missing piece:
    "(ii) NO background-guard analogue at M >= 5"
    (critical/nodes/l1_fpc5_large_source_payment/statement.md:33-34).
    But background/nodes/l1_joint_core_background_johnson_bound is
    PROVED and is stated at ARBITRARY support size h, exactly like
    the overlap cap.  Its (CJ2) couples core and background:
        |D_1 cap D_2| + |R_1 cap R_2| <= r = 2d - h,
    and its denominator (CJ3) is
        J_CJ = b d^2 + N u^2 - N b r,      u = ell - s,  s = h - d.
    QUESTION: on the 408 residual rows -- the ones the plain
    Johnson denominator J = d^2 - N r cannot pay -- does J_CJ > 0
    anywhere?  Exact integer arithmetic; both J and J_CJ are
    quadratics in d, so the sign regions are solved exactly rather
    than sampled.

(B) The BRK-DISJ power-control arm did NOT fire.  Claimed reason:
    for a PRIMITIVE member, F cannot vanish at any petal point
    (F(x)=0 with x in petal i forces W(x)=c_i F(x)=0, so (X-x)
    divides gcd(F,W)).  Hence Z(F) is automatically disjoint from
    the petals and the "core disjoint from petals" hypothesis is
    not needed for the overlap cap.  This checks that claim
    exhaustively on the same cells.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import random
import sys
from math import isqrt

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260808/t_petal_lemma")
from fpc5_exact import p7_large_source_sieve            # noqa: E402
from tpetal_refute import members_of                    # noqa: E402


def neg_interval(a, b, c):
    """Exact integer interval [lo,hi] of d where a d^2 + b d + c <= 0.

    a > 0.  Returns None when the quadratic is positive everywhere.
    """
    disc = b * b - 4 * a * c
    if disc < 0:
        return None
    s = isqrt(disc)
    # lo = ceil((-b-s)/(2a)), hi = floor((-b+s)/(2a)); widen by 1 and
    # trim by direct evaluation so no rounding can bias the answer.
    lo = (-b - s) // (2 * a) - 2
    hi = (-b + s) // (2 * a) + 2
    while lo <= hi and a * lo * lo + b * lo + c > 0:
        lo += 1
    while hi >= lo and a * hi * hi + b * hi + c > 0:
        hi -= 1
    return (lo, hi) if lo <= hi else None


def probe_a(k=2 ** 40):
    N = k - 1
    rows = p7_large_source_sieve()
    rescued_rows = 0
    rescued_d = 0
    total_residual_d = 0
    u_nonneg_rows = 0
    samples = []
    for r in rows:
        t, ell = r["t"], r["ell"]
        h = t * ell
        dlo, dhi = r["residual_d_window"]
        total_residual_d += dhi - dlo + 1
        # b is the chart's background capacity: S - M*ell, recomputed.
        rate = int(r["rate"].split("/")[1])
        S = (rate - 1) * k + 1
        b = S - r["M"] * ell
        # u = ell - s = ell - (h - d) = d - (t-1)ell.
        # SELF-CORRECTION: (CJ2) chooses u BACKGROUND agreement points
        # from the b-point background block, so u must satisfy
        # 0 <= u <= b, i.e. (t-1)ell <= d <= (t-1)ell + b.  The first
        # version of this probe imposed only u >= 0 and therefore
        # "rescued" rows with u = 2.8e10 out of a b = 2 background
        # block, which is meaningless.
        umin_d = (t - 1) * ell
        umax_d = (t - 1) * ell + b
        lo = max(dlo, umin_d)
        dhi = min(dhi, umax_d)
        if lo > dhi or b <= 0:
            continue
        u_nonneg_rows += 1
        # J_CJ(d) = (b+N)d^2 - 2N((t-1)ell + b) d + N[(t-1)^2 ell^2 + b t ell]
        A = b + N
        B = -2 * N * ((t - 1) * ell + b)
        Cc = N * ((t - 1) ** 2 * ell ** 2 + b * t * ell)
        bad = neg_interval(A, B, Cc)
        if bad is None:
            good_lo, good_hi = lo, dhi          # J_CJ > 0 on the whole band
        else:
            blo, bhi = bad
            if blo <= lo and bhi >= dhi:
                continue                        # J_CJ <= 0 everywhere here
            good_lo, good_hi = (bhi + 1, dhi) if bhi < dhi else (lo, blo - 1)
            good_lo = max(good_lo, lo)
        cnt = good_hi - good_lo + 1
        if cnt > 0:
            rescued_rows += 1
            rescued_d += cnt
            if len(samples) < 3:
                dv = good_lo
                samples.append({
                    "rate": r["rate"], "M": r["M"], "t": t, "ell": ell,
                    "b": b, "d": dv,
                    "J_plain": dv * dv - N * (2 * dv - h),
                    "J_CJ": A * dv * dv + B * dv + Cc,
                    "u": dv - (t - 1) * ell,
                    "rescued_d_width": cnt})
    return {"residual_rows": len(rows),
            "rows_with_u_ge_0_somewhere": u_nonneg_rows,
            "rows_RESCUED_by_CJ3": rescued_rows,
            "residual_d_values_total": total_residual_d,
            "d_values_rescued_by_CJ3": rescued_d,
            "fraction_of_residual_d_mass_rescued":
                round(rescued_d / total_residual_d, 8)
                if total_residual_d else None,
            "samples": samples}


def probe_b(seed=7, ncfg=60):
    rng = random.Random(seed)
    checked = 0
    members = 0
    bad = []
    for (t, ell, d, q, ncore) in [(4, 1, 3, 13, 7), (4, 1, 3, 11, 5),
                                  (5, 1, 4, 17, 8), (6, 1, 4, 17, 8),
                                  (4, 2, 5, 19, 8), (5, 1, 3, 13, 6)]:
        h = t * ell
        for _ in range(ncfg):
            pts = rng.sample(range(1, q), h + ncore)
            petals = [pts[i * ell:(i + 1) * ell] for i in range(t)]
            petalset = set(p for pet in petals for p in pet)
            # DELIBERATELY let the core swallow petal points
            core = sorted(set(pts[h:]) | set(list(petalset)[:2]))
            labels = rng.sample(range(0, q), t)
            mem, _, cls = members_of(petals, labels, core, d, q, True,
                                     2_000_000)
            if cls.startswith("CLASS-S"):
                continue
            checked += 1
            for f, w, rs in mem:
                members += 1
                if rs & petalset:
                    bad.append({"t": t, "ell": ell, "d": d, "q": q,
                                "petal_roots": sorted(rs & petalset)})
    return {"configs_checked": checked, "primitive_members_seen": members,
            "members_with_a_PETAL_ROOT": len(bad),
            "claim": "primitivity forbids a petal root of F",
            "verdict": "CONFIRMED" if not bad else "REFUTED",
            "counterexamples": bad[:3]}


def main():
    print(json.dumps({"PROBE_A_CJ3_background_guard": probe_a(),
                      "PROBE_B_primitivity_implies_petal_disjoint":
                          probe_b()}, indent=1))


if __name__ == "__main__":
    main()
