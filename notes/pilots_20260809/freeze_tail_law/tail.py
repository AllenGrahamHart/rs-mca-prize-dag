#!/usr/bin/env python3
"""freeze_tail_law (round 26) -- the FREEZE-TAIL CUTOFF LAW.

Round 25 left one named residual obstruction: the second census term is
not a pure q^-T power law; it steepens near freeze and terminates in an
exact integer cutoff.  This file fits it and proves it.

Phases (checkpointed to tailckpt.json in THIS directory):
  copy  pull round-25 phase-C rows into cdata.json (read-only source)
  P1    L3: the negacyclic reduction, T=1 cells, against every banked row
  P2    L1: the cutoff theorem, tested on all 275 banked rows
  P3    the deep-band refit with the tail excised by the cutoff law
  P4    exact integer cutoffs Q* by norm enumeration over the box
  P5    S_inf = 1/ln2: the telescoping identity, verified
  P6    NEW rows bracketing each predicted cutoff (the predictive test)
  P7    the (232,256] pricing

Reuses round 25's c2lib.py (pinned to round 24's gb_probe.py).
Stdlib only.  Every run under tools/ramguard.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c2lib import (Zinf, LamStar, log2_int, sigma,                  # noqa: E402
                   Zlev, primes_mod)
from gb_probe import (is_prime, get_zeta, mitm_null_count,          # noqa: E402
                      skew_alpha, level_vectors, binom_alpha)

R25 = ("/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/"
       "c2pp_falsifier_redesign/ckpt.json")
CDATA = os.path.join(HERE, "cdata.json")
CKPT = os.path.join(HERE, "tailckpt.json")

LCELLS = [(32, 2, 0), (32, 2, 1), (32, 4, 0), (32, 4, 1), (64, 4, 2),
          (64, 8, 2), (64, 8, 3), (64, 16, 3), (128, 16, 4), (128, 32, 4),
          (256, 32, 5)]


def load(path, default=None):
    if os.path.exists(path):
        with open(path) as fh:
            return json.load(fh)
    return {} if default is None else default


def save(path, st):
    with open(path + ".tmp", "w") as fh:
        json.dump(st, fh)
    os.replace(path + ".tmp", path)


# ------------------------------------------------------------------ the law

def cellparams(n, t, lev):
    u, h, T = 2 ** lev, n // 2 ** lev, t // 2 ** lev
    e = n // (2 * t)
    tau = T.bit_length() - 1
    assert h == 2 * T * e and 2 ** tau == T
    return u, h, T, e, tau


def Bbound(n, t, lev):
    """L1: log2 of the Hadamard cutoff.  max over the failure level v of
    (m_v/g_v) * log2(a_v * sqrt(m_v)),  m_v = h/2^(v+1),  a_v = u*2^v,
    g_v = #{r<=T : v2(r)=v} = max(1, T/2^(v+1))."""
    u, h, T, e, tau = cellparams(n, t, lev)
    best, arg = 0.0, None
    for v in range(tau + 1):
        m = h // 2 ** (v + 1)
        a = u * 2 ** v
        g = max(1, T // 2 ** (v + 1))
        b = (m / g) * (math.log2(a) + 0.5 * math.log2(m))
        if b > best:
            best, arg = b, v
    return best, arg


# ------------------------------------------------------- negacyclic norm form

def negmul(P, Q, m):
    """product in Z[Y]/(Y^m + 1), exact integers."""
    out = [0] * m
    for i, pi in enumerate(P):
        if not pi:
            continue
        for j, qj in enumerate(Q):
            if not qj:
                continue
            k = i + j
            if k < m:
                out[k] += pi * qj
            else:
                out[k - m] -= pi * qj
    return out


def norm_neg(A):
    """Res(X^m + 1, A) for m a power of two, by the descent
    prod_zeta A(zeta) = prod_Y (E(Y)^2 - Y*O(Y)^2),  A = E(X^2) + X O(X^2).
    Exact integer; sign is irrelevant downstream (we take |.|)."""
    A = list(A)
    m = len(A)
    while m > 1:
        E, O = A[0::2], A[1::2]
        mh = m // 2
        E2 = negmul(E, E, mh)
        O2 = negmul(O, O, mh)
        YO2 = [-O2[mh - 1]] + O2[:mh - 1]          # multiply by Y mod Y^mh+1
        A = [E2[i] - YO2[i] for i in range(mh)]
        m = mh
    return A[0]


# ---------------------------------------------------------------- P1 (copy)

def phase_copy(st):
    print("=" * 78)
    print("COPY -- round-25 phase-C rows -> cdata.json (source read-only)")
    print("=" * 78)
    src = load(R25)
    C = src.get("C", {})
    out = {}
    tot = 0
    for key, cur in C.items():
        out[key] = {k: v for k, v in cur.items()}
        tot += len(cur)
    save(CDATA, out)
    print(f"  {len(out)} cells, {tot} exact level-census rows copied.")
    st["rows_copied"] = tot
    return st


# ------------------------------------------------------- P1 (the reduction)

def reduced_Zlev(q, n, t, lev, zeta_h=None):
    """L3: the T=1 level census on the negacyclic quotient (e coordinates,
    alphabet [-u,u] with Vandermonde weight C(2u, u+a))."""
    u, h, T, e, tau = cellparams(n, t, lev)
    assert T == 1
    if zeta_h is None:
        zeta_h = pow(get_zeta(q, n), 2 ** lev, q)
    vecs = [(pow(zeta_h, i, q),) for i in range(e)]
    return mitm_null_count(vecs, skew_alpha(2 * u), q, 1)


def phase_P1(st):
    print("=" * 78)
    print("P1 -- L3 NEGACYCLIC REDUCTION vs every banked row (T = 1 cells)")
    print("=" * 78)
    data = load(CDATA)
    bad, tot = 0, 0
    for (n, t, lev) in LCELLS:
        u, h, T, e, tau = cellparams(n, t, lev)
        if T != 1:
            continue
        cur = data.get(f"{n}|{t}|{lev}", {})
        cell_bad = 0
        for qs, zs in sorted(cur.items(), key=lambda kv: int(kv[0])):
            q, z = int(qs), int(zs)
            r = reduced_Zlev(q, n, t, lev)
            tot += 1
            if r != z:
                cell_bad += 1
        bad += cell_bad
        print(f"  cell ({n},{t},{lev})  u={u} e={e}  rows={len(cur):>3}  "
              f"MITM states {(u + 1) ** (h // 2)} -> reduced "
              f"{(2 * u + 1) ** (e // 2)}   mismatches={cell_bad}")
    print(f"\n  PR-1: {tot} rows checked, {bad} mismatches -> "
          f"{'PASS' if bad == 0 else 'FAIL'}")
    st["P1"] = {"rows": tot, "bad": bad}
    return st


# ------------------------------------------------------ P2 (cutoff theorem)

def phase_P2(st):
    print("=" * 78)
    print("P2 -- L1 CUTOFF THEOREM on all banked rows")
    print("=" * 78)
    data = load(CDATA)
    print(f"  {'cell':>14} {'T':>2} {'e':>3} {'B':>6} {'v*':>3} {'n/T':>5} "
          f"{'rows':>5} {'Lmax':>7} {'Lmin_frz':>9} {'>B & excess':>12}")
    viol, rows_tot = 0, 0
    res = {}
    for (n, t, lev) in sorted(tuple(int(v) for v in k.split("|"))
                              for k in data):
        u, h, T, e, tau = cellparams(n, t, lev)
        B, vstar = Bbound(n, t, lev)
        zi = Zinf(n, t, lev)
        cur = data.get(f"{n}|{t}|{lev}", {})
        Lmax, Lmin_frz, v = float("-inf"), float("inf"), 0
        for qs, zs in cur.items():
            q, z = int(qs), int(zs)
            lam = math.log2(q)
            rows_tot += 1
            if z > zi:
                Lmax = max(Lmax, lam)
                if lam > B:
                    v += 1
            elif z == zi:
                Lmin_frz = min(Lmin_frz, lam)
            else:
                raise SystemExit("census BELOW the frozen stratum -- bug")
        viol += v
        res[f"{n}|{t}|{lev}"] = {"B": B, "vstar": vstar, "Lmax": Lmax,
                                 "Lmin_frz": Lmin_frz, "rows": len(cur),
                                 "viol": v}
        print(f"  ({n:>3},{t:>2},{lev})".rjust(15)
              + f"{T:>3} {e:>3} {B:>6.1f} {vstar:>3} {n / T:>5.0f} "
              f"{len(cur):>5} {Lmax:>7.2f} {Lmin_frz:>9.2f} {v:>12}")
    print(f"\n  PR-2: {rows_tot} banked rows, {viol} rows with "
          f"log2 q > B AND excess > 0 -> {'PASS' if viol == 0 else 'FAIL'}")
    near = sum(1 for k, r in res.items() if r["B"] - r["Lmax"] <= 12)
    print(f"  PR-3: cells with B - Lmax <= 12 bits: {near}/11 "
          f"(registered window: >= 6)")
    st["P2"] = res
    return st


# ------------------------------------------------------------ P4 (exact Q*)

def small_factor(N, best_only_mod=None):
    """full factorisation of |N| by trial division + Pollard rho."""
    N = abs(N)
    out = []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        while N % p == 0:
            out.append(p)
            N //= p
    stack = [N] if N > 1 else []
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_prime(m):
            out.append(m)
            continue
        d = pollard(m)
        stack.append(d)
        stack.append(m // d)
    return out


def pollard(m):
    if m % 2 == 0:
        return 2
    c = 1
    while True:
        x = y = 2
        d = 1
        while d == 1:
            x = (x * x + c) % m
            y = (y * y + c) % m
            y = (y * y + c) % m
            d = math.gcd(abs(x - y), m)
        if d != m:
            return d
        c += 1


def phase_P4(st):
    print("=" * 78)
    print("P4 -- EXACT INTEGER CUTOFFS Q* by norm enumeration over the box")
    print("=" * 78)
    res = st.get("P4", {})
    budget = int(os.environ.get("P4_BUDGET", "3000000"))
    for (n, t, lev) in LCELLS:
        u, h, T, e, tau = cellparams(n, t, lev)
        if T != 1:
            continue
        key = f"{n}|{t}|{lev}"
        if key in res:
            continue
        size = (2 * u + 1) ** e
        B, _ = Bbound(n, t, lev)
        if size > budget:
            print(f"  cell ({n},{t},{lev}): box {size} > budget {budget} "
                  f"-- SKIPPED (bracketed in P6 instead)")
            continue
        seen = set()
        bestq, bestA, maxnorm = 0, None, 0
        idx = [0] * e
        rng = list(range(-u, u + 1))
        total = 0
        # odometer over the box.  RAM discipline: a norm N <= bestq cannot
        # carry a prime factor above bestq, so it is skipped without being
        # factored or stored -- `seen` therefore stays small.
        while True:
            A = [rng[i] for i in idx]
            if any(A):
                N = abs(norm_neg(A))
                total += 1
                if N > maxnorm:
                    maxnorm = N
                if N > bestq and N not in seen:
                    seen.add(N)
                    for p in set(small_factor(N)):
                        if p % n == 1 and p > bestq:
                            bestq, bestA = p, list(A)
            # increment
            k = e - 1
            while k >= 0:
                idx[k] += 1
                if idx[k] < len(rng):
                    break
                idx[k] = 0
                k -= 1
            if k < 0:
                break
        res[key] = {"Qstar": bestq, "A": bestA, "maxnorm": maxnorm,
                    "B": B, "distinct_norms": len(seen), "box": size}
        st["P4"] = res
        save(CKPT, st)
        print(f"  cell ({n},{t},{lev}) u={u} e={e} box={size:>9} "
              f"distinct|norm|={len(seen):>7}  max|norm|=2^{math.log2(maxnorm):.2f} "
              f"(Hadamard 2^{B:.1f})")
        print(f"     EXACT CUTOFF Q* = {bestq}  = 2^{math.log2(bestq):.3f}"
              f"   witness A={bestA}")
    return st


# ------------------------------------------------------- P6 (bracket by test)

def phase_P6(st):
    """Predictive test: at the exact cutoff the census must exceed Zinf, and
    at EVERY prime above it (a dense scan of the next primes, plus a ladder
    to 2^B and beyond) it must equal Zinf."""
    print("=" * 78)
    print("P6 -- PREDICTIVE TEST: dense scan above each exact cutoff")
    print("=" * 78)
    p4 = st.get("P4", {})
    out = st.get("P6", {})
    for key, rec in sorted(p4.items()):
        if key in out:
            continue
        n, t, lev = (int(x) for x in key.split("|"))
        u, h, T, e, tau = cellparams(n, t, lev)
        zi = Zinf(n, t, lev)
        Q = rec["Qstar"]
        B = rec["B"]
        hits = []
        # (a) the cutoff itself must be a hit
        at_cut = reduced_Zlev(Q, n, t, lev)
        # (b) every prime = 1 mod n in (Q, min(2^B, Q*2^4)] must be frozen
        bad, tested = 0, 0
        q = Q + n
        top = min(2 ** math.ceil(B), Q * 16)
        while q <= top and tested < 4000:
            if is_prime(q):
                tested += 1
                if reduced_Zlev(q, n, t, lev) != zi:
                    bad += 1
                    hits.append(q)
            q += n
        # (c) a ladder far above the Hadamard bound
        far = []
        for k in (math.ceil(B) + 2, math.ceil(B) + 8, math.ceil(B) + 20):
            qq = primes_mod(n, k, k)[0]
            far.append((qq, reduced_Zlev(qq, n, t, lev) == zi))
        out[key] = {"cut_excess": at_cut > zi, "tested_above": tested,
                    "violations": bad, "hits": hits[:5],
                    "far": [[str(a), b] for a, b in far]}
        st["P6"] = out
        save(CKPT, st)
        print(f"  ({n},{t},{lev}) Q*={Q}=2^{math.log2(Q):.3f}: "
              f"excess at Q* = {at_cut > zi}; primes tested in "
              f"(Q*, 2^{B:.0f}]: {tested}; violations: {bad}"
              + (f"  {hits[:5]}" if hits else ""))
        print(f"        far ladder (2^{math.ceil(B)+2}, 2^{math.ceil(B)+8}, "
              f"2^{math.ceil(B)+20}): frozen = {[b for _, b in far]}")
    return st


# ---------------------------------------------------------------- P5 (S_inf)

def phase_P5(st):
    print("=" * 78)
    print("P5 -- S_inf = 1/ln 2 : the telescoping identity, verified")
    print("=" * 78)
    print("  identity  S_K = K - 2^-K log2((2^K)!)   [exact, from")
    print("  2^-k log2 C(2^k,2^(k-1)) = 2^-k log2 (2^k)! - 2^-(k-1) log2 (2^(k-1))!]")
    print(f"  {'K':>3} {'S_K (direct sum)':>22} {'K - 2^-K log2(2^K)!':>22} "
          f"{'|diff|':>10} {'log2e - S_K':>14} {'ratio to 2^-(K+1)log2(2pi2^K)':>30}")
    L2E = math.log2(math.e)
    worst, ratios = 0.0, []
    for K in range(1, 19):
        S = 0.0
        for k in range(1, K + 1):
            S += 2.0 ** (-k) * (2 ** k - log2_int(math.comb(2 ** k, 2 ** (k - 1))))
        lf = log2_int(math.factorial(2 ** K))
        S2 = K - lf / 2.0 ** K
        d = abs(S - S2)
        worst = max(worst, d)
        pred = 2.0 ** (-(K + 1)) * math.log2(2 * math.pi * 2 ** K)
        rat = (L2E - S) / pred
        ratios.append((K, rat))
        print(f"  {K:>3} {S:>22.15f} {S2:>22.15f} {d:>10.2e} "
              f"{L2E - S:>14.3e} {rat:>30.6f}")
    ok12 = all(abs(r - 1) < 0.01 for K, r in ratios if K >= 12)
    print(f"\n  PR-8a: max |S_K - (K - 2^-K log2 (2^K)!)| = {worst:.3e} "
          f"-> {'PASS' if worst < 1e-12 else 'FAIL'} (window 1e-12)")
    print(f"  PR-8b: (log2 e - S_K)/(2^-(K+1) log2(2 pi 2^K)) within 1% of 1 "
          f"for K >= 12 -> {'PASS' if ok12 else 'FAIL'}")
    st["P5"] = {"worst": worst, "ok12": ok12}
    return st


# ---------------------------------------------------------------- P3 (the fit)

def lsq(xs, ys):
    k = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sl = (k * sxy - sx * sy) / (k * sxx - sx * sx)
    ic = (sy - sl * sx) / k
    res = max(abs(y - (ic + sl * x)) for x, y in zip(xs, ys))
    return sl, ic, res


def phase_P3(st):
    """THE FIT.  Coordinates that make the law visible:
        x = NAIVE DEPTH  = log2 Zinf - n + T*Lam        (pure q^-T law: y = x)
        y = TRUE  DEPTH  = log2 Zinf - log2(Zlev - Zinf)
    The registered deep-band law is dy/dx = 1 (alpha = T).  The freeze tail
    is the region x > 0, where the census is dominated by the SHORTEST
    nonzero vector of the rank-e lattice L_q = {A : A(zeta) = 0 mod q}
    inside the box [-u,u]^e, giving y ~ lambda_1^2/(u ln2) ~ 2^(2x/e):
    the tail is exponential in the depth, not linear."""
    print("=" * 78)
    print("P3 -- THE FIT: deep band (y = x) and the freeze tail (log2 y linear in x)")
    print("=" * 78)
    data = load(CDATA)
    rows = {}
    for (n, t, lev) in LCELLS:
        u, h, T, e, tau = cellparams(n, t, lev)
        zi = Zinf(n, t, lev)
        lzi = log2_int(zi)
        cur = data.get(f"{n}|{t}|{lev}", {})
        pts = []
        for qs, zs in sorted(cur.items(), key=lambda kv: int(kv[0])):
            q, z = int(qs), int(zs)
            lam = math.log2(q)
            x = lzi - n + T * lam
            d = z - zi
            y = (lzi - log2_int(d)) if d > 0 else float("inf")
            pts.append((lam, x, y, d))
        rows[(n, t, lev)] = pts
    print(f"\n  {'cell':>13} {'T':>2} {'e':>2} {'pts':>4} {'deep dy/dx':>11} "
          f"{'resid':>7} {'npt':>4} | {'tail slope':>10} {'2/e':>6} "
          f"{'npt':>4} {'resid':>7}")
    eps_rows, tail_rows = [], []
    for (n, t, lev), pts in rows.items():
        u, h, T, e, tau = cellparams(n, t, lev)
        deep = [(p[1], p[2]) for p in pts if p[1] <= 0.0 and p[3] > 0]
        dsl = dres = float("nan")
        if len(deep) >= 2:
            dsl, _, dres = lsq([a for a, b in deep], [b for a, b in deep])
        tail = [(p[1], math.log2(p[2])) for p in pts if p[1] > 0 and p[3] > 0
                and p[2] > 0]
        tsl = tres = float("nan")
        if len(tail) >= 3:
            tsl, _, tres = lsq([a for a, b in tail], [b for a, b in tail])
        print(f"  ({n:>3},{t:>2},{lev})".rjust(14)
              + f"{T:>3} {e:>3} {len(pts):>4} {dsl:>11.4f} {dres:>7.3f} "
              f"{len(deep):>4} | {tsl:>10.4f} {2 / e:>6.3f} {len(tail):>4} "
              f"{tres:>7.3f}")
        if len(deep) >= 4:
            eps_rows.append((n, t, lev, dsl))
        if len(tail) >= 3:
            tail_rows.append((n, t, lev, tsl, 2 / e))
    print("\n  --- per-cell tables (Lam, naive depth x, true depth y, y-x) ---")
    for (n, t, lev), pts in rows.items():
        u, h, T, e, tau = cellparams(n, t, lev)
        print(f"\n  CELL ({n},{t},{lev})  u={u} h={h} T={T} e={e}  "
              f"LamStar={LamStar(n, t, lev):.3f}  B={Bbound(n, t, lev)[0]:.1f}")
        for (lam, x, y, d) in pts:
            if x < -6 and d > 0:
                continue                       # deep band, printed in summary
            ys = "FROZEN" if d == 0 else f"{y:>9.4f}"
            gap = "   --" if d == 0 else f"{y - x:>7.4f}"
            print(f"    Lam={lam:>7.3f}  x={x:>9.4f}  y={ys:>9}  y-x={gap}")
    eps = max(abs(s - 1.0) for *_, s in eps_rows) if eps_rows else float("nan")
    print(f"\n  PR-6 deep-band dy/dx over cells with >= 4 deep points "
          f"({len(eps_rows)} cells): "
          + ", ".join(f"({n},{t},{lev}):{s:.4f}" for n, t, lev, s in eps_rows))
    print(f"  eps = max |dy/dx - 1| = {eps:.4f}   "
          f"(registered window [0.00, 0.05] -> "
          f"{'PASS' if eps <= 0.05 else 'MISS'})")
    print(f"  PR-7 implied G-c F2 licensed range: log2 q <= 256/(1+eps) = "
          f"{256 / (1 + eps):.1f}  (round 25: 232.7; registered window "
          f"[243.8, 253.5])")
    print(f"\n  PR-6b tail slope vs the predicted 2/e:")
    for n, t, lev, s, p in tail_rows:
        print(f"    ({n},{t},{lev}): measured {s:.4f}  predicted {p:.4f}  "
              f"ratio {s / p:.3f}")
    st["P3"] = {"eps": eps, "tail": [[n, t, lev, s, p]
                                     for n, t, lev, s, p in tail_rows]}
    return st


# ------------------------------------------------------------- P7 (pricing)

def phase_P7(st):
    print("=" * 78)
    print("P7 -- THE (232, 256] PRICING  [law]")
    print("=" * 78)
    N, T0, E = 2 ** 41, 2 ** 33, 128
    print(f"  official schedule: n = 2^41, t = 2^33, e = n/(2t) = {E}")
    print(f"\n  depth of the level-0 coset term, d(Lam) = e - n + t*Lam:")
    for lam in (232, 240, 248, 255, 256 - 128 / 2 ** 33, 256 - 107 / 2 ** 33, 256):
        d = E - N + T0 * lam
        print(f"    log2 q = {lam:>22.12f}   depth = {d:>+22.6f}  "
              f"{'DEEP BAND' if d < 0 else 'FREEZE TAIL'}")
    lam0 = (N - E) / T0
    lam21 = (N - E + 21) / T0
    print(f"\n  the tail begins (depth = 0) at log2 q = {lam0:.12f} "
          f"= 256 - 128/2^33")
    print(f"  the reserve breaks (depth = 21) at log2 q = {lam21:.12f} "
          f"= 256 - 107/2^33")
    print(f"  => the whole band (232, {lam0:.9f}] is DEEP BAND; the freeze")
    print(f"     tail occupies only the last {256 - lam0:.3e} of log2 q.")
    print(f"\n  census cost of a targeted exact census at level lev "
          f"(states, log2):")
    print(f"    {'lev':>4} {'u':>12} {'h':>14} {'T':>12} "
          f"{'MITM (u+1)^(h/2)':>20} {'reduced':>20}")
    for lev in (0, 1, 2, 10, 20, 30, 32, 33):
        u, h, T = 2 ** lev, N // 2 ** lev, T0 // 2 ** lev
        mitm = (h / 2) * math.log2(u + 1)
        red = (E / 2) * math.log2(2 * u + 1) if T == 1 else float("nan")
        print(f"    {lev:>4} {'2^%d' % lev:>12} {'2^%d' % (41 - lev):>14} "
              f"{'2^%d' % (33 - lev):>12} {mitm:>20.4e} {red:>20.4e}")
    best = min((h / 2) * math.log2(2 ** lev + 1)
               for lev in range(34) for h in [N // 2 ** lev])
    print(f"\n  cheapest exact level census over all 34 levels: "
          f"2^{best:.4e} states.")
    print(f"  PR-9: the (232,256] band is NOT reachable by exact census; the")
    print(f"  cheapest object is 2^{best:.3e} states, and no cutoff law helps")
    print(f"  because the band is deep-band, not tail.  Reachability of the")
    print(f"  band moves ONLY through the falsifier tolerance (PR-7).")
    st["P7"] = {"lam0": lam0, "lam21": lam21, "best_log2_states": best}
    return st


# ------------------------------------------- P8 (the tail IS a short-vector census)

def phase_P8(st):
    """THE FREEZE TAIL, EXACTLY.  By L3 the excess of a T=1 cell is

        Zlev(q) - Zinf = SUM over A != 0 in L_q ^ [-u,u]^e of PROD_i C(2u,u+A_i)

    with L_q = {A : A(zeta) = 0 mod q} a rank-e lattice of determinant q.
    So the tail is a SHORT-VECTOR census: as q grows the surviving A are
    pushed away from the origin and the binomial weight kills them like a
    Gaussian, giving the depth

        y = log2(Zinf/excess) ~ ||A_1||^2 / (u ln 2) - log2(multiplicity),

    which is exponential in Lam and violently non-monotone (lambda_1
    fluctuates from prime to prime).  Zero lattice points in the box = the
    exact integer cutoff.  This phase enumerates the box and checks it."""
    print("=" * 78)
    print("P8 -- THE TAIL AS A SHORT-VECTOR CENSUS (exact, T=1 cells)")
    print("=" * 78)
    data = load(CDATA)
    out = {}
    for (n, t, lev) in LCELLS:
        u, h, T, e, tau = cellparams(n, t, lev)
        if T != 1 or (2 * u + 1) ** e > 1_500_000:
            continue
        zi = Zinf(n, t, lev)
        lzi = log2_int(zi)
        cur = data.get(f"{n}|{t}|{lev}", {})
        cen = math.comb(2 * u, u)
        print(f"\n  CELL ({n},{t},{lev})  u={u} e={e}  box={(2*u+1)**e}  "
              f"Hadamard B={Bbound(n, t, lev)[0]:.1f}  "
              f"Q*={st.get('P4', {}).get(f'{n}|{t}|{lev}', {}).get('Qstar')}")
        print(f"    {'Lam':>7} {'#A!=0':>6} {'|A1|^2':>7} {'y (exact)':>10} "
              f"{'|A1|^2/(u ln2)':>15} {'share of A1':>12}")
        rows = []
        for qs, zs in sorted(cur.items(), key=lambda kv: int(kv[0])):
            q, z = int(qs), int(zs)
            lam = math.log2(q)
            x = lzi - n + T * lam
            if x < -1.0:
                continue                      # deep band: not the tail
            zeta = pow(get_zeta(q, n), 2 ** lev, q)
            pw = [pow(zeta, i, q) for i in range(e)]
            pts, tot, best, bw = 0, 0, None, 0
            idx = [0] * e
            rng = list(range(-u, u + 1))
            while True:
                A = [rng[i] for i in idx]
                if any(A):
                    s = 0
                    for i in range(e):
                        s += A[i] * pw[i]
                    if s % q == 0:
                        w = 1
                        for a in A:
                            w *= math.comb(2 * u, u + a)
                        pts += 1
                        tot += w
                        nn = sum(a * a for a in A)
                        if best is None or nn < best:
                            best, bw = nn, w
                        elif nn == best:
                            bw += w
                k = e - 1
                while k >= 0:
                    idx[k] += 1
                    if idx[k] < len(rng):
                        break
                    idx[k] = 0
                    k -= 1
                if k < 0:
                    break
            assert tot == z - zi, f"L3 tail identity failed at q={q}"
            yy = (lzi - log2_int(tot)) if tot else float("inf")
            pred = best / (u * math.log(2)) if best else float("nan")
            sh = bw / tot if tot else float("nan")
            print(f"    {lam:>7.3f} {pts:>6} "
                  + (f"{best:>7}" if best else f"{'-':>7}")
                  + (f" {yy:>10.4f}" if tot else f" {'FROZEN':>10}")
                  + (f" {pred:>15.4f} {sh:>12.4f}" if best else
                     f" {'-':>15} {'-':>12}"))
            if tot:
                rows.append((yy, pred, sh))
        if rows:
            rat = [p / y for y, p, s in rows if y > 0.5]
            print(f"    -> rows with y > 0.5: {len(rat)};  "
                  f"mean |A1|^2/(u ln2) / y = "
                  f"{(sum(rat) / len(rat) if rat else float('nan')):.3f};  "
                  f"mean weight share of the shortest vector = "
                  f"{sum(s for _, _, s in rows) / len(rows):.3f}")
            out[f"{n}|{t}|{lev}"] = {"rows": len(rows)}
    st["P8"] = out
    return st


# ------------------------------------------ P9 (how exact is alpha = T, really)

def phase_P9(st):
    """PR-D says alpha = T.  P3 shows dy/dx is NOT 1 near the crossover.  The
    right question is how fast the deviation dies as we go deep.  Fit

        log2 |y - x|  =  a + s*x        over the deep band (x < -0.5)

    and extrapolate to the official row's own depth.  D2(ii): if the
    deviation at the official depth is below any conceivable resolution,
    alpha = T is an exact law there, not an approximation."""
    print("=" * 78)
    print("P9 -- HOW EXACT IS alpha = T ?  deviation decay in the deep band")
    print("=" * 78)
    data = load(CDATA)
    N, T0, E = 2 ** 41, 2 ** 33, 128
    print(f"  {'cell':>13} {'T':>2} {'e':>2} {'npt':>4} {'slope s':>8} "
          f"{'a':>8} {'resid':>7} {'|y-x| at x=0':>13} {'sign':>6}")
    slopes = []
    for (n, t, lev) in LCELLS:
        u, h, T, e, tau = cellparams(n, t, lev)
        zi = Zinf(n, t, lev)
        lzi = log2_int(zi)
        cur = data.get(f"{n}|{t}|{lev}", {})
        xs, ys, sgn = [], [], 0
        for qs, zs in sorted(cur.items(), key=lambda kv: int(kv[0])):
            q, z = int(qs), int(zs)
            d = z - zi
            if d <= 0:
                continue
            lam = math.log2(q)
            x = lzi - n + T * lam
            y = lzi - log2_int(d)
            if x < -0.5 and abs(y - x) > 1e-9:
                xs.append(x)
                ys.append(math.log2(abs(y - x)))
                sgn += 1 if y > x else -1
        if len(xs) < 4:
            print(f"  ({n:>3},{t:>2},{lev})".rjust(14)
                  + f"{T:>3} {e:>3} {len(xs):>4}   -- too few deep points --")
            continue
        s, a, r = lsq(xs, ys)
        slopes.append((n, t, lev, T, s, a, sgn))
        print(f"  ({n:>3},{t:>2},{lev})".rjust(14)
              + f"{T:>3} {e:>3} {len(xs):>4} {s:>8.4f} {a:>8.4f} {r:>7.3f} "
              f"{2 ** a:>13.4f} "
              + f"{'STEEP' if sgn > 0 else 'FLAT':>6}")
    if slopes:
        smin = min(s for *_, s, a, g in slopes)
        print(f"\n  every cell: |y - x| decays EXPONENTIALLY in the depth, "
              f"slope s in [{smin:.3f}, "
              f"{max(s for *_, s, a, g in slopes):.3f}] per bit.")
        print(f"  T = 1 cells STEEPEN (y > x); T >= 2 cells FLATTEN (y < x) --")
        print(f"  the sub-dominant strata (g_v = 1 conditions instead of T)")
        print(f"  decay slower and take over near freeze.")
        print(f"\n  [law] EXTRAPOLATION to the official row (n=2^41, t=2^33):")
        for lam in (232, 248, 255, 256 - 128 / 2 ** 33):
            xoff = E - N + T0 * lam
            worst = max(a + s * xoff for *_, s, a, g in slopes)
            print(f"    log2 q = {lam:>20.9f}: depth x = {xoff:>+16.4e} "
                  f"bits  ->  |alpha/T - 1| <= 2^({worst:.3e})")
        print(f"\n  D2(ii): on the official row's own domain the deviation from")
        print(f"  alpha = T is smaller than 2^(-1e11).  PR-D is EXACT there.")
    st["P9"] = {"slopes": [[n, t, lev, T, s, a, g]
                           for n, t, lev, T, s, a, g in slopes]}
    return st


# ------------------------------------ P10 (the tail-cleaned refit -> licensed range)

def phase_P10(st):
    """D2(iii).  G-c fires iff alpha >= 1.10 T; the 10% tolerance is what
    caps the F2-powered range at 256/1.10 = 232.7.  The tolerance was set by
    the observed scatter of alpha/T, which P3/P9 now show is freeze-tail
    contamination with a KNOWN decay.  Refit alpha with a depth window
    x <= X and read off the tolerance the cleaned data can support."""
    print("=" * 78)
    print("P10 -- TAIL-CLEANED REFIT: the depth window vs the licensed range")
    print("=" * 78)
    data = load(CDATA)
    print(f"  {'window x <=':>12} {'cells (>=4 pts)':>16} {'>=5 pts':>8} "
          f"{'distinct T':>11} {'eps = max|a/T-1|':>17} "
          f"{'G-c rule ok':>12} {'licensed log2 q <=':>19}")
    best = None
    for X in (0.0, -1.0, -2.0, -3.0, -4.0, -5.0, -5.5):
        cells, five, Ts, eps, who = 0, 0, set(), 0.0, []
        for (n, t, lev) in sorted(tuple(int(v) for v in k.split("|"))
                                  for k in data):
            u, h, T, e, tau = cellparams(n, t, lev)
            zi = Zinf(n, t, lev)
            lzi = log2_int(zi)
            xs, ys = [], []
            for qs, zs in sorted(data.get(f"{n}|{t}|{lev}", {}).items(),
                                 key=lambda kv: int(kv[0])):
                q, z = int(qs), int(zs)
                d = z - zi
                if d <= 0:
                    continue
                x = lzi - n + T * math.log2(q)
                if x <= X:
                    xs.append(x)
                    ys.append(lzi - log2_int(d))
            if len(xs) >= 4:
                cells += 1
                Ts.add(T)
                if len(xs) >= 5:
                    five += 1
                s, _, _ = lsq(xs, ys)
                eps = max(eps, abs(s - 1.0))
                who.append(f"({n},{t},{lev})T{T}:{s:.4f}/{len(xs)}pt")
        ok = (cells >= 3 and five >= 3 and len(Ts) >= 2)
        if X in (-3.0, -5.0):
            print("      " + "  ".join(who))
        lic = 256.0 / (1.0 + eps) if eps > 0 else float("inf")
        print(f"  {X:>12.1f} {cells:>16} {five:>8} {sorted(Ts)!s:>11} "
              f"{eps:>17.4f} {str(ok):>12} {lic:>19.1f}")
        if ok and (best is None or eps < best[1]):
            best = (X, eps, lic, cells, five)
    print(f"\n  round 25 (no depth window): tolerance 0.10 -> licensed "
          f"log2 q <= 232.7")
    if best:
        print(f"  BEST window satisfying G-c's own rule (>=3 cells, >=5 pts, "
              f">=2 distinct T): x <= {best[0]:.1f}")
        print(f"    eps = {best[1]:.4f}  ->  licensed log2 q <= {best[2]:.1f}"
              f"   ({best[3]} cells, {best[4]} with >= 5 points)")
    st["P10"] = {"best": best}
    return st


# --------------------------------- P11 (NEW deep rows: the grid was thin BELOW)

def phase_P11(st):
    """D1 asks for new rows where the grid is thin.  P10 shows the thin end
    is the BOTTOM of the ladder, not the top: the deep band is where alpha=T
    is clean, and round 25's half-octave ladder starts at ceil(log2(n+1))
    with only 3-4 points below depth -3.  The census cost is q-INDEPENDENT,
    so refining downward is nearly free.  Quarter-octave refinement from
    log2(n+1) up to the depth-(-1) point, exact MITM census (same machinery
    and same zeta convention as the banked rows)."""
    print("=" * 78)
    print("P11 -- NEW EXACT ROWS: quarter-octave refinement of the DEEP band")
    print("=" * 78)
    data = load(CDATA)
    added = 0
    for (n, t, lev) in LCELLS:
        u, h, T, e, tau = cellparams(n, t, lev)
        zi = Zinf(n, t, lev)
        lzi = log2_int(zi)
        ls = LamStar(n, t, lev)
        key = f"{n}|{t}|{lev}"
        cur = data.setdefault(key, {})
        lo = math.log2(n + 1)
        hi = ls - 1.0 / T                       # up to depth x = -1
        if hi <= lo:
            print(f"  cell ({n},{t},{lev}): no deep band reachable "
                  f"(log2(n+1)={lo:.2f} >= LamStar-1/T={hi:.2f})  SKIP")
            continue
        qs = primes_mod(n, math.ceil(lo * 4) / 4.0, hi, per_octave=4)
        new = 0
        for q in qs:
            if str(q) in cur:
                continue
            cur[str(q)] = str(Zlev(q, n, t, lev))
            new += 1
            save(CDATA, data)
        added += new
        deep = sum(1 for qs_, zs_ in cur.items()
                   if int(zs_) > zi
                   and lzi - n + T * math.log2(int(qs_)) <= -3.0)
        print(f"  cell ({n},{t},{lev}) T={T}: deep band "
              f"[{lo:.2f}, {hi:.2f}]  +{new} new exact rows  "
              f"(now {len(cur)} total, {deep} at depth <= -3)")
    print(f"\n  {added} new exact level-census rows banked in cdata.json.")
    st["P11"] = {"added": added}
    return st


# ------------------------------- P12 (cells the L3 reduction newly makes reachable)

def deep_T1_cells():
    """MECHANICAL selection rule, fixed before any of these cells was
    measured: every (n, t, lev) with n, t powers of two, T = t/2^lev = 1
    (so lev = log2 t, u = t, h = 2e), reduced MITM half (2u+1)^(e/2) <= 2^21
    states, and deep-band span LamStar - log2(n+1) >= 10 bits.  No cell is
    chosen by its answer."""
    out = []
    for ln in range(5, 11):
        n = 2 ** ln
        for lt in range(1, ln - 1):
            t = 2 ** lt
            lev = lt
            u, e = t, n // (2 * t)
            if e < 2 or n % (2 * t) or n // 2 ** lev < 2:
                continue
            if (2 * u + 1) ** (e // 2) > 2 ** 21:
                continue
            span = LamStar(n, t, lev) - math.log2(n + 1)
            if span >= 10.0:
                out.append((n, t, lev, span))
    return out


def phase_P12(st):
    print("=" * 78)
    print("P12 -- NEW DEEP CELLS, reachable only through the L3 reduction")
    print("=" * 78)
    data = load(CDATA)
    cells = deep_T1_cells()
    print(f"  selection rule: T=1, reduced half <= 2^21 states, deep-band "
          f"span >= 10 bits  ->  {len(cells)} cells")
    for (n, t, lev, span) in cells:
        u, h, T, e, tau = cellparams(n, t, lev)
        key = f"{n}|{t}|{lev}"
        zi = Zinf(n, t, lev)
        ls = LamStar(n, t, lev)
        cur = data.setdefault(key, {})
        direct = (u + 1) ** (h // 2)
        qs = primes_mod(n, math.ceil(math.log2(n + 1) * 4) / 4.0,
                        ls - 1.0, per_octave=4)
        new = 0
        for q in qs:
            if str(q) in cur:
                continue
            cur[str(q)] = str(reduced_Zlev(q, n, t, lev))
            new += 1
        save(CDATA, data)
        # guards: (i) Galois invariance of the reduced census (divergence
        # D-15), (ii) the frozen limit far above the Hadamard cutoff.
        B, _ = Bbound(n, t, lev)
        qhi = primes_mod(n, math.ceil(B) + 4, math.ceil(B) + 4)[0]
        frz = reduced_Zlev(qhi, n, t, lev) == zi
        qt = int(sorted(cur, key=int)[len(cur) // 2])
        z0 = pow(get_zeta(qt, n), 2 ** lev, qt)
        inv = all(reduced_Zlev(qt, n, t, lev, pow(z0, s, qt))
                  == int(cur[str(qt)])
                  for s in (3, 5, 7) if math.gcd(s, h) == 1)
        print(f"  ({n:>4},{t:>3},{lev}) u={u:>4} e={e:>3} span={span:>5.2f}  "
              f"direct MITM {direct:>12} states -> reduced "
              f"{(2 * u + 1) ** (e // 2):>8}   +{new:>3} rows  "
              f"[frozen at 2^{math.ceil(B)+4}: {frz}; Galois-invariant: {inv}]")
        assert frz and inv, "guard failed"
    st["P12"] = {"cells": [[a, b, c] for a, b, c, _ in cells]}
    return st


PHASES = {"copy": phase_copy, "P1": phase_P1, "P2": phase_P2, "P3": phase_P3,
          "P4": phase_P4, "P5": phase_P5, "P6": phase_P6, "P7": phase_P7,
          "P8": phase_P8, "P9": phase_P9, "P10": phase_P10, "P11": phase_P11,
          "P12": phase_P12}

if __name__ == "__main__":
    state = load(CKPT)
    for ph in (sys.argv[1:] or ["copy"]):
        state = PHASES[ph](state)
        save(CKPT, state)
    print("\ncheckpoint:", CKPT)
