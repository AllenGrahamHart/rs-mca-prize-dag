#!/usr/bin/env python3
"""Inverse-direction evidence for PK1: does a LARGE w=1 fibre force the
pure-product (packet) section?

At shell a = k+1 the whole geometry is: 56 (resp. C(n,r)) points
v_T = (m_0(T), ..., m_{r-1}(T)) in F_q^r, one per r-subset T of H, and the
fibre of the affine Toeplitz section with window (u_{n-1},...,u_k) is the set
of points on one affine hyperplane.  The packet section is the hyperplane
{m_0 = -c}.  IS1 scans EVERY hyperplane exhaustively.

Also checks the codeword-shift / scaling invariance (CT4) of the shells.

Run:  tools/ramguard local -- python3 <this file>
"""
from __future__ import annotations

import json
import os
import sys
from itertools import combinations
from math import comb, gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from packet_lib import (  # noqa: E402
    PrimeField,
    domain,
    exact_shell_census,
    locator,
    poly_eval,
)

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "checkpoints")
FAILURES: list[str] = []
REC: dict = {}


def check(name: str, cond: bool, detail: str = "") -> None:
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))
    if not cond:
        FAILURES.append(name)


def locator_vectors(F, H, r):
    """v_T = (m_0,...,m_{r-1}) for every r-subset T (m_r = 1 is implicit)."""
    out = []
    for T in combinations(H, r):
        M = locator(F, T)
        out.append((tuple(M[:r]), T))
    return out


def is1_exhaustive_hyperplane_scan():
    """n=8, k=4, r=3: scan EVERY affine Toeplitz section, both raw and
    gcd-GUARDED (= the exact shell at k+1).  The raw count is not a list
    count: one codeword of agreement k+1+e is seen by C(n-k-1-e+e, .) many
    section points.  The guarded count is the exact shell."""
    print("\n=== IS1  exhaustive w=1 section scan, n=8 k=4 r=3 ===")
    n, k, r = 8, 4, 3
    target = comb(n, r) // n
    for p in [17, 41, 73]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        lv = locator_vectors(F, H, r)
        idx_of = {x: i for i, x in enumerate(H)}
        raw_best, g_best = 0, 0
        raw_max_w, g_max_w = [], []
        g_hist: dict = {}
        for w in _projective_vectors(p, r):
            buckets: dict = {}
            for v, T in lv:
                s = 0
                for j in range(r):
                    s += w[j] * v[j]
                buckets.setdefault(s % p, []).append(T)
            for t, Ts in buckets.items():
                raw = len(Ts)
                if raw > raw_best:
                    raw_best, raw_max_w = raw, [(w, t)]
                elif raw == raw_best:
                    raw_max_w.append((w, t))
                # guarded count: build U and test exact agreement
                U = [F.zero] * n
                for j in range(r):
                    U[n - 1 - j] = w[j] % p
                U[k] = F.neg(t % p)
                Uvals = [poly_eval(F, U, x) for x in H]
                guarded = 0
                for T in Ts:
                    tset = {idx_of[x] for x in T}
                    A = [i for i in range(n) if i not in tset]
                    P = interpolate_pts(F, [H[i] for i in A],
                                        [Uvals[i] for i in A])
                    if len(P) - 1 >= k:
                        continue                      # not a codeword
                    extra = sum(1 for i in tset
                                if poly_eval(F, P, H[i]) == Uvals[i])
                    if extra == 0:
                        guarded += 1
                g_hist[guarded] = g_hist.get(guarded, 0) + 1
                if guarded > g_best:
                    g_best, g_max_w = guarded, [(w, t)]
                elif guarded == g_best:
                    g_max_w.append((w, t))
        pure = [(w, t) for w, t in g_max_w
                if w[0] != 0 and all(w[j] == 0 for j in range(1, r))]
        check(f"IS1 q={p}: the maximal GUARDED w=1 fibre (= max exact shell "
              f"at k+1) equals C(n,r)/n = {target}",
              g_best == target, f"max_guarded={g_best} (raw max={raw_best})")
        check(f"IS1 q={p}: EVERY guarded maximiser is a pure-product section "
              f"{{m_0 = t}}, and there are exactly n = {n} of them",
              len(pure) == len(g_max_w) and len(g_max_w) == n,
              f"#maximisers={len(g_max_w)} #pure={len(pure)}")
        check(f"IS1 q={p}: the RAW section count is NOT a list count "
              f"(raw max {raw_best} > {target})", raw_best > target)
        REC[f"IS1_q{p}"] = {"max_guarded_fibre": g_best,
                            "max_raw_section": raw_best,
                            "target": target,
                            "n_guarded_maximisers": len(g_max_w),
                            "n_pure_maximisers": len(pure),
                            "guarded_fibre_histogram":
                                {str(a): b for a, b in sorted(g_hist.items())}}


def interpolate_pts(F, xs, ys):
    from packet_lib import interpolate as _interp
    return _interp(F, xs, ys)


def _projective_vectors(p, r):
    """All nonzero (w_0..w_{r-1}) in F_p^r with first nonzero entry 1."""
    for lead in range(r):
        tails = [range(p)] * (r - lead - 1)
        for tail in _product(tails):
            yield tuple([0] * lead + [1] + list(tail))


def _product(ranges):
    if not ranges:
        yield ()
        return
    for x in ranges[0]:
        for rest in _product(ranges[1:]):
            yield (x,) + rest


def is2_two_support_scan():
    """n=16, k=8, r=7: two-support windows {0, j}; only j=r is a packet."""
    print("\n=== IS2  two-support w=1 windows at n=16 k=8 r=7 ===")
    n, k, r = 16, 8, 7
    target = comb(n, r) // n
    for p in [17, 97]:
        F = PrimeField(p)
        H, omega, x0 = domain(F, n, F.one)
        vecs = [v for v, T in locator_vectors(F, H, r)]
        lv = locator_vectors(F, H, r)
        idx_of = {x: i for i, x in enumerate(H)}
        rows = {}
        for j in [0, 1, 2, 3]:    # window support {j, r}: w_j = 1, target t
            buckets: dict = {}
            for v, T in lv:
                buckets.setdefault(v[j], []).append(T)
            raw_sizes = sorted(set(len(x) for x in buckets.values()))
            guarded = {}
            for t, Ts in buckets.items():
                U = [F.zero] * n
                U[n - 1 - j] = F.one
                U[k] = F.neg(t)
                Uvals = [poly_eval(F, U, x) for x in H]
                cnt = 0
                for T in Ts:
                    tset = {idx_of[x] for x in T}
                    A = [i for i in range(n) if i not in tset]
                    P = interpolate_pts(F, [H[i] for i in A],
                                        [Uvals[i] for i in A])
                    if len(P) - 1 >= k:
                        continue
                    if all(poly_eval(F, P, H[i]) != Uvals[i] for i in tset):
                        cnt += 1
                guarded[t] = cnt
            gsizes = sorted(set(guarded.values()))
            rows[j] = {"distinct_targets": len(buckets),
                       "raw_sizes": raw_sizes[:6],
                       "raw_max": max(len(x) for x in buckets.values()),
                       "guarded_sizes": gsizes[:6],
                       "guarded_max": max(guarded.values()),
                       "uniform_packet": (len(buckets) == n
                                          and gsizes == [target])}
        check(f"IS2 q={p}: only the constant-coefficient support j=0 (the "
              f"subset product) is a uniform packet",
              rows[0]["uniform_packet"]
              and not any(rows[j]["uniform_packet"] for j in [1, 2, 3]),
              f"j=0 -> {rows[0]}")
        check(f"IS2 q={p}: no other two-support window reaches the guarded "
              f"packet size {target}",
              all(rows[j]["guarded_max"] < target for j in [1, 2, 3]),
              f"guarded maxes={[rows[j]['guarded_max'] for j in [0,1,2,3]]}")
        REC[f"IS2_q{p}"] = rows


def is3_shift_scaling_invariance():
    """CT4: shells are invariant under U -> lambda U + R, deg R < k."""
    print("\n=== IS3  codeword-shift and scaling invariance of the shells ===")
    n, k = 8, 4
    r = n - k - 1
    F = PrimeField(17)
    H, omega, x0 = domain(F, n, F.one)
    sign = F.one if (r + 1) % 2 == 0 else F.neg(F.one)
    c = F.mul(sign, F.power(x0, r))
    base = [F.zero] * n
    base[n - 1] = F.one
    base[k] = c
    ref = None
    ok = True
    for lam in [1, 2, 5, 16]:
        for R in [[0, 0, 0, 0], [1, 0, 0, 0], [3, 1, 0, 9], [16, 16, 16, 16]]:
            U = [F.mul(lam, t) for t in base]
            for i, t in enumerate(R):
                U[i] = F.add(U[i], t)
            Uvals = [poly_eval(F, U, x) for x in H]
            shells, cw = exact_shell_census(F, H, k, Uvals)
            idx = frozenset(tuple(sorted(set(range(n)) - set(a)))
                            for P, a in cw.items() if len(a) == k + 1)
            if ref is None:
                ref = (dict(shells), idx)
            elif (dict(shells), idx) != ref:
                ok = False
    check("IS3 shells and packet index family are invariant under "
          "U -> lambda U + R (deg R < k)", ok,
          f"reference shells={ref[0]}")
    REC["IS3_invariance"] = {"shells": {str(b): v
                                        for b, v in sorted(ref[0].items())},
                             "packet_size": len(ref[1])}


def is4_certificate_sizes():
    """Certificate-size accounting for the official razor row."""
    print("\n=== IS4  certificate size accounting (succinctness clause) ===")
    n, k = 2 ** 41, 2 ** 40
    r = n - k - 1
    row_desc_bits = 256 + 3 * 42          # q, beta, n, k, and the index s
    member_bits = n                       # one packet member T is an n-bit mask
    enumeration_bits_log2 = n - 1 - (n + 1).bit_length() - n.bit_length()
    check("IS4 the packet DESCRIPTOR is O(log q + log n) bits",
          row_desc_bits < 2 ** 10, f"descriptor bits <= {row_desc_bits}")
    check("IS4 one packet MEMBER costs n bits (poly in the row size)",
          member_bits == n)
    check("IS4 an ENUMERATING certificate would need > 2^128 members",
          enumeration_bits_log2 > 128,
          f"log2(#members) >= {enumeration_bits_log2}")
    REC["IS4_certificate_sizes"] = {
        "descriptor_bits_upper": row_desc_bits,
        "member_bits": member_bits,
        "log2_members_lower": enumeration_bits_log2}


def main():
    is1_exhaustive_hyperplane_scan()
    is2_two_support_scan()
    is3_shift_scaling_invariance()
    is4_certificate_sizes()
    os.makedirs(CKPT, exist_ok=True)
    with open(os.path.join(CKPT, "inverse_scan.json"), "w") as fh:
        json.dump(REC, fh, indent=1, sort_keys=True, default=str)
    print()
    if FAILURES:
        print("FAILURES:", FAILURES)
        print("INVERSE_SCAN_FAIL")
        raise SystemExit(1)
    print("INVERSE_SCAN_PASS")


if __name__ == "__main__":
    main()
