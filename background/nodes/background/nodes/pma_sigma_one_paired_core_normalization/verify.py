#!/usr/bin/env python3
"""Verifier for PMA sigma-one paired-core normalization."""

from itertools import combinations
from math import comb
from random import Random


def inv(a, p):
    return pow(a % p, p - 2, p)


def poly_add(a, b, p):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] = (out[i] + x) % p
    for i, x in enumerate(b):
        out[i] = (out[i] + x) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(a, c, p):
    return [(c * x) % p for x in a]


def poly_mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_eval(a, x, p):
    ans = 0
    for c in reversed(a):
        ans = (ans * x + c) % p
    return ans


def locator(points, p):
    out = [1]
    for x in points:
        out = poly_mul(out, [(-x) % p, 1], p)
    return out


def interpolate(points, values, p):
    out = [0]
    for i, xi in enumerate(points):
        basis = [1]
        den = 1
        for j, xj in enumerate(points):
            if i == j:
                continue
            basis = poly_mul(basis, [(-xj) % p, 1], p)
            den = den * (xi - xj) % p
        out = poly_add(out, poly_scale(basis, values[i] * inv(den, p), p), p)
    return out


def classify(domain, k, word, core, p):
    core = tuple(core)
    core_set = set(core)
    q_core = interpolate(core, [word[x] for x in core], p)
    lc = locator(core, p)
    fibers = {}
    for x in domain:
        if x in core_set:
            continue
        value = (word[x] - poly_eval(q_core, x, p)) * inv(poly_eval(lc, x, p), p) % p
        fibers.setdefault(value, []).append(x)
    sizes = sorted(len(xs) for xs in fibers.values())
    paired = sizes == [1] + [2] * ((len(domain) - k) // 2)
    return paired, q_core, lc, fibers


def reconstruct(domain, k, word, core, p):
    paired, q_core, lc, fibers = classify(domain, k, word, core, p)
    assert paired
    singleton_values = [a for a, xs in fibers.items() if len(xs) == 1]
    assert len(singleton_values) == 1
    a0 = singleton_values[0]
    y = fibers[a0][0]
    p0 = poly_add(q_core, poly_scale(lc, a0, p), p)
    petals = []
    anchors = []
    labels = []
    for a, xs in sorted(fibers.items()):
        if a == a0:
            continue
        c = (a - a0) % p
        petals.append(tuple(sorted(xs)))
        labels.append(c)
        anchors.append(poly_add(p0, poly_scale(lc, c, p), p))
    assert len(petals) == (len(domain) - k) // 2
    assert len(set(labels)) == len(labels) and all(labels)
    assert all(poly_eval(p0, x, p) == word[x] for x in tuple(core) + (y,))
    for petal, anchor in zip(petals, anchors):
        assert all(poly_eval(anchor, x, p) == word[x] for x in petal)
    return y, p0, petals, labels, anchors, lc


def constructed_trials():
    rng = Random(20260715)
    checks = 0
    for p, n, k in [(101, 9, 5), (127, 11, 5), (131, 12, 6)]:
        assert (n - k) % 2 == 0
        domain = tuple(range(1, n + 1))
        for _ in range(30):
            core = tuple(sorted(rng.sample(domain, k - 1)))
            rest = [x for x in domain if x not in core]
            rng.shuffle(rest)
            y = rest[0]
            petals = [tuple(rest[i:i + 2]) for i in range(1, len(rest), 2)]
            base = [rng.randrange(p) for _ in range(k - 1)] + [rng.randrange(1, p)]
            lc = locator(core, p)
            labels = rng.sample(range(1, p), len(petals))
            word = {x: poly_eval(base, x, p) for x in core + (y,)}
            for c, petal in zip(labels, petals):
                anchor = poly_add(base, poly_scale(lc, c, p), p)
                for x in petal:
                    word[x] = poly_eval(anchor, x, p)
            paired, _, _, _ = classify(domain, k, word, core, p)
            assert paired
            ry, p0, rpetals, rlabels, anchors, rlc = reconstruct(
                domain, k, word, core, p
            )
            assert ry == y
            assert set(rpetals) == {tuple(sorted(t)) for t in petals}
            assert p0 == base
            assert set(rlabels) == set(labels)
            if len(anchors) >= 2:
                diff = poly_add(anchors[0], poly_scale(anchors[1], -1, p), p)
                roots = {x for x in domain if poly_eval(diff, x, p) == 0}
                assert roots == set(core)
                assert len(diff) - 1 == k - 1
                assert rlc == lc
            checks += 1
    return checks


def exhaustive_word_trials():
    p, n, k = 7, 5, 3
    domain = tuple(range(n))
    paired_count = 0
    checked = 0
    # Deterministic coefficient family, with every core checked for each word.
    for coeffs in combinations(range(p + k - 1), k):
        # Deterministically map combinations to coefficient vectors; this keeps
        # the verifier small while exercising non-layout words as well.
        poly = [x % p for x in coeffs]
        word = {x: (poly_eval(poly, x, p) + x ** 4) % p for x in domain}
        for core in combinations(domain, k - 1):
            paired, _, _, _ = classify(domain, k, word, core, p)
            if paired:
                reconstruct(domain, k, word, core, p)
                paired_count += 1
            checked += 1
    assert checked > 500
    return checked, paired_count


def route_cut_checks():
    checks = 0
    for L in [8, 16, 64, 4096]:
        for kappa in range(1, 5):
            if L < kappa + 4:
                continue
            lineray = comb(L + 1, kappa + 3)
            paving_num = comb(L, kappa)
            # Compare to the unfloored paving charge paving_num/(kappa+1).
            assert lineray * (kappa + 1) > paving_num
            lhs = lineray * (kappa + 1)
            rhs = paving_num
            ratio_num = (L + 1) * (L - kappa) * (L - kappa - 1)
            ratio_den = (kappa + 2) * (kappa + 3)
            assert lhs * ratio_den == rhs * ratio_num
            checks += 1
    return checks


def mutation_checks():
    p, n, k = 101, 9, 5
    domain = tuple(range(1, n + 1))
    core = (1, 2, 3, 4)
    lc = locator(core, p)
    base = [8, 7, 6, 5, 4]
    rest = [5, 6, 7, 8, 9]
    y = rest[0]
    word = {x: poly_eval(base, x, p) for x in core + (y,)}
    for c, pair in zip([11, 29], [(6, 7), (8, 9)]):
        anchor = poly_add(base, poly_scale(lc, c, p), p)
        for x in pair:
            word[x] = poly_eval(anchor, x, p)
    assert classify(domain, k, word, core, p)[0]

    # Removing the singleton shift does not recover the nonzero-shift base.
    q_core = interpolate(core, [word[x] for x in core], p)
    assert q_core != base

    # Merging a singleton into a doubleton destroys the (2,...,2,1) signature.
    mutated = dict(word)
    q_core, lc = q_core, lc
    target = (mutated[6] - poly_eval(q_core, 6, p)) * inv(poly_eval(lc, 6, p), p) % p
    mutated[y] = (poly_eval(q_core, y, p) + target * poly_eval(lc, y, p)) % p
    assert not classify(domain, k, mutated, core, p)[0]
    return 2


def main():
    c1 = constructed_trials()
    c2, paired = exhaustive_word_trials()
    c3 = route_cut_checks()
    c4 = mutation_checks()
    print(
        "PMA_PAIRED_CORE_NORMALIZATION_PASS "
        f"constructed={c1} enumerated={c2} paired={paired} "
        f"route_cut={c3} mutations={c4}"
    )


if __name__ == "__main__":
    main()
