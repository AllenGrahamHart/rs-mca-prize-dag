# L1 two-petal small-support anchor closure

- **status:** PROVED
- **role:** remove the two-petal bounded-small-support mixed branch
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Work in one maximal-sunflower chart with petal size `ell`, background size
`b<ell`, and generated field `q=poly(n)`. Let a non-planted listed word touch
exactly two petals. Write

```text
a = larger petal support size,
z = smaller petal support size,
r = background agreement count,
d = exact missed-core defect.
```

For every fixed integer `A>=1`, if `z<=A`, then

```text
d <= ell+A-1,
ell-r <= z,
ell-a <= z,
G_R=(ell-r)+(ell-a) <= 2A.                    (TS1)
```

Consequently the whole class is contained in the proved B11
background-petal anchor gate with

```text
E_d=A-1,       V_R=2A,
```

and is polynomially bounded at the L1 lower cutoff.

For the critical singleton case `z=1`, the identities sharpen to

```text
r=ell-1,       d=a in {ell-1,ell},       G_R<=2.       (TS2)
```

Thus no unpaid exact two-petal contributor can touch one petal in only one
point. Every surviving singleton-petal mixed contributor touches at least
three petals.

## Scope

The constant `A` is fixed independently of the row. This theorem does not
pay two-petal profiles whose smaller support grows, or any profile with three
or more touched petals, and it does not promote either target.
