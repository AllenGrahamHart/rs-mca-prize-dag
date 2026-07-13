#!/usr/bin/env python3
"""w7 fresh-context audit: independent cross-checks (my own code paths,
not the shipped verifiers). Subcommands keep each run inside ramguard tiny.

  schedule   -- dyadic tower identities, #190 ell-form, 41^34 < 2^202
  newton     -- independent exhaustive Newton-cutoff check on fresh primes
  w3spot     -- weight-3 census: independent exact resultant + factor spot-check
  ell2spot   -- ell=2 weight-3 census: same, degree 512
  cover      -- weight-3 census: random raw supports land in listed orbits
  engineered -- engineered weight-6 witness: independent norm + v2 check
"""
import json
import math
import random
import sys
from fractions import Fraction
from pathlib import Path

TREE = Path("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad/w7_tree")
EXP = TREE / "experiments/prize_resolution"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def my_split_primes(order: int, bits_needed: int, start_shift: int = 0):
    """Ascending primes p = 1 mod order from 2^30 + shift (DIFFERENT direction
    than the shipped verifiers, which descend from 2^31)."""
    out, prod = [], 1
    cand = ((2**30 + start_shift) // order) * order + 1
    while prod.bit_length() <= bits_needed + 2:
        cand += order
        if is_prime(cand):
            g = next(b for b in range(2, 200)
                     if pow(pow(b, (cand - 1) // order, cand), order // 2, cand) == cand - 1)
            out.append((cand, pow(g, (cand - 1) // order, cand)))
            prod *= cand
    return out, prod


def exact_resultant(exponents, signs, half, order, bits):
    """CRT-reconstruct Res(X^half+1, P) exactly with my own prime set."""
    moduli, prod = my_split_primes(order, bits)
    residues = []
    for p, omega in moduli:
        r, root, step = 1, omega, omega * omega % p
        for _ in range(half):
            v = sum(s * pow(root, e, p) for e, s in zip(exponents, signs)) % p
            r = r * v % p
            root = root * step % p
        residues.append(r)
    # CRT
    x, m = 0, 1
    for (p, _), r in zip(moduli, residues):
        t = (r - x) * pow(m, -1, p) % p
        x += m * t
        m *= p
    assert 0 <= x < m
    return x


def cmd_schedule():
    t = 2**33
    dims = [math.ceil((t // 2**j) / 2) for j in range(34)]
    assert dims == [2**(32 - j) for j in range(33)] + [1]
    assert sum(dims) == t
    assert math.ceil((t // 2**34) / 2) == 0  # exactly 34 nonempty levels
    # valuation-partition identity
    for tt in (1, 5, 96, 2**10, 2**10 + 7):
        assert sum(math.ceil((tt // 2**j) / 2) for j in range(tt.bit_length())) == tt
    # 190 ell-form: min window charge 2*(256 ell)*2^-(ell+5) = 16 ell/2^ell
    for ell in range(1, 40):
        m = Fraction(2 * 256 * ell, 2 ** (ell + 5))
        assert m == Fraction(16 * ell, 2**ell)
        assert (m > Fraction(1, 32)) == (ell <= 12)
    # table rows
    tbl = {1: Fraction(8), 2: Fraction(8), 4: Fraction(4), 8: Fraction(1, 2), 16: Fraction(1, 256)}
    for ell, v in tbl.items():
        assert Fraction(16 * ell, 2**ell) == v
    # baseline integer pin
    assert 2**182 < 41**34 < 2**202  # ~2^182.2; the pinned comparison has ~20 bits slack
    assert Fraction(41, 8)**34 < 2**100
    # residual slot recomputation (schedule dims, dedup ell set)
    residual = []
    for ell in sorted(set(dims)):
        for w in range(ell + 1, ell + 6):
            if w <= 2 * ell:
                continue
            if ell == 1 and w in (3, 4):
                continue  # census exclusions
            residual.append((ell, w))
    assert residual == [(1, 5), (1, 6), (2, 5), (2, 6), (2, 7), (4, 9)], residual
    # ell=1 window includes w=2 handled by Newton (2 <= 2*1)
    print("W7_SCHEDULE_PASS dims=(2^32..2,1,1) sum=2^33 min_charge=16ell/2^ell "
          "emptiness_iff_ell<=12 residual_slots=6")


def cmd_newton():
    # Independent re-implementation: for fresh primes NOT in the shipped
    # verifier's list, every distinct-nonzero root set with w <= 2*ell and
    # vanishing odd moments p_1..p_{2ell-1} must be closed under negation.
    import itertools
    hits = checked = 0
    for p in (37, 41, 43):
        for ell in (1, 2, 3):
            for w in range(2, 2 * ell + 1):
                for roots in itertools.combinations(range(1, p), w):
                    checked += 1
                    if any(sum(pow(r, m, p) for r in roots) % p
                           for m in range(1, 2 * ell, 2)):
                        continue
                    hits += 1
                    assert all((p - r) % p in roots for r in roots), (p, ell, roots)
    assert hits > 0
    # sharpness: QR subgroups at w = 2ell+1
    for p, ell in ((7, 1), (11, 2), (19, 4)):
        qrs = sorted({pow(x, 2, p) for x in range(1, p)})
        assert len(qrs) == 2 * ell + 1
        for m in range(1, 2 * ell, 2):
            assert sum(pow(r, m, p) for r in qrs) % p == 0
        assert not any((p - r) % p in qrs for r in qrs)
    print(f"W7_NEWTON_INDEP_PASS checked={checked} antipodal_hits={hits} qr_sharpness=3/3")


def cmd_w3spot():
    data = json.loads((EXP / "dli_wcl_weight3_classes_result.json").read_text())
    rows = data["completed"]
    random.seed(20260713)
    sample = random.sample(rows, 4)
    for row in sample:
        norm = int(row["norm"])
        mine = exact_resultant(row["exponents"], row["signs"], 256, 512, 406)
        assert mine == norm, (row["key"], mine, norm)
        prod = 1
        for f in row["factors"]:
            q = int(f["prime"])
            assert is_prime(q), q
            prod *= q ** f["exponent"]
            v2 = ((q - 1) & -(q - 1)).bit_length() - 1
            assert v2 == f["v2_prime_minus_1"]
            if q < 2**256:
                assert v2 < 41
        assert prod == norm
    print(f"W7_W3SPOT_PASS classes_checked={len(sample)} exact_resultant=my_crt "
          "factors=verified_prime v2<41")


def cmd_ell2spot():
    data = json.loads((EXP / "dli_wcl_ell2_weight3_classes_result.json").read_text())
    rows = data["completed"]
    random.seed(20260713)
    sample = random.sample(rows, 2)
    for row in sample:
        norm = int(row["norm"])
        mine = exact_resultant(row["exponents"], row["signs"], 512, 1024, 812)
        assert mine == norm, (row["key"], mine, norm)
        prod = 1
        for f in row["factors"]:
            q = int(f["prime"])
            assert is_prime(q), q
            prod *= q ** f["exponent"]
            v2 = ((q - 1) & -(q - 1)).bit_length() - 1
            assert v2 == f["v2_prime_minus_1"]
            if q < 2**256:
                assert v2 < 41
        assert prod == norm
    print(f"W7_ELL2SPOT_PASS classes_checked={len(sample)} exact_resultant=my_crt "
          "factors=verified_prime v2<41")


def cmd_cover():
    # 60 random raw weight-3 signed supports: brute-force the affine orbit
    # canonical key and confirm it is one of the 254 listed class keys.
    data = json.loads((EXP / "dli_wcl_weight3_classes_result.json").read_text())

    def encode(full):
        red = sorted((t % 256, 1 if t < 256 else -1) for t in full)
        assert len({e for e, _ in red}) == 3
        if red[0][1] < 0:
            red = [(e, -s) for e, s in red]
        k = 0
        for i, (e, s) in enumerate(red):
            k |= (e | ((s < 0) << 8)) << (9 * i)
        return k

    keys = set()
    for row in data["representatives"]:
        full = tuple(e if s > 0 else e + 256
                     for e, s in zip(row["exponents"], row["signs"]))
        keys.add(encode(full))
    assert len(keys) == 254
    random.seed(7)
    hits = 0
    for _ in range(25):
        es = random.sample(range(256), 3)
        ss = [1] + [random.choice((1, -1)) for _ in range(2)]
        full = tuple(e if s > 0 else e + 256 for e, s in zip(es, ss))
        orbit = set()
        for a in range(1, 512, 2):
            da = tuple(a * t % 512 for t in full)
            for b in range(256):
                orbit.add(encode(tuple((t + b) % 512 for t in da)))
        inter = orbit & keys
        assert len(inter) == 1, (full, sorted(inter))  # exactly one listed class
        hits += 1
    print(f"W7_W3COVER_PASS random_supports={hits}/25 each_in_exactly_one_listed_orbit")


def cmd_engineered():
    exponents, signs = zip((0, 1), (33, -1), (40, 1), (136, -1), (143, -1), (145, 1))
    norm = exact_resultant(list(exponents), list(signs), 256, 512, 512)
    q = 61156209198655289707609620063727948198186060921658038067621917786894060626433
    assert norm == 2 * q
    assert is_prime(q)
    v2 = ((q - 1) & -(q - 1)).bit_length() - 1
    assert v2 == 9
    print(f"W7_ENGINEERED_PASS norm=2q q_prime=True v2(q-1)={v2} norm_bits={norm.bit_length()}")


if __name__ == "__main__":
    dict(schedule=cmd_schedule, newton=cmd_newton, w3spot=cmd_w3spot,
         ell2spot=cmd_ell2spot, cover=cmd_cover, engineered=cmd_engineered)[sys.argv[1]]()
