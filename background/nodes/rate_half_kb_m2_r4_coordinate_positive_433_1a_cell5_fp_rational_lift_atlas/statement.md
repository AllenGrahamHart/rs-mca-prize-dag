# KoalaBear positive 433-1a cell-5 deployed rational lift atlas

Let `X` be the fully guarded deployed-field common locus from the cell-5,
sign-row `(-1,-1)` calculation, and let `P(b,t)` be the reciprocal projection
polynomial of the preceding node.  The map

```text
X(F_p) -> {(b,t) in F_p^2 : P(b,t)=0}
```

is injective.

The reciprocal polynomial has degree exactly four in `b` on every guarded
deployed-field point.  Indeed its leading coefficient satisfies

```text
A0(t)=(t+1)C(t),
C(t)=t^3-33423359t^2-33423357t-1,                (KBL-0)
```

where `t=-1` is guarded and `C` has no root in `F_p` by the certificate
below.

More explicitly, the elimination basis contains one equation

```text
r(t^2+1)^2 + M_r(b,t)=0,                         (KBL-1)
```

and four equations `c L_j(b,t)+M_j(b,t)=0`, for `j=2,3,4,5`.  The exact
`L_j,M_j,M_r` are sealed in the result JSON.  The four leading coefficients
`L_j` have no simultaneous zero at a guarded `F_p` point of `P=0`.
Consequently `r` is recovered from `(KBL-1)` and at least one of the four
equations uniquely recovers `c`.

This is an `F_p`-point lift theorem, not a scheme-theoretic global chart.  It
does not assert that every `F_p` point of `P=0` lifts to `X`, classify a
signed family or colored edge, delete cell 5 or `433-1a -> O0b`, or prove a
Prize result.
