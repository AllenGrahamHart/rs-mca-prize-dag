#!/usr/bin/env python3
"""Independent verification of upstream PR #395 Theorem C1 (curve second moment identity).

Claim (verbatim from PR #395 diff, note cap25_v13_bc_l4_curve_second_moment.md, section 2):

    M2 = Sum_{s in B} N_{w+1}(theta(s))^2
       = S1 + Sum_{e=w+2}^{min(m,n-m)} Sum_{R subset D, |R|=m-e} sp^Gamma_{w+1}(e;R)

  with sp^Gamma_{w+1}(e;R) := #{ (A,B) : A,B monic degree-e, split over disjoint root
  sets in D\R, deg(A-B) <= e-w-2, Phi_{w+1}(l_R * A) in Gamma }
  and: top nonzero stratum e=w+2 is exactly the constant-shift pairs A, B=A-c (c in B^x).

Definitions (from PR #395 section 1, restated):
  B = F_p; D = mu_n subset B^x (n | p-1); l_T = prod_{x in T}(X-x);
  a_i(T) = coefficient of X^{m-i} in l_T (a_0=1); Phi_{w+1}(T)=(a_1,...,a_{w+1});
  curve: phi_1(s)=s, phi_j(s)=z*_j+(s-z*_1)phi_{j-1}(s), theta(s)=(s,phi_2,...,phi_{w+1});
  Gamma={theta(s): s in B}; Fib(z)={T in C(D,m): Phi(T)=z}; N(z)=|Fib(z)|;
  V = Phi^{-1}(Gamma); S1=|V|.

PRE-REGISTERED CRITERIA (all exact integer arithmetic mod p; no floats):
 CONFIRM requires ALL of:
  (C-a) every row: M2_def == M2_pairs == M2_a1        [Prop C1-1: a_1-equality = prefix-equality on VxV]
  (C-b) every row: M2_def == S1 + sum_e sp_sum[e]      [Theorem C1 main identity]
  (C-c) every row, every e: direct VxV off-diagonal e-histogram == sp_sum[e]
  (C-d) every counted top-stratum pair: A-B nonzero constant; every off-diagonal
        equal-prefix pair has e >= w+2 and deg(A-B) <= e-w-2; no e beyond min(m,n-m)
  (C-e) n=8 rows: honest-difference-poly constraint-(i) equivalence on ALL ordered pairs
        of distinct m-subsets: [deg(l_T - l_T') <= m-w-2] <=> [Phi(T)==Phi(T')];
        and naive full-pair RHS enumeration == bucketed RHS enumeration (also on R5,R6)
  (C-f) non-vacuity: N1 |Gamma|=p each row; N2 >=5 rows S1>0; N3 >=2 rows offdiag>0;
        N4 >=1 row top stratum>0; N5 >=1 row deeper stratum (e>w+2)>0;
        N6 edge row R7 (w+2 > min(m,n-m)): S1>0 and M2==S1
  (C-g) [flag-only] small rows: T valid <=> (X-r)l_T top w+1 coeffs == z*, r=a_1(T)-z*_1
 REFUTE: any exact mismatch in (C-a)-(C-d).
"""
import itertools, sys, time

def primitive_root(p):
    fac = []
    q = p - 1
    d = 2
    while d * d <= q:
        if q % d == 0:
            fac.append(d)
            while q % d == 0:
                q //= d
        d += 1
    if q > 1:
        fac.append(q)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return g
    raise RuntimeError

def mu_n(p, n):
    assert (p - 1) % n == 0, (p, n)
    g = primitive_root(p)
    h = pow(g, (p - 1) // n, p)
    D = []
    x = 1
    for _ in range(n):
        D.append(x)
        x = x * h % p
    assert len(set(D)) == n
    return sorted(D)

def poly_from_roots(roots, p):
    # descending coefficients: c[0]=1 (leading), c[i] = coeff of X^{deg-i}
    c = [1]
    for r in roots:
        c = [ (c[i] - r * (c[i-1] if i >= 1 else 0)) % p for i in range(len(c)) ] + [(-r * c[-1]) % p]
    return tuple(c)

def poly_diff_deg(A, B, p):
    # A,B same length (monic, same degree e); return deg(A-B), -1 for zero poly
    e = len(A) - 1
    for i in range(len(A)):
        if (A[i] - B[i]) % p != 0:
            return e - i
    return -1

def theta_curve(p, w, zstar):
    # returns dict s -> theta(s) tuple, and the set Gamma
    th = {}
    for s in range(p):
        phi = [s]
        for j in range(2, w + 2):
            phi.append((zstar[j-1] + (s - zstar[0]) * phi[-1]) % p)
        th[s] = tuple(phi)
    return th

def run_row(name, p, n, m, w, zstar, do_naive_rhs, do_constraint_i, do_aug_gate, expect_edge=False):
    t0 = time.time()
    D = mu_n(p, n)
    Dset = set(D)
    depth = w + 1
    print(f"--- {name}: p={p} n={n} m={m} w={w} z*={zstar}")
    th = theta_curve(p, w, zstar)
    Gamma = set(th.values())
    assert len(Gamma) == p, "N1 FAIL: theta not injective"
    # phase 2: enumerate all m-subsets, prefix map
    Phi = {}
    Lpoly = {}
    for T in itertools.combinations(D, m):
        c = poly_from_roots(T, p)
        fT = frozenset(T)
        Lpoly[fT] = c
        Phi[fT] = tuple(c[1:depth+1])
    # fibers over Gamma
    from collections import defaultdict
    fib = defaultdict(list)
    for fT, z in Phi.items():
        fib[z].append(fT)
    S1_sum = 0
    M2_def = 0
    for s in range(p):
        Nz = len(fib.get(th[s], ()))
        S1_sum += Nz
        M2_def += Nz * Nz
    V = [fT for fT, z in Phi.items() if z in Gamma]
    Vset = set(V)
    S1 = len(V)
    assert S1 == S1_sum, "Fact 0 FAIL: S1 != sum of curve fibers"
    # M2_pairs (group V by full prefix) and M2_a1 (group V by a_1 only)
    gp = defaultdict(int); ga = defaultdict(int)
    for fT in V:
        gp[Phi[fT]] += 1
        ga[Phi[fT][0]] += 1
    M2_pairs = sum(v*v for v in gp.values())
    M2_a1 = sum(v*v for v in ga.values())
    # direct off-diagonal e-histogram from VxV (within equal-prefix fibers)
    hist = defaultdict(int)
    top_const_ok = True
    emin_ok = True
    for z, members in gp.items():
        if members < 2:
            continue
        Ts = [fT for fT in V if Phi[fT] == z]
        for T1 in Ts:
            for T2 in Ts:
                if T1 == T2:
                    continue
                e = len(T1 - T2)
                hist[e] += 1
                if e < w + 2:
                    emin_ok = False
                Ap = poly_from_roots(sorted(T1 - T2), p)
                Bp = poly_from_roots(sorted(T2 - T1), p)
                dd = poly_diff_deg(Ap, Bp, p)
                if dd > e - w - 2:
                    emin_ok = False
                if e == w + 2:
                    # must be nonzero constant shift
                    if dd != 0:
                        top_const_ok = False
    emax_bound = min(m, n - m)
    e_range_ok = all(e <= emax_bound for e in hist)
    # RHS: bucketed enumeration of sp^Gamma(e;R)
    sp_sum = defaultdict(int)
    sp_sum_naive = defaultdict(int) if do_naive_rhs else None
    top_pairs_examples = []
    for e in range(w + 2, emax_bound + 1):
        rsize = m - e
        for R in itertools.combinations(D, rsize):
            Rset = frozenset(R)
            rest = sorted(Dset - Rset)
            # bucket key = first min(w+2, e+1) descending coefficients of l_P
            klen = min(w + 2, e + 1)
            buckets = defaultdict(list)
            for P in itertools.combinations(rest, e):
                cP = poly_from_roots(P, p)
                fP = frozenset(P)
                valid = (Rset | fP) in Vset
                buckets[cP[:klen]].append((fP, cP, valid))
            for key, items in buckets.items():
                for (fP, cP, validP) in items:
                    if not validP:
                        continue
                    for (fQ, cQ, validQ) in items:
                        if fP == fQ or (fP & fQ):
                            continue
                        sp_sum[e] += 1
                        if e == w + 2 and len(top_pairs_examples) < 4:
                            c = (cP[-1] - cQ[-1]) % p
                            top_pairs_examples.append((sorted(fP), sorted(fQ), c))
            if do_naive_rhs:
                # honest full-pair enumeration with real difference polynomials
                Ps = [(frozenset(P), poly_from_roots(P, p)) for P in itertools.combinations(rest, e)]
                for fP, cP in Ps:
                    if not ((Rset | fP) in Vset):
                        continue
                    for fQ, cQ in Ps:
                        if fP == fQ or (fP & fQ):
                            continue
                        if poly_diff_deg(cP, cQ, p) <= e - w - 2:
                            sp_sum_naive[e] += 1
    offdiag = sum(sp_sum.values())
    rhs = S1 + offdiag
    # constraint-(i) equivalence on all ordered pairs (honest difference polys)
    ci_ok = True
    if do_constraint_i:
        allT = list(Phi.keys())
        for i, T1 in enumerate(allT):
            for T2 in allT:
                if T1 == T2:
                    continue
                d = poly_diff_deg(Lpoly[T1], Lpoly[T2], p)
                lhs = (d <= m - w - 2)
                rhseq = (Phi[T1] == Phi[T2])
                if lhs != rhseq:
                    ci_ok = False
    # aug-locator gate (C-g)
    aug_ok = True
    if do_aug_gate:
        for fT, c in Lpoly.items():
            a1 = c[1]
            r = (a1 - zstar[0]) % p
            # (X-r)*l_T descending coeffs
            cc = list(c)
            full = [ (cc[i] - r * (cc[i-1] if i >= 1 else 0)) % p for i in range(len(cc)) ] + [(-r * cc[-1]) % p]
            topw1 = tuple(full[1:depth+1])
            lhs = (fT in Vset)
            rhseq = (topw1 == tuple(z % p for z in zstar))
            if lhs != rhseq:
                aug_ok = False
    ok_a = (M2_def == M2_pairs == M2_a1)
    ok_b = (M2_def == rhs)
    ok_c = all(hist.get(e, 0) == sp_sum.get(e, 0) for e in set(hist) | set(sp_sum))
    ok_d = top_const_ok and emin_ok and e_range_ok
    ok_naive = (sp_sum_naive is None) or (dict(sp_sum_naive) == dict(sp_sum))
    edge_ok = (not expect_edge) or (S1 > 0 and M2_def == S1 and emax_bound < w + 2)
    print(f"  S1={S1}  M2_def={M2_def}  M2_pairs={M2_pairs}  M2_a1={M2_a1}  RHS=S1+{offdiag}={rhs}")
    print(f"  strata sp_sum={dict(sorted(sp_sum.items()))}  direct hist={dict(sorted(hist.items()))}")
    if top_pairs_examples:
        print(f"  top-stratum examples (P, P', c=const shift): {top_pairs_examples[:2]}")
    print(f"  gates: C-a={ok_a} C-b={ok_b} C-c={ok_c} C-d={ok_d} naive==bucket={ok_naive}"
          + (f" constraint-i={ci_ok}" if do_constraint_i else "")
          + (f" aug={aug_ok}" if do_aug_gate else "")
          + (f" edge={edge_ok}" if expect_edge else "")
          + f"  ({time.time()-t0:.1f}s)")
    return dict(S1=S1, M2=M2_def, offdiag=offdiag, top=sp_sum.get(w+2, 0),
                deep=sum(v for e, v in sp_sum.items() if e > w + 2),
                ok=ok_a and ok_b and ok_c and ok_d and ok_naive and ci_ok and edge_ok,
                aug_ok=aug_ok)

def main():
    rows = []
    # R7 planted z* construction: n=8,m=5,w=2 (edge: w+2=4 > min(5,3)=3), guarantee S1>0
    p7, n7, m7, w7 = 97, 8, 5, 2
    D7 = mu_n(p7, n7)
    T0 = tuple(D7[:m7])
    c0 = poly_from_roots(T0, p7)
    a = c0[1:w7+2]
    z1 = (a[0] - 1) % p7
    z7 = [z1] + [ (a[j] - a[j-1]) % p7 for j in range(1, w7+1) ]
    rows.append(("R1", 97, 8, 4, 2, (0,0,0), True, True, True, False))
    rows.append(("R2", 97, 8, 4, 2, (3,1,4), True, True, True, False))
    rows.append(("R3", 97, 8, 4, 1, (0,0), True, True, True, False))
    rows.append(("R4", 97, 8, 4, 1, (5,9), True, True, True, False))
    rows.append(("R5", 13, 12, 5, 2, (0,0,0), True, False, True, False))
    rows.append(("R6", 13, 12, 5, 2, (2,7,1), True, False, True, False))
    rows.append(("R7", p7, n7, m7, w7, tuple(z7), True, False, True, True))
    rows.append(("R8", 113, 16, 4, 1, (7,11), False, False, False, False))
    # R9/R10: STRENGTHENED (added criterion N3'): z* != 0 rows constructed to contain an
    # equal-prefix multi-member fiber, so the off-diagonal ledger is exercised at z* != 0.
    # Construction: pick a full-prefix fiber (over all of B^{w+1}) with >=2 members and
    # prefix a; set z*_1 = a_1 - 1, z*_j = a_j - (a_1 - z*_1) a_{j-1} = a_j - a_{j-1};
    # then every member is valid at this z*. Assert z* != 0.
    def planted_pair_zstar(p, n, m, w):
        from collections import defaultdict as dd
        D = mu_n(p, n)
        fibs = dd(list)
        for T in itertools.combinations(D, m):
            c = poly_from_roots(T, p)
            fibs[tuple(c[1:w+2])].append(T)
        best = None
        for a, Ts in sorted(fibs.items()):
            if len(Ts) >= 2:
                z = [(a[0] - 1) % p] + [ (a[j] - a[j-1]) % p for j in range(1, w+1) ]
                if any(zi != 0 for zi in z):
                    best = tuple(z)
                    break
        assert best is not None
        return best
    z9 = planted_pair_zstar(97, 8, 4, 1)
    z10 = planted_pair_zstar(13, 12, 5, 1)
    rows.append(("R9", 97, 8, 4, 1, z9, True, False, True, False))
    rows.append(("R10", 13, 12, 5, 1, z10, True, False, True, False))
    results = []
    all_ok = True
    aug_all = True
    for (name, p, n, m, w, z, naive, ci, aug, edge) in rows:
        r = run_row(name, p, n, m, w, z, naive, ci, aug, edge)
        results.append((name, r))
        all_ok = all_ok and r["ok"]
        aug_all = aug_all and r["aug_ok"]
    # non-vacuity (C-f)
    n2 = sum(1 for _, r in results if r["S1"] > 0)
    n3 = sum(1 for _, r in results if r["offdiag"] > 0)
    n4 = sum(1 for _, r in results if r["top"] > 0)
    n5 = sum(1 for _, r in results if r["deep"] > 0)
    zx = {name: z for (name, p, n, m, w, z, *_ ) in rows}
    n3p = sum(1 for name, r in results
              if r["offdiag"] > 0 and any(v != 0 for v in zx[name]))
    print(f"\nNon-vacuity: rows with S1>0: {n2} (need>=5); offdiag>0: {n3} (need>=2); "
          f"top>0: {n4} (need>=1); deep(e>w+2)>0: {n5} (need>=1); "
          f"z*!=0 with offdiag>0: {n3p} (need>=1)")
    nv = (n2 >= 5 and n3 >= 2 and n4 >= 1 and n5 >= 1 and n3p >= 1)
    print(f"aug-locator gate (C-g, flag-only): {'PASS' if aug_all else 'FLAG'}")
    verdict = "CONFIRMED" if (all_ok and nv) else "NOT-CONFIRMED"
    print(f"\nVERDICT (pre-registered criteria): {verdict}")
    return 0 if (all_ok and nv) else 1

if __name__ == "__main__":
    sys.exit(main())
