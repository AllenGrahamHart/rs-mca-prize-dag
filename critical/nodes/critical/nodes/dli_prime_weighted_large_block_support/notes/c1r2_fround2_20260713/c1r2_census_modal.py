#!/usr/bin/env python3
"""C1' F-ROUND 2 census (runs on Modal via tools/modal_run_script.py, single
2CPU/16GiB/270s worker). RAW ledger, schedule r2 (level L, odd moments
1,3,...,2L-1). Exact-rational verdict path.

MODES (argv):
  scan  L Qmax [BAR]   : exact (E-1)/r for all primes q=1 mod 2N up to Qmax at
                         level L (cheap A_total DP). (E-1)/r is an EXACT upper
                         bound on K' (W_cl>=0). Prints every row with
                         (E-1)/r >= BAR (default 1e-3) + top-25 + candidates
                         (>=1) + max. No orbit enumeration.
  wcl   L q1,q2,...    : exact W_cl (primitive signed-shift orbit ledger,
                         weights L+1..L+5) + E-1 + r + K' + kill verdict for the
                         listed q. Includes q=7937 positive control (L=1) and
                         the W_cl:=0 mutation control.

Enumerator conventions REUSED VERBATIM from
critical/nodes/dli_prime_weighted_large_block_support/notes/
m2_c1prime_level_scaled_modal.py (primitive_root, orbit_key over 2N signed
shifts, primitive_orbit_count) and verify_m2_c1prime_result.py (K' definition,
kill test). A_total DP is the summed-over-k signed_all_census marginal.
"""
from __future__ import annotations
import itertools
import sys
from fractions import Fraction
import numpy as np

N = 32
NPRIME = 2 * N            # 64  (n')
LIT_KILL = Fraction(4)    # E-1 > 4 r (1+W_cl)  <=>  K' > 4   (M2 verbatim)
AMBER = Fraction(1)       # stricter watch line (see falsifiers doc)


# ---- field helpers (verbatim shape from m2 script) ----
def primitive_root(q):
    remaining = q - 1
    factors = set()
    d = 2
    while d * d <= remaining:
        while remaining % d == 0:
            factors.add(d); remaining //= d
        d += 1
    if remaining > 1:
        factors.add(remaining)
    c = 2
    while any(pow(c, (q - 1) // f, q) == 1 for f in factors):
        c += 1
    return c


def omega_of(q):
    assert (q - 1) % NPRIME == 0, f"q={q} not 1 mod {NPRIME}"
    w = pow(primitive_root(q), (q - 1) // NPRIME, q)
    assert pow(w, NPRIME, q) == 1 and pow(w, NPRIME // 2, q) != 1
    return w


# ---- exact E via A_total DP (summed-over-k signed_all_census marginal) ----
def a_total(q, L):
    w = omega_of(q)
    dp = np.zeros((q,) * L, dtype=np.int64)
    dp[(0,) * L] = 1
    axes = tuple(range(L))
    for i in range(N):
        vp = tuple(pow(w, ((2 * ell - 1) * i) % NPRIME, q) for ell in range(1, L + 1))
        vm = tuple((q - x) % q for x in vp)
        nd = 2 * dp + np.roll(dp, vp, axis=axes) + np.roll(dp, vm, axis=axes)
        assert int(nd.max()) < (1 << 62), f"int64 headroom guard tripped q={q} L={L}"
        dp = nd
    return int(dp[(0,) * L])


def e_minus_1(q, L):
    return Fraction(q ** L * a_total(q, L), 4 ** N) - 1


def r_of(q, L):
    return Fraction(q ** L, 2 ** N)


# ---- W_cl: raw primitive signed-shift orbit ledger (verbatim from m2) ----
def orbit_key(vector):
    best = None
    for shift in range(NPRIME):
        moved = [0] * N
        for exponent, coefficient in enumerate(vector):
            if coefficient == 0:
                continue
            target = (exponent + shift) % NPRIME
            if target >= N:
                moved[target - N] -= coefficient
            else:
                moved[target] += coefficient
        key = tuple(moved)
        if best is None or key < best:
            best = key
    return best


def primitive_orbit_count(q, level, weight):
    omega = omega_of(q)
    odd_powers = [
        np.array([pow(omega, (2 * ell - 1) * e, q) for e in range(N)], dtype=np.int64)
        for ell in range(1, level + 1)
    ]
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    combos = itertools.combinations(range(N), weight)
    reps = set()
    chunk = 100_000
    while True:
        block = list(itertools.islice(combos, chunk))
        if not block:
            break
        supports = np.asarray(block, dtype=np.int64)
        hit = np.ones((len(supports), len(signs)), dtype=bool)
        for powers in odd_powers:
            hit &= (powers[supports] @ signs.T) % q == 0
        for si, gi in np.argwhere(hit):
            support = tuple(int(v) for v in supports[si])
            signed = tuple(int(v) for v in signs[gi])
            primitive = True
            for mask in range(1, (1 << weight) - 1):
                if all(
                    sum(signed[k] * pow(omega, (2 * ell - 1) * support[k], q)
                        for k in range(weight) if (mask >> k) & 1) % q != 0
                    for ell in range(1, level + 1)
                ):
                    continue
                if all(
                    sum(signed[k] * pow(omega, (2 * ell - 1) * support[k], q)
                        for k in range(weight) if (mask >> k) & 1) % q == 0
                    for ell in range(1, level + 1)
                ):
                    primitive = False
                    break
            if not primitive:
                continue
            vec = [0] * N
            for e, c in zip(support, signed):
                vec[e] = c
            reps.add(orbit_key(tuple(vec)))
    return len(reps)


def w_cl(q, L):
    counts = {w: primitive_orbit_count(q, L, w) for w in range(L + 1, L + 6)}
    ledger = sum(Fraction(counts[w] * NPRIME, 2 ** w) for w in counts)
    return ledger, counts


# ---- prime sieve for q = 1 mod 2N ----
def primes_1_mod_np(Qmax):
    sieve = bytearray([1]) * (Qmax + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(Qmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [q for q in range(1, Qmax + 1, NPRIME) if q <= Qmax and sieve[q]]


def check_row(q, L):
    """Full exact evaluation of one row; returns dict."""
    em1 = e_minus_1(q, L)
    r = r_of(q, L)
    ledger, counts = w_cl(q, L)
    kprime = em1 / (r * (1 + ledger))
    lit = em1 > LIT_KILL * r * (1 + ledger)      # K' > 4
    amb = kprime >= AMBER                          # K' >= 1
    return dict(q=q, L=L, em1=em1, r=r, ledger=ledger, counts=counts,
                kprime=kprime, lit=lit, amb=amb)


def fmt(fr):
    return f"{fr.numerator}/{fr.denominator}"


def do_scan(L, Qmax, bar):
    ps = primes_1_mod_np(Qmax)
    # in-hypothesis: 2^N >= q^L  and N >= 16 L
    cap = 2 ** (N // L)   # q^L <= 2^N  => q <= 2^(N/L)
    ps = [q for q in ps if q <= cap]
    assert N >= 16 * L, f"N>=16L violated at L={L}"
    assert ps, "NONEMPTINESS: no primes in scope"
    rows = []
    for q in ps:
        em1 = e_minus_1(q, L)
        ratio = em1 / r_of(q, L)     # exact (E-1)/r  = K' upper bound
        rows.append((q, em1, ratio))
    rows.sort(key=lambda t: t[2], reverse=True)
    print(f"# SCAN L={L}  primes(q=1 mod {NPRIME}, q<=min({Qmax},2^{N}/{L}-cap={cap}))={len(ps)}")
    print(f"# (E-1)/r is an EXACT upper bound on K' (W_cl>=0). LITERAL kill needs (E-1)/r>4; amber needs >=1.")
    over1 = [t for t in rows if t[2] >= 1]
    over4 = [t for t in rows if t[2] >= 4]
    print(f"# rows with (E-1)/r>=1 (amber-relevant): {len(over1)}   >=4 (literal-relevant): {len(over4)}")
    print("# --- all rows with (E-1)/r >= %g ---" % bar)
    shown = [t for t in rows if float(t[2]) >= bar]
    for q, em1, ratio in shown[:200]:
        print(f"L={L} q={q:>7} (E-1)/r={float(ratio):.6f}  E-1={fmt(em1)}")
    print("# --- top 25 by (E-1)/r ---")
    for q, em1, ratio in rows[:25]:
        print(f"TOP L={L} q={q:>7} (E-1)/r={float(ratio):.6f}")
    qmax, _, rmax = rows[0]
    print(f"# MAX (E-1)/r at L={L}: q={qmax} ratio={float(rmax):.6f} (K'<= this)")
    print("# CANDIDATES (need W_cl):", ",".join(str(t[0]) for t in over1) or "(none>=1)")
    # also always flag near-amber for the record
    near = [t for t in rows if 0.1 <= float(t[2]) < 1]
    print("# NEAR (0.1<=(E-1)/r<1):", ",".join(str(t[0]) for t in near) or "(none)")


def do_wcl(L, qs):
    worst = None
    for q in qs:
        row = check_row(q, L)
        verdict = "LITERAL-KILL" if row["lit"] else ("AMBER" if row["amb"] else "survives")
        print(f"L={L} q={q:>7}: K'={float(row['kprime']):.9f} "
              f"W_cl={fmt(row['ledger'])} orbits={row['counts']} "
              f"(E-1)/r={float(row['em1']/row['r']):.4f} -> {verdict}")
        print(f"      exact E-1={fmt(row['em1'])}  r={fmt(row['r'])}  "
              f"K'={fmt(row['kprime'])}")
        if worst is None or row["kprime"] > worst[0]:
            worst = (row["kprime"], q, row)
    # positive control (L=1, q=7937): K' = 15584479363607/... /(r*237)
    if L == 1 and 7937 in qs:
        pc = check_row(7937, 1)
        assert pc["counts"] == {2: 0, 3: 2, 4: 8, 5: 31, 6: 126}, \
            f"POSCTRL orbit mismatch: {pc['counts']}"
        assert pc["ledger"] == Fraction(236), f"POSCTRL W_cl!=236: {pc['ledger']}"
        assert pc["em1"] == Fraction(15584479363607, 144115188075855872), \
            f"POSCTRL E-1 mismatch: {fmt(pc['em1'])}"
        assert abs(float(pc["kprime"]) - 0.246909432) < 1e-8, \
            f"POSCTRL K' mismatch: {float(pc['kprime'])}"
        print("POSITIVE CONTROL PASS: L=1 q=7937 raw-ledger K'=0.246909432, "
              "W_cl=236, orbits+E-1 exact.")
    # mutation control: delete the ledger at q=7937 => must fire literal kill
    if L == 1 and 7937 in qs:
        pc = check_row(7937, 1)
        k_nol = pc["em1"] / (pc["r"] * (1 + 0))       # W_cl := 0
        fired = pc["em1"] > LIT_KILL * pc["r"] * (1 + 0)
        assert fired and k_nol > 4, "MUTATION CONTROL FAILED: W_cl=0 did not fire kill"
        print(f"MUTATION CONTROL PASS: q=7937 with W_cl:=0 gives K'={float(k_nol):.4f}"
              f">4 => KILL fires (ledger is load-bearing, kill detector works).")
    if worst:
        w = worst[2]
        print(f"# WORST K' in this wcl batch: q={worst[1]} K'={float(worst[0]):.9f} "
              f"({'LITERAL-KILL' if w['lit'] else 'AMBER' if w['amb'] else 'survives'})")


def main():
    mode = sys.argv[1]
    if mode == "scan":
        L = int(sys.argv[2]); Qmax = int(sys.argv[3])
        bar = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-3
        do_scan(L, Qmax, bar)
    elif mode == "wcl":
        L = int(sys.argv[2])
        qs = [int(x) for x in sys.argv[3].split(",") if x]
        do_wcl(L, qs)
    else:
        raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    main()
