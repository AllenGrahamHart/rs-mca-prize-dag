# Budget-three antipodal reverse-residual stratification

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_antipodal_pencil_degree_floor`

Retain the centered antipodal quotient pencil over a field. Here `D` is monic
of degree four, `U` is monic, `V` is nonzero, and the four `c_i` are pairwise
distinct:

```text
G_i=U+c_iV,       deg U=r,       v=deg V<=r-1,
D product_i G_i=Y^d-1,           d=4r+4,
sum_i c_i=0.                                             (RRS1)
```

Assume the characteristic is zero or exceeds `d`. Let `e_j` be the elementary
symmetric functions of the four `c_i`, and define

```text
q=min{j in {2,3,4}:e_j!=0},       h=r-v.                 (RRS2)
```

The set in `(RRS2)` is nonempty. Put

```text
T(Y)=dD(Y)U(Y)-Y(D'(Y)U(Y)+4D(Y)U'(Y)).                 (RRS3)
```

Then `T` is nonzero and has the exact degree

```text
deg T=r+4-qh.                                            (RRS4)
```

In particular `qh<=r+4`, recovering the generic and intermediate degree
floors. More sharply, every distinct root of `U` that is repeated, lies in
`Z(D)`, or equals zero is a root of `T`. Hence

```text
#({alpha in Z(U):U'(alpha)=0 or D(alpha)=0 or alpha=0})
 <=r+4-qh.                                               (RRS5)
```

On the maximal official row `r=2^37-1`:

```text
e_2!=0, deg V=2^36-2
  ==> deg T=1 and the exceptional-root count is at most one;   (RRS6)

e_2=0, e_3!=0, deg V=(2^38-4)/3
  ==> deg T=2 and the exceptional-root count is at most two.   (RRS7)
```

Thus a solution on either lowest-degree boundary has a linear or quadratic
original-coordinate differential residual. This theorem does not exclude
solutions above those boundaries or prove the adjacent crossing.
