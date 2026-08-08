#!/usr/bin/env python3
"""c2pp_gb_probe -- the G-b falsifier of C2''-r3, executed.

A SINGLE-TOWER, MULTI-JUNCTION, SEQUENTIALLY CONDITIONED census of the
coset selection factor

    omega_j := P[state_j in the coset column | null] / P[state_j in the coset column]
               (REPOSE_C2PP_R3_DRAFT.md:133-137)

over a window of CONSECUTIVE junctions of ONE dyadic-descent tower, at a
2-power ladder of q-scales.  No uniform stacking; no single-junction proxy
multiplied by anything.  Every registration is in PREREG.md
"# PILOT REGISTRATIONS" (appended before this file existed).

Stdlib only.  Exact integers throughout.  Run under tools/ramguard.
"""
import json
import math
import os
import sys
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "gb_checkpoint.json")

# ---------------------------------------------------------------- number theory


def is_prime(m):
    if m < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0:
            return m == p
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def least_primitive_root(q):
    """Verbatim convention of m1_dli_m1_tower_census_modal.py:241-252."""
    x, d, fac = q - 1, 2, []
    while d * d <= x:
        while x % d == 0:
            fac.append(d)
            x //= d
        d += 1
    if x > 1:
        fac.append(x)
    fac = sorted(set(fac))
    return next(c for c in range(2, q)
                if all(pow(c, (q - 1) // r, q) != 1 for r in fac))


def get_zeta(q, n):
    """Deterministic primitive n-th root; IDENTICAL convention to the banked
    m1_dli_m1_tower_census_modal.py:255-261."""
    assert (q - 1) % n == 0, f"mu_{n} does not exist in F_{q}"
    z = pow(least_primitive_root(q), (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z


def q_ladder(n, ks):
    """2-power grid (CATCH-Z6): least prime q = 1 mod n with q >= 2^k."""
    out = []
    for k in ks:
        q = ((1 << k) + n - 1) // n * n + 1
        while not is_prime(q):
            q += n
        if q not in out:
            out.append(q)
    return out


# ------------------------------------------------------------- tower structure


def blocks(t):
    """U_j = {odd u : u * 2^j <= t}; verbatim dli_model.py:56-63."""
    out = []
    j = 0
    while 2 ** j <= t:
        out.append([u for u in range(1, t // 2 ** j + 1, 2)])
        j += 1
    return out


def level_vectors(q, n, t, level):
    """Constraint columns of the LEVEL-`level` state m_level.

    P1 LEMMA: the accumulated conditioning N_{>level-1} = {m_level is
    T-null on Z/h_level}, T = floor(t / 2^level), characters zeta_{h}^{r i}.
    Returns (h, T, [v_i]) with v_i in F_q^T.
    """
    h = n // 2 ** level
    T = t // 2 ** level
    zeta_h = pow(get_zeta(q, n), 2 ** level, q)      # exact order h
    assert pow(zeta_h, h, q) == 1 and (h == 1 or pow(zeta_h, h // 2, q) != 1)
    vecs = [tuple(pow(zeta_h, (r * i) % h, q) for r in range(1, T + 1))
            for i in range(h)]
    return h, T, vecs


def junction_vectors(q, n, t, j):
    """Skew columns of JUNCTION j: w_i = (zeta_{h_j}^{u i})_{u in U_j},
    i in Z/h_{j+1}; verbatim structure of dli_model.py:66-72."""
    U = blocks(t)[j]
    hj = n // 2 ** j
    hj1 = n // 2 ** (j + 1)
    zj = pow(get_zeta(q, n), 2 ** j, q)              # exact order h_j
    vecs = [tuple(pow(zj, (u * i) % hj, q) for u in U) for i in range(hj1)]
    return hj1, len(U), vecs


# ------------------------------------------------------------ exact MITM census


def _half(vecs, alpha, q, T):
    """Incremental dict DP over one half; keys are partial sums in F_q^T.
    Dict size caps at min(|alpha|^cells, q^T) -- this is what makes the
    census cost q-INDEPENDENT at small cell counts (PREREG P4)."""
    dp = {(0,) * T: 1}
    for v in vecs:
        nxt = {}
        for key, w in dp.items():
            for val, wt in alpha:
                if val == 0:
                    nk = key
                else:
                    nk = tuple((key[r] + val * v[r]) % q for r in range(T))
                ww = w * wt
                if nk in nxt:
                    nxt[nk] += ww
                else:
                    nxt[nk] = ww
        dp = nxt
    return dp


def mitm_null_count(vecs, alpha, q, T):
    """EXACT integer  sum over assignments (M_i) in alpha^cells of
    prod_i weight(M_i)  subject to  sum_i M_i v_i = 0 in F_q^T."""
    assert T >= 1, "CATCH-19B: no zero-constraint cell is measured"
    mid = len(vecs) // 2
    Lh = _half(vecs[:mid], alpha, q, T)
    Rh = _half(vecs[mid:], alpha, q, T)
    if len(Lh) > len(Rh):
        Lh, Rh = Rh, Lh
    tot = 0
    for key, w in Lh.items():
        wr = Rh.get(tuple((-c) % q for c in key))
        if wr:
            tot += w * wr
    return tot


def binom_alpha(u):
    """The U-induced level alphabet: value M in 0..u with weight C(u,M)."""
    return [(M, math.comb(u, M)) for M in range(u + 1)]


def skew_alpha(u):
    """The U-induced skew alphabet at a junction with u = 2^{j+1}:
    d in -u/2..u/2 with weight C(u, u/2 + d)  (Vandermonde: the number of
    (a,b) in [0,u/2]^2 with a-b = d weighted by C(u/2,a)C(u/2,b))."""
    return [(d, math.comb(u, u // 2 + d))
            for d in range(-(u // 2), u // 2 + 1)]


def flat_alpha(u):
    """Unweighted state alphabet (the banked n_null object)."""
    return [(M, 1) for M in range(u + 1)]


def subset_alpha():
    return [(0, 1), (1, 1)]


# ------------------------------------------------------------------ log helpers


def log2_int(x):
    if x <= 0:
        return float("-inf")
    b = x.bit_length()
    if b <= 900:
        return math.log2(x)
    return (b - 53) + math.log2(x >> (b - 53))


def log2_ratio(a, b):
    return log2_int(a) - log2_int(b)


# ----------------------------------------------------------------- measurements


def measure_row(q, n, t, window, want_r3=True):
    """One tower = one (n, t, q) row.  Returns the per-junction record over
    the CONSECUTIVE window, with genuine sequential conditioning."""
    rec = {"q": q, "n": n, "t": t, "window": list(window), "junctions": []}
    B = blocks(t)
    nlev = len(B)
    # cost guard: MITM half size is (2^lev+1)^ceil(h/2); the SECONDARY R3
    # object needs one level shallower than omega and is dropped (never
    # approximated) when that level exceeds the wall.
    def half_cost(lev):
        h = n // 2 ** lev
        return (2 ** lev + 1) ** ((h + 1) // 2)
    if want_r3 and any(half_cost(j) > 2_000_000 or n // 2 ** j < 2
                       for j in window):
        want_r3 = False
        rec["R3_skipped"] = "level below window exceeds the exact-census wall"
    need = sorted({j + 1 for j in window} |
                  ({j for j in window} if want_r3 else set()))
    Z = {}
    for lev in need:
        h, T, vecs = level_vectors(q, n, t, lev)
        if T < 1 or h < 2:
            Z[lev] = None
            continue
        Z[lev] = mitm_null_count(vecs, binom_alpha(2 ** lev), q, T)
    for j in window:
        lev = j + 1
        h, T, vecs = level_vectors(q, n, t, lev)
        u = 2 ** lev
        assert T >= 1 and h >= 2, "CATCH-19B guard"
        assert j <= nlev - 2, "junction outside the schedule"
        Cj = mitm_null_count(vecs, subset_alpha(), q, T)          # coset census
        Cj_w = mitm_null_count(vecs, [(0, 1), (u, 1)], q, T)      # guard
        assert Cj == Cj_w, "coset column: {0,u} census != subset census"
        Zj = Z[lev]
        assert Zj >= 1 and Cj >= 1, "trivial solution missing -- machinery bug"
        # omega_j = P[COSET|null]/P[COSET] = (C/2^h)/(Z/2^n)   (Bayes, PREREG P2)
        lw = log2_ratio(Cj, Zj) + (n - h)
        # exactness guard: the two orderings of the same ratio agree
        alt = (log2_int(Cj) - h) - (log2_int(Zj) - n)
        assert abs(lw - alt) < 1e-9, "Bayes identity guard tripped"
        rec["junctions"].append({
            "j": j, "h": h, "T": T, "u": u, "L_j": len(B[j]),
            "C_j": Cj, "Z_j": Zj,
            "log2_omega": lw,
            "ceiling_bits": n - h,
            "at_ceiling": Cj == Zj,
            "P_cos_log2": h - n,
            "P_nul_log2": log2_int(Zj) - n,
        })
    rec["Sigma_W"] = sum(x["log2_omega"] for x in rec["junctions"])
    rec["ceiling_Sigma"] = sum(x["ceiling_bits"] for x in rec["junctions"])
    if want_r3 and all(Z.get(j) for j in window):
        r3 = 0.0
        terms = []
        ok = True
        for j in window:
            if Z.get(j) is None or Z.get(j + 1) is None:
                ok = False
                break
            hj1, Lj, wv = junction_vectors(q, n, t, j)
            Pblk = mitm_null_count(wv, skew_alpha(2 ** (j + 1)), q, Lj)
            # E[rho_j|null]/E[rho_j] = (P_nul(j-1)/P_nul(j)) / Pblk_j
            term = (log2_ratio(Z[j], Z[j + 1])
                    - (log2_int(Pblk) - n))
            terms.append({"j": j, "Pblk_count": Pblk, "term_bits": term})
            r3 += term
        if ok:
            rec["R3_terms"] = terms
            rec["R3_W"] = r3
    return rec


BANKED_F2B_NULL = {                     # m1_dli_m1_tower_census_modal.py:192-201
    (2, 97): 443841, (2, 193): 223041, (2, 8353): 10881, (2, 32801): 7713,
    (3, 97): 443841, (3, 193): 223041, (4, 97): 4369, (4, 193): 1137,
}


def positive_control():
    """PR6, GATING: reproduce the banked n=32 null-state counts exactly."""
    out = []
    ok = True
    for (t, q), want in sorted(BANKED_F2B_NULL.items()):
        h, T, vecs = level_vectors(q, 32, t, 1)
        got = mitm_null_count(vecs, flat_alpha(2), q, T)
        out.append({"t": t, "q": q, "want": want, "got": got,
                    "ok": got == want})
        ok &= got == want
    return ok, out


# ------------------------------------------------------------------ entry point


CELLS = {
    # --- depth cells (PREREG P5 fallback ladder) ---------------------------
    "L0": {"n": 32, "t": 16, "window": [0, 1, 2, 3],
           "ks": [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32]},
    "L1": {"n": 32, "t": 8, "window": [0, 1, 2],
           "ks": [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32]},
    "L2": {"n": 64, "t": 32, "window": [1, 2, 3, 4],
           "ks": [7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32]},
    "L4": {"n": 128, "t": 64, "window": [3, 4, 5],
           "ks": [8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24, 28, 32]},
    # --- q-SENSITIVITY CONTROLS: cells whose ladder CROSSES the balance
    # point log2 q = n/t (PREREG D-4).  These decide whether a flat
    # Sigma_W is SATURATION or a q-blind functional.  Shallow by
    # construction: sub-balance and depth are not simultaneously
    # reachable (see the second wall in the report).
    "S1": {"n": 32, "t": 2, "window": [0],
           "ks": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 24]},
    "S2": {"n": 32, "t": 4, "window": [0, 1],
           "ks": [6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24]},
    "S3": {"n": 64, "t": 8, "window": [1, 2],
           "ks": [7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24]},
    "S4": {"n": 64, "t": 4, "window": [1],
           "ks": [7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 24]},
}


def load_ckpt():
    if os.path.exists(CKPT):
        with open(CKPT) as fh:
            return json.load(fh)
    return {"control": None, "rows": {}}


def save_ckpt(st):
    tmp = CKPT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(st, fh)
    os.replace(tmp, CKPT)


def main(argv):
    cells = argv[1:] or ["L0"]
    st = load_ckpt()
    if st["control"] is None:
        ok, rows = positive_control()
        st["control"] = {"ok": ok, "rows": rows}
        save_ckpt(st)
    print("POSITIVE CONTROL (PR6, gating): "
          f"{'PASS' if st['control']['ok'] else 'FAIL'}")
    for r in st["control"]["rows"]:
        print(f"   n=32 t={r['t']:>2} q={r['q']:>6}  n_null want={r['want']:>7}"
              f"  got={r['got']:>7}  {'ok' if r['ok'] else '*** MISMATCH ***'}")
    if not st["control"]["ok"]:
        raise SystemExit("PR6 FAILED -- no G-b read is taken.")
    for cell in cells:
        spec = CELLS[cell]
        n, t, W = spec["n"], spec["t"], spec["window"]
        qs = q_ladder(n, spec["ks"])
        print(f"\n{'=' * 72}\nCELL {cell}: n={n} t={t} window={W} "
              f"(J={len(W)} consecutive junctions), {len(qs)} q-scales\n"
              f"  q ladder: {qs}\n{'=' * 72}")
        for q in qs:
            key = f"{cell}|{q}"
            if key in st["rows"]:
                continue
            rec = measure_row(q, n, t, W)
            st["rows"][key] = rec
            save_ckpt(st)
            js = "  ".join(f"j={x['j']}:{x['log2_omega']:.4f}"
                           for x in rec["junctions"])
            cz = " ".join(f"[C{x['j']}={x['C_j']},Z{x['j']}={x['Z_j']}]"
                          for x in rec["junctions"])
            print(f"  q={q:<12} log2q={math.log2(q):6.2f} bal={n / t:5.1f}  {js}"
                  f"   Sigma_W={rec['Sigma_W']:9.4f}"
                  + (f"  R3_W={rec['R3_W']:9.4f}" if "R3_W" in rec else "")
                  + f"\n      {cz}")
    with open(os.path.join(HERE, "gb_results.json"), "w") as fh:
        json.dump(st, fh, indent=1)
    print("\nwritten: gb_results.json")


if __name__ == "__main__":
    main(sys.argv)
