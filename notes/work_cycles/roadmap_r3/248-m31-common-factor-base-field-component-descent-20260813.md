# Cycle 248: M31 common-factor base-field component descent (2026-08-13)

The higher-degree full gcd is now reduced from arbitrary geometric
components to components defined over the deployed base field.  On the
Mersenne row,

```text
F=F_((2^31-1)^4),       char(F)=2147483647>43.
```

A non-`F(X)` geometric component of degree `delta` has a distinct
conjugate.  Every `F(X)`-rational selected pair on it lies in the
intersection, so Bezout permits at most `delta^2` pairs.  Across all
non-base-field components the loss is at most `d^2`.  Therefore

```text
base-field component pairs
 >= 7583-(52-d)^2-d^2
 >= 5079                  for 2<=d<=43.
```

At least one base-field absolutely irreducible component carries `132`
pairs.  The union of all such components carries at least `126263`
received inside points and has at most `3974` exceptions.

This is a normalization theorem, not a component classification.  The
remaining branch may still be reducible and may mix several base-field
components.

```text
start:                   01a72118f
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ cf2b7fd8
result:                  NARROWED; base-field descent PROVED
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; rate-half crossing remains TARGET
Mersenne residual:       130237<=e<=1044241
first-support residual:  MCA star or F(X)-components of total degree 2..43
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       classify the base-field components and their arms
export target:           extend przchojecki/rs-mca PR #1165 after review
```
