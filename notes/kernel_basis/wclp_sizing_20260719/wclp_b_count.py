#!/usr/bin/env python3
"""wclp_b_count.py -- exact (2,7) analogous quotient orbit count via Burnside.

Model (derived from the audited (2,6) census conventions in
experiments/prize_resolution/dli_wcl_ell2_weight6_candidate_orbits_modal.py):

A (2,w) router candidate presentation for w = k+3 (selected k-set normalized
to contain 1, complementary TRIPLE with free product d = zeta^c) is
  ({exponents of the k-1 non-1 selected roots}, c),
quotiented by odd Galois dilation (512 units mod 1024) and rebasing (k
presentations; rebasing at x = zeta^a maps exponents e -> e-a and c -> c-3a,
because the complement always has THREE roots).

Unnormalized model: W = {(Q, c)}, Q a legal k-subset of Z_1024 (legal =
pairwise base-exponent-distinct mod 512, i.e. no antipodal pair {a, a+512}),
c in Z_1024; group H = {(t, r)} = dilations x scalings, |H| = 512*1024,
acting by (Q,c) -> (tQ + r, tc + 3r).  Presentations = W restricted to 0 in Q
with rebasing = residual scaling, so presentation-orbits == H-orbits on W.

Burnside collapse (proved in-line below by the translation-conjugacy of
(t,r) ~ (t, r-(t-1)s) and the c-equation (t-1)c = -3r having g=gcd(t-1,1024)
solutions iff g | r):
    orbits = (1/512) * sum_{t odd mod 1024} N_inv_k(t)
where N_inv_k(t) = # legal k-subsets of Z_1024 invariant under mult-by-t.

Controls (both must reproduce audited numbers exactly):
  k=3 (weight 6): orbits must equal 404,740 (the audited (2,6) census);
  pair orbits (weight 6 selected pairs under dilation alone) must equal 1,514.

All arithmetic exact integers.
"""
from math import comb, gcd

ORDER = 1024
HALF = 512


def clean_pair_multiset(t: int, maxlen: int) -> dict[int, int]:
    """Partner-pair length multiset for mult-by-t cycles on Z_1024.

    Returns {cycle_length: number_of_partner_PAIRS {C, iota(C)}} over clean
    cycles (no internal antipodal pair), lengths <= maxlen.  iota(a) = a+512
    commutes with mult-by-t, so it maps cycles to cycles; a cycle with
    iota(C) == C contains an internal antipodal pair and is unusable.
    """
    seen = [False] * ORDER
    cycles = []
    cell = [None] * ORDER
    for s in range(ORDER):
        if seen[s]:
            continue
        c = []
        a = s
        while not seen[a]:
            seen[a] = True
            c.append(a)
            a = a * t % ORDER
        fc = tuple(sorted(c))
        cycles.append(fc)
        for x in c:
            cell[x] = fc
    m: dict[int, int] = {}
    done = set()
    for c in cycles:
        if c in done:
            continue
        partner = cell[(c[0] + HALF) % ORDER]
        if partner == c:  # internal antipodal pair -> dirty, unusable
            done.add(c)
            continue
        done.add(c)
        done.add(partner)
        if len(c) <= maxlen:
            m[len(c)] = m.get(len(c), 0) + 1
    return m


def n_inv_k4(m: dict[int, int]) -> int:
    """# legal 4-subsets invariant: unions of clean cycles totaling 4,
    at most one cycle per partner pair (2 orientations each)."""
    m1 = m.get(1, 0)
    m2 = m.get(2, 0)
    m3 = m.get(3, 0)
    m4 = m.get(4, 0)
    return (
        2 * m4
        + 4 * m3 * m1
        + 4 * comb(m2, 2)
        + 8 * m2 * comb(m1, 2)
        + 16 * comb(m1, 4)
    )


def n_inv_k3(m: dict[int, int]) -> int:
    m1 = m.get(1, 0)
    m2 = m.get(2, 0)
    m3 = m.get(3, 0)
    return 2 * m3 + 4 * m2 * m1 + 8 * comb(m1, 3)


def main() -> None:
    total4 = 0
    total3 = 0
    total_pairs = 0       # weight-6 selected-pair orbits under dilation alone
    total_triples = 0     # weight-7 selected-triple orbits under dilation alone
    for t in range(1, ORDER, 2):
        m = clean_pair_multiset(t, 4)
        total4 += n_inv_k4(m)
        total3 += n_inv_k3(m)
        # normalized selected sets: exclude the {0},{512} singleton partner
        # pair (0 and 512 are always fixed points of mult-by-t).
        m1p = m.get(1, 0) - 1
        m2 = m.get(2, 0)
        m3 = m.get(3, 0)
        total_pairs += 2 * m2 + 4 * comb(m1p, 2)
        total_triples += 2 * m3 + 4 * m2 * m1p + 8 * comb(m1p, 3)

    assert total4 % 512 == 0, total4
    assert total3 % 512 == 0, total3
    assert total_pairs % 512 == 0, total_pairs
    assert total_triples % 512 == 0, total_triples
    orbits7 = total4 // 512
    orbits6 = total3 // 512
    pair_orbits6 = total_pairs // 512
    triple_orbits7 = total_triples // 512

    # combinatorial identities (exact)
    legal_pairs = comb(511, 2) * 4        # audited: 521,220
    legal_triples = comb(511, 3) * 8      # weight-7 analogue
    print("CONTROL weight-6 candidate orbits :", orbits6, "(audited 404,740)")
    print("CONTROL weight-6 pair orbits      :", pair_orbits6, "(audited 1,514)")
    print("CONTROL legal pairs               :", legal_pairs, "(audited 521,220)")
    assert orbits6 == 404_740, orbits6
    assert pair_orbits6 == 1_514, pair_orbits6
    assert legal_pairs == 521_220, legal_pairs
    print()
    print("WEIGHT-7 legal normalized triples :", legal_triples)
    print("WEIGHT-7 triple orbits (dilation) :", triple_orbits7)
    print("WEIGHT-7 router presentations     :", triple_orbits7 * ORDER)
    print("WEIGHT-7 candidate orbits (2,7)   :", orbits7)
    print("blow-up vs (2,6)                  : %.2f x" % (orbits7 / 404_740))


if __name__ == "__main__":
    main()
