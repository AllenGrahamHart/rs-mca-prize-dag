# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matchings 1 and 2 are

```text
(de,de), (-de,bf),         (sigma_o ef,sigma_c cf),
(de,de), (-de,sigma_c cf), (sigma_o ef,bf).
```

Write `L_i(q)=B_i-q A_i`. The first equation factors exactly as

```text
paired(q,q) = 4 L_0(q) L_1(q)^2 L_2(q).
```

The characteristic is odd, so every finite `q=de` solution lies on one of
the three branches `q=B_i/A_i`. Every denominator root enters the
exceptional census. At direct replay, all 36 zero-denominator source points
are empty branches; no free branch occurs.

Let `m=df`, `s=(d+f)^2`, and `z=1/d`. Then

```text
M(z) = 1 + (2m-s)z^2 + m^2 z^4 = 0,
e = qz,  f = mz.
```

For matching 1 the second equation is `P(z)=paired(-q,bmz)=0`; for
matching 2 it is `P(z)=paired(-q,sigma_c cmz)=0`. In both cases `P` is
quadratic. Divide `M` by `P` in the exact four-dimensional source algebra.
Every row has linear remainder `R(z)=r_0+r_1 z`. If
`P(z)=p_0+p_1 z+p_2 z^2`, a common root satisfies the division-free cut

```text
r_1^2 p_0 - r_1 r_0 p_1 + p_2 r_0^2 = 0.
```

The compiler norms this cut through the basis `1,t,b,bt`. The candidate
`r` set contains all roots of the norm numerator and denominator and all
inverse-guard numerators and denominators. Every candidate is lifted through
the base `t` quadratic, `b` quadratic, linear `c` recovery, and compact
kernel. At each guarded source point, all roots of `M` and `P` are
intersected. For each common nonzero `z`, set `d=1/z`, `e=qz`, and `f=mz`.

Direct replay verifies both product equations, the squared-sum equation,
`paired(q,q)=0`, and the matching-specific second equation. Matching 1 then
checks `paired(sigma_o ef,sigma_c cf)` in all four lanes; matching 2 checks
`paired(sigma_o ef,bf)` in both `sigma_o` lanes at each fixed `sigma_c`.

Across all 36 branch rows there are 360 candidate `r` values and 216 guarded
source points. Matching 1 has no common `z` lift. Matching 2 has 32 `z`
candidates and 64 final-lane evaluations; every final value is nonzero. The
target-boundary, witness, free-branch, and unresolved ledgers are empty.

Matching 1 covers `4*4=16` raw cases and matching 2 covers another 16.
The internal branches do not multiply that count. All 32 stated cases are
empty. QED.
