#!/usr/bin/env python3
"""Toy verifier for the list-size terminus program (pilot 2026-08-03).

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

Checks, exhaustively, on planted + random toy fixtures:

  P1  SHADOW LEMMA.  For EVERY member z in P^1(F_q):
          L(w_z, tau) >= RAW_high := #{maximal joint-explanation sets
                                       of size >= tau}
      (raw = every joint pair, no L_P >= 2 selection).
  P2  How often the min over members is EXACTLY RAW_high.
  P3  PROJECTIVE RANK CENSUS.  For k+1 <= j <= tau,
          SUM_{m in P^1(F_q)} G_j(m) = R_j + (q+1) D_j     (exact)
      with G_j(m) = #{S, |S|=j : I_S(w_m) in C},
           D_j = #{S : A(S) = B(S) = 0}      (rank 0, joint explanation)
           R_j = #{S : rank[A(S); B(S)] = 1} (exactly one member)
  P4a the sub-counting inequality L(w_m,tau) * C(tau,j) <= G_j(m).
  P5  every raw high joint set is shadowed at every member.

Banked machinery consumed, never re-derived (hard law 5):
  bandlib.Row/plant (xr_graded_band_ledger), THEOREM I and the KEY LEMMA
  (background/nodes/xr_band_key_lemma_pencil_mass).
The scan here is written locally (not imported) because bandlib's scan
thresholds rays at A, while this pilot needs the full agreement profile
at threshold tau < A and the (0:1) member.
"""
import itertools
import json
import sys
from collections import defaultdict
from math import comb

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/xr_graded_band_ledger")
from bandlib import Row, plant  # noqa: E402  (read-only import)


# ---------------------------------------------------------------- helpers
def lagrange(row, S, vals):
    """deg < |S| interpolant of vals on S, as a coefficient tuple."""
    q = row.q
    m = len(S)
    coeff = [0] * m
    for idx, j in enumerate(S):
        num = [1]
        den = 1
        for t in S:
            if t == j:
                continue
            new = [0] * (len(num) + 1)
            for e, ce in enumerate(num):
                if ce:
                    new[e] = (new[e] - ce * row.xs[t]) % q
                    new[e + 1] = (new[e + 1] + ce) % q
            num = new
            den = den * (row.xs[j] - row.xs[t]) % q
        w = vals[idx] * pow(den, q - 2, q) % q
        for e in range(len(num)):
            coeff[e] = (coeff[e] + w * num[e]) % q
    return tuple(coeff)


def profile(row, u, v):
    """One exhaustive pass over k-subsets.

    Returns
      joints : frozenset -> size   (maximal joint-explanation sets, |Z| >= k)
      lists  : member -> set of agreement sets of size >= tau
               member is z in F_q, or the string 'inf' for w_(0:1) = v
      maxagr : member -> max agreement of any codeword with that member
    """
    n, k, q = row.n, row.k, row.q
    tau = row.tau
    joints = {}
    lists = defaultdict(set)
    maxagr = defaultdict(int)
    for W in itertools.combinations(range(n), k):
        f = row.interp(W, [u[i] for i in W])
        g = row.interp(W, [v[i] for i in W])
        Z = []            # a_i = b_i = 0 : joint explanation
        buck = defaultdict(list)   # finite z with a_i + z b_i = 0
        zb = []           # b_i = 0, a_i != 0 : agrees with the (0:1) member
        for i in range(n):
            a = (row.ev(f, row.xs[i]) - u[i]) % q
            b = (row.ev(g, row.xs[i]) - v[i]) % q
            if a == 0 and b == 0:
                Z.append(i)
            elif b == 0:
                zb.append(i)
            else:
                buck[(-a) * pow(b, q - 2, q) % q].append(i)
        Zf = frozenset(Z)
        joints[Zf] = len(Zf)
        # every member's agreement set through this k-subset
        for z, extra in buck.items():
            S = Zf | frozenset(extra)
            maxagr[z] = max(maxagr[z], len(S))
            if len(S) >= tau:
                lists[z].add(S)
        for z in range(q):
            if z not in buck:                       # agreement set is Zf
                maxagr[z] = max(maxagr[z], len(Zf))
                if len(Zf) >= tau:
                    lists[z].add(Zf)
        S = Zf | frozenset(zb)
        maxagr['inf'] = max(maxagr['inf'], len(S))
        if len(S) >= tau:
            lists['inf'].add(S)
    return joints, lists, maxagr


def rank_census(row, u, v, j):
    """R_j, D_j and G_j(m) for every member m in P^1(F_q), exhaustive."""
    n, k, q = row.n, row.k, row.q
    R = D = 0
    G = defaultdict(int)
    for S in itertools.combinations(range(n), j):
        A = lagrange(row, S, [u[i] for i in S])[k:]
        B = lagrange(row, S, [v[i] for i in S])[k:]
        zeroA = not any(A)
        zeroB = not any(B)
        if zeroA and zeroB:                     # rank 0
            D += 1
            for z in range(q):
                G[z] += 1
            G['inf'] += 1
            continue
        if zeroB:                               # A != 0, B = 0: only (0:1)
            R += 1
            G['inf'] += 1
            continue
        # B != 0.  A + zB = 0 solvable iff A is a scalar multiple of B.
        piv = next(i for i, x in enumerate(B) if x)
        z = (-A[piv]) * pow(B[piv], q - 2, q) % q
        if all((A[i] + z * B[i]) % q == 0 for i in range(len(A))):
            R += 1
            G[z] += 1
        # else rank 2: no member
    return R, D, dict(G)


# ---------------------------------------------------------------- fixtures
def fixtures():
    """(name, row, u, v).  Planted high-depth cores + random controls."""
    out = []
    # toy row: k=5, t=h=4 -> A=9, tau = k + ceil(h/2) = 7, band = [6,7]
    r = Row(14, 5, 4, 101)
    r.tau = r.k + (r.h + 1) // 2
    # one planted depth-2 core (size 7 = tau) with two live slopes
    spec = [dict(Z=list(range(7)), slopes=[1, 2], blocks=[[7, 8], [9, 10]])]
    u, v, _ = plant(r, spec, seed=11)
    out.append(("k5t4_core7_2slopes", r, u, v))
    u, v, _ = plant(r, spec, seed=12)
    out.append(("k5t4_core7_2slopes_b", r, u, v))
    # a depth-2 core with ONE live slope: L_P = 1, so N_d = 0 but RAW = 1
    spec1 = [dict(Z=list(range(7)), slopes=[3], blocks=[[7, 8]])]
    u, v, _ = plant(r, spec1, seed=13)
    out.append(("k5t4_core7_1slope_RAWonly", r, u, v))
    # two disjoint-block depth-2 cores
    spec2 = [dict(Z=list(range(7)), slopes=[1], blocks=[[7, 8]]),
             dict(Z=[0, 1, 2, 3, 9, 10, 11], slopes=[4], blocks=[[12, 13]])]
    u, v, _ = plant(r, spec2, seed=14)
    out.append(("k5t4_two_cores", r, u, v))
    # random control (empty band expected)
    import random
    for s in (21, 22):
        rnd = random.Random(s)
        u = [rnd.randrange(r.q) for _ in range(r.n)]
        v = [rnd.randrange(1, r.q) for _ in range(r.n)]
        out.append((f"k5t4_random_{s}", r, u, v))
    # second row: k=4, t=5 -> A=9, tau = 4+3 = 7
    r2 = Row(13, 4, 5, 61)
    r2.tau = r2.k + (r2.h + 1) // 2
    spec3 = [dict(Z=list(range(7)), slopes=[2, 5], blocks=[[7, 8], [9, 10]])]
    u, v, _ = plant(r2, spec3, seed=31)
    out.append(("k4t5_core7_2slopes", r2, u, v))
    rnd = random.Random(41)
    u = [rnd.randrange(r2.q) for _ in range(r2.n)]
    v = [rnd.randrange(1, r2.q) for _ in range(r2.n)]
    out.append(("k4t5_random", r2, u, v))
    return out


# ---------------------------------------------------------------- main
def main():
    results = []
    fails = []
    for name, r, u, v in fixtures():
        n, k, q, A, tau = r.n, r.k, r.q, r.A, r.tau
        joints, lists, maxagr = profile(r, u, v)
        members = list(range(q)) + ['inf']
        L = {m: len(lists[m]) for m in members}
        big = [Z for Z, s in joints.items() if s >= tau]
        raw_high = len(big)
        # occupancy N_d style count is a SUB-count of raw_high; recorded for
        # the selected-vs-raw gap (definitions item 8) via bandlib's ledger.
        maxJ = max(joints.values())
        max_ray = max(maxagr.values())
        adm = dict(
            v_nonvanishing=all(x != 0 for x in v),
            tangent_gate_P1=max_ray <= A,          # includes (0:1)
            below_cascade=maxJ <= A - 2,
            kpack=True,
        )
        bigsets = [Z for Z, s in joints.items() if s >= k]
        for a in range(len(bigsets)):
            for b in range(a + 1, len(bigsets)):
                if len(bigsets[a] & bigsets[b]) > k - 1:
                    adm["kpack"] = False
        admissible = all(adm.values())

        minL = min(L.values())
        rec = dict(name=name, n=n, k=k, h=r.h, A=A, tau=tau, q=q,
                   admissible=admissible, gates=adm,
                   max_joint=maxJ, max_ray_agreement=max_ray,
                   raw_high=raw_high, min_L=minL, max_L=max(L.values()),
                   members_at_min=sum(1 for m in members if L[m] == minL),
                   members_equal_raw_high=sum(1 for m in members
                                              if L[m] == raw_high))
        # ---- P1 / P5 ----
        p1 = [m for m in members if L[m] < raw_high]
        rec["P1_violations"] = p1
        if p1:
            fails.append((name, "P1", p1[:5]))
        p5bad = []
        for Z in big:
            for m in members:
                if not any(Z <= S for S in lists[m]):
                    p5bad.append((sorted(Z), m))
        rec["P5_violations"] = len(p5bad)
        if p5bad:
            fails.append((name, "P5", p5bad[:3]))
        # ---- P3 / P4a : the projective rank census ----
        cens = []
        for j in range(k + 1, tau + 1):
            R, D, G = rank_census(r, u, v, j)
            tot = sum(G.get(m, 0) for m in members)
            ok = (tot == R + (q + 1) * D)
            sub = all(L[m] * comb(tau, j) <= G.get(m, 0) for m in members)
            cens.append(dict(j=j, R=R, D=D, sum_G=tot,
                             identity_ok=ok, subcount_ok=sub,
                             bound_min=min((G.get(m, 0) // comb(tau, j))
                                           for m in members)))
            if not ok:
                fails.append((name, f"P3 j={j}", (tot, R, D)))
            if not sub:
                fails.append((name, f"P4a j={j}", None))
        rec["census"] = cens
        results.append(rec)
        print(f"{name:28s} adm={admissible} RAW_high={raw_high:3d} "
              f"minL={minL:3d} maxL={max(L.values()):3d} "
              f"#members==RAW={rec['members_equal_raw_high']:4d}/{q+1} "
              f"P1viol={len(p1)} P5viol={len(p5bad)}")
    out = dict(results=results, fails=fails,
               verdict="PASS" if not fails else "FAIL")
    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("\nVERDICT:", out["verdict"], "  failures:", len(fails))
    for f in fails:
        print("  FAIL", f)


if __name__ == "__main__":
    main()
