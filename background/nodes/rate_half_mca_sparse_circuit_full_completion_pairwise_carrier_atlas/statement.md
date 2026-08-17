# Full-completion pairwise carrier atlas

- **status:** PROVED
- **correction dimension:** `10`
- **supports:** `2,3,4,5`

Let `M_c>0` be exact support-`c` completion maxima and let `B_c` be
attaining carriers, so `|B_c|=M_c+c-1`.  The support-two carrier `B_2` is
the full ground-set parallel class at a projective point `P`, of size
`b_2=M_2+1`.

For each `c in {3,4,5}`, exactly one of the following conservative routes
applies to the position of `P` relative to an attaining deletion span.

```text
T_c: (u,g)=(b_2+|B_c|,10-c),
A_c: (u,g)=(b_2+|B_c|-1,11-c),
F_c: B_2 subset B_c and M_c>=M_2+1.                 (CA1)
```

Here `(u,g)` means that a fixed `g`-dimensional correction subspace
vanishes on a fixed `u`-point set.  The `A_c` route also conservatively
covers proper-subspan positions with no shared anchor.

Assume `F_3` and `F_d` for one `d in {4,5}`.  Put

```text
r_3=M_3-M_2+1,
r_d=M_d-M_2+d-2,
t=|(B_3\B_2) intersect (B_d\B_2)|.
```

Then

```text
0<=t<=min(r_3,M_d-M_2),                              (CA2)
u=b_2+r_3+r_d-t,
g=10-d if t=0, and g=11-d if t>0.                   (CA3)
```

The Cartesian product of the support-four and support-five alternatives is
exhaustive.  Each listed fixed union may be charged simultaneously with all
other inherited caps.

## Falsifier

An attaining carrier position outside `(CA1)`; a full-completion carrier
with fewer than `d-2` points outside `B_3`; an overlap beyond `(CA2)`; or a
fixed-union dimension smaller than `(CA3)`.
