# Cycle 244: M31 interpolation common-factor router (2026-08-13)

At the first residual support `e=130237`, every selected affine explanation
line gives a distinct pair `(a,b) in RS_6^2` agreeing with the received pair
on at least 807 inside coordinates.  The capped charge after 2,704 removed
lines is only 132,203, so an unsafe family still forces line 2,705.

Let `I_264` be the weight-`(1,5,5)` interpolation kernel through all 130,237
inside received points.  Exact monomial counting gives

```text
dim I_264 >= 131175-130237 = 938.
```

Every selected pair is a common `F(X)`-rational zero of this kernel: after
substitution, a kernel polynomial has degree at most 264 but at least 807
roots.  If the kernel has no positive-`(Y,Z)`-degree common factor, two
generic members are coprime of `(Y,Z)`-degree at most 52.  Affine Bezout then
permits at most `52^2=2704` common pairs, contradicting line 2,705.

The generic branch is therefore paid.  The exact first-support residual is a
common interpolation factor over the algebraic closure of `F(X)`.  Calling
that factor a split pencil would require a further classification theorem;
the next route action is to bound its degree, classify its low-degree ruled
components, or show that the remaining component families have insufficient
line/core mass.

```text
start:                   ed1ec5b68
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 7934f552
result:                  NARROWED; coprime interpolation branch PROVED safe
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130237<=e<=1044241
first-support residual:  positive-YZ-degree common interpolation factor
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       classify and charge the common interpolation factor
export target:           extend przchojecki/rs-mca PR #1165 after review
```
