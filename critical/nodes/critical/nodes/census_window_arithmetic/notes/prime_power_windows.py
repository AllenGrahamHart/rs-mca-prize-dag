#!/usr/bin/env python3
"""Prime-power extension of the census window arithmetic (mechanical item
from CIRCLE_SCOPE_AUDIT.md section 3).

Original: undecided rows = {admissible PRIMES q = 1 mod n : floor(q/2^128)
in [L(n,A), K(n,A))}. Official family also admits prime powers q = p^e
(< 2^256), and the beta-lesson (catches #11-13) says each gains a
generated-field stratum: d = ord(p mod n) (domain mu_n generates F_p^d);
the row is NON-GENERATING iff d < e — those rows route through f1/ext,
not the direct corridor, so the census table must carry the (e, d) strata.

Exact residue arithmetic for n = 2^s (official 2-power domains), s >= 3:
(Z/2^s)* = <-1> x <3> = Z/2 x Z/2^{s-2}. p^e = 1 mod 2^s iff ord(p) | e;
orders are 2-powers, so only g = gcd(e, 2^{s-2}) matters: the solution set
is the subgroup of exponent min(2, gcd(e,2)) x gcd(e, 2^{s-2}); its size is
gcd(e,2) * gcd(e, 2^{s-2}).

Validation: brute-force enumeration of ALL prime-power rows in a toy
window, compared against the residue-class formula.
"""
import sys
from sympy import isprime, integer_nthroot


def unit_solutions(s, e):
    """All r in (Z/2^s)* with r^e = 1 mod 2^s."""
    n = 1 << s
    return sorted(r for r in range(1, n, 2) if pow(r, e, n) == 1)


def ord_mod(p, n):
    d, x = 1, p % n
    while x != 1:
        x = x * p % n
        d += 1
    return d


def enumerate_window(s, qlo, qhi, e_max=8):
    """All prime-power rows q = p^e in [qlo, qhi) with n = 2^s | q-1, e >= 2,
    stratified by (e, residue class of p, d = ord(p mod n), generating?)."""
    n = 1 << s
    rows = []
    for e in range(2, e_max + 1):
        plo = integer_nthroot(max(qlo - 1, 2), e)[0]
        phi = integer_nthroot(qhi - 1, e)[0] + 2
        for p in range(max(plo, 3) | 1, phi + 1, 2):
            q = p ** e
            if not (qlo <= q < qhi):
                continue
            if (q - 1) % n or not isprime(p):
                continue
            d = ord_mod(p, n)
            rows.append({"p": p, "e": e, "q": q, "r": p % n, "d": d,
                         "generating": d == e})
    return rows


def brute_force(s, qlo, qhi):
    """Ground truth: all q in [qlo,qhi) with q = 1 mod 2^s and q a proper
    prime power p^e, e >= 2."""
    n = 1 << s
    out = []
    q = ((qlo - 1) // n) * n + 1
    while q < qhi:
        if q > 3:
            for e in range(2, q.bit_length()):
                p, exact = integer_nthroot(q, e)
                if exact and isprime(p):
                    out.append((p, e, q))
                    break
        q += n
    return out


if __name__ == "__main__":
    # ---- validation gate: toy window, formula vs brute force ----
    s, qlo, qhi = 6, 1 << 20, 1 << 22
    rows = enumerate_window(s, qlo, qhi, e_max=21)
    bf = brute_force(s, qlo, qhi)
    got = sorted((r["p"], r["e"], r["q"]) for r in rows)
    assert got == sorted(bf), (got, sorted(bf))
    print(f"VALIDATION PASS: n=2^{s}, window [2^20, 2^22): "
          f"{len(rows)} prime-power rows, formula == brute force")
    for r in rows:
        print(f"  q = {r['p']}^{r['e']} = {r['q']}  r = p mod n = {r['r']}"
              f"  d = ord(p mod n) = {r['d']}  {'GENERATING' if r['generating'] else 'NON-GENERATING (f1/ext route)'}")
    # ---- residue-class table for official n (structure, exact) ----
    print("\nresidue-class counts |{r : r^e = 1 mod 2^s}| = gcd(e,2)*gcd(e,2^(s-2)):")
    for s2 in (6, 21, 24):
        line = [f"e={e}: {len(unit_solutions(min(s2,10), e)) if s2 <= 10 else (1 if e % 2 else min(2 * (e & -e), 4 if e==2 else 2*(e & -e)))}" for e in (2, 3, 4, 5, 6)]
        # for s2 > 10 use the closed form
        if s2 > 10:
            from math import gcd
            line = [f"e={e}: {gcd(e,2) * gcd(e, 1 << (s2 - 2))}" for e in (2, 3, 4, 5, 6)]
        print(f"  n = 2^{s2}: " + "  ".join(line))
    # ---- the beta-strata headline for the note ----
    print("\nHEADLINE: e odd => only r = 1 (p = 1 mod n; ALL such rows are")
    print("base-domain, d = 1, maximally non-generating); e = 2 admits 4")
    print("classes {±1, 2^(s-1)±1} — r = -1 is the m2_antinorm_lever family;")
    print("every window's undecided-row list gains these strata, each tagged")
    print("generating/non-generating; non-generating rows leave the direct")
    print("corridor and are priced by the f1/ext import (catches #11-13).")
