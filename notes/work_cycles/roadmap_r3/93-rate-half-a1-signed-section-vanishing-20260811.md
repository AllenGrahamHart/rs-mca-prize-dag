# Cycle 93: signed tangent packets have no section (2026-08-11)

## Cycle pins

```text
our start:       d9d075ec0
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Bounded vertical modification

The positive part `P_pos` of each signed normal form is a proper subdivisor
of the distinguished vertical fibre. Its degree is `r=3` in the first two
packets and `r=4` in the last. Its modification subspace is nilpotent and
has rank `r` in the negative pushforward block, giving

```text
pi_*O_C(P_pos)=O direct_sum O(1-d)^r direct_sum O(-d)^(e-1-r).
```

Thus `O_C(P_pos)` has only its canonical section. Since `R_0` is nonempty and
lies on other domain fibres, that section does not survive in
`O_C(P_pos-R_0)`. All three signed packets have `h^0=0`.

## Burn-down

```text
result:                  FIXED section counts in all 6 tangent packets
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The tangent degree-one branch is now a finite geometric dichotomy: three
effective canonical classes with one section and three signed classes with
none. Closure still needs an independent reason that neither section orbit
can occur for the Hankel/Forney curve.
