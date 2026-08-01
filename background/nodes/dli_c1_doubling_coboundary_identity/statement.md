# DLI C1 doubling-coboundary identity

- **status:** PROVED
- **closure:** proof
- **scope:** every subgroup `H = <omega>` of `F_q^*` with `-1 in H`
  (official C1 instantiation: `|H| = 512` at L=1)
- **consumer:** `dli_c1r3_gated_envelope_bound` (evidence)
- **provenance:** identified in Pro's adversarial audit of the
  inverse-flatness strategy
  (`notes/pro_briefs_20260801/responses/blackhole/`), audited, symbolically
  re-derived, and exactly replayed on our side 2026-08-01.

For a multiplicative coset `C = cH` in `Q = F_q^*/H`, define

```text
D(C) = prod_(h in H) (1 - zeta_q^(ch)),
A(C) = prod_(h in H) (1 + zeta_q^(ch)).
```

**(i) Coboundary identity.** Since squaring maps `cH` onto `2cH`,

```text
A(C) = D(2C) / D(C).                                    (DB-1)
```

**(ii) Positivity.** `-1 in H` pairs each factor with its conjugate, so
`D(C) > 0` and `A(C) > 0`; with `L(C) = log D(C)` and the doubling
permutation `sigma(C) = 2C` on `Q`,

```text
log A(C) = L(sigma C) - L(C),
prod_(C in any sigma-orbit) A(C) = 1.                   (DB-2)
```

**(iii) Consumer form (|H| = 2N, half-section of size N).** Conjugate
pairing over the full orbit gives `A(C) = 2^(2N) T(c)` for the C1 cosine
product `T`, and Parseval yields exactly

```text
X := Z - 2^N/q = (q-1)/(q 2^N) * avg_(C in Q) A(C),     (DB-3)
```

so the L=1 C1-ZERO target `X <= 4` is the exponential-moment inequality

```text
avg_C exp( L(2C) - L(C) )  <=  4 q/(q-1) * 2^N.         (DB-4)
```

**(iv) Small-orbit dichotomy.** If the class of 2 in `Q` has order `r`,
then `2^r in H`, hence `q | 2^(|H| r) - 1`: for every cutoff `R`, all
small-orbit rows divide the finite integer list `2^(|H| r) - 1`,
`r <= R` — an exact resultant router. At `r = 1` (`2 in H`), `(DB-1)`
gives `A(C) = 1` identically and `(DB-3)` pins `X = (q-1)/(q 2^N)`
exactly — the exact-flatness rows.

This theorem does not bound `A(C)` on long doubling orbits (the open
large-orbit exponential-moment problem), does not prove C1-ZERO, SWIF-4,
or any inverse-flatness statement, does not by itself transfer beyond
L=1 (the L=1 gate surplus caveat is recorded in the audit), and does not
prove either Prize result.

## Falsifier

A split prime and coset violating `(DB-1)` in exact arithmetic; a
`sigma`-orbit whose `A`-product differs from 1; a row with `2 in H` whose
excess differs from `(q-1)/(q 2^N)`; or `q` in a small-orbit class not
dividing `2^(|H| r) - 1`.
