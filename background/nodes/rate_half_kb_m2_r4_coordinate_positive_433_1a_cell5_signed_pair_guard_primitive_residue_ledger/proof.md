# Proof

By the generic-reducedness theorem,

```text
A_g ~= K[s]/(chi_L(s)),
```

where `s` maps to `ell=x1+2*x0+3*b` and `chi_L` is monic, squarefree, and of
degree 24.

## Exact primitive polynomial

Starting from the hash-pinned 24-by-24 multiplication matrix, Nemo forms the
Krylov matrix of the first coordinate vector over `K`, solves exactly for
the twenty-fifth vector, and verifies the relation before exporting the 25
rational-function coefficients.  Their maximum numerator and denominator
degrees in `t` are 68 and 48.  The result packet has SHA-256

```text
8867cfc4f2c4a5accd898382b687e5327f5f4c2cb793dfd34897137d3ffc5f7e.
```

The independent checker specializes every coefficient at the regular fiber
`t=2` and obtains exactly the degree-24 polynomial independently derived
from finite-field Krylov elimination.  The canonical generic coefficient
hash is

```text
9ff9aa0ee5a792f088b9a0b8120e87f8af02b2ce5802596e8b9101a1d38d0e40.
```

Since the primary calculation checks the rational-function Krylov identity,
this polynomial is `chi_L`, not merely a fitted specialization.

## Exact irreducible factorization

Nemo's exact factorization over `F_p(t)` returns five monic irreducible
factors, all with multiplicity one, in degrees

```text
4,4,4,8,4.
```

The factor packet has SHA-256

```text
00c4a7f0c90726b91b2310fa184d5eaf0ca3fab2b4d6a6ada1a4e1ae10f75cae.
```

An independent standard-library rational-function implementation reduces
every coefficient canonically and multiplies the five factors back to the
25 coefficients of `chi_L` exactly.  At `t=2` it additionally verifies that
all five specialized factors are squarefree and pairwise coprime.  The
primary factor algorithm supplies irreducibility over `K`; the independent
checker supplies product, degree, multiplicity, and separability audits.

The factors are pairwise coprime because they are distinct irreducibles
(also because `chi_L` is squarefree).  The Chinese remainder theorem now
gives `(KBRL-1)`.  Each quotient by an irreducible polynomial is a field, so
there are four degree-four residue fields and one degree-eight residue field.
Squarefreeness makes the total extension etale, hence gives 24 distinct
geometric points after algebraic closure.  QED.
