# Cycle 247: M31 common-factor weighted-degree bound (2026-08-13)

The full interpolation gcd cannot consume almost all of the degree-`264`
weight budget.  If its weighted degree is `w`, division embeds the
at-least-`938`-dimensional kernel into weighted degree `264-w`.  The
adjacent exact monomial counts are

```text
M(46)=935 < 938 <= 990=M(47).
```

Therefore `w<=217` and `deg_(Y,Z)P<=43`.  Combining this with the
degree-one classification sharpens the higher-degree branch to

```text
2<=deg_(Y,Z)P<=43,
captured sections >=5083,
factor points >=126266,
inside exceptions <=3971.
```

This does not classify the possibly reducible higher-degree gcd or pay the
MCA projective-star branch.  It removes nine possible factor degrees and tightens the mass
available to the next classification theorem.

```text
start:                   89268cdf3
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ d339b8f0
result:                  NARROWED; weighted-degree bound PROVED
DAG delta:               +1 PROVED node, +4 edges, -1 mistyped evidence edge
critical status delta:   none; rate-half crossing remains TARGET
Mersenne residual:       130237<=e<=1044241
first-support residual:  MCA projective star or full-gcd degree 2..43
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       pay the star or classify degree-2..43 components
export target:           extend przchojecki/rs-mca PR #1165 after review
```
