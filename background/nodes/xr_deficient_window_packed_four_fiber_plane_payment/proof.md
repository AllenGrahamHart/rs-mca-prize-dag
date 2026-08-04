# Proof

The two-block kernel-slack router gives exactly two disjoint selected blocks,
each of size `r=2ell+1`, and

```text
4ell+2=2r<=e<=2r+sigma=4ell+2+sigma.
```

This is `(P4F2)`.

In an exact profile `(ell,ell,1)`, a part of size `ell` fills its complete
`phi` fiber because every fiber has size at most `ell`. The two disjoint
blocks therefore use four distinct complete fibers of size `ell`. There
cannot be a fifth such fiber contained in `D`, since the official
`ell>sigma+2` gives

```text
5ell>4ell+2+sigma>=e.
```

Thus the four full fibers are fixed by `D` and `phi`, independently of the
target. Their complement in `D` is a fixed tail of size `t=e-4ell`. Each
block uses one tail point, and block disjointness makes the two points
distinct.

An individual selected block chooses two of the four full fibers and one tail
point. Hence there are

```text
binom(4,2)t=6t                                         (1)
```

possible block geometries.

Fix one block geometry and one affine plane. Choose one point from each of its
two full fibers and its tail point. Their three `phi` values are pairwise
distinct. The proved common-ray eliminant with plane dimension `m=2` shows
that a fixed such triple lies in one selected block for at most three target
parameters. Every target contributes its two selected blocks, so double
counting block occurrences gives

```text
2|Tau_pack intersect plane|<=3(6t),
```

which is `(P4F3)`.

Let the affine hull have dimension `s`. The generalized-weight core
incidence supplies every target with at least

```text
B_(s-2)=product_(j=3)^s(w+j)/(s-2)!
```

independent `(s-2)`-subsets of core-agreement hyperplanes. Each cuts the hull
to an affine plane. There are at most `binom(N,s-2)` possible core subsets,
and `(P4F3)` bounds the owner count of each resulting plane. Double counting
proves `(P4F4)`.

For the official arithmetic, cancel `(s-2)!` and compare

```text
9t (N)_(s-2) / product_(j=3)^s(w+j)                  (2)
```

with

```text
floor((17n^2-25(n-e))/25).                           (3)
```

The exact values for every permitted tail are replayed by `verify.py`; all
lie below `(3)` and give the table in the statement. QED.
