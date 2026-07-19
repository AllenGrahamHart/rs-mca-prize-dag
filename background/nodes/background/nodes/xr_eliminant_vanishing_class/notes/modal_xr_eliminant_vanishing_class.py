#!/usr/bin/env python3
r"""
Modal dispatch job for node: xr_eliminant_vanishing_class.

============================ PRE-REGISTERED SPEC ============================
(quoted verbatim from prize/nodes/xr_eliminant_vanishing_class/statement.md)

  "The triple-level u5 dichotomy's structured branch: classify support/slope
   configurations where the light-triangle eliminant vanishes IDENTICALLY ...
   E32-extended enumerates ALL eliminant-vanishing light configurations at
   n = 16 exhaustively; the classification will be written along the observed
   cases ... coordinate-special stagnation means lying on a PROPER hypersurface
   inside the profile cell -- the remaining obligation is 'per pair, aligned
   light triples on an explicit proper hypersurface are rationed'."

  Falsifier: "an unpaid identically-vanishing configuration class at toys (the
   census reports it directly)."

  Banked (from the node ledger): E32-MERGED (profile level, 17/17) + E32-COORD
  (382,200 exact n=8 placements, 0 coordinate-special vanishings).  This job
  EXTENDS the exhaustive coordinate-level census from the banked n=8 to
  n = 9..13 across several primes -- the level the local machine could not reach
  ("already too large for this machine under the current RAM/runtime
  constraints", verify_e32_merged_census docstring).
============================================================================

CONSTRUCTION (faithful to the banked normal-form evaluator in
experimental/scripts/verify_e32_merged_census.py + verify_e32_coordinate_sliver.py):
  For a triple of size-A supports T0,T1,T2 in an n-point domain over F_p, each
  T carries the (A-k)-dim lambda-space chart (kernel words with fixed pivots).
  The light-triangle eliminant is the normal-form matrix stacking, per union
  coordinate, the three charts and their slope-scaled copies (slopes 1,2,3);
  normal_rank = 3t - rank.  A POSITIVE normal_rank inside a full-rank light
  profile is a coordinate-special ("identically vanishing") eliminant -- the
  falsifier.  The scan iterates all ordered light-budget support triples per row,
  skips profile-forced-defect profiles, and evaluates the pointwise eliminant.

CORRECTNESS GATE (banked E32-COORD n=8, must pass in-cloud before the scan):
  row coord_n8_k2_A4 (p=11) and coord_n8_k3_A4 (p=11) over domain 0..7:
  light triples > 0 and ZERO coordinate-special defects (reproduces the pinned
  e32_coordinate_sliver certificate result).

Self-contained (stdlib only).  One JSON line prefixed with the node name.
"""

import modal
import json
import time
from itertools import combinations, permutations
from dataclasses import dataclass

app = modal.App("rs-mca-xr_eliminant_vanishing_class")
image = modal.Image.debian_slim()


class Fp:
    def __init__(self, p):
        self.p = p

    def sub(self, a, b):
        return (a - b) % self.p

    def mul(self, a, b):
        return (a * b) % self.p

    def neg(self, a):
        return (-a) % self.p

    def inv(self, a):
        if a % self.p == 0:
            raise ZeroDivisionError
        return pow(a, self.p - 2, self.p)


def rref(F, rows_in):
    rows = [r[:] for r in rows_in]
    if not rows:
        return rows, [], 0
    ncols = len(rows[0])
    pivots = []
    rank = 0
    for col in range(ncols):
        piv = None
        for rr in range(rank, len(rows)):
            if rows[rr][col] % F.p:
                piv = rr
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = F.inv(rows[rank][col])
        rows[rank] = [F.mul(inv, x) for x in rows[rank]]
        for rr in range(len(rows)):
            if rr != rank and rows[rr][col] % F.p:
                c = rows[rr][col]
                rows[rr] = [F.sub(x, F.mul(c, y)) for x, y in zip(rows[rr], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return rows, pivots, rank


def rank_mat(F, rows):
    return rref(F, rows)[2]


def solve_square(F, A, b):
    aug = [row[:] + [rhs] for row, rhs in zip(A, b)]
    R, pivots, rnk = rref(F, aug)
    n = len(A)
    if rnk != n or pivots[:n] != list(range(n)):
        raise ValueError("singular chart")
    return [R[i][n] for i in range(n)]


def lambda_space_chart(F, domain, k, T):
    pivots = list(T[:k])
    free = list(T[k:])
    Vp = [[pow(domain[x], d, F.p) for x in pivots] for d in range(k)]
    basis = []
    for q in free:
        rhs = [F.neg(pow(domain[q], d, F.p)) for d in range(k)]
        pivot_values = solve_square(F, Vp, rhs)
        word = [0] * len(domain)
        for x, val in zip(pivots, pivot_values):
            word[x] = val
        word[q] = 1
        basis.append(word)
    return basis


def normal_rank(F, domain, k, supports):
    A = len(supports[0])
    t = A - k
    bases = [lambda_space_chart(F, domain, k, T) for T in supports]
    slopes = (1, 2, 3) if F.p != 17 else (1, 3, 5)
    union = sorted(set().union(*(set(T) for T in supports)))
    rows = []
    for coord in union:
        row = []
        for basis in bases:
            row.extend(lam[coord] for lam in basis)
        rows.append(row)
    for coord in union:
        row = []
        for z, basis in zip(slopes, bases):
            row.extend(F.mul(z, lam[coord]) for lam in basis)
        rows.append(row)
    got = rank_mat(F, rows)
    return 3 * t - got


@dataclass(frozen=True)
class Profile:
    h: int
    a: int
    b: int
    c: int
    x0: int
    x1: int
    x2: int
    outside: int

    @property
    def r01(self):
        return self.h + self.a

    @property
    def r02(self):
        return self.h + self.b

    @property
    def r12(self):
        return self.h + self.c

    @property
    def sigma(self):
        return 2 * self.h + self.a + self.b + self.c

    def budgets(self):
        return (2 * self.h + self.a + self.b,
                2 * self.h + self.a + self.c,
                2 * self.h + self.b + self.c)

    def as_dict(self):
        return {"h": self.h, "a": self.a, "b": self.b, "c": self.c,
                "x0": self.x0, "x1": self.x1, "x2": self.x2,
                "outside": self.outside, "sigma": self.sigma}


def realize_profile(P):
    sizes = (P.h, P.a, P.b, P.c, P.x0, P.x1, P.x2, P.outside)
    cells = []
    cur = 0
    for size in sizes:
        cells.append(list(range(cur, cur + size)))
        cur += size
    H, AB, AC, BC, X0, X1, X2, _ = cells
    T0 = tuple(sorted(H + AB + AC + X0))
    T1 = tuple(sorted(H + AB + BC + X1))
    T2 = tuple(sorted(H + AC + BC + X2))
    return T0, T1, T2


def profile_of_triple(n, triple):
    S0, S1, S2 = (set(T) for T in triple)
    h_set = S0 & S1 & S2
    a_set = (S0 & S1) - S2
    b_set = (S0 & S2) - S1
    c_set = (S1 & S2) - S0
    x0_set = S0 - S1 - S2
    x1_set = S1 - S0 - S2
    x2_set = S2 - S0 - S1
    used = len(h_set | a_set | b_set | c_set | x0_set | x1_set | x2_set)
    return Profile(len(h_set), len(a_set), len(b_set), len(c_set),
                   len(x0_set), len(x1_set), len(x2_set), n - used)


def is_light_budget_profile(P, k):
    return P.sigma <= 2 * k and max(P.budgets()) >= k + 1


def paid_taxonomy_labels(P, k):
    labels = []
    if P.sigma == 2 * k:
        labels.append("light_heavy_boundary")
    if P.h > 0 and P.a == P.b == P.c == 0:
        labels.append("sunflower_core")
    if min(P.r01, P.r02, P.r12) == 0:
        labels.append("disconnected_pair_overlap")
    if max(P.r01, P.r02, P.r12) >= k:
        labels.append("rung_2b_boundary_or_tangent")
    return labels or ["unclassified_coordinate_special"]


def row_audit(name, p, n, k, A, domain, time_budget=None):
    F = Fp(p)
    supports = list(combinations(range(n), A))
    profile_full_rank = {}
    examples = []
    light_triples = 0
    full_rank_placements = 0
    coordinate_special_defects = 0
    completed = True
    t0 = time.time()
    for triple in permutations(supports, 3):
        if time_budget and (time.time() - t0) > time_budget:
            completed = False
            break
        P = profile_of_triple(n, triple)
        if not is_light_budget_profile(P, k):
            continue
        light_triples += 1
        if P not in profile_full_rank:
            profile_full_rank[P] = normal_rank(F, domain, k, realize_profile(P)) == 0
        if not profile_full_rank[P]:
            continue
        kd = normal_rank(F, domain, k, triple)
        full_rank_placements += 1
        if kd:
            coordinate_special_defects += 1
            if len(examples) < 12:
                examples.append({"profile": P.as_dict(), "kernel_dim": kd,
                                 "supports": [list(T) for T in triple],
                                 "paid_taxonomy_labels": paid_taxonomy_labels(P, k)})
    return {"name": name, "field": f"F_{p}", "n": n, "k": k, "A": A,
            "t": A - k, "supports": len(supports),
            "light_triples": light_triples,
            "full_rank_coordinate_placements": full_rank_placements,
            "coordinate_special_defects": coordinate_special_defects,
            "completed_exhaustively": completed,
            "defect_examples": examples}


def run_gate():
    fails = []

    def ck(name, cond):
        if not cond:
            fails.append(name)

    r1 = row_audit("coord_n8_k2_A4", 11, 8, 2, 4, list(range(8)))
    ck("gate n8 k2 A4: light triples > 0", r1["light_triples"] > 0)
    ck("gate n8 k2 A4: zero coordinate-special defects", r1["coordinate_special_defects"] == 0)
    r2 = row_audit("coord_n8_k3_A4", 11, 8, 3, 4, list(range(8)))
    ck("gate n8 k3 A4: light triples > 0", r2["light_triples"] > 0)
    ck("gate n8 k3 A4: zero coordinate-special defects", r2["coordinate_special_defects"] == 0)
    return {"gate_pass": len(fails) == 0, "gate_fails": fails,
            "gate_rows": [r1, r2]}


def scan(total_budget_s=8400.0):
    # extend the exhaustive coordinate census beyond the banked n=8:
    # n = 9..13, k in {2,3}, A=4, several primes (the vanishing is p-specific).
    rows_spec = []
    for n in (9, 10, 11, 12, 13):
        for k in (2, 3):
            for p in (11, 13, 23, 29):
                if p <= n:
                    continue  # need >= n distinct nonzero-or-zero field elements
                rows_spec.append((f"coord_n{n}_k{k}_A4_p{p}", p, n, k, 4, list(range(n))))
    budget_per = total_budget_s / max(1, len(rows_spec))
    out = []
    for (name, p, n, k, A, domain) in rows_spec:
        r = row_audit(name, p, n, k, A, domain, time_budget=budget_per)
        out.append(r)
    falsifiers = [r for r in out if r["coordinate_special_defects"] > 0]
    return {
        "extension": "n=9..13 exhaustive coordinate-level census (banked was n=8)",
        "rows": out,
        "num_rows": len(out),
        "num_completed_exhaustive": sum(1 for r in out if r["completed_exhaustively"]),
        "falsifier_rows_with_coordinate_special_vanishing": falsifiers,
        "overall_verdict": ("FALSIFIER_UNPAID_VANISHING_FOUND" if falsifiers
                            else "NO_COORDINATE_SPECIAL_VANISHING_BRANCH_EMPTY"),
    }


@app.function(image=image, cpu=4, memory=8192, timeout=10800)
def run():
    gate = run_gate()
    if not gate["gate_pass"]:
        result = {"node": "xr_eliminant_vanishing_class", "status": "GATE_FAILED", "gate": gate}
        print("xr_eliminant_vanishing_class " + json.dumps(result), flush=True)
        return result
    sc = scan()
    result = {"node": "xr_eliminant_vanishing_class", "status": "OK", "gate": gate, "scan": sc}
    print("xr_eliminant_vanishing_class " + json.dumps(result), flush=True)
    return result


@app.local_entrypoint()
def main():
    call = run.spawn()
    print("SPAWNED xr_eliminant_vanishing_class fc_id=" + str(call.object_id))
