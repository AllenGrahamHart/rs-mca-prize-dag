# Cycle 92: signed tangent packets have exact local forms (2026-08-11)

## Cycle pins

```text
our start:       b9c5d4ac3
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
open upstream:   39 PRs; #1160 is local near-rational support control
compute:         none
critical open:   28
```

## Exact signed packet ledger

Exact excess-degree and omission accounting closes every latent degree in
the three `I_0>0` packets. Their complete degree-two Picard classes are

```text
(1,1,1,4): A+2B-R_0,       deg A=deg B=1;
(2,0,1,5): A+2B-R_0,       deg A=deg B=1;
(2,0,2,6): 2B-R_0,         deg B=2.
```

The associated vertical and contact divisors are exact. Every ordinary
incidence has contact multiplicity one, and no rank-loss or contact degree
is left outside the bounded packet. The classes remain signed, so this is a
classification rather than an exclusion.

The proved leaf is
`rate_half_ca_hankel_a1_first_degree_core_one_signed_packet_local_normal_forms`.

## Burn-down

```text
result:                  CLASSIFIED all 6 tangent packets locally
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next seek a common obstruction to the three canonical effective classes and
the three exact signed classes, using the bounded Forney and adjugate tails.
