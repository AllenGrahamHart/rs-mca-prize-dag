# KoalaBear positive 433-1a cell-5 generic signed-pair colored exclusion

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, guard-localized squared `DE+/DE-` pair plus the colored `BE`
  record
- **consumer:** `rate_half_band_closure`

Let `K=F_2130706433(t)`, let `P(b,t)` be the proved reciprocal projection
polynomial, and write the second equation of the proved rational lift atlas
as

```text
c L_2(b,t)+M_2(b,t)=0.
```

The hash-pinned exact function-field computation gives

```text
gcd(P,L_2)=1 in K[b].                              (KBGCE-0)
```

Thus `L_2` is a unit modulo `P`: chart 2 reconstructs `c` on the entire
generic common locus.  The other three rational charts are needed only at
special fibers of `t`.

Let

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
H(e)=Delta^2(N+D e^2)^2-e^2 q^2=0.              (KBGCE-1)
```

Let `C(e)` be the exact outside-edge resultant for the colored `BE` record,
with product `be` and squared sum `(b+e)^2`, restricted to the same residue
field.  Exact computation in `E_j[e]` gives

```text
gcd(H,C)=e^2-1   for j=1,2,3,5,
gcd(H,C)=1       for j=4.                        (KBGCE-2)
```

The target support contains six distinct antipodal pairs represented by
`1,b,c,d,e,f`, so `e^2-1` is a target-collision guard.  Every packet in this
sign row contains the `DE+`, `DE-`, and `BE` records.  Therefore no
admissible realization exists on the entire generic cell-5 sign row
`(-1,-1)`.

This theorem does not classify the finite exceptional `t` fibers, treat
another common sign row or matching cell, delete cell 5 or `433-1a -> O0b`,
close K3, a Prize row, or either Prize result.  No `DF+/DF-/CF` computation
is required for this sign row because its packets already contain the
excluded `DE+/DE-/BE` triple.

## Falsifier

An admissible generic cell-5 `(-1,-1)` packet, failure of `(KBGCE-0)`, a
residue factor on which the exact Bezout identity fails, a valid target
support with `e^2=1`, or a source-equation normalization not represented by
`(KBGCE-1)` or `C(e)`.
