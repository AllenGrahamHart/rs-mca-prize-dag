#!/usr/bin/env python3
"""w3 wave-3 audit: fresh in-vivo replay of the codex fiber-descent chain
against the BANKED census ground truth (cg_petal_census_results.json).

Checks per banked small-scale cell (M,A) with M | gcd(n,k):
  D1. rebuild the banked word; re-enumerate periodic contributors; per-cell
      (classes, codewords) must REPRODUCE the banked JSON exactly.
  D2. Fourier descent mechanics on every scale-M contributor f:
      residue decomposition f -> (f_0..f_{M-1}), deg f_r < k/M; descended
      word U'; the tuple's exact COMMON agreement set == S/K (both dirs).
  D3. injectivity of the map on the cell's contributors.
  D4. commit-2 claim: c(S)=M exactly => descended support APERIODIC in Z_{n/M}.
  D5. (8-rows only) EXACT interleaved common-support list L_M(U',A/M) by full
      enumeration; verify classes <= L_M; report L_M vs banked B719=719*Q.
  D6. ordinary quotient component lists and the aperiodic-filtered ordinary
      list L_P at agreement A/M (ESP consumables), reported.
"""
import itertools, json, sys
from math import comb
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/critical/nodes/petal_growth/notes")
from cg_petal_census import (order_n_domain, build_word, periodic_contributors,
                             classify_cell, ev, stab_order, is_prime)

GT = json.load(open("/home/u2470931/smooth-read-solomin/prize/critical/nodes/petal_growth/notes/cg_petal_census_results.json"))

def quotient_domain(dom, n, M, p):
    # H^M with representative exponents i (x_y = dom[i], y = dom[i]^M = dom[(M*i)%n])
    N = n // M
    reps = list(range(N))                      # exponent i -> y = g0^(M i)
    ys = [pow(dom[1], (M * i) % n, p) for i in range(N)]
    return reps, ys

def descend_word(values, dom, n, M, p):
    N = n // M
    zeta = pow(dom[1], n // M, p)              # generator of K (order M)
    invM = pow(M, -1, p)
    Uc = []                                    # Uc[i][r]
    for i in range(N):
        x = dom[i]
        fib = [values[(i + (n // M) * j) % n] for j in range(M)]  # U(zeta^j x)= exponent i + j*n/M
        row = []
        for r in range(M):
            s = 0
            for j in range(M):
                s += pow(zeta, (-j * r) % M and (M - (j * r) % M) or 0, p) * fib[j]
            # zeta^{-jr} = zeta^{M - (jr mod M)} careful: implement directly
            row.append(0)
        Uc.append(row)
    # redo cleanly with modular inverse powers
    zinv = pow(zeta, p - 2, p)
    Uc = []
    for i in range(N):
        x = dom[i]; xinv = pow(x, p - 2, p)
        fib = [values[(i + (n // M) * j) % n] for j in range(M)]
        row = []
        for r in range(M):
            s = sum(pow(zinv, j * r, p) * fib[j] for j in range(M)) % p
            row.append(s * invM % p * pow(xinv, r, p) % p)
        Uc.append(row)
    return Uc

def components(poly, k, M):
    K0 = k // M
    return [tuple(poly[r + M * s] if r + M * s < len(poly) else 0 for s in range(K0)) for r in range(M)]

def main():
    checked_cells = 0; d2 = d3 = d4 = 0; d5_rows = []
    mismatches = []
    for rec in GT:
        n, k, p, t = rec["n"], rec["k"], rec["p"], rec["t"]
        layout, seed, smode = rec["layout"], rec["seed"], rec["scalars"]
        if n > 16:  # RAM/time law: 8/16 rows here; 32-row mechanics identical
            continue
        dom = order_n_domain(p, n)
        values, core, petals, bg, scal = build_word(n, k, p, dom, layout, smode, seed)
        contr = periodic_contributors(n, k, 1, p, dom, values)
        classes = classify_cell(n, k, 1, petals, contr)
        # D1: reproduce banked fp0_all table
        mytab = {}
        for S, info in classes.items():
            key = f"{info['c']},{info['A']}"
            c = mytab.setdefault(key, [0, 0])
            c[0] += 1; c[1] += len(info["polys"])
        banked = {kk: (v["classes"], v["codewords"]) for kk, v in rec["fp0_all"].items()}
        mine = {kk: tuple(v) for kk, v in mytab.items()}
        if banked != mine:
            mismatches.append((n, k, p, layout, smode, seed, banked, mine)); continue
        # group contributors by cell
        for key, _ in mytab.items():
            M, A = map(int, key.split(","))
            if k % M or n % M: continue
            checked_cells += 1
            N, K0 = n // M, k // M
            _, ys = quotient_domain(dom, n, M, p)
            Uc = descend_word(values, dom, n, M, p)
            cell_polys = [(poly, S) for poly, S in contr.items()
                          if stab_order(S, n) == M and len(S) == A]
            seen = set()
            for poly, S in cell_polys:
                comps = components(list(poly) + [0]*(k-len(poly)), k, M)
                assert all(len(c) == K0 for c in comps)
                # D2: common agreement set == S/K
                Sbar = set()
                for i in range(N):
                    if all(ev(comps[r], ys[i], p) == Uc[i][r] for r in range(M)):
                        Sbar.add(i)
                fibS = {i for i in range(N) if all(((i + (n//M)*j) % n) in S for j in range(M))}
                if Sbar != fibS or len(Sbar) != A // M:
                    print("D2 FAIL", n,k,p,layout,smode,M,A,poly); return 1
                d2 += 1
                # D4: aperiodicity of Sbar in Z_N
                MM = 2; aper = True
                while MM <= N:
                    if all(((x + N//MM) % N) in Sbar for x in Sbar): aper = False; break
                    MM *= 2
                if not aper:
                    print("D4 FAIL (descended support periodic)", n,k,p,M,A); return 1
                d4 += 1
                if comps_t := tuple(comps):
                    if comps_t in seen: print("D3 FAIL inj", n,k,p,M,A); return 1
                    seen.add(comps_t)
            d3 += len(cell_polys)
            # D5: exact interleaved list on 8-rows (M=2, K0=2 -> p^4 tuples)
            if n == 8 and M == 2 and p <= 97:
                a_thr = A // M
                # enumerate quotient codewords deg<K0 as value vectors on ys
                qcw = []
                for coeffs in itertools.product(range(p), repeat=K0):
                    qcw.append(tuple(ev(coeffs, y, p) for y in ys))
                # per-component agreement masks
                masks = [[], []]
                for r in range(M):
                    tgt = [Uc[i][r] for i in range(N)]
                    for vals in qcw:
                        m = 0
                        for i in range(N):
                            if vals[i] == tgt[i]: m |= (1 << i)
                        masks[r].append(m)
                from collections import Counter
                c0 = Counter(masks[0]); c1 = Counter(masks[1])
                LM = 0; LM_exactP = 0
                for m0, n0 in c0.items():
                    for m1, n1 in c1.items():
                        inter = m0 & m1
                        if bin(inter).count("1") >= a_thr:
                            LM += n0 * n1
                Q = comb(N - 1, a_thr) if a_thr <= N-1 else 0
                d5_rows.append((n,k,p,layout,smode,seed,M,A,len(cell_polys),LM,719*Q))
                if len(cell_polys) > LM:
                    print("D5 FAIL: classes > exact interleaved list", n,k,p,M,A); return 1
    print(f"D1 reproduced banked tables: {'0 mismatches' if not mismatches else mismatches[:3]}")
    print(f"D2 descent common-support identity: {d2} contributors PASS")
    print(f"D3 injectivity: {d3} contributors PASS")
    print(f"D4 exact-scale => aperiodic descended support: {d4} PASS")
    print("D5 exact interleaved lists (8-rows, M=2): cell -> (classes, L_M(U'), B719)")
    for row in d5_rows[:12]:
        print("   ", row[:6], f"(M,A)=({row[6]},{row[7]})", "classes=", row[8], "L_M=", row[9], "B719=", row[10])
    print(f"D5 total cells with exact L_M: {len(d5_rows)}; all classes<=L_M")
    return 0

if __name__ == "__main__":
    sys.exit(main())
