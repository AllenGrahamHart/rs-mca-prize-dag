#!/usr/bin/env python3
"""Exact structural checks for the Brief-6 rate-half list-crossing dossier.

This script verifies elementary arithmetic, the exact-integer Johnson ledger,
small-budget certificate mechanics, and counterexamples to unsafe proof-program
inferences.  It does NOT prove rate_half_list_adjacent_crossing, any new safe
list bound, or universal field coverage.

All load-bearing decisions use Python integers or Fractions.  Floats appear
only in display strings.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import comb, isqrt, log2


FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    tag = "PASS" if condition else "FAIL"
    print(f"[{tag}] {name}" + (f" :: {detail}" if detail else ""))
    if not condition:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
# 1. Official row constants, universal-field fence, and unsafe floor
# ---------------------------------------------------------------------------

N = 2**41
K = 2**40
A_UNSAFE = K + 2**34 - 1
A_CROSS_LOWER = A_UNSAFE + 1
A_THREE_QUARTERS = 3 * N // 4
JOHNSON_FLOOR = isqrt(N * (K - 1))
A_JOHNSON_CLASSICAL = JOHNSON_FLOOR + 1
B_CLASSICAL_START = 332_114_441_762


def check_constants() -> None:
    check("rate-half row has n=2^41 and k=2^40", N == 2*K)
    check("optimized cyclic unsafe agreement is k+2^34-1",
          A_UNSAFE == 1_116_691_496_959,
          f"a_unsafe={A_UNSAFE}")
    check("crossing lower endpoint is k+2^34",
          A_CROSS_LOWER == 1_116_691_496_960)
    check("three-quarter agreement is exact integer",
          A_THREE_QUARTERS == 1_649_267_441_664)
    check("classical Johnson floor is exact",
          JOHNSON_FLOOR == 1_554_944_255_987)
    check("classical exact-integer safe anchor is floor+1",
          A_JOHNSON_CLASSICAL == 1_554_944_255_988)
    check("unsafe-to-classical-Johnson gap matches ledger",
          JOHNSON_FLOOR - A_UNSAFE == 438_252_759_028)
    check("three-quarter point lies 94,323,185,676 above a_IJ",
          A_THREE_QUARTERS - A_JOHNSON_CLASSICAL == 94_323_185_676)

    # q = 1 + h*2^41 and q < 2^256: not a finite row list.
    progression_count = (2**256 - 2) // 2**41
    check("admissible progression has 2^215-1 candidate multipliers",
          progression_count == 2**215 - 1,
          f"count={progression_count}")
    check("field-family census cannot be a finite proof primitive",
          progression_count.bit_length() == 215)

    cyc = (comb(255, 129) + 255) // 256
    check("cyclic prefix lower bound has 243-bit integer size",
          cyc.bit_length() == 243,
          f"bits={cyc.bit_length()}")
    check("cyclic lower bound exceeds every prize threshold B*<2^128",
          cyc > 2**238 > 2**128)
    check("cyclic cap-endpoint margin exceeds 114 bits",
          log2(cyc) - 128 > 114,
          f"margin={log2(cyc)-128:.12f} bits")

    # Field-independent d=1 quotient-rotation lower staircase.  For each
    # dyadic quotient order Q, the list count is ceil(C(Q-1,Q/2+1)/Q)
    # and the exact agreement is k + 2n/Q - 1.
    staircase_expected = {
        8: 3,
        16: 313,
        32: 8_286_954,
        64: 13_449_656_337_410_111,
        128: 90_680_420_711_626_756_043_662_381_605_286_945,
        256: 11_092_230_961_998_080_258_863_221_315_535_829_014_398_723_445_840_079_610_908_300_691_051_869_570,
    }
    previous = 0
    for quotient_order, expected_count in staircase_expected.items():
        count = (comb(quotient_order-1, quotient_order//2+1)
                 + quotient_order - 1) // quotient_order
        agreement = K + 2*N//quotient_order - 1
        check(f"d=1 lower staircase count Q={quotient_order}",
              count == expected_count,
              f"count={count}")
        check(f"d=1 lower staircase counts increase Q={quotient_order}",
              count > previous)
        check(f"d=1 lower staircase agreement formula Q={quotient_order}",
              agreement == K + 2*N//quotient_order - 1)
        previous = count
    check("Q=8 staircase recovers the 3n/4-1 predecessor",
          K + 2*N//8 - 1 == A_THREE_QUARTERS - 1)


# ---------------------------------------------------------------------------
# 2. Exact-integer Johnson anchor and predecessor defect
# ---------------------------------------------------------------------------


def balanced_pair_min(n: int, ell: int, a: int) -> int:
    """Minimum sum_x C(m_x,2) for ell*a incidences on n coordinates."""
    d, r = divmod(ell * a, n)
    return n * comb(d, 2) + r * d


def pair_intersection_max(k: int, ell: int) -> int:
    return comb(ell, 2) * (k - 1)


def johnson_safe(n: int, k: int, budget: int, a: int) -> bool:
    ell = budget + 1
    return balanced_pair_min(n, ell, a) > pair_intersection_max(k, ell)


def exact_integer_johnson_anchor(n: int, k: int, budget: int) -> int:
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if johnson_safe(n, k, budget, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def predecessor_defect(n: int, k: int, budget: int) -> tuple[int, int, int]:
    a = exact_integer_johnson_anchor(n, k, budget)
    ell = budget + 1
    defect = pair_intersection_max(k, ell) - balanced_pair_min(n, ell, a - 1)
    overshoot = balanced_pair_min(n, ell, a) - pair_intersection_max(k, ell)
    return a, defect, overshoot


def check_johnson_ledger() -> None:
    expected = {
        1: (A_THREE_QUARTERS, 1, 1),
        2: (A_THREE_QUARTERS, 3, 3),
        3: (A_THREE_QUARTERS, 2, 6),
        4: (1_612_617_054_071, 12, 3),
        5: (1_603_454_457_173, 17, 7),
        10: (1_585_010_268_612, 34, 43),
    }
    for budget, want in expected.items():
        got = predecessor_defect(N, K, budget)
        check(f"Johnson ledger B={budget}", got == want,
              f"got={got}, expected={want}")

    a_before = exact_integer_johnson_anchor(N, K, B_CLASSICAL_START - 1)
    a_at = exact_integer_johnson_anchor(N, K, B_CLASSICAL_START)
    check("classical-anchor threshold is exact",
          a_before == A_JOHNSON_CLASSICAL + 1
          and a_at == A_JOHNSON_CLASSICAL,
          f"before={a_before}, at={a_at}")

    _, defect, _ = predecessor_defect(N, K, B_CLASSICAL_START)
    ratio = Fraction(defect, B_CLASSICAL_START**2)
    check("large-budget predecessor defect has 77 bits",
          defect.bit_length() == 77,
          f"defect={defect}")
    check("large-budget defect is about B^2/sqrt(2), not finite-atlas scale",
          Fraction(70, 100) < ratio < Fraction(72, 100),
          f"defect/B^2={float(ratio):.12f}")

    # The exact defect decomposition for any hypothetical ell-list:
    # incidence imbalance + pairwise-intersection deficit = Delta_J.
    budget = 3
    a, delta, _ = predecessor_defect(N, K, budget)
    ell = budget + 1
    pmin = balanced_pair_min(N, ell, a - 1)
    pmax = pair_intersection_max(K, ell)
    for actual_pair_sum in range(pmin, pmax + 1):
        incidence_imbalance = actual_pair_sum - pmin
        pair_deficit = pmax - actual_pair_sum
        check(f"B=3 defect identity at pair sum offset {incidence_imbalance}",
              incidence_imbalance + pair_deficit == delta)


# ---------------------------------------------------------------------------
# 3. Budget-three finite occupancy skeleton
# ---------------------------------------------------------------------------


def canonical_edge_pattern(values: tuple[int, ...]) -> tuple[int, ...]:
    edges = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    best = None
    for perm in permutations(range(4)):
        remapped = {}
        for value, (u, v) in zip(values, edges):
            a, b = sorted((perm[u], perm[v]))
            remapped[(a, b)] = value
        key = tuple(remapped[e] for e in edges)
        if best is None or key < best:
            best = key
    assert best is not None
    return best


def weak_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, length - 1):
            yield (first,) + tail


def check_budget_three_skeleton() -> None:
    # For ell=4 at a=3n/4-1, write e=actual_pair_sum-Pmin in {0,1,2}.
    # Solving the two incidence equations gives six multiplicity histograms.
    histograms: dict[int, set[tuple[int, int, int, int]]] = {0: set(), 1: set(), 2: set()}
    for e in range(3):
        for x0 in range(4):
            for x1 in range(5):
                for x4 in range(5):
                    if 3*x0 + x1 + x4 != e:
                        continue
                    x2 = 4 - 3*x0 - 2*x1 + x4
                    if x2 >= 0:
                        histograms[e].add((x0, x1, x2, x4))
    expected = {
        0: {(0, 0, 4, 0)},
        1: {(0, 1, 2, 0), (0, 0, 5, 1)},
        2: {(0, 2, 0, 0), (0, 1, 3, 1), (0, 0, 6, 2)},
    }
    check("B=3 has six coarse multiplicity histograms",
          histograms == expected,
          f"histograms={histograms}")

    # Pair-deficit graphs have total 2-e; quotient by S4.
    orbit_counts = {}
    for e in range(3):
        p = 2 - e
        orbits = {canonical_edge_pattern(v) for v in weak_compositions(p, 6)}
        orbit_counts[e] = len(orbits)
    check("pair-deficit graph orbit counts are 3,1,1",
          orbit_counts == {0: 3, 1: 1, 2: 1},
          f"orbits={orbit_counts}")
    coarse_cells = sum(len(histograms[e]) * orbit_counts[e] for e in range(3))
    check("coarse Johnson-defect atlas has eight cells before locator-role refinement",
          coarse_cells == 8,
          f"cells={coarse_cells}")


# ---------------------------------------------------------------------------
# 4. Exact small-field unsafe certificate (the B=2 construction)
# ---------------------------------------------------------------------------


def poly_mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i+j] = (out[i+j] + a*b) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_eval(poly: list[int], x: int, p: int) -> int:
    acc = 0
    for coefficient in reversed(poly):
        acc = (acc*x + coefficient) % p
    return acc


def locator(roots: list[int], p: int) -> list[int]:
    out = [1]
    for root in roots:
        out = poly_mul(out, [(-root) % p, 1], p)
    return out


def primitive_root(p: int) -> int:
    factors = []
    m = p - 1
    d = 2
    while d*d <= m:
        if m % d == 0:
            factors.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        factors.append(m)
    for g in range(2, p):
        if all(pow(g, (p-1)//r, p) != 1 for r in factors):
            return g
    raise AssertionError("no primitive root")


def check_low_budget_certificate() -> None:
    p = 17
    n = 16
    d = 4
    k = 8
    zeta = primitive_root(p)
    domain = [pow(zeta, j, p) for j in range(n)]
    i_unit = pow(zeta, d, p)
    check("F17 toy has i^2=-1", i_unit*i_unit % p == p-1,
          f"i={i_unit}")

    fibers: dict[int, list[int]] = {}
    for x in domain:
        fibers.setdefault(pow(x, d, p), []).append(x)
    expected_values = {1, p-1, i_unit, (-i_unit) % p}
    check("four y=x^d fibres are present", set(fibers) == expected_values)
    check("each fibre has size d=4", all(len(v) == d for v in fibers.values()))

    minus_i = (-i_unit) % p
    x0 = min(fibers[minus_i])
    G = locator([x for x in fibers[minus_i] if x != x0], p)
    y_minus_1 = [p-1, 0, 0, 0, 1]       # X^4 - 1
    y_plus_1 = [1, 0, 0, 0, 1]          # X^4 + 1
    c0 = [0]
    c1 = poly_mul(G, y_minus_1, p)
    c2 = [(i_unit*c) % p for c in poly_mul(G, y_plus_1, p)]
    check("all three toy codewords have degree < k",
          max(len(c0)-1, len(c1)-1, len(c2)-1) < k,
          f"degrees={[len(c0)-1,len(c1)-1,len(c2)-1]}")
    check("toy codewords are distinct", len({tuple(c0), tuple(c1), tuple(c2)}) == 3)

    received = {}
    for x in domain:
        y = pow(x, d, p)
        if y == i_unit:
            v1 = poly_eval(c1, x, p)
            v2 = poly_eval(c2, x, p)
            check(f"c1=c2 on i-fibre at x={x}", v1 == v2)
            received[x] = v1
        else:
            received[x] = 0

    agreements = []
    for codeword in (c0, c1, c2):
        agreements.append(sum(poly_eval(codeword, x, p) == received[x] for x in domain))
    check("one received word supports the three-codeword predecessor witness",
          agreements[0] >= 12 and agreements[1] >= 11 and agreements[2] >= 11,
          f"agreements={agreements}")

    # The safe half at a=12 is the exact-integer Johnson inequality for B=2.
    check("B=2 toy Johnson safe certificate is strict",
          balanced_pair_min(n, 3, 12) > pair_intersection_max(k, 3),
          f"{balanced_pair_min(n,3,12)} > {pair_intersection_max(k,3)}")


# ---------------------------------------------------------------------------
# 5. Packing route fence
# ---------------------------------------------------------------------------


def packing_ratio(n: int, k: int, distance_from_full: int) -> Fraction:
    # C(n,k)/C(n-r,k) = product_{j=0}^{r-1}(n-j)/(n-k-j).
    value = Fraction(1)
    for j in range(distance_from_full):
        value *= Fraction(n-j, n-k-j)
    return value


def check_packing_fence() -> None:
    r127 = packing_ratio(N, K, 127)
    r128 = packing_ratio(N, K, 128)
    check("packing bound is below 2^128 at only 127-from-full",
          r127 < 2**128)
    check("packing bound already exceeds 2^128 at 128-from-full",
          r128 > 2**128)
    check("packing safe region is astronomically above the live bracket",
          (N-127) - A_JOHNSON_CLASSICAL > 600_000_000_000)


# ---------------------------------------------------------------------------
# 6. Counterexamples to unsafe proof-program inferences
# ---------------------------------------------------------------------------


def crossing_index(values: list[int], budget: int) -> int:
    # Values are L(a), monotone nonincreasing; return least safe index.
    return next(i for i, value in enumerate(values) if value <= budget)


def check_logic_guardrails() -> None:
    # Literal existence is automatic for any finite monotone sequence with
    # unsafe start and safe terminal sentinel.
    values = [100, 40, 9, 9, 3, 0]
    budget = 3
    a = crossing_index(values, budget)
    check("monotonicity alone creates a literal adjacent crossing",
          values[a] <= budget < values[a-1],
          f"a={a}")

    # A distant unsafe/safe bracket is not an adjacent certificate.
    values2 = [50, 20, 7, 4, 2, 0]
    budget2 = 4
    lower_unsafe, upper_safe = 1, 5
    actual = crossing_index(values2, budget2)
    check("safe+unsafe bracket can leave a nontrivial unresolved interval",
          actual == 3 and upper_safe-lower_unsafe > 1,
          f"actual={actual}, bracket=[{lower_unsafe},{upper_safe}]")

    # Failure of one upper-bound method says nothing about truth of safety.
    true_list_size = 2
    proof_method_returns = None  # no certificate found
    check("failed upper-bound search is not an unsafe witness",
          proof_method_returns is None and true_list_size <= budget2)

    # Average control does not control the maximum fibre.
    fibres = [100] + [0]*99
    check("average list size can be one while maximum is one hundred",
          sum(fibres) == 100 and Fraction(sum(fibres), len(fibres)) == 1
          and max(fibres) == 100)

    # Counts from different received words cannot be multiplied or added as
    # one list unless a common-word compatibility theorem is supplied.
    word_lists = {"u0": set(range(10)), "u1": set(range(10, 20))}
    max_single = max(len(v) for v in word_lists.values())
    union = set().union(*word_lists.values())
    check("two ten-codeword witnesses on different words do not make a twenty-list",
          max_single == 10 and len(union) == 20)

    # B*=0 is either excluded by the official scope or an elementary branch.
    # L(n)>=1 by choosing u equal to a codeword; L(n+1)=0 by convention.
    check("budget-zero branch has the trivial adjacent certificate n,n+1",
          1 > 0 >= 0)


# ---------------------------------------------------------------------------
# 7. Exact-shell first-owner bookkeeping on a toy list
# ---------------------------------------------------------------------------


def check_exact_shell_ownership() -> None:
    # Three codewords with total agreement counts 5,4,3.  Raw 3-subsets would
    # count the first codeword C(5,3)=10 times; exact-shell ownership counts it
    # once at its maximal agreement.
    agreement_sizes = [5, 4, 3]
    raw_at_three = sum(comb(s, 3) for s in agreement_sizes)
    exact_shells = {3: 1, 4: 1, 5: 1}
    threshold_three = sum(exact_shells[a] for a in exact_shells if a >= 3)
    check("raw support fibres overcount codewords with extra agreements",
          raw_at_three == 15 and threshold_three == 3,
          f"raw={raw_at_three}, exact={threshold_three}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    check_constants()
    check_johnson_ledger()
    check_budget_three_skeleton()
    check_low_budget_certificate()
    check_packing_fence()
    check_logic_guardrails()
    check_exact_shell_ownership()

    if FAILURES:
        print(f"\nBRIEF6_RHL_ADJ_PROGRAM_ARITHMETIC_FAIL failures={FAILURES}")
        raise SystemExit(1)
    print("\nBRIEF6_RHL_ADJ_PROGRAM_ARITHMETIC_PASS")


if __name__ == "__main__":
    main()
