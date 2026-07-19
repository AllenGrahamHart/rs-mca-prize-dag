#!/usr/bin/env python3
"""g1a_check3 — exact window arithmetic for the G1 coverage hypothesis.

Per cell (s, rho, n'): compute
  C = C(n'-1, k')  [k' = rho*n']
  q* (falsifier threshold): coverage FALSIFIED (rigorously, F4 theorem,
      valid for official fields q >= 2 n'^2) for all q with
      2n' | q-1, 2 n'^2 <= q < q* := 3 C / (4 (k'+1) * (121/128) * nb^6)
  q** (first-moment-fit threshold): first-moment weighted census fits budget
      iff q >= q** := C * wbar * 128/(121 nb^6), wbar = (1-rho) k' + 3
  TRIV: unconditional PROVED window iff (k'+2)(C(n'-1,k')+C(n'-1,k'+1))
      <= (121/128) nb^6  (q-independent)
under both budget readings nb = 2n' (own row) and nb = n0 (top row).
"""
from math import comb, log2
from fractions import Fraction

BUD = Fraction(121, 128)

def cell(npr, rho_num, rho_den, nb):
    kpr = npr * rho_num // rho_den
    C1 = comb(npr - 1, kpr)
    C2 = comb(npr - 1, kpr + 1)
    budget = BUD * nb ** 6
    qstar = Fraction(3 * C1, 4 * (kpr + 1)) / budget
    wbar = (1 - Fraction(rho_num, rho_den)) * kpr + 3
    qss = Fraction(C1) * wbar / budget
    triv = (kpr + 2) * (C1 + C2) <= budget
    return kpr, C1, qstar, qss, triv

def fmt(x):
    try:
        return f"2^{log2(x):7.1f}" if x > 0 else "  -    "
    except OverflowError:
        return f"2^{(x.numerator.bit_length() - x.denominator.bit_length()):7d}"

print("=== per-cell thresholds (rate 1/2 and 1/4), own-row budget nb=2n' ===")
print("rho   n'    k'   log2C     q*(falsified below)  q**(fm-fit above)  TRIVIAL?")
for (rn, rd) in [(1, 2), (1, 4)]:
    for npr in [32, 64, 128, 256, 512, 1024, 2048, 4096]:
        kpr, C1, qs, qss, triv = cell(npr, rn, rd, 2 * npr)
        print(f"1/{rd}  {npr:5d} {kpr:5d} {log2(C1):7.1f}   {fmt(qs)}"
              f"            {fmt(qss)}      {triv}")

print()
print("=== s=13 tower, rate 1/2, q ~ 2^26 (minimal official), top-row budget nb=8192 ===")
n0 = 8192
q = n0 * n0 + 1  # stand-in magnitude for minimal official field
for npr in [64, 128, 256, 512, 1024, 2048, 4096]:
    kpr, C1, qs, qss, triv = cell(npr, 1, 2, n0)
    status = ("FALSIFIED (rigorous)" if q < qs and q >= 2 * npr * npr else
              "first-moment VIOLATED (not rigorous)" if q < qss else
              "fits first moment (conditional lemma)" if not triv else
              "PROVED trivially")
    if triv:
        status = "PROVED trivially"
    print(f" n'={npr:5d}: q*={fmt(qs)} q**={fmt(qss)} triv={triv}  -> q=2^26: {status}")

print()
print("=== prize fields: smallest falsified n' at rate 1/2 (top-row budget nb=2n'... both) ===")
for qexp in (26, 64, 128, 256):
    q = 2 ** qexp
    for reading, nbf in (("own-row nb=2n'", lambda np_: 2 * np_),
                         ("top-row nb=16n'", lambda np_: 16 * np_)):
        ans = None
        for npr in [64, 128, 256, 512, 1024, 2048, 4096, 8192]:
            kpr, C1, qs, qss, triv = cell(npr, 1, 2, nbf(npr))
            if q < qs and q >= 2 * npr * npr:
                ans = npr; break
        print(f" q=2^{qexp:3d} {reading:16s}: smallest rigorously falsified n' = {ans}")

print()
print("=== headline exact instances ===")
# s=8 primary cell, minimal official field
kpr, C1, qs, qss, triv = cell(128, 1, 2, 256)
q = 65537
lower = Fraction(C1, 4 * q * (kpr + 1))
print(f"s=8 rho=1/2 primary (n'=128,k'=64,q=65537): B(c*) >= {float(lower):.3e}"
      f" vs budget {float(BUD*256**6):.3e}  ratio {float(lower/(BUD*256**6)):.2e}"
      f"  q < q*? {q < qs}  (q >= 2n'^2? {q >= 2*128*128})")
# s=13 primary cell
kpr, C1, qs, qss, triv = cell(4096, 1, 2, 8192)
q = 8192 ** 2
lower = Fraction(C1, 4 * q * (kpr + 1))
print(f"s=13 rho=1/2 primary (n'=4096,q~2^26): log2 B(c*) >= "
      f"{lower.numerator.bit_length() - lower.denominator.bit_length()}"
      f" vs budget 2^{log2(float(BUD*8192**6)):.1f}")
# smallest s falsified at minimal fields, rate 1/2, primary cell, top-row budget
for s in range(6, 17):
    n0 = 2 ** s
    npr = n0 // 2
    kpr, C1, qs, qss, triv = cell(npr, 1, 2, n0)
    q = n0 * n0 + 1
    ok = (q < qs) and (q >= 2 * npr * npr)
    print(f"  s={s:2d} minimal-official primary cell falsified: {ok}")
