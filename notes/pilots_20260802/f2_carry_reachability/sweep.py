#!/usr/bin/env python3
"""F2A.2 carry-reachability sweep.

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_carry_reachability/sweep.py

For every (p, n, c) it records, EXACTLY (integer arithmetic):
  * the per-pair difference multiset delta_i = s_i(+1) - s_i(-1) mod 2p,
  * the reachable-sumset growth curve |S_k| and its covering numbers,
  * the terminal reachable set and its exact subgroup/coset structure,
  * the Myhill-Nerode quotient of the reachable prefix states under the
    REACHABLE continuation set (the true carry-automaton width).

Floats (display only): the L1-normalised carry-DFT mass and the local
contraction-dial statistics 4ab/(a+b)^2.
"""

from __future__ import annotations

import json
import math
import os
import random
import statistics
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from f2model import (  # noqa: E402
    Fp2,
    carry_dft_l1_normalized,
    deltas,
    describe_structure,
    divisors,
    half_flag,
    is_prime,
    local_balance,
    myhill_nerode_classes,
    pair_reps,
    residues,
    sumset_curve,
    suffix_sumsets,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")

P_LO, P_HI = 7, 199
MAX_PAIRS_CURVE = 512      # pairs used for curve / suffix / MN work
CURVE_PREFIX_JSON = 48     # how much of the |S_k| curve to store verbatim


def admissible_orders(p: int) -> list[int]:
    return [n for n in divisors(p * p - 1)
            if n % 2 == 0 and (p - 1) % n != 0]


def pick_orders(p: int) -> list[int]:
    adm = admissible_orders(p)
    if not adm:
        return []
    picks = {adm[0], p + 1, adm[-1]}
    if len(adm) > 2:
        picks.add(adm[len(adm) // 2])
    return sorted(x for x in picks if x in set(adm))


def pick_frequencies(p: int, rng: random.Random) -> list[tuple[str, tuple]]:
    out = [("c_in_Fp(c=1)", (1, 0)),
           ("c_trace_zero(c=w)", (0, 1)),
           ("c=1+w", (1, 1))]
    for i in range(3):
        while True:
            c = (rng.randrange(p), rng.randrange(p))
            if c[1] != 0 and c[0] != 0:
                break
        out.append((f"c_random{i}", c))
    return out


def v2(x: int) -> int:
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k


def analyse(p: int, n: int, F: Fp2, reps, cname: str, c) -> dict:
    two_p = 2 * p
    ds_all = deltas(F, c, reps)
    m_total = len(ds_all)
    ds = ds_all[:MAX_PAIRS_CURVE]

    zero = sum(1 for d in ds_all if d == 0)
    odd = sum(1 for d in ds_all if d % 2 == 1)
    distinct = len(set(ds_all))
    g_all = math.gcd(two_p, *ds_all) if ds_all else two_p

    sizes, S, k_term = sumset_curve(ds, two_p)
    struct = describe_structure(S, two_p)
    k_full = next((k for k, s in enumerate(sizes) if s == two_p), None)

    # reachable-continuation Myhill-Nerode widths
    C = suffix_sumsets(ds, two_p)
    m = len(ds)
    cuts = sorted(set(list(range(0, min(m, 24) + 1))
                      + [m - i for i in range(0, min(m, 24) + 1) if m - i >= 0]
                      + [m * i // 8 for i in range(9)]))
    mn = {}
    Pmask = 1
    prefix_masks = [1]
    from f2model import rot
    full = (1 << two_p) - 1
    for d in ds:
        Pmask |= rot(Pmask, d, two_p, full)
        prefix_masks.append(Pmask)
    for k in cuts:
        mn[k] = myhill_nerode_classes(p, prefix_masks[k], C[k])
    mn_max = max(mn.values())
    mn_argmax = max(mn, key=lambda k: mn[k])

    # order dependence of the covering number
    kfull_orders = []
    for seed in (11, 23, 37):
        shuffled = list(ds_all)
        random.Random(seed).shuffle(shuffled)
        sz, _, _ = sumset_curve(shuffled[:MAX_PAIRS_CURVE], two_p)
        kfull_orders.append(next((k for k, s in enumerate(sz) if s == two_p),
                                 None))

    # contraction dial (display-only floats)
    bals = []
    for y in reps[:MAX_PAIRS_CURVE]:
        sp, sm = residues(F, c, y)
        bals.append(local_balance(p, sp, sm))
    bal_stats = {
        "min": min(bals) if bals else None,
        "mean": statistics.fmean(bals) if bals else None,
        "median": statistics.median(bals) if bals else None,
        "max": max(bals) if bals else None,
        "frac_below_0.5": (sum(1 for b in bals if b < 0.5) / len(bals)
                           if bals else None),
        "frac_below_0.1": (sum(1 for b in bals if b < 0.1) / len(bals)
                           if bals else None),
    }

    return {
        "p": p, "n": n, "c_name": cname, "c": list(c),
        "m_pairs_total": m_total, "m_pairs_used": m,
        "v2_p_minus_1": v2(p - 1), "v2_p_plus_1": v2(p + 1), "v2_n": v2(n),
        "gcd_n_pm1": math.gcd(n, p - 1),
        "n_divides_p_plus_1": (p + 1) % n == 0,
        "delta_zero_count": zero,
        "delta_odd_count": odd,
        "delta_distinct": distinct,
        "delta_gcd_with_2p": g_all,
        "sumset_curve_prefix": sizes[:CURVE_PREFIX_JSON],
        "terminal_size": struct["size"],
        "terminal_index_in_Z2p": struct["index"],
        "terminal_is_subgroup": struct["is_subgroup"],
        "terminal_is_full": struct["is_full"],
        "terminal_elements": struct["elements"],
        "k_terminal": k_term,
        "k_full_2p": k_full,
        "k_full_shuffled": kfull_orders,
        "mn_width_max": mn_max,
        "mn_argmax_cut": mn_argmax,
        "mn_widths": {str(k): v for k, v in sorted(mn.items())},
        "carry_dft_L1_over_2p": carry_dft_l1_normalized(p),
        "balance_stats": bal_stats,
    }


def mode_contraction_sample(p: int, F: Fp2, reps, c, cap: int = 256) -> dict:
    """Per-mode contraction bits: -log2 |M_i(k)|^2/(a_i+b_i)^2, averaged."""
    two_p = 2 * p
    recs = []
    for y in reps[:cap]:
        sp, sm = residues(F, c, y)
        a = 2 * abs(math.cos(math.pi * sp / p))
        b = 2 * abs(math.cos(math.pi * sm / p))
        bal = local_balance(p, sp, sm)
        du = (half_flag(p, sp) - half_flag(p, sm)) % 2
        recs.append((sp, sm, a, b, bal, du))
    per_mode = {}
    for k in range(1, two_p, 2):
        tot = 0.0
        for sp, sm, a, b, bal, du in recs:
            arg = math.pi * k * (sp - sm) / (2 * p) + (math.pi / 2 if du else 0)
            factor = 1.0 - bal * math.sin(arg) ** 2
            factor = max(factor, 1e-300)
            tot += -math.log2(factor)
        per_mode[k] = tot / len(recs) if recs else 0.0
    vals = list(per_mode.values())
    kmin = min(per_mode, key=lambda k: per_mode[k])
    return {
        "pairs_used": len(recs),
        "bits_per_pair_min": min(vals),
        "bits_per_pair_median": statistics.median(vals),
        "bits_per_pair_max": max(vals),
        "worst_mode_k": kmin,
        "worst_mode_is_k_eq_p": kmin == p,
        "modes_with_bits_below_0.01": sum(1 for v in vals if v < 0.01),
        "n_odd_modes": len(vals),
    }


def main() -> None:
    t0 = time.time()
    os.makedirs(OUT, exist_ok=True)
    rows = []
    modes = []
    primes = [q for q in range(P_LO, P_HI + 1) if is_prime(q)]
    mode_sample_p = {31, 61, 101, 151, 199}
    for p in primes:
        F = Fp2.make(p)
        rng = random.Random(1000 + p)
        freqs = pick_frequencies(p, rng)
        for n in pick_orders(p):
            mu = F.subgroup(n)
            reps = pair_reps(F, mu)
            if not reps:
                continue
            for cname, c in freqs:
                rows.append(analyse(p, n, F, reps, cname, c))
            if p in mode_sample_p and n == p + 1:
                for cname, c in freqs:
                    rec = mode_contraction_sample(p, F, reps, c)
                    rec.update({"p": p, "n": n, "c_name": cname,
                                "c": list(c)})
                    modes.append(rec)
        print(f"  p={p} done rows={len(rows)} t={time.time()-t0:.1f}s",
              flush=True)

    with open(os.path.join(OUT, "sweep.json"), "w") as f:
        json.dump({"meta": {"p_range": [P_LO, P_HI],
                            "max_pairs_curve": MAX_PAIRS_CURVE,
                            "rows": len(rows),
                            "seconds": round(time.time() - t0, 1)},
                   "rows": rows}, f, indent=1)
    with open(os.path.join(OUT, "mode_contraction.json"), "w") as f:
        json.dump({"rows": modes}, f, indent=1)
    print(f"F2A2_SWEEP_DONE rows={len(rows)} modes={len(modes)} "
          f"seconds={time.time()-t0:.1f}")


if __name__ == "__main__":
    main()
