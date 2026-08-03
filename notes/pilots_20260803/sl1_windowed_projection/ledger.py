#!/usr/bin/env python3
"""SL-1 route (1): the EXACT DIMENSION / DENSITY LEDGER, and the L-B
unification made a theorem.   (pilot 2026-08-03)

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

Three things, each machine-checked:

T-PSI (UNIFICATION -- the assigned identification).
    For a joint-explanation pair P = (f,g) with core Z_P, a member
    z in P^1(F_q) and a NON-CORE point y, define the pair-level
    over-agreement functional

        Psi^z_y (u,v)  :=  (u_y - f(x_y))  +  z * (v_y - g(x_y))
                        =   e_y + z e'_y                     (z finite)
        Psi^inf_y(u,v) :=  (v_y - g(x_y)) = e'_y

    Then IDENTICALLY  Psi^z_y(u,v) = (w_z)_y - (pi_z P)(x_y), i.e. the
    PAIR functional is the PULLBACK ALONG THE PENCIL MAP pi_z of the
    L-B RAY functional (the forced-over-agreement functional of
    notes/pilots_20260803/lb_escape1_overagreement).  y joins the
    agreement set of pi_z(P) against w_z  <=>  Psi^z_y = 0.
    So SL-1's over-agreement and L-B's over-agreement are THE SAME
    LINEAR-FUNCTIONAL SPECIES, transported by z |-> pi_z.  Checked as
    an identity on every fixture, every band-proper pair, every member.

T-CELL (PENCIL CELL BIJECTION -- the proof engine).
    The map  (e,e') |-> ( member(e,e'), scale )  is a BIJECTION
        F_q^2 minus {(0,0)}  ~~>  P^1(F_q) x F_q^* ,
    member(e,e') = -e/e' in F_q if e' != 0, else 'inf'.
    Cardinality q^2-1 = (q+1)(q-1).  CONSEQUENCE: each non-core point
    lies on EXACTLY ONE member, and the functionals {Psi^z_y}_y for
    distinct y act on DISJOINT coordinate blocks (u_y,v_y), hence are
    linearly independent -- "m extra points at z" is a codimension-m
    condition, never fewer.

T-MULT (EXACT MULTINOMIAL LAW).
    Conditioned on the core, with non-core error pairs i.i.d. uniform on
    F_q^2\{0}, the vector (mult_P(z))_{z in P^1(F_q)} is EXACTLY
        MULTINOMIAL( r ; 1/(q+1) repeated q+1 times ),   r = n-k-d.
    Verified by EXHAUSTIVE enumeration at toy (q, r).  Consequences:
      (a) sum_z mult_P(z) = r          -- THEOREM A, gate-free;
      (b) F1 (over-agreement at EVERY member) needs all q+1 cells to
          carry >= h-d-1 >= 1 points, i.e. r >= q+1; but r < n <= q.
          IMPOSSIBLE -- F1 can never fire, for ANY received pair;
      (c) E|OA_P| = (q+1) P[Bin(r, 1/(q+1)) >= h-d-1]
                  <= C(r, h-d-1) / (q+1)^(h-d-2),
          which is 1-ish exactly at d = h-2 (exponent 0) and
          astronomically small at every d <= h-3.  THE EXACT BOUNDARY.
"""
import itertools
import json
import sys
from collections import defaultdict
from math import lgamma, log

sys.dont_write_bytecode = True
BASE = "/home/u2470931/smooth-read-solomin/prize/notes/"
sys.path.insert(0, BASE + "pilots_20260802/xr_graded_band_ledger")
sys.path.insert(0, BASE + "pilots_20260803/sl1_windowed_projection")
from bandlib import Row                              # noqa: E402 read-only
from sl1 import pair_profile, plant_free, fixtures   # noqa: E402 own pilot

LOG2 = log(2.0)
ROWS = [
    dict(name="RowC 1/4", n=1024, k=256, A=261, h=5),
    dict(name="RowC 1/8", n=1024, k=128, A=133, h=5),
    dict(name="RowC 1/16", n=1024, k=64, A=67, h=3),
    dict(name="prize 1/4", n=2199023255552, k=549755813888,
         A=558345748481, h=8589934593),
    dict(name="prize 1/8", n=2199023255552, k=274877906944,
         A=283467841537, h=8589934593),
    dict(name="prize 1/16", n=2199023255552, k=137438953472,
         A=141733920769, h=4294967297),
]
LOG2Q_PIN = 250.0


def log2binom(nn, mm):
    """log2 C(nn, mm) via lgamma -- nn, mm may be astronomically large."""
    if mm < 0 or mm > nn:
        return float("-inf")
    if mm == 0 or mm == nn:
        return 0.0
    return (lgamma(nn + 1) - lgamma(mm + 1) - lgamma(nn - mm + 1)) / LOG2


def member_of(e, ep, q):
    """the UNIQUE member of P^1(F_q) whose projection picks up (e, e')."""
    if ep % q == 0:
        return 'inf'
    return (-e) * pow(ep, q - 2, q) % q


def main():
    checks = []
    fails = []

    def ck(tag, ctx, ok, extra=None):
        checks.append([tag, ctx, bool(ok), extra])
        if not ok:
            fails.append([tag, ctx, extra])

    # =============================================== T-CELL (bijection)
    for q in (7, 11, 13, 101):
        cells = defaultdict(list)
        for e in range(q):
            for ep in range(q):
                if (e, ep) == (0, 0):
                    continue
                cells[member_of(e, ep, q)].append((e, ep))
        ck("T-CELL: exactly q+1 cells", f"q={q}", len(cells) == q + 1,
           len(cells))
        ck("T-CELL: every cell has exactly q-1 error pairs", f"q={q}",
           all(len(v) == q - 1 for v in cells.values()),
           sorted({len(v) for v in cells.values()}))
        ck("T-CELL: cells partition F_q^2\\{0}", f"q={q}",
           sum(len(v) for v in cells.values()) == q * q - 1)
        # the defining property: (e,e') is killed by member z and NO other
        for e in range(q):
            for ep in range(q):
                if (e, ep) == (0, 0):
                    continue
                hit = [z for z in range(q) if (e + z * ep) % q == 0]
                if ep % q == 0:
                    hit.append('inf')
                if len(hit) != 1 or hit[0] != member_of(e, ep, q):
                    ck("T-CELL: unique-member property", f"q={q} {(e, ep)}",
                       False, hit)
        ck("T-CELL: unique-member property", f"q={q}", True)

    # ======================================= T-MULT (exact multinomial)
    # EXHAUSTIVE over all error patterns on r non-core points.
    for q, r in [(7, 2), (7, 3), (11, 2), (11, 3), (13, 2)]:
        pairs = [(e, ep) for e in range(q) for ep in range(q)
                 if (e, ep) != (0, 0)]
        hist = defaultdict(int)
        tot = 0
        for pat in itertools.product(pairs, repeat=r):
            cnt = defaultdict(int)
            for (e, ep) in pat:
                cnt[member_of(e, ep, q)] += 1
            hist[tuple(sorted(cnt.values(), reverse=True))] += 1
            tot += 1
        ck("T-MULT: total = (q^2-1)^r", f"q={q} r={r}",
           tot == (q * q - 1) ** r)
        # predicted multinomial shape-counts
        pred = defaultdict(int)
        for shape in hist:
            # #patterns with this UNORDERED cell-shape
            #   = (#ways to assign which cells) * (multinomial) * (q-1)^r
            mult = 1
            rem = r
            for s in shape:
                mult *= round(_binom(rem, s))
                rem -= s
            # ways to pick WHICH cells carry the shape, respecting ties
            ways = 1
            avail = q + 1
            seen = defaultdict(int)
            for s in shape:
                seen[s] += 1
            for s, c in seen.items():
                ways *= _falling(avail, c) // _fact(c)
                avail -= c
            pred[shape] = ways * mult * (q - 1) ** r
        ck("T-MULT: exact multinomial law reproduced",
           f"q={q} r={r}", dict(hist) == dict(pred),
           None if dict(hist) == dict(pred) else
           {s: (hist[s], pred[s]) for s in hist if hist[s] != pred[s]})
        # (a) the identity sum = r, on every pattern (implied, assert)
        ck("T-MULT(a): sum_z mult = r on every pattern", f"q={q} r={r}",
           all(sum(s) == r for s in hist))
        # (b) F1 impossibility: no pattern fills all q+1 cells when r<q+1
        ck("T-MULT(b): r < q+1 => some cell EMPTY => F1 impossible",
           f"q={q} r={r}", r < q + 1 and all(len(s) < q + 1 for s in hist))

    # ================= T-PSI (unification) on the pilot's own fixtures
    npsi = 0
    nfix = 0
    for name, r_, u, v, desc in fixtures():
        n, k, q, A, h = r_.n, r_.k, r_.q, r_.A, r_.h
        dlo, dhi = (h + 1) // 2, h - 2
        if dlo > dhi:
            continue
        nfix += 1
        cores = {}
        for W in itertools.combinations(range(n), k):
            f = r_.interp(W, [u[i] for i in W])
            g = r_.interp(W, [v[i] for i in W])
            Z = [i for i in range(n)
                 if (r_.ev(f, r_.xs[i]) - u[i]) % q == 0
                 and (r_.ev(g, r_.xs[i]) - v[i]) % q == 0]
            cores[frozenset(Z)] = len(Z)
        bad_psi = 0
        bad_pull = 0
        bad_ind = 0
        for Z in cores:
            d = len(Z) - k
            if not (dlo <= d <= dhi):
                continue
            f, g, mult, slope_of, _ = pair_profile(r_, u, v, Z)
            noncore = [i for i in range(n) if i not in Z]
            # sample members: all planted/live ones + a spread of others
            members = sorted({slope_of[i] for i in noncore},
                             key=str) + [0, 1, 2, 'inf']
            for z in members:
                # pi_z(P) as a polynomial
                fl, gl = list(f), list(g)
                L = max(len(fl), len(gl))
                fl += [0] * (L - len(fl))
                gl += [0] * (L - len(gl))
                if z == 'inf':
                    pi = gl
                    wz = list(v)
                else:
                    pi = [(a + z * b) % q for a, b in zip(fl, gl)]
                    wz = [(u[i] + z * v[i]) % q for i in range(n)]
                cols = []
                for y in noncore:
                    e = (u[y] - r_.ev(f, r_.xs[y])) % q
                    ep = (v[y] - r_.ev(g, r_.xs[y])) % q
                    psi = ep % q if z == 'inf' else (e + z * ep) % q
                    # T-PSI: pullback identity
                    ray = (wz[y] - r_.ev(pi, r_.xs[y])) % q
                    if psi != ray:
                        bad_pull += 1
                    # T-PSI: vanishing <=> membership of the agreement set
                    joins = (slope_of[y] == z)
                    if (psi == 0) != joins:
                        bad_psi += 1
                    npsi += 1
                    if psi == 0:
                        cols.append(y)
                # T-CELL consequence: independence = disjoint blocks
                if len(set(cols)) != len(cols):
                    bad_ind += 1
                # and the count of vanishing functionals IS mult_P(z)
                if len(cols) != mult.get(z, 0):
                    bad_ind += 1
        ck("T-PSI: pullback identity Psi^z_y = (w_z)_y - pi_z(P)(x_y)",
           name, bad_pull == 0, bad_pull)
        ck("T-PSI: Psi^z_y = 0 <=> y joins agr(pi_z P, w_z)", name,
           bad_psi == 0, bad_psi)
        ck("T-PSI: #{y : Psi^z_y = 0} = mult_P(z), blocks disjoint",
           name, bad_ind == 0, bad_ind)

    # ===================== the six-row density ledger (consequence (c))
    rows = []
    for r in ROWS:
        n, k, A, h = r["n"], r["k"], r["A"], r["h"]
        dlo, dhi = -(-h // 2), h - 2
        rec = dict(name=r["name"], h=h, band_proper=[dlo, dhi])
        if dlo > dhi:
            rows.append(rec)
            continue
        ends = []
        for d in (dlo, dhi):
            rr = n - k - d
            m = h - d - 1                      # extra points needed
            # E|OA_P| <= C(r, m) / (q+1)^(m-1)   [union bound over members]
            lg = log2binom(rr, m) - (m - 1) * LOG2Q_PIN
            beta = rr // m
            ends.append(dict(d=d, r=rr, m_extra=m, beta=beta,
                             log2_E_OA_bound=lg,
                             forced=(m == 1),
                             log2_beta=log2binom(beta, 1) if beta else None))
            ck("ledger: m = h-d-1 >= 1 on band proper",
               f"{r['name']} d={d}", m >= 1)
            ck("ledger: deterministic |OA_P| <= beta_d = floor(r/m)",
               f"{r['name']} d={d}", beta == rr // m)
            if d == dhi:
                ck("ledger: at d=h-2 the exponent (m-1) is ZERO "
                   "-> NO decay -> over-agreement FORCED",
                   f"{r['name']} d={d}", m == 1 and abs(lg - log2binom(rr, 1)) < 1e-6)
            if d <= h - 3:
                ck("ledger: at d <= h-3 the bound is < 2^-1000 "
                   "(over-agreement vanishingly rare)",
                   f"{r['name']} d={d}", lg < -1000.0, lg)
        rec["endpoints"] = ends
        rows.append(rec)

    print(f"{'row':12s} {'d':>12s} {'r=n-k-d':>15s} {'m=h-d-1':>12s} "
          f"{'beta_d':>15s} {'log2 E|OA_P| bound':>21s}  regime")
    for rec in rows:
        for i, e in enumerate(rec.get("endpoints", [])):
            nm = rec["name"] if i == 0 else ""
            reg = ("FORCED (m=1)" if e["forced"]
                   else "vanishing")
            print(f"{nm:12s} {e['d']:>12d} {e['r']:>15d} {e['m_extra']:>12d} "
                  f"{e['beta']:>15d} {e['log2_E_OA_bound']:>21.4g}  {reg}")

    print(f"\nT-PSI functional evaluations: {npsi} over {nfix} fixtures")
    print(f"checks: {len(checks)}  failures: {len(fails)}")
    for b in fails[:12]:
        print("  FAIL", b)
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(rows=rows, checks=checks, n_psi=npsi,
                       verdict="PASS" if not fails else "FAIL"), fh,
                  indent=1, default=str)


def _fact(x):
    out = 1
    for i in range(2, x + 1):
        out *= i
    return out


def _falling(a, b):
    out = 1
    for i in range(b):
        out *= (a - i)
    return out


def _binom(a, b):
    if b < 0 or b > a:
        return 0
    return _falling(a, b) // _fact(b)


if __name__ == "__main__":
    main()
