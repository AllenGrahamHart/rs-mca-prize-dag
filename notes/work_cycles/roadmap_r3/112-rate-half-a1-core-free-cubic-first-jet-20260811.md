# Cycle 112: core-free cubic first-jet perfect pairing (2026-08-11)

## Cycle pins

```text
our start:       ccaa0b408
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
upstream PRs:    refreshed through #1160; no overlapping Hankel packet
compute:         none
critical open:   28
```

## Local jet gate

At a supported slope away from `E_w`, the regular determinant order equals
the rank loss `c`. Every positive Smith exponent is therefore one. If
`Q_gamma=Q_min R_gamma`, the derivative moment pairing

```text
(A,B) |-> dot Phi(Q_min^2AB)
```

has rank `c` and right radical exactly `span{R_gamma}`. At `c=1`,

```text
dot Phi(Q_min^2(X-r_gamma))=0,
dot Phi(Q_min^2)!=0.
```

This applies at every supported slope in the three `w=0` packets. The
`w=1` packet has at most the one slope cut out by `E_1` as an exception.

## Burn-down

```text
result:                  EXPOSED perfect first-jet apolar pairing
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next insert the heavy-row cube/contact identities and the endpoint source
moments into this pairing. That is the first route here capable of producing
a field-valued contradiction rather than another support-degree count.
