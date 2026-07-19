#!/usr/bin/env python3
"""Fresh independent brute-force cross-check of list_subsqrt_interleaving_collapse.

Theorem under test (Codex branch, commit 0933bb9):
  C <= F^n linear, q=|F|, threshold a, L = max_u #{c in C : agr(c,u) >= a}.
  L_m = max over U in (F^n)^m of #{(c_1..c_m) in C^m :
        |{j : c_i[j]==u_i[j] for ALL i}| >= a}   (common support).
  If 1 <= L < q then L <= L_m <= floor(L(q-1)/(q-L)); if L^2 < q then L_m = L.

Written from the statement alone; no code shared with the Codex packet.
"""
import itertools, sys
from math import comb, floor

def all_subspaces(q, n, k):
    """All distinct k-dim subspaces of F_q^n as sorted tuples of codewords."""
    vecs = list(itertools.product(range(q), repeat=n))
    def add(u, v): return tuple((a + b) % q for a, b in zip(u, v))
    def smul(s, u): return tuple((s * a) % q for a in u)
    seen = set()
    out = []
    nz = [v for v in vecs if any(v)]
    for gens in itertools.combinations(nz, k):
        # span
        span = {tuple([0]*n)}
        for g in gens:
            newspan = set()
            for s in range(q):
                sg = smul(s, g)
                for w in span:
                    newspan.add(add(w, sg))
            span = newspan
        if len(span) != q**k:
            continue  # dependent generators
        key = tuple(sorted(span))
        if key not in seen:
            seen.add(key)
            out.append(key)
    return out

def masks_for(code, words, a_dummy=None):
    """mask[u_idx][c_idx] = bitmask of agreement positions."""
    n = len(words[0])
    M = []
    for u in words:
        row = []
        for c in code:
            m = 0
            for j in range(n):
                if c[j] == u[j]:
                    m |= (1 << j)
            row.append(m)
        M.append(row)
    return M

POP = [bin(x).count("1") for x in range(1 << 10)]

def base_L(M, a):
    return max(sum(1 for m in row if POP[m] >= a) for row in M)

def counters(M, n):
    """Per received word: dict mask -> multiplicity over codewords."""
    out = []
    for row in M:
        d = {}
        for m in row:
            d[m] = d.get(m, 0) + 1
        out.append(list(d.items()))
    return out

def interleaved_L(M, n, a, m):
    """Exact L_m by enumeration over all received m-tuples (common support)."""
    C = counters(M, n)
    W = len(C)
    best = 0
    if m == 2:
        for i in range(W):
            ci = C[i]
            for j in range(W):
                cj = C[j]
                tot = 0
                for m1, k1 in ci:
                    for m2, k2 in cj:
                        if POP[m1 & m2] >= a:
                            tot += k1 * k2
                if tot > best:
                    best = tot
    elif m == 3:
        for i in range(W):
            ci = C[i]
            for j in range(W):
                cj = C[j]
                # pre-merge rows i,j
                merged = {}
                for m1, k1 in ci:
                    for m2, k2 in cj:
                        mm = m1 & m2
                        merged[mm] = merged.get(mm, 0) + k1 * k2
                merged = list(merged.items())
                for l in range(W):
                    cl = C[l]
                    tot = 0
                    for m12, k12 in merged:
                        for m3, k3 in cl:
                            if POP[m12 & m3] >= a:
                                tot += k12 * k3
                    if tot > best:
                        best = tot
    else:
        raise ValueError
    return best

def interleaved_L_separate(M, n, a, m):
    """Mutation-control object: SEPARATE supports (each row agrees >= a on
    its own set). Equals product of per-row list maxima."""
    L = base_L(M, a)
    return L ** m

def run_grid():
    theorem_checks = 0
    collapse_checks = 0
    growth_instances = []   # L_m > L (allowed only when L^2 >= q)
    violations = []
    grid = []
    # exhaustive tiny grids
    for q, n, ks, ms in [
        (2, 2, (1,), (2, 3)),
        (2, 3, (1, 2), (2, 3)),
        (3, 2, (1,), (2, 3)),
        (3, 3, (1, 2), (2,)),
        (3, 3, (1,), (3,)),
        (5, 2, (1,), (2, 3)),
        (5, 3, (1, 2), (2,)),
        (7, 2, (1,), (2,)),
    ]:
        grid.append((q, n, ks, ms))
    for q, n, ks, ms in grid:
        words = list(itertools.product(range(q), repeat=n))
        for k in ks:
            for code in all_subspaces(q, n, k):
                M = masks_for(code, words)
                for a in range(1, n + 1):
                    L = base_L(M, a)
                    if not (1 <= L < q):
                        continue
                    ub = floor(L * (q - 1) / (q - L))
                    for m in ms:
                        Lm = interleaved_L(M, n, a, m)
                        theorem_checks += 1
                        if not (L <= Lm <= ub):
                            violations.append((q, n, k, a, m, L, Lm, ub, code))
                        if L * L < q:
                            collapse_checks += 1
                            if Lm != L:
                                violations.append(
                                    ("COLLAPSE", q, n, k, a, m, L, Lm, code))
                        if Lm > L:
                            growth_instances.append((q, n, k, a, m, L, Lm, ub))
    print(f"theorem inequality checks: {theorem_checks}")
    print(f"collapse (L^2<q) equality checks: {collapse_checks}")
    print(f"violations: {len(violations)}")
    for v in violations[:10]:
        print("  VIOLATION:", v)
    print(f"growth instances (L_m > L, requires L^2>=q): {len(growth_instances)}")
    for g in growth_instances[:8]:
        print("  growth:", g)
    return violations, growth_instances

def mutation_controls(growth_instances):
    """(a) mutated claim 'L_m = L always' must be falsified by some instance;
       (b) separate-support hypothesis mutation must break the collapse;
       (c) harness self-test: perturbed L_m must trip the checker."""
    ok_a = len(growth_instances) > 0
    print(f"MUTATION (a) [claim 'L_m=L even when L^2>=q' falsified in-grid]: "
          f"{'FIRED' if ok_a else 'NOT FIRED (grid too small)'}")

    # (b) separate-support on a collapse-regime instance with L >= 2
    q, n, k = 5, 2, 1
    words = list(itertools.product(range(q), repeat=n))
    fired_b = None
    for code in all_subspaces(q, n, k):
        M = masks_for(code, words)
        for a in range(1, n + 1):
            L = base_L(M, a)
            if 2 <= L and L * L < q:
                Lsep = interleaved_L_separate(M, n, a, 2)
                ub = floor(L * (q - 1) / (q - L))
                if Lsep > L:
                    fired_b = (q, n, k, a, L, Lsep, ub)
                    break
        if fired_b:
            break
    print(f"MUTATION (b) [separate-support breaks collapse]: "
          f"{'FIRED ' + str(fired_b) if fired_b else 'NOT FIRED'}")

    # (c) checker self-test: inject +1 into L_m on a collapse instance
    q, n, k = 5, 2, 1
    code = all_subspaces(q, n, k)[0]
    M = masks_for(code, words)
    tripped = False
    for a in range(1, n + 1):
        L = base_L(M, a)
        if 1 <= L < q and L * L < q:
            Lm = interleaved_L(M, n, a, 2) + 1  # inject fault
            if Lm != L:
                tripped = True
                break
    print(f"MUTATION (c) [harness detects injected L_m fault]: "
          f"{'FIRED' if tripped else 'NOT FIRED'}")

if __name__ == "__main__":
    v, g = run_grid()
    mutation_controls(g)
    sys.exit(1 if v else 0)
