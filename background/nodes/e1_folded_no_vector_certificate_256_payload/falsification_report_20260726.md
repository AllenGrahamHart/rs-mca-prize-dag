# N'=256 bounded box-falsification report

## Contract

The campaign searched only for a falsifier: one explicit nonzero vector

```text
w in {-2,-1,0,1,2}^128,
sum_i w_i rho_256^i = 0 mod p.
```

A returned vector would be an exact counterexample. A miss cannot certify the
absence of vectors.

## Run

- Modal app: `ap-uImvgijoKNeruVABf32Cc9`
- image: `im-oBqJ2AAS3SnE49Cks3w8cc`
- seeds: `1729, 2718, 31415, 65537`
- worker cap: `8` CPUs, `16 GiB`, `240 s`
- observed worker times: `81.648107--125.331106 s`
- launcher SHA-256:
  `4d2e5f842b77dc604df58b8dad064fad6c23390aad90b8ed8b40d915f97cd326`
- checker SHA-256:
  `cd13813d859aefb1d332a50d68dcc5b6cc08c6480dc3c447c25ee85800c94070`
- result SHA-256:
  `3fcb4725226e996df9c274dd9e653e3a1354b6620c207e3c325289639f6cbcd2`

The launcher performed deterministic unimodular row mixing, LLL, bounded BKZ
at block sizes `28,36,42`, and exact signed sums of negacyclic shifts of the
eight shortest reduced rows. Multiplication by `rho_256` preserves the kernel
and acts by a negacyclic coordinate shift because `rho_256^128=-1`.

## Result

All four workers returned `NO_WITNESS_WITHIN_SEARCH_BUDGET`. The strongest
recorded frontiers were:

```text
minimum basis norm^2:             483
minimum basis infinity norm:        5
minimum signed-pair infinity norm:   5
```

The result checker and eight hostile mutations pass:

```text
E1_N256_BOX_CHECK_SELFTEST_PASS vector_mutations=4 campaign_mutations=4
E1_N256_BOX_CAMPAIGN_AUDIT status=INCOMPLETE workers=4 witnesses=0
```

## Ruling

`INCOMPLETE`. This is bounded resistance evidence only. It does not promote
the node, does not support the old zero-certificate claim, and is not a reason
to fund a larger BKZ run. The next useful work is analytic family-uniform E1
density control or a materially different exact box algorithm.
