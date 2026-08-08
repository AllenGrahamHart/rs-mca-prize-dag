# KoalaBear aligned-negative literal-assignment coverage

- **status:** PROVED
- **scope:** all twelve literal internal source-star assignments in the
  aligned negative `c2(1,1,2)` source-line branch
- **dependencies:** negative reconstruction factor gate and q-slice
  resultant gate
- **consumer:** source-line literal-assignment coverage

Keep the literal frame

```text
J_0={2,1/2,b,1/b},       q(T)=(T-c)(T-d).          (KBNL-1)
```

The eight fixed-moving assignments `F00,...,F07` and four moving-moving
assignments `M00,...,M03` are reconstructed directly. No endpoint
normalization or matching-centralizer covariance is used.

For each assignment the five linear reconstruction equations are covered by
two exact `4 x 4` minor charts. On `c+d != 0`, omit the first internal target
row. On `c+d=0`, omit the middle target row; its determinant contains
`cd+1=1-c^2`, which is nonzero on the named open. Every other determinant
factor is an inherited collision, internal-incidence, or negative-chart
unit.

On either chart the remaining consistency numerator has exactly five
irreducible factors. The factors shared with the selected determinant are
units. What remains is one component for each fixed-moving assignment and
two components for each moving-moving assignment, exactly matching the
literal versions of the normalized `B/C` survivor census.

For each survivor component reconstruct `U` and put `G=U^2-WV^2`. After
dividing the two forced `(W-w)^2` factors, make the q-slice quartic monic and
subtract

```text
((W-1/c)(W-1/d))^2.
```

If `m_j` is the coefficient of `W^j` in the mismatch, exact reduction on
every literal survivor component gives

```text
m_0=(cd-1)(cd+1)/(c^2 d^2).                       (KBNL-2)
```

Since `cd!=1`, passage forces `cd=-1`. On the generic chart every component
also gives

```text
m_1-m_3=4(c^2-1)/c,                               (KBNL-3)
```

which is nonzero on the named open. On the `c+d=0` chart, `cd=-1` already
implies `c^2=1`, again forbidden. Thus no aligned-negative literal
assignment passes the necessary q-slice identity.

The certificate covers `12 x 2=24` assignment/chart cells and 32 survivor
component checks. It does not classify any near-negative cell.

## Falsifier

A compatible literal assignment absent from the census, a selected minor
with an unlocalized determinant factor, a missed consistency component, or
failure of `(KBNL-2)` or `(KBNL-3)` on a survivor component.
