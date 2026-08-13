# Proof

## Triple-overlap forces one line

Fix `0<=r<=s`, and consider the explanations assigned to selected slopes
in the exact deficit layer `h=e-r`.  Such an explanation has exactly
`m-e+r` outside agreements.  Ownership requires at least `e-r` agreements
inside `E`; write `S_i` for those inside agreement coordinates.  Thus

```text
|E \ S_i|<=r.                                         (1)
```

The owner bound gives `floor(e/(e-r))=1` because `r<=s<e/2`.  Hence
different selected slopes in this layer have different assigned
explanations.

For explanations `a_i,a_j` assigned to distinct slopes
`gamma_i,gamma_j`, put

```text
p_ij=(a_i-a_j)/(gamma_i-gamma_j).
```

This is a degree-`<K` codeword and `p_ij=q` on `S_i intersect S_j`.
For any three indices,

```text
|S_i intersect S_j intersect S_k|>=e-3r>=K.           (2)
```

Both `p_ij` and `p_ik` equal `q` on this triple intersection.  Evaluation
on `K` distinct coordinates is injective for degree-`<K` polynomials, so
`p_ij=p_ik`.  Fixing two anchors shows that every explanation in the exact
layer lies on one affine codeword line.  Families of size at most two lie
on such a line directly.

## Outside packing

Every member of the line has exactly `A_r=m-e+r` outside agreements.  The
common agreement core on zeros of the nonzero line direction has size
`g<=K-1=c`.  Away from that core, each outside coordinate agrees for at
most one line parameter.  Therefore

```text
L_r(A_r-g)<=n-g.
```

The hypothesis `N-m>s` gives `n-A_r=N-m-r>0`.  Thus the ratio
`(n-g)/(A_r-g)` increases with `g`.  Substituting `g<=c` proves `(TT1)`.

## Profile

The cumulative prefix argument gives `N_h<=B_h` for `h<=H`.  Sum the
nonincreasing owner weights by parts on those layers.  The remaining layers
are exactly `h=e-r` for `0<=r<=s`; apply `(TT1)` and the unit owner weight
to each.  This proves `(TT2)`.

When positive Johnson caps are available through `H`, put
`u=floor(e/2)`.  Prefix layers through `u` have owner weight at most `e`,
while every layer from `u+1` through `H` has weight one.  Hence

```text
prefix <= e*N_u+(N_H-N_u)
       <= (e-1)J_u+J_H,
```

which proves `(TT3)`.

## Uniform official arithmetic

For the positive-Johnson rational cap

```text
F(n,A)=n(A-c)/(A^2-nc),
```

cross multiplication shows that `F` increases with `n` and decreases with
`A`.  Over `K<=e<d` one has `n<=N`.  The minimum agreements at
`u=floor(e/2)` and `H` occur at `e=d-1`.  Substitution with the conservative
upper length `N` gives

```text
floor(F(N,A_u))<=31,       floor(F(N,A_H))<=47
```

for both official rows.  These denominators are positive.

For a fixed `r`, the ratio

```text
(N-e-c)/(m-e+r-c)
```

is nondecreasing in `e`: decrementing numerator and denominator by one
increases the ratio because their difference is `N-m-r>0`.  Also
`floor((e-K)/3)` is nondecreasing.  Thus the line sum is maximized at
`e=d-1`.

At that endpoint the line sums are `9405342` and `9405365`.  Since
`e-1<=d-2`, `(TT3)` is at most

```text
KoalaBear:   (67472-2)*31+47+9405342=11496959;
Mersenne-31: (67448-2)*31+47+9405365=11496238.
```

Both are strictly below their printed budgets.  The primary verifier checks
all endpoint inputs with exact integers.  The independent audit recomputes
the floor sums by quotient grouping and checks a sharp finite
triple-overlap model.
