# Proof

Put `K=Q(zeta_256)` and `pi=1-zeta_256`. The four magnitude-one
coefficients are precisely the coefficients that survive modulo two. If
their exponents are `e_1,...,e_4`, the integral expansion at `zeta=1+pi`
gives

```text
mu=v_pi(alpha)=v_2(R)
  =ord_(X=1)(sum_(i=1)^4 X^(e_i) mod 2).             (1)
```

This is the same local argument as in the proved conductor-`256` cofactor
router: coefficients below the first odd Hasse derivative are even and have
`pi`-adic valuation at least `128`, while the first odd derivative has its
displayed valuation.

The square-mass bound and the official field floor give

```text
R<=20^64,
p>=B_P 2^128,
B_P=317494674775468773183020924238786383963,
m<=floor(20^64/(B_P 2^128))=1707433<2^21.            (2)
```

Hence `mu=v_2(m)<=20`.

Work modulo `(X+1)^32`. In characteristic two, `X^32=1` in this quotient.
After reducing the four exponents modulo `32` and cancelling equal residues
in pairs, the parity support has size zero, two, or four. Empty support has
order at least `32`, contradicting `(2)`. For a nonempty support `J`, Lucas'
criterion gives the exact Hasse test

```text
ord_(X=1)(sum_(r in J)X^r)
 =min{j: sum_(r in J) binom(r,j)=1 mod 2},
binom(r,j)=1 mod 2  iff  j & ~r = 0.                 (3)
```

The complete subset census in `{0,...,31}` gives

```text
|J|=2: {1,2,4,8,16},
|J|=4: {1,2,3,4,5,6,8,9,10,12,17,18,20,24}.         (4)
```

Intersecting `(4)` with `mu<=20` proves `(P44-1)`. Every retained value has
an explicit four-residue witness, so this is an exact local list rather than
only an upper envelope.

Local cyclotomic reciprocity gives

```text
R/2^mu=1 mod 256.
```

The row prime is `1 mod 256`; dividing `R=pm` by `2^mu` therefore proves
`(P44-2)`.

For an odd rational prime `q`, every prime above `q` in `K` has residue
degree `ord_256(q)`. Taking ideal norms proves `(P44-3)`. There are `6622`
integers satisfying `(2)`, `(P44-1)`, and `(P44-2)`. Factoring their odd
parts and applying `(P44-3)` leaves `1133`, with the stated valuation
distribution. Both committed verifiers replay this finite sieve by
independent Hasse implementations. The odd part one is always admissible,
so every pure power `2^mu` in `(P44-1)` survives.

Finally the preceding exact weighted payment allows at most

```text
floor(1971/256)=7
```

complete shift/sign orbits. Fourteen locally admissible pure branches, and
`1133` necessary-sieve cofactor values in total, show that the existing
local/ideal-family router cannot supply that cap without an additional
profile-specific exclusion. This last sentence is a method boundary; it
does not assert simultaneous realization of the branches. QED.
