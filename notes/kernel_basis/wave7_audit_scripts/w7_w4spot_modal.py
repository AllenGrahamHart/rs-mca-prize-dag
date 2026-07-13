#!/usr/bin/env python3
"""w7 audit (Modal): independent weight-4 spot-check — my own CRT prime set
(ascending from 2^30, disjoint from the shipped verifier's descending set),
2 random classes: exact resultant, factor product, Miller-Rabin, v2 < 41."""
import gzip
import json
import random

GZ = "dli_wcl_weight4_section_result.json.gz"


def is_prime(n):
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


def my_split_primes(order, bits_needed):
    out, prod = [], 1
    cand = (2**30 // order) * order + 1
    while prod.bit_length() <= bits_needed + 2:
        cand += order
        if is_prime(cand):
            g = next(b for b in range(2, 200)
                     if pow(pow(b, (cand - 1) // order, cand), order // 2, cand) == cand - 1)
            out.append((cand, pow(g, (cand - 1) // order, cand)))
            prod *= cand
    return out


def exact_resultant(exponents, signs, half, order, bits):
    moduli = my_split_primes(order, bits)
    x, m = 0, 1
    for p, omega in moduli:
        r, root, step = 1, omega, omega * omega % p
        for _ in range(half):
            v = sum(s * pow(root, e, p) for e, s in zip(exponents, signs)) % p
            r = r * v % p
            root = root * step % p
        t = (r - x) * pow(m, -1, p) % p
        x += m * t
        m *= p
    assert 0 <= x < m
    return x


with gzip.open(GZ, "rt", encoding="utf-8") as fh:
    data = json.load(fh)
rows = data["full_completed"]
random.seed(20260713)
for row in random.sample(rows, 2):
    norm = int(row["norm"])
    mine = exact_resultant(row["exponents"], row["signs"], 256, 512, 514)
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
print("W7_W4SPOT_PASS classes_checked=2 exact_resultant=my_crt factors=verified_prime v2<41")
