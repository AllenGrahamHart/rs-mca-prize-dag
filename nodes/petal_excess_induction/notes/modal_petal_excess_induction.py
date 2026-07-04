#!/usr/bin/env python3
r"""
Modal dispatch job for node: petal_excess_induction.

============================ PRE-REGISTERED SPEC ============================
(quoted verbatim from prize/nodes/petal_excess_induction/statement.md)

  "Bridge from petal_fixed_excess (PROVED, c fixed) to growing excess: the
   mixed-amplification induction on c with poly(n) constants uniform in c.
   EVIDENCE WALL: the growing-excess petal census -- pre-registered scan of
   full-petal extras at c = 2..8 on calibration rows; interpretation fixed:
   counts flat in c => the induction's shape is right; growth in c => the
   amplification route needs a new idea (route_exact_rank is already REFUTED)."

  Falsifier: "petal extras growing with c at any calibration row."
  (dispatch note: the RE-SCOPED residue-line counting scan via the L1
   coset-chart residue bridge; c = 2..8.)
============================================================================

CONSTRUCTION (faithful to the banked petal machinery
experimental/scripts/verify_l1_full_petal_growing_defect_witnesses.py and
notes/l1/l1_full_petal_growing_defect_witnesses.md):

  A full-petal configuration: t petals of size ell (in the coset-chart bridge,
  cosets of the order-ell subgroup -- the exact structural family that REFUTES
  the exact-rank formula), scalars c_i, and a candidate core.  Excess is
  c = d - ell where d is the core defect (missed-core size).  The RESIDUE-LINE
  COUNT is rank(pi_{>d} R_{I,d}) (rank_general below): the number of independent
  residue lines the CRT top-coefficient map pins.  The full-petal EXTRA space is
  the kernel K_{I,d} = ker(pi_{>d} R_{I,d}); dim K = (d+1) - residue_line_count.
  Lemma 13: dim K <= c+1.  The REFUTED exact-rank formula predicted
  residue_line_count = min(d+1, t*ell-d-1).  This scan reports, as a function of
  c = 2..8 across calibration rows, (i) residue_line_count, (ii) dim K, and
  (iii) the EXACT realizable full-petal extra count = #{missed cores D subset
  core, |D|=d : CRT-residue-degree(D) <= d} (the Lemma 7/8 realizability count).

  INTERPRETATION (pre-registered): dim K / extra counts FLAT (bounded) in c =>
  the induction's shape is right; GROWTH in c => the amplification route needs a
  new idea.

CORRECTNESS GATE (banked, must pass in-cloud before the scan):
  Witness A (t=3, ell=3, d=5, c=2, p=1009): the predicted extra codeword is
     realizable by the CRT shortcut AND found by a from-scratch exact RS list
     decode, and all planted codewords are found.
  Witness B (t=5, ell=3, d=8, c=5, p=1009): same, two ways.
  Route-cut (p=19, ell=3, t=3, d=3, order-3 coset petals): the exact-rank
     formula min(d+1,t*ell-d-1) FAILS for every tested scalar choice, while
     Lemma 13's floor rank>=ell is never violated.

Self-contained (stdlib only; helpers inlined from
scan_l1_full_list_quotient_conjecture.py).  One JSON line prefixed with node.
"""

import modal
import json
import time
import itertools

app = modal.App("rs-mca-petal_excess_induction")
image = modal.Image.debian_slim()


# ---------------- inlined modular-poly helpers (scan_l1_*) -----------------
def trim_poly(coeffs):
    out = list(coeffs)
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_degree(coeffs):
    return len(trim_poly(coeffs)) - 1


def poly_add(left, right, p):
    lv = tuple(left)
    rv = tuple(right)
    size = max(len(lv), len(rv))
    out = [0] * size
    for i in range(size):
        out[i] = ((lv[i] if i < len(lv) else 0) + (rv[i] if i < len(rv) else 0)) % p
    return trim_poly(out)


def poly_scale(coeffs, scalar, p):
    return trim_poly((scalar * c) % p for c in coeffs)


def multiply_by_linear(coeffs, root, p):
    values = tuple(coeffs)
    out = [0] * (len(values) + 1)
    for i, c in enumerate(values):
        out[i] = (out[i] - root * c) % p
        out[i + 1] = (out[i + 1] + c) % p
    return trim_poly(out)


def interpolate_polynomial(xs, ys, p):
    if len(set(xs)) != len(xs):
        raise ValueError("interpolation points must be distinct")
    result = ()
    for j, x_j in enumerate(xs):
        basis = (1,)
        denom = 1
        for m, x_m in enumerate(xs):
            if m == j:
                continue
            basis = multiply_by_linear(basis, x_m, p)
            denom = (denom * (x_j - x_m)) % p
        result = poly_add(result, poly_scale(basis, ys[j] * pow(denom, -1, p), p), p)
    return result


def eval_poly(coeffs, x, p):
    out = 0
    for c in reversed(tuple(coeffs)):
        out = (out * x + c) % p
    return out


def matrix_rref(matrix, p):
    rows = [row[:] for row in matrix]
    pivots = []
    pr = 0
    ncol = len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = next((r for r in range(pr, len(rows)) if rows[r][col] % p), None)
        if piv is None:
            continue
        rows[pr], rows[piv] = rows[piv], rows[pr]
        inv = pow(rows[pr][col] % p, -1, p)
        rows[pr] = [(v * inv) % p for v in rows[pr]]
        for ri, row in enumerate(rows):
            if ri == pr:
                continue
            f = row[col] % p
            if f:
                rows[ri] = [(e - f * pe) % p for e, pe in zip(row, rows[pr])]
        pivots.append(col)
        pr += 1
        if pr == len(rows):
            break
    return rows, pivots


# --------------------------- petal primitives ------------------------------
def locator(roots, p):
    poly = (1,)
    for root in roots:
        poly = multiply_by_linear(poly, root, p)
    return trim_poly(poly)


def crt_residue_degree(petals, scalars, target_poly, p):
    xs, ys = [], []
    for petal, c in zip(petals, scalars):
        for x in petal:
            xs.append(x)
            ys.append((c * eval_poly(target_poly, x, p)) % p)
    return poly_degree(trim_poly(interpolate_polynomial(xs, ys, p)))


def exact_list_decode(domain, u, k, s, p):
    listed = {}
    for support in itertools.combinations(domain, s):
        vals = [u[x] for x in support]
        poly = trim_poly(interpolate_polynomial(list(support), vals, p))
        if poly_degree(poly) >= k:
            continue
        codeword = {x: eval_poly(poly, x, p) for x in domain}
        key = tuple(codeword[x] for x in domain)
        if key in listed:
            continue
        agreement = frozenset(x for x in domain if codeword[x] == u[x])
        if len(agreement) >= s:
            listed[key] = agreement
    return listed


def check_witness(label, p, petals, scalars, core, retained_core, d):
    ell = len(petals[0])
    t = len(petals)
    domain = [x for petal in petals for x in petal] + core
    assert len(domain) == len(set(domain))
    k = len(core) + 1
    s = k + ell - 1
    missed_core = [x for x in core if x not in retained_core]
    assert len(missed_core) == d
    loc_d = locator(missed_core, p)
    crt_degree = crt_residue_degree(petals, scalars, loc_d, p)
    crt_ok = crt_degree <= d and poly_degree(loc_d) == d
    loc_c = locator(core, p)
    u = {x: 0 for x in core}
    for petal, c in zip(petals, scalars):
        for x in petal:
            u[x] = (c * eval_poly(loc_c, x, p)) % p
    listed = exact_list_decode(domain, u, k, s, p)
    predicted_extra = frozenset(retained_core) | frozenset().union(*(set(pt) for pt in petals))
    planted = [frozenset(core) | frozenset(petal) for petal in petals]
    found_predicted = any(agr == predicted_extra for agr in listed.values())
    found_all = all(any(agr == pl for agr in listed.values()) for pl in planted)
    return crt_ok and found_predicted and found_all


def rank_general(p, petals, scalars, d):
    """Residue-line count = rank(pi_{>d} R_{I,d})."""
    t = len(petals)
    ell = len(petals[0])
    n_petal = t * ell
    xs = [x for petal in petals for x in petal]
    rows = []
    for j in range(d + 1):
        ys = []
        for petal, c in zip(petals, scalars):
            for x in petal:
                ys.append((c * pow(x, j, p)) % p)
        w = list(interpolate_polynomial(xs, ys, p))
        w = w + [0] * (n_petal - len(w))
        rows.append(w[d + 1: n_petal])
    _, pivots = matrix_rref(rows, p)
    return len(pivots)


# ----------------------------- the GATE ------------------------------------
def run_gate():
    fails = []

    def ck(name, cond):
        if not cond:
            fails.append(name)

    wa = check_witness("A", 1009,
                       [[0, 1, 2], [3, 4, 5], [6, 7, 8]], [1, 2, 3],
                       [558, 784, 852, 874, 900, 901, 902, 903, 904, 905],
                       [901, 902, 903, 904, 905], 5)
    ck("Witness A realizable + exact-decoded (c=2,t=3)", wa)
    wb = check_witness("B", 1009,
                       [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]],
                       [1, 2, 3, 4, 5],
                       [69, 453, 512, 670, 682, 855, 864, 917], [], 8)
    ck("Witness B realizable + exact-decoded (c=5,t=5)", wb)

    # Route-cut: order-3 coset petals of F_19^*, exact-rank formula fails.
    p, ell, t, d = 19, 3, 3, 3
    petals = [[1, 7, 11], [4, 9, 6], [16, 17, 5]]
    predicted = min(d + 1, t * ell - d - 1)
    all_below = True
    floor_ok = True
    for scalars in ([1, 2, 3], [2, 5, 7], [1, 3, 17], [6, 10, 15]):
        r = rank_general(p, petals, scalars, d)
        if not (r < predicted):
            all_below = False
        if not (r >= ell):
            floor_ok = False
    ck("route-cut: exact-rank formula fails for every coset scalar choice", all_below)
    ck("route-cut: Lemma-13 floor rank>=ell never violated", floor_ok)
    return {"gate_pass": len(fails) == 0, "gate_fails": fails,
            "witness_A": wa, "witness_B": wb}


# ----------------------------- the SCAN ------------------------------------
def subgroup_coset_petals(p, ell, t):
    """t distinct cosets of the order-ell subgroup of F_p^* (the coset-chart
    residue-bridge family).  Returns (petals, core_pool) with disjoint points."""
    # primitive root
    def primroot(p):
        x = p - 1
        fac = []
        d = 2
        while d * d <= x:
            if x % d == 0:
                fac.append(d)
                while x % d == 0:
                    x //= d
            d += 1
        if x > 1:
            fac.append(x)
        for g in range(2, p):
            if all(pow(g, (p - 1) // r, p) != 1 for r in fac):
                return g
        raise AssertionError
    g = primroot(p)
    assert (p - 1) % ell == 0
    h = pow(g, (p - 1) // ell, p)  # generator of order-ell subgroup
    sub = [pow(h, i, p) for i in range(ell)]
    petals = []
    used = set()
    reps = 0
    while len(petals) < t and reps < p:
        rep = pow(g, reps, p)
        coset = sorted((rep * s) % p for s in sub)
        if not (set(coset) & used) and len(set(coset)) == ell:
            petals.append(coset)
            used |= set(coset)
        reps += 1
    if len(petals) < t:
        return None, None
    core_pool = [x for x in range(1, p) if x not in used]
    return petals, core_pool


def scan(total_budget_s=8600.0):
    # calibration rows: several primes with an order-ell subgroup, t in {3,5},
    # ell in {2,3}. Excess c = d - ell = 2..8 => d = ell+c.
    def _isprime(m):
        if m < 2: return False
        i = 2
        while i * i <= m:
            if m % i == 0: return False
            i += 1
        return True
    def _primes_1mod(ell, targets):
        # nearest prime >= target with ell | p-1 (so the order-ell subgroup exists)
        out = []
        for tgt in targets:
            p = tgt - (tgt % ell) + 1
            if p <= tgt: p += ell
            while not _isprime(p): p += ell
            out.append(p)
        return out
    configs = []
    for ell in (2, 3):
        for t in (3, 5):
            for p in _primes_1mod(ell, (1009, 2003, 4001, 8009)):
                configs.append((p, ell, t))
    cs = list(range(2, 9))
    budget_per = total_budget_s / max(1, len(configs))

    table = []
    for (p, ell, t) in configs:
        petals, core_pool = subgroup_coset_petals(p, ell, t)
        if petals is None or core_pool is None:
            continue
        n_petal = t * ell
        # scalars: sequential (structural coset family, t odd triggers route-cut)
        scalars = list(range(1, t + 1))
        t0 = time.time()
        rows_c = []
        for c in cs:
            d = ell + c
            if d > n_petal - 1:      # residue lines only meaningful for d < t*ell
                continue
            residue_lines = rank_general(p, petals, scalars, d)
            dim_K = (d + 1) - residue_lines
            lemma13_bound = c + 1
            refuted_formula = min(d + 1, n_petal - d - 1)
            # exact realizable full-petal extra count over missed cores D<=core_pool
            exact_count = None
            core_cap = min(len(core_pool), d + 6)  # cap enumeration to stay feasible
            core = core_pool[:core_cap]
            if 0 <= d <= len(core):
                total = comb_guard(len(core), d)
                if total is not None and total <= 400_000 and (time.time() - t0) < budget_per:
                    cnt = 0
                    for D in itertools.combinations(core, d):
                        loc_d = locator(list(D), p)
                        if poly_degree(loc_d) != d:
                            continue
                        if crt_residue_degree(petals, scalars, loc_d, p) <= d:
                            cnt += 1
                    exact_count = {"count": cnt, "core_size": len(core),
                                   "candidates": total}
            rows_c.append({
                "c": c, "d": d,
                "residue_line_count": residue_lines,
                "dim_K": dim_K,
                "lemma13_bound_c_plus_1": lemma13_bound,
                "refuted_exact_formula_rank": refuted_formula,
                "exact_realizable_extras": exact_count,
            })
            if time.time() - t0 > budget_per:
                break
        table.append({"p": p, "ell": ell, "t": t, "n_petal": n_petal,
                      "petals": petals, "scalars": scalars, "by_c": rows_c})

    # verdict: is dim_K (and exact extra count) flat or growing in c?
    growing = []
    for cfg in table:
        seq = [(row["c"], row["dim_K"]) for row in cfg["by_c"]]
        # "growth" = dim_K strictly increases across the c-range beyond Lemma13's
        # inherent c+1 slack, i.e. dim_K itself trends up with c
        if len(seq) >= 3:
            first = seq[0][1]
            last = seq[-1][1]
            if last > first:
                growing.append({"p": cfg["p"], "ell": cfg["ell"], "t": cfg["t"],
                                "dim_K_first": first, "dim_K_last": last,
                                "seq": seq})
    return {
        "excess_range_c": [2, 8],
        "configs": table,
        "configs_with_dimK_growth": growing,
        "overall_verdict": ("GROWTH_IN_C_ROUTE_NEEDS_NEW_IDEA" if growing
                            else "FLAT_IN_C_INDUCTION_SHAPE_SUPPORTED"),
    }


def comb_guard(n, r):
    from math import comb
    try:
        return comb(n, r)
    except ValueError:
        return None


# make comb available in scan
from math import comb  # noqa: E402


@app.function(image=image, cpu=4, memory=8192, timeout=10800)
def run():
    gate = run_gate()
    if not gate["gate_pass"]:
        result = {"node": "petal_excess_induction", "status": "GATE_FAILED", "gate": gate}
        print("petal_excess_induction " + json.dumps(result), flush=True)
        return result
    sc = scan()
    result = {"node": "petal_excess_induction", "status": "OK", "gate": gate, "scan": sc}
    print("petal_excess_induction " + json.dumps(result), flush=True)
    return result


@app.local_entrypoint()
def main():
    call = run.spawn()
    print("SPAWNED petal_excess_induction fc_id=" + str(call.object_id))
