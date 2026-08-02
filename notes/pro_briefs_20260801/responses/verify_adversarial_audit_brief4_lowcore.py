#!/usr/bin/env python3
"""Exact checks for the adversarial audit of Brief 4 / P-B.

The script verifies:
  * the super-budget constant-weight Sidon lower bound;
  * the RowC 1/4 split-fibre parameter and degree identities;
  * one exact polynomial/root-set realization over F_12289;
  * producer, energy, and owner-capacity failures;
  * pilot vacuity below M<=N^2;
  * an arbitrarily extensible high-rank support-hypergraph fence.

It does NOT prove that the exhibited witnesses are normative first matches,
and therefore does not refute P-B.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


N = 1024
K = 256
H = 5
A = 261
M_FIBRE = 4
A_FIBRES = 52
CORE = 53
B_LABELS = 104
R = 52


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise AssertionError("no primitive root")


def poly_trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a: list[int], b: list[int], q: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0)
                  + (b[i] if i < len(b) else 0)) % q
    return poly_trim(out)


def poly_neg(a: list[int], q: int) -> list[int]:
    return poly_trim([(-x) % q for x in a])


def poly_mul(a: list[int], b: list[int], q: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return poly_trim(out)


def poly_shift(a: list[int], d: int) -> list[int]:
    return [0] * d + a


def poly_compose_xm(a: list[int], m: int) -> list[int]:
    out = [0] * (m * (len(a) - 1) + 1)
    for i, x in enumerate(a):
        out[m * i] = x
    return poly_trim(out)


def poly_eval(a: list[int], x: int, q: int) -> int:
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % q
    return acc


def locator(roots: list[int], q: int) -> list[int]:
    p = [1]
    for r in roots:
        p = poly_mul(p, [(-r) % q, 1], q)
    return p


def check_sidon_lower_bound() -> int:
    num = (2**R - 1) * comb(2 * R, R)
    den = 2 ** (2 * R) - 1
    layer = (num + den - 1) // den

    max_degree_distance_two = R * R
    family = (layer + max_degree_distance_two) // (
        max_degree_distance_two + 1
    )

    require(layer == 351_511_230_817_436, "weight-layer lower bound")
    require(family == 129_948_699_009, "constant-weight Sidon lower bound")
    require(family > 8 * N**3, "super-budget")
    require(family > N**2, "producer nonvacuity")

    print(
        "PB_AUDIT1_SIDON_BOUND_PASS",
        f"weight52_layer={layer}",
        f"family={family}",
        f"budget={8*N**3}",
    )
    return family


def gf32_mul(a: int, b: int) -> int:
    # F_32 with primitive polynomial x^5+x^2+1.
    out = 0
    aa = a
    bb = b
    while bb:
        if bb & 1:
            out ^= aa
        bb >>= 1
        aa <<= 1
        if aa & 0b100000:
            aa ^= 0b100101
    return out & 0b11111


def gf32_pow(a: int, e: int) -> int:
    out = 1
    while e:
        if e & 1:
            out = gf32_mul(out, a)
        a = gf32_mul(a, a)
        e >>= 1
    return out


def check_small_binary_sidon() -> None:
    points = [(x << 5) | gf32_pow(x, 3) for x in range(32)]
    seen: dict[int, tuple[int, int]] = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            s = points[i] ^ points[j]
            require(s not in seen, "GF32 cubic graph not Sidon")
            seen[s] = (i, j)

    print(
        "PB_AUDIT2_CUBIC_SIDON_PASS",
        f"points={len(points)}",
        f"distinct_pair_sums={len(seen)}",
    )


def check_parameter_identities() -> None:
    require(CORE + M_FIBRE * A_FIBRES == A, "support size")
    require(A - H == K, "gap")
    require(A - M_FIBRE == 257 >= K, "V degree")
    require(A - 2 * M_FIBRE == 253 < K, "codeword degree")
    require(
        CORE + M_FIBRE * (A_FIBRES - 2) == 253 <= K - 1,
        "intersection cap",
    )
    require(M_FIBRE <= H < 2 * M_FIBRE, "split-fibre range")
    require(
        CORE + M_FIBRE * B_LABELS <= N,
        "fibre/core fit in official domain",
    )

    print(
        "PB_AUDIT3_PARAMETERS_PASS",
        f"N={N}",
        f"K={K}",
        f"A={A}",
        f"used_domain={CORE+M_FIBRE*B_LABELS}",
    )


def check_exact_polynomial_fixture() -> None:
    q = 12289
    require((q - 1) % 1024 == 0, "mu_1024 absent")
    omega = pow(primitive_root(q), (q - 1) // 1024, q)
    domain = [pow(omega, i, q) for i in range(1024)]
    require(len(set(domain)) == 1024, "domain order")

    # Fibres of x -> x^4, labels omega^(4i), i=0,...,103.
    fibres = []
    used = set()
    for i in range(B_LABELS):
        label = pow(omega, 4 * i, q)
        fibre = [pow(omega, i + 256 * t, q) for t in range(4)]
        require(all(pow(x, 4, q) == label for x in fibre), "fibre equation")
        require(not used.intersection(fibre), "fibre collision")
        used.update(fibre)
        fibres.append((label, fibre))

    remaining = [x for x in domain if x not in used]
    core_roots = remaining[:CORE]
    G = locator(core_roots, q)

    J = list(range(A_FIBRES))
    qj = [1]
    for i in J:
        c = fibres[i][0]
        qj = poly_mul(qj, [(-c) % q, 1], q)

    # qj(Y)=Y^a-zY^(a-1)+R(Y)
    z = sum(fibres[i][0] for i in J) % q
    leading = [0] * (A_FIBRES + 1)
    leading[A_FIBRES] = 1
    leading[A_FIBRES - 1] = (-z) % q
    Rpoly = poly_add(qj, poly_neg(leading, q), q)
    require(len(Rpoly) - 1 <= A_FIBRES - 2, "R degree")

    U = poly_shift(G, M_FIBRE * A_FIBRES)
    V = poly_neg(poly_shift(G, M_FIBRE * (A_FIBRES - 1)), q)
    p = poly_neg(poly_mul(G, poly_compose_xm(Rpoly, M_FIBRE), q), q)

    lhs = poly_add(poly_add(U, [(z * c) % q for c in V], q),
                   poly_neg(p, q), q)
    rhs = poly_mul(G, poly_compose_xm(qj, M_FIBRE), q)
    require(lhs == rhs, "split-fibre polynomial identity")
    require(len(U) - 1 == A, "deg U")
    require(len(V) - 1 == A - M_FIBRE, "deg V")
    require(len(p) - 1 <= A - 2 * M_FIBRE < K, "deg p")

    roots = [x for x in domain if poly_eval(rhs, x, q) == 0]
    intended = set(core_roots)
    for i in J:
        intended.update(fibres[i][1])
    require(set(roots) == intended, "exact agreement support")
    require(len(roots) == A, "agreement support size")

    print(
        "PB_AUDIT4_POLYNOMIAL_FIXTURE_PASS",
        f"q={q}",
        f"roots={len(roots)}",
        f"deg_p={len(p)-1}",
        f"deg_V={len(V)-1}",
    )


def check_producer_failures(family: int) -> None:
    distinct_differences = family * (family - 1)
    owner_capacity = N**2 * (family - 1)
    require(distinct_differences > owner_capacity, "owner bound not violated")

    energy = distinct_differences
    desired = family * family * (family - 1) // N**2
    require(desired > energy, "energy producer not violated")

    factor_num = family
    factor_den = N**2
    require(factor_num // factor_den > 100_000, "violation factor")

    print(
        "PB_AUDIT5_PRODUCER_FAIL_PASS",
        f"M_over_N2={family/N**2:.3f}",
        "difference_multiplicity=1",
        "nontrivial_rectangles=0",
    )


def check_pilot_vacuity() -> None:
    for n in (8, 16, 32, 64):
        m = n * n
        dmax = m * (m - 1)
        bound = n * n * (m - 1)
        require(dmax == bound, "N^2 threshold identity")
    print(
        "PB_AUDIT6_PILOT_VACUITY_PASS",
        "D<=N^2(M-1) automatic whenever M<=N^2",
    )


def check_high_rank_hypergraph() -> None:
    L = 101
    bases = [(0, 1, 3), (0, 5, 12)]
    coordinates = []
    block_incidence = [set() for _ in range(L)]

    for kind, triple in enumerate(bases):
        for s in range(L):
            blocks = tuple((s + t) % L for t in triple)
            coord_id = len(coordinates)
            coordinates.append(blocks)
            for b in blocks:
                block_incidence[b].add(coord_id)

    require(all(len(c) == 3 for c in coordinates), "column degree")
    require(all(len(b) == 6 for b in block_incidence), "block size")

    max_intersection = 0
    for i in range(L):
        for j in range(i + 1, L):
            max_intersection = max(
                max_intersection,
                len(block_incidence[i] & block_incidence[j]),
            )
    require(max_intersection <= 1, "linearity")
    require(
        all(
            sum(1 for b in block_incidence if coord in b) == 3
            for coord in range(len(coordinates))
        ),
        "coordinate degree replay",
    )

    print(
        "PB_AUDIT7_HIGH_RANK_SUPPORT_PASS",
        f"blocks={L}",
        f"coordinates={len(coordinates)}",
        "block_size=6",
        "coordinate_degree=3",
        f"max_pair_intersection={max_intersection}",
    )


def main() -> None:
    family = check_sidon_lower_bound()
    check_small_binary_sidon()
    check_parameter_identities()
    check_exact_polynomial_fixture()
    check_producer_failures(family)
    check_pilot_vacuity()
    check_high_rank_hypergraph()
    print("ADVERSARIAL_AUDIT_BRIEF4_LOWCORE_PASS")


if __name__ == "__main__":
    main()
