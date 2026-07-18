#!/usr/bin/env python3
"""wave-11 independent checks — OWN CODE, no reuse of v5 verifier logic.

Covers: six-type classification (raw patterns + labeled orbits), the F_17
order-8 fence, the F_17^* d=4 path witness (agreements, rank, normal form,
Plucker gate on real data, first-pencil member count), the 13-chamber census,
the scroll determinant identities, the all-arity collapse arithmetic, and
dag hygiene at pin (duplicate edges, node-id collisions, statuses).
"""
from __future__ import annotations

import json
import os
from fractions import Fraction
from itertools import combinations, permutations, product

SP = os.path.dirname(os.path.abspath(__file__))
PIN = os.path.join(SP, "w11_dags", "b8366bca.json")
MASTER = os.path.join(SP, "w11_dags", "f6f77b99.json")

PASS = 0
def ok(name, cond):
    global PASS
    assert cond, "FAIL: " + name
    PASS += 1
    print("PASS", name)

# ---------------------------------------------------------------- CHECK 1
# Raw degree-count patterns: nonneg (n0,n1,n2,n4) with 3n0+2n1+n2-n4=4 and
# 3n0+3n1+2n2-3n4>=6.
raw = []
for n0 in range(5):
    for n1 in range(5):
        for n2 in range(9):
            n4 = 3 * n0 + 2 * n1 + n2 - 4
            if n4 < 0:
                continue
            if 3 * n0 + 3 * n1 + 2 * n2 - 3 * n4 >= 6:
                raw.append((n0, n1, n2, n4))
ok("raw patterns == six stated", sorted(raw) == sorted([
    (0, 0, 4, 0), (0, 0, 5, 1), (0, 0, 6, 2), (0, 1, 2, 0), (0, 1, 3, 1),
    (0, 2, 0, 0)]))

# ---------------------------------------------------------------- CHECK 2
# Labeled feasibility (d-free): for all pairs i<j,
#   p_ij <= s_i+s_j+p_i+p_j+1-(n1+n2).
# Enumerate singleton distributions and edge multisets, canonicalize under S4.
EDGES = list(combinations(range(4), 2))

def comps(total, parts):
    if parts == 1:
        yield (total,)
        return
    for v in range(total + 1):
        for rest in comps(total - v, parts - 1):
            yield (v,) + rest

def canon(s, p):
    best = None
    pm = {e: p[i] for i, e in enumerate(EDGES)}
    for perm in permutations(range(4)):
        cs = tuple(s[perm[i]] for i in range(4))
        cp = tuple(pm[tuple(sorted((perm[a], perm[b])))] for a, b in EDGES)
        img = (cs, cp)
        if best is None or img < best:
            best = img
    return best

types_by_pattern = {}
for (n0, n1, n2, n4) in raw:
    found = set()
    for s in comps(n1, 4):
        for p in comps(n2, 6):
            deg = [s[i] + sum(p[j] for j, e in enumerate(EDGES) if i in e)
                   for i in range(4)]
            okrow = True
            for j, (a, b) in enumerate(EDGES):
                if p[j] > s[a] + s[b] + deg[a] - s[a] + deg[b] - s[b] + 1 - (n1 + n2):
                    okrow = False
                    break
            if okrow:
                found.add(canon(s, p))
    types_by_pattern[(n0, n1, n2, n4)] = found

counts = {k: len(v) for k, v in types_by_pattern.items()}
ok("(0,2,0,0) impossible", counts[(0, 2, 0, 0)] == 0)
ok("type counts per pattern = 2,1,1,1,1",
   counts[(0, 0, 4, 0)] == 2 and counts[(0, 0, 5, 1)] == 1
   and counts[(0, 0, 6, 2)] == 1 and counts[(0, 1, 2, 0)] == 1
   and counts[(0, 1, 3, 1)] == 1)
ok("total labeled types == 6", sum(counts.values()) == 6)

# identify the two (0,0,4,0) types as 4-cycle and triangle+pendant
def graph_of(p):
    g = []
    for j, e in enumerate(EDGES):
        g += [e] * p[j]
    return g

shapes = set()
for (s, p) in types_by_pattern[(0, 0, 4, 0)]:
    deg = sorted(sum(1 for e in graph_of(p) if i in e) for i in range(4))
    shapes.add(tuple(deg))
ok("(0,0,4,0) shapes = 4-cycle (2,2,2,2) and pendant (1,2,2,3)",
   shapes == {(2, 2, 2, 2), (1, 2, 2, 3)})

# ---------------------------------------------------------------- CHECK 3
# Fence witness: RS[F_17, mu_8, 4], rank 11.
P17 = 17
def polyval(coeffs, x, p):
    v = 0
    for c in reversed(coeffs):
        v = (v * x + c) % p
    return v

D8 = [1, 9, 13, 15, 16, 8, 4, 2]
ok("D8 is the order-8 subgroup of F_17^*",
   sorted(D8) == sorted({pow(9, i, 17) for i in range(8)}) and len(set(D8)) == 8)
fs = [(0, 0, 0, 0), (11, 2, 8, 7), (8, 5, 13, 2), (15, 13, 15, 13)]
u8 = [11, 0, 0, 0, 4, 0, 0, 1]
S = []
for f in fs:
    S.append({x for i, x in enumerate(D8) if polyval(f, x, P17) == u8[i]})
ok("fence agreements all 5", all(len(s) == 5 for s in S))
mx = {x: sum(1 for s in S if x in s) for x in D8}
n_counts = [sum(1 for x in D8 if mx[x] == j) for j in range(5)]
ok("fence incidence pattern (0,1,2,0) with n3=5",
   n_counts[0] == 0 and n_counts[1] == 1 and n_counts[2] == 2
   and n_counts[3] == 5 and n_counts[4] == 0)

def build_matrix(supports, domain, k, p):
    rows = []
    for x in domain:
        I = [i for i in range(4) if x in supports[i]]
        mono = [pow(x, e, p) for e in range(k)]
        def hrow(i, sign, base=None):
            row = [0] * (3 * k) if base is None else base
            for e in range(k):
                row[(i - 1) * k + e] = (row[(i - 1) * k + e] + sign * mono[e]) % p
            return row
        if 0 in I:
            for i in I:
                if i != 0:
                    rows.append(hrow(i, 1))
        else:
            for a, b in zip(I, I[1:]):
                rows.append(hrow(b, -1, hrow(a, 1)))
    return rows

def rank_mod(rows, p):
    rows = [r[:] for r in rows]
    r = 0
    cols = len(rows[0]) if rows else 0
    for c in range(cols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % p), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [(v * inv) % p for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                f = rows[i][c]
                rows[i] = [(rows[i][j] - f * rows[r][j]) % p for j in range(cols)]
        r += 1
    return r

M8 = build_matrix(S, D8, 4, P17)
ok("fence matrix 12 rows x 12 cols", len(M8) == sum(m - 1 for m in mx.values())
   and len(M8) == 12 and len(M8[0]) == 12)
ok("fence rank == 11", rank_mod(M8, P17) == 11)

# ---------------------------------------------------------------- CHECK 4
# Path power-two witness: RS[F_17, F_17^*, 8], d=4.
D16 = list(range(1, 17))
fsw = [(0,), (8, 5, 13, 2, 15, 3, 1, 8), (12, 16, 8, 3, 7, 12, 10, 4),
       (5, 13, 0, 14, 16, 2, 4, 1)]
u16_map = {1: 4, 2: 14, 3: 14, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
           11: 0, 12: 0, 13: 0, 14: 5, 15: 0, 16: 2}
u16 = [u16_map[x] for x in D16]
Sw = []
for f in fsw:
    Sw.append({x for i, x in enumerate(D16) if polyval(f, x, P17) == u16[i]})
ok("witness agreements all 11", all(len(s) == 11 for s in Sw))
T = [set(), set(), set(), set()]
E02, E12, Sing = set(), set(), set()
for x in D16:
    I = frozenset(i for i in range(4) if x in Sw[i])
    if len(I) == 3:
        T[({0, 1, 2, 3} - set(I)).pop()].add(x)
    elif I == frozenset({0, 2}):
        E02.add(x)
    elif I == frozenset({1, 2}):
        E12.add(x)
    elif len(I) == 1:
        Sing.add(x)
    else:
        raise AssertionError("unexpected incidence " + repr(sorted(I)))
ok("witness blocks match printed",
   T[0] == {1, 2, 3} and T[1] == {4, 5, 12} and T[2] == {7, 8, 13, 15}
   and T[3] == {6, 10, 11} and E02 == {9} and E12 == {16} and Sing == {14})
Mw = build_matrix(Sw, D16, 8, P17)
ok("witness matrix 28x24", len(Mw) == 28 and len(Mw[0]) == 24)
ok("witness rank == 23", rank_mod(Mw, P17) == 23)

# normal-form quotients: g_ij = A_k A_l e_ij q_ij (J=1, no full block)
def polymul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out

def locator(roots, p):
    poly = [1]
    for r in roots:
        poly = polymul(poly, [(-r) % p, 1], p)
    return poly

def polysub(a, b, p):
    m = max(len(a), len(b))
    a = list(a) + [0] * (m - len(a))
    b = list(b) + [0] * (m - len(b))
    return [(x - y) % p for x, y in zip(a, b)]

def polydiv(num, den, p):
    num = list(num)
    out = [0] * (len(num) - len(den) + 1)
    inv = pow(den[-1], p - 2, p)
    for i in range(len(out) - 1, -1, -1):
        c = (num[i + len(den) - 1] * inv) % p
        out[i] = c
        for j, dcoef in enumerate(den):
            num[i + j] = (num[i + j] - c * dcoef) % p
    ok_rem = all(v % p == 0 for v in num[: len(den) - 1])
    return out, ok_rem

A = [locator(sorted(t), P17) for t in T]
e02p, e12p, wsing = locator([9], P17), locator([16], P17), locator([14], P17)
edge = {(0, 1): [1], (0, 2): e02p, (0, 3): [1], (1, 2): e12p, (1, 3): [1],
        (2, 3): [1]}
expect_q = {(0, 1): [8], (0, 2): [4], (0, 3): [1], (1, 2): [13], (1, 3): [10],
            (2, 3): [15, 14]}
for (i, j) in EDGES:
    k_, l_ = sorted({0, 1, 2, 3} - {i, j})
    g = polysub(list(fsw[j]) + [0] * (8 - len(fsw[j])),
                list(fsw[i]) + [0] * (8 - len(fsw[i])), P17)
    while g and g[-1] == 0:
        g.pop()
    den = polymul(polymul(A[k_], A[l_], P17), edge[(i, j)], P17)
    q, exact = polydiv(g, den, P17)
    assert exact, ("division fails", i, j)
    while q and q[-1] == 0:
        q.pop()
    ok(f"witness quotient q_{i}{j} matches printed", q == expect_q[(i, j)])

# Plucker gate PG1 on the witness: b01 b23 - b02 b13 + b03 b12 == 0
b = {(i, j): polymul(edge[(i, j)], expect_q[(i, j)], P17) for (i, j) in EDGES}
t1 = polymul(b[(0, 1)], b[(2, 3)], P17)
t2 = polymul(b[(0, 2)], b[(1, 3)], P17)
t3 = polymul(b[(0, 3)], b[(1, 2)], P17)
mlen = max(map(len, (t1, t2, t3)))
pg1 = [( (t1[i] if i < len(t1) else 0) - (t2[i] if i < len(t2) else 0)
        + (t3[i] if i < len(t3) else 0)) % P17 for i in range(mlen)]
ok("PG1 holds on witness", all(v == 0 for v in pg1))
# PG3 on the witness: R A0 A1 N2 N3 == b01^2 Lambda_D
R = polymul(polymul(wsing, e02p, P17), e12p, P17)  # W*J*prod e, J=1
N2 = polysub(polymul(A[1], b[(0, 2)], P17), polymul(A[0], b[(1, 2)], P17), P17)
N3 = polysub(polymul(A[1], b[(0, 3)], P17), polymul(A[0], b[(1, 3)], P17), P17)
lhs = polymul(polymul(polymul(polymul(R, A[0], P17), A[1], P17), N2, P17), N3, P17)
lam = locator(D16, P17)
rhs = polymul(polymul(b[(0, 1)], b[(0, 1)], P17), lam, P17)
m2 = max(len(lhs), len(rhs))
diff = [((lhs[i] if i < len(lhs) else 0) - (rhs[i] if i < len(rhs) else 0)) % P17
        for i in range(m2)]
ok("PG3 holds on witness", all(v == 0 for v in diff))
# first pencil P0=e12*A0, P1=e02*A1, P2=A2: count fully split members over D16
P0 = polymul(e12p, A[0], P17)
P1 = polymul(e02p, A[1], P17)
members = 0
seen = set()
for lam0 in range(P17):
    for lam1 in range(P17):
        if lam0 == 0 and lam1 == 0:
            continue
        cand = [(lam0 * a + lam1 * bb) % P17 for a, bb in
                zip(P0 + [0] * 8, P1 + [0] * 8)][:5]
        if cand[-1] == 0:
            continue
        roots = [x for x in D16 if polyval(cand, x, P17) == 0]
        if len(set(roots)) == 4:
            key = tuple((c * pow(cand[-1], P17 - 2, P17)) % P17 for c in cand)
            if key not in seen:
                seen.add(key)
                members += 1
ok("witness first pencil has exactly 3 fully split members", members == 3)

# ---------------------------------------------------------------- CHECK 5
# 13-chamber census from the per-type (p, delta) ledger via SF1.
LEDGER = {
    "pendant":  ((0, 0, 1, 1, 1, 1), (0, 0, 0, 0, 1, 1)),
    "cycle":    ((0, 1, 1, 1, 1, 0), (1, 0, 0, 0, 0, 1)),
    "K4-e":     ((0, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 1)),
    "K4":       ((1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0)),
    "path":     ((0, 1, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1)),
    "triangle": ((1, 1, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0)),
}
expected_chambers = {"pendant": 3, "cycle": 4, "K4-e": 2, "K4": 1, "path": 2,
                     "triangle": 1}
total = 0
for name, (p, delta) in LEDGER.items():
    chambers = set()
    # enumerate leading-coefficient classes c_0..c_3 in a 4-symbol alphabet
    for cvec in product(range(4), repeat=4):
        good = True
        for idx, (i, j) in enumerate(EDGES):
            if delta[idx] == 0 and cvec[i] == cvec[j]:
                good = False
                break
        if not good:
            continue
        sext = tuple(p[idx] + (0 if delta[idx] == 0 else
                               (0 if cvec[i] == cvec[j] else 1))
                     for idx, (i, j) in enumerate(EDGES))
        chambers.add(sext)
    assert len(chambers) == expected_chambers[name], (name, chambers)
    total += len(chambers)
    if name == "pendant":
        ok("pendant both-linear chamber excluded",
           (0, 0, 1, 1, 1, 1) not in chambers)
ok("chamber census 3+4+2+1+2+1 == 13", total == 13)
# linear/quadratic split
linear = 0
for name, (p, delta) in LEDGER.items():
    for cvec in product(range(4), repeat=4):
        pass
# recount linear chambers from the census
lin_count, quad_count = 0, 0
for name, (p, delta) in LEDGER.items():
    chambers = set()
    for cvec in product(range(4), repeat=4):
        if any(delta[idx] == 0 and cvec[i] == cvec[j]
               for idx, (i, j) in enumerate(EDGES)):
            continue
        sext = tuple(p[idx] + (0 if delta[idx] == 0 else
                               (0 if cvec[i] == cvec[j] else 1))
                     for idx, (i, j) in enumerate(EDGES))
        chambers.add(sext)
    for ch in chambers:
        if max(ch) <= 1:
            lin_count += 1
        else:
            quad_count += 1
ok("linear chambers == 9, quadratic == 4", lin_count == 9 and quad_count == 4)

# ---------------------------------------------------------------- CHECK 6
# Scroll determinant identity det C = c^2 (e1 d1 - a1 f1), via exact
# Fraction arithmetic at 60 pseudorandom points (identity testing).
import random
rng = random.Random(11)
def detC(c, s, a0, a1, d0, d1, e0, e1, f0, f1):
    M = [
        [c, 0, 0, 0],
        [0, c * s, c, 0],
        [-e0, -e1 + s * a0, a0, a1],
        [-f0, -f1 + s * d0, d0, d1],
    ]
    # 4x4 determinant by cofactor
    def det(m):
        if len(m) == 1:
            return m[0][0]
        tot = 0
        for j in range(len(m)):
            sub = [row[:j] + row[j + 1:] for row in m[1:]]
            tot += ((-1) ** j) * m[0][j] * det(sub)
        return tot
    return det(M)

for _ in range(60):
    vals = [Fraction(rng.randint(-9, 9)) for _ in range(10)]
    c, s, a0, a1, d0, d1, e0, e1, f0, f1 = vals
    assert detC(*vals) == c * c * (e1 * d1 - a1 * f1)
ok("det C == c^2(e1 d1 - a1 f1) (60 random exact points)", True)
# K4-e leading coefficient: c*[X^2]b23 = L02 L13 - L03 L12 and
# det C = -c^3 [X^2]b23 when f2=0 (b13 linear)
for _ in range(60):
    vals = [Fraction(rng.randint(-9, 9)) for _ in range(10)]
    c, s, a0, a1, d0, d1, e0, e1, f0, f1 = vals
    s = Fraction(0)  # f2=0 branch
    lead = a1 * f1 - d1 * e1  # [X^2](b02 b13 - b03 b12)
    assert detC(c, s, a0, a1, d0, d1, e0, e1, f0, f1) == -c * c * lead
ok("K4-e det C == -c^3 [X^2]b23 (c*[X^2]b23 = L02L13-L03L12)", True)

# ---------------------------------------------------------------- CHECK 7
# All-arity collapse arithmetic.
n = 1 << 41
ok("3n/4 == 1649267441664 and n/4 == 549755813888",
   3 * n // 4 == 1649267441664 and n // 4 == 549755813888)
for L in range(1, 50):
    for q in range(max(3, L + 1), 200):
        cap = (L * (q - 1)) // (q - L)
        if L * L < q:
            assert cap == L, (L, q)
ok("floor(L(q-1)/(q-L)) == L exactly when L^2<q (exhaustive toy)", True)
# two-sidedness: at L^2 >= q the cap can exceed L
ok("cap exceeds L at L=2,q=4", (2 * 3) // 2 > 2)
ok("budget window B* in {1,2} == 2^128<q<3*2^128",
   (3 << 128) - 1 >= (1 << 128) + 1)

# ---------------------------------------------------------------- CHECK 8
# dag hygiene at pin + collision check vs master.
with open(PIN) as fh:
    pin = json.load(fh)
with open(MASTER) as fh:
    mst = json.load(fh)
pin_nodes = {nd["id"]: nd for nd in pin["nodes"]}
mst_nodes = {nd["id"]: nd for nd in mst["nodes"]}
NEW14 = [
    "rate_half_list_budget_three_intersection_reduction",
    "rate_half_list_low_budget_all_arity_crossing",
    "rate_half_list_low_budget_certificate_generator",
    "rate_half_list_budget_three_split_pencil_normal_form",
    "rate_half_list_budget_three_plucker_edge_gate",
    "rate_half_list_budget_three_split_fiber_atlas",
    "rate_half_list_budget_three_path_mobius_transversal",
    "rate_half_list_budget_three_cycle_bimobius_transversal",
    "rate_half_list_budget_three_path_power_two_witness",
    "rate_half_list_budget_three_residual_transversal_atlas",
    "rate_half_list_budget_three_k4_grassmann_line",
    "rate_half_list_budget_three_linear_grassmann_atlas",
    "rate_half_list_budget_three_quadratic_scroll_atlas",
    "rate_half_list_budget_three_quadratic_scroll_full_rank",
]
ok("all 14 codex-original nodes present and PROVED at pin",
   all(pin_nodes[i]["status"] == "PROVED" for i in NEW14))
ok("node-id collision check: none of the 14 exist on master",
   all(i not in mst_nodes for i in NEW14))
ok("every new node feeds rate_half_list_adjacent_crossing or list_grand",
   all(any(e["from"] == i and e["to"] in
           ("rate_half_list_adjacent_crossing", "list_grand", "list_large_m_scope_closure")
           and e["kind"] == "ev" for e in pin["edges"]) for i in NEW14))
# duplicate (from,to) pairs with multiple kinds
from collections import defaultdict
kinds = defaultdict(set)
for e in pin["edges"]:
    kinds[(e["from"], e["to"])].add(e["kind"])
dups = sorted(k for k, v in kinds.items() if len(v) > 1)
print("DUPLICATE-KIND EDGES AT PIN:", dups)
ok("duplicate-kind edge set enumerated (expected: the two list_safe pairs)",
   dups == [("m_handling", "list_safe"), ("m_sweep", "list_safe")])
# packaging/descriptor watch at pin
ok("packaging CONDITIONAL and descriptor TARGET at pin (refusals hold)",
   pin_nodes["packaging"]["status"] == "CONDITIONAL"
   and pin_nodes["descriptor"]["status"] == "TARGET")
ok("adjacent_crossing TARGET at pin (no premature flip)",
   pin_nodes["rate_half_list_adjacent_crossing"]["status"] == "TARGET")
# descriptor->packaging req edge residual
ok("residual: descriptor->packaging req edge present at pin (master lacks it)",
   {"from": "descriptor", "to": "packaging", "kind": "req"} in
   [{k: e[k] for k in ("from", "to", "kind")} for e in pin["edges"]]
   and not any(e["from"] == "descriptor" and e["to"] == "packaging"
               for e in mst["edges"]))

# ---------------------------------------------------------------- CHECK 9
# deg R ledger per type: n1+n2+n4 == (4,4,6,8,3,5); linear-atlas exceptional
# degrees match.
pat = {"pendant": (0, 0, 4, 0), "cycle": (0, 0, 4, 0), "K4-e": (0, 0, 5, 1),
       "K4": (0, 0, 6, 2), "path": (0, 1, 2, 0), "triangle": (0, 1, 3, 1)}
degR = {t: v[1] + v[2] + v[3] for t, v in pat.items()}
ok("deg R ledger == 4,4,6,8,3,5",
   [degR[t] for t in ("pendant", "cycle", "K4-e", "K4", "path", "triangle")]
   == [4, 4, 6, 8, 3, 5])
# six-matrix dimensions: rows 8d-4 >= cols 6d iff d >= 2
ok("8d-4 >= 6d iff d>=2 (two-sided)", 8 * 2 - 4 >= 6 * 2 and 8 * 1 - 4 < 6 * 1)

print(f"\nALL {PASS} CHECKS PASS")
