# F3 h=3 activation-bound compiler

Status: ARITHMETIC COMPILER + MACHINE-VERIFIED EVIDENCE.

This note repairs the h=3 per-row accident pose by naming the exact sparsity
input that the arithmetic compiler consumes.  It is not a proof of that input.

## Pre-registration

For `H = mu_n <= F_p^*`, `p = 1 mod n`, `p >= n^2`, let `A_3(n,p)` denote the
number of dilation-normalized, non-toral, unordered h=3 shape pairs that pass
the actual common-root activation test:

```text
E1(sigma)(zeta) = E2(sigma)(zeta) = 0
```

for a primitive `n`th root `zeta` modulo `p`.

The corrected target is:

```text
H3-ACT(C):  A_3(n,p) <= C n        for every p = 1 mod n, p >= n^2.
```

This is deliberately a prime-ideal/common-root statement.  The random norm
sample already refuted the stronger rational norm-gcd heuristic: some shapes
have a common rational norm factor `p = 1 mod 96`, `p >= 96^2`, but do not
activate at any primitive root modulo that prime.

## Compiler

The existing pose gives

```text
T_3 <= toral + poisson_boundary + n A_3(n,p).
```

with

```text
toral = binom(n/3,2) if 3 | n, else 0
poisson_boundary <= n^2 / 72       when p >= n^2.
```

Thus `H3-ACT(C)` implies

```text
T_3 <= binom(n/3,2)[3|n] + n^2/72 + C n^2.
```

The replay checks the threshold exactly.  For `C=16`, this is already below
the F3 floor `n^3` for every `n >= 17`; the `n=16` row remains covered by the
existing direct small-row gates.

## Banked n=96 evidence

The complete all-core Terminal C aggregate is not Burnside-deduplicated, so the
raw oriented count is evidence rather than an exact normalized orbit table.  It
is still useful at the correct per-row level:

```text
total oriented activations: 720 / 11808706
maximum oriented activation count at one prime: 92
```

The follow-up deduplication `F3_H3_ACTIVATION_ORBIT_DEDUP.md` reduces the same
activation list to:

```text
unique affine/Galois pair-orbits: 167
maximum deduped per-prime activation count: 27
repeated canonical orbits across threshold primes: 0
```

The maximum occurs at one threshold prime in the `n=96` aggregate and is below
`n` even before deduplication, and far below `n` after deduplication.  This does
not prove `H3-ACT(1)`; it identifies the exact object the proof or a full
certificate must count.

## Remaining proof debt

To close h=3 by this route, prove one of:

1. `H3-ACT(C)` uniformly for an absolute `C`, using the repaired rich-curve
   Stepanov route.  The reduced-condition gate is banked as `RC-RED(13)`;
   the remaining theorem gate is rank-form `RC-NV` plus constants after the
   degeneracy filters; or
2. a per-row certificate family that gives `A_3(n,p) <= Cn` at every official
   h=3 row not covered by a theorem.

The old rational norm-coprimality formulation should not be used as a premise.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_bound_compiler.py
```

Expected digest:

```text
H3_ACTIVATION_BOUND_COMPILER_PASS
```
