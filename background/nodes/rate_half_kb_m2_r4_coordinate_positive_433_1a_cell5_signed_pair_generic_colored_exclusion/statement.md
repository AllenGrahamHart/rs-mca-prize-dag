# KoalaBear positive 433-1a cell-5 generic signed-pair colored exclusion

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, chart 2, guard-localized squared `DE+/DE-` pair plus the
  colored `BE` record
- **consumer:** `rate_half_band_closure`

Let `K=F_2130706433(t)` and let

```text
A_g ~= product_(j=1)^5 E_j,       E_j=K[s]/(phi_j),
(deg phi_1,...,deg phi_5)=(4,4,4,8,4)
```

be the proved primitive residue decomposition of the squared signed-pair
algebra.  In one residue field write `x=x0`,

```text
D=D(x),   N=N(x),   q^2=x beta^2(x-1)^2,
Delta=t^2(t^2-1).
```

Any `DE+` lift with target representative `e` satisfies

```text
P(e)=Delta^2(N+D e^2)^2-e^2 q^2=0.              (KBGCE-1)
```

Let `C(e)` be the exact outside-edge resultant for the colored `BE` record,
with product `be` and squared sum `(b+e)^2`, restricted to the same residue
field.  Exact computation in `E_j[e]` gives

```text
gcd(P,C)=e^2-1   for j=1,2,3,5,
gcd(P,C)=1       for j=4.                        (KBGCE-2)
```

The target support contains six distinct antipodal pairs represented by
`1,b,c,d,e,f`, so `e^2-1` is a target-collision guard.  Therefore no
admissible generic chart-2 `DE+/DE-/BE` realization exists on any of the
five signed-pair residue components.

This theorem does not cover rational `c` charts 3--5, classify exceptional
`t` fibers, prove the `DF+/DF-/CF` analogue, treat another common sign row
or matching cell, delete cell 5 or `433-1a -> O0b`, close K3, a Prize row,
or either Prize result.

## Falsifier

An admissible generic chart-2 `DE+/DE-/BE` packet, a residue factor on which
the exact Bezout identity fails, a valid target support with `e^2=1`, or a
source-equation normalization not represented by `(KBGCE-1)` or `C(e)`.
