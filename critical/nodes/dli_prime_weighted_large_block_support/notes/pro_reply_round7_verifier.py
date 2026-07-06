#!/usr/bin/env python3
"""
Exact verifier for the DLI-CLOSE-5 B1 sub-volume counterexample.

It certifies an admissible R* row with a sub-volume weight-3..5 window and
four multiplier-independent primitive weight-5 generator orbits.

No external packages are required.
"""
from itertools import combinations, product
from math import comb, gcd, isqrt

q = 110_849
n = 64
N = n // 2
L = 1
q_minus_1_factorisation = {2: 8, 433: 1}
prime_factors_q_minus_1 = [2, 433]
pocklington_witness = 3
smallest_primitive_root = 3
omega = 98_761
modulus_for_multiplier_certificate = 1_000_003

# Listed in positive-leading-sign form: sum a*z^e = 0 at z=omega.
polynomial_terms = [
    [(0, 1), (4, 1), (21, 1), (27, -1), (29, 1)],
    [(0, 1), (3, 1), (21, -1), (23, 1), (28, -1)],
    [(0, 1), (3, 1), (6, -1), (25, -1), (29, 1)],
    [(0, 1), (3, 1), (8, 1), (19, -1), (25, 1)],
]


def trial_prime(m: int) -> bool:
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2
    return True


def pocklington_prime_check() -> None:
    assert q - 1 == (2 ** 8) * 433
    assert trial_prime(2) and trial_prime(433)
    F = q - 1
    assert F > isqrt(q)
    a = pocklington_witness
    assert pow(a, q - 1, q) == 1
    for p in prime_factors_q_minus_1:
        assert gcd(pow(a, (q - 1) // p, q) - 1, q) == 1


def is_primitive_root(g: int) -> bool:
    return all(pow(g, (q - 1) // p, q) != 1 for p in prime_factors_q_minus_1)


def vec_from_terms(terms):
    c = [0] * N
    for e, a in terms:
        assert 0 <= e < N and a in (-1, 1)
        c[e] += a
    assert all(x in (-1, 0, 1) for x in c)
    return tuple(c)


def mul_vec(c, d):
    """Multiply in Z[z]/(z^N+1), reduced to exponents 0..N-1."""
    out = [0] * N
    for i, a in enumerate(c):
        if not a:
            continue
        for j, b in enumerate(d):
            if not b:
                continue
            e = (i + j) % (2 * N)
            coeff = a * b
            if e >= N:
                e -= N
                coeff = -coeff
            out[e] += coeff
    return tuple(out)


def shift_vec(c, shift):
    out = [0] * N
    for i, a in enumerate(c):
        if not a:
            continue
        e = (i + shift) % (2 * N)
        coeff = a
        if e >= N:
            e -= N
            coeff = -coeff
        out[e] += coeff
    return tuple(out)


def normalize(c):
    """Canonical representative under signed shifts; z^N=-1 already includes global sign."""
    best = None
    for s in range(2 * N):
        t = shift_vec(c, s)
        if best is None or t < best:
            best = t
    return best


def dilate_vec(c, a):
    """Galois dilation z -> z^a, a odd mod 2N."""
    out = [0] * N
    for i, coeff0 in enumerate(c):
        if not coeff0:
            continue
        e = (a * i) % (2 * N)
        coeff = coeff0
        if e >= N:
            e -= N
            coeff = -coeff
        out[e] += coeff
    return tuple(out)


def l0_weight(c) -> int:
    return sum(1 for x in c if x)


def eval_mod_q(c) -> int:
    return sum(a * pow(omega, i, q) for i, a in enumerate(c) if a) % q


def primitive_at_pinned_embedding(c) -> bool:
    items = [(i, a) for i, a in enumerate(c) if a]
    m = len(items)
    for mask in range(1, (1 << m) - 1):
        s = 0
        for j, (i, a) in enumerate(items):
            if (mask >> j) & 1:
                s = (s + a * pow(omega, i, q)) % q
        if s == 0:
            return False
    return True


def enumerate_primitive_vanisher_orbits(max_weight=5):
    """Exhaustive enumeration of primitive signed-shift classes of weights 3..max_weight."""
    reps = {}
    powers = [pow(omega, i, q) for i in range(N)]
    for wt in range(3, max_weight + 1):
        for pos in combinations(range(N), wt):
            for signs in product((1, -1), repeat=wt):
                value = sum(s * powers[i] for i, s in zip(pos, signs)) % q
                if value != 0:
                    continue
                c = [0] * N
                for i, s in zip(pos, signs):
                    c[i] = s
                c = tuple(c)
                if primitive_at_pinned_embedding(c):
                    reps[normalize(c)] = c
    return reps


def matrix_for_left_multiplication(c, p):
    columns = []
    for j in range(N):
        e = [0] * N
        e[j] = 1
        columns.append(mul_vec(c, tuple(e)))
    return [[columns[col][row] % p for col in range(N)] for row in range(N)]


def invert_matrix_mod(A, p):
    nrows = len(A)
    M = [row[:] + [1 if i == j else 0 for j in range(nrows)] for i, row in enumerate(A)]
    for col in range(nrows):
        pivot = None
        for r in range(col, nrows):
            if M[r][col] % p:
                pivot = r
                break
        if pivot is None:
            raise AssertionError("singular multiplication matrix modulo certificate prime")
        M[col], M[pivot] = M[pivot], M[col]
        inv_pivot = pow(M[col][col], -1, p)
        M[col] = [(x * inv_pivot) % p for x in M[col]]
        for r in range(nrows):
            if r == col:
                continue
            factor = M[r][col] % p
            if factor:
                M[r] = [(M[r][k] - factor * M[col][k]) % p for k in range(2 * nrows)]
    return [row[nrows:] for row in M]


def mat_vec_mod(A, v, p):
    return [sum(A[i][j] * (v[j] % p) for j in range(N)) % p for i in range(N)]


def certify_no_ternary_multiplier_between_generators(generators):
    """
    Complete reduced-ternary multiplier check.

    For each source P_i, invert left multiplication by P_i modulo p=1,000,003.
    If a reduced ternary integer multiplier m existed with P_i*m equal to a
    signed shift of P_j, then the unique modular solution would have every
    coordinate in {0, ±1}.  The verifier checks that this never happens.
    """
    p = modulus_for_multiplier_certificate
    allowed = {0, 1, p - 1}
    for i, source in enumerate(generators):
        inv = invert_matrix_mod(matrix_for_left_multiplication(source, p), p)
        for j, target0 in enumerate(generators):
            if i == j:
                continue
            for s in range(2 * N):
                target = shift_vec(target0, s)
                sol = mat_vec_mod(inv, target, p)
                assert any(x not in allowed for x in sol), (i, j, s, sol)


def certify_no_level_lift(generators):
    # A level-32 lift into level 64 has, after any signed shift, support all of one parity.
    for c in generators:
        for s in range(2 * N):
            supp = [i for i, a in enumerate(shift_vec(c, s)) if a]
            assert not all(i % 2 == supp[0] % 2 for i in supp)


def certify_no_same_norm_dilation(generators):
    reps = [normalize(c) for c in generators]
    for i, c in enumerate(generators):
        dilation_class = {normalize(dilate_vec(c, a)) for a in range(1, 2 * N, 2)}
        for j, rep in enumerate(reps):
            if i != j:
                assert rep not in dilation_class, (i, j)


def main():
    pocklington_prime_check()
    assert q % n == 1
    assert q < 2 ** 256
    assert 2 ** N >= q ** L

    assert not is_primitive_root(2)
    assert is_primitive_root(smallest_primitive_root)
    assert omega == pow(smallest_primitive_root, (q - 1) // n, q)
    assert pow(omega, n, q) == 1
    assert pow(omega, N, q) == q - 1

    generators = [vec_from_terms(t) for t in polynomial_terms]
    for c in generators:
        assert l0_weight(c) == 5
        assert eval_mod_q(c) == 0
        assert primitive_at_pinned_embedding(c)

    found = enumerate_primitive_vanisher_orbits(max_weight=5)
    listed_reps = {normalize(c) for c in generators}
    assert set(found) == listed_reps
    assert len(found) == 4

    certify_no_ternary_multiplier_between_generators(generators)
    certify_no_level_lift(generators)
    certify_no_same_norm_dilation(generators)

    total_signed_vectors = sum(comb(N, w) * (2 ** w) for w in range(3, 6))
    # For n=2N a power of two, every nonzero signed shift has only the zero fixed
    # vector on reduced ternary vectors, so the action is free on weights 1..N-1.
    total_orbits_weight_3_to_5 = total_signed_vectors // (2 * N)
    assert total_signed_vectors % (2 * N) == 0
    assert total_orbits_weight_3_to_5 == 110_298
    assert total_orbits_weight_3_to_5 < q

    print("DLI-CLOSE-5 B1 verifier: PASS")
    print(f"q={q}, n'={n}, N={N}, L={L}, primitive root g={smallest_primitive_root}, omega={omega}")
    print("Pocklington witness a=3 with q-1=2^8*433")
    print(f"sub-volume: signed-shift orbits of weights 3..5 = {total_orbits_weight_3_to_5} < q = {q}")
    print("primitive vanisher orbits of weights <=5 at pinned embedding: exactly 4")
    for idx, c in enumerate(generators, 1):
        terms = [(i, a) for i, a in enumerate(c) if a]
        print(f"  P{idx}: {terms}")
    print("independence checks: no signed-shift coincidence, no reduced ternary multiplier, no level lift, no same-norm dilation")
    print("certified base generator count in the weight-3..5 window: 4 (this is B1, not a B2/B3 aggregate break)")


if __name__ == "__main__":
    main()
