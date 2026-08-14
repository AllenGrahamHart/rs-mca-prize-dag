# Proof

Let `Z_lo` be the selected post-near records with `theta<=387`. The seed
compiler proves

```text
|Z_lo| >= 190604046733790                              (1)
```

and bounds their distinct minimizing pair types by

```text
|P| <= Q_10(387)=869784434119.                         (2)
```

Consequently one pair `p_0=(a_0,b_0)` owns at least

```text
ceil(190604046733790/869784434119)=220                 (3)
```

distinct actual slopes. Fix eighteen of them.

## Fit the core basis into the other fourteen slots

Let `P_2` be the pair types owning at least two records and

```text
J_2=intersection_(p in P_2) H_p,
H_(a,b)={x:r_0(x)=a(x), r_1(x)=b(x)}.
```

The large-shared-core payment gives

```text
|J_2|<=K-4923.                                        (4)
```

Anchor the component-span construction at the dense pair `p_0`. It chooses
further pair types `p_1,...,p_t`, where `t<=10`, such that

```text
intersection_(i=0)^t H_(p_i)=J_2.                    (5)
```

In fact `t>=1`. If `t=0`, all heavy pair components equal those of `p_0`,
so there is only one heavy pair. Singleton pair types contribute at most
`Q_10(387)` records and the fixed pair contributes at most
`n-m+1=981105`, contradicting (1).

Choose one owned record from every `p_i`, `1<=i<=t`, and choose a second
record from

```text
q=min(t,14-t)
```

of these pairs. Together with the eighteen `p_0` records this uses
`18+t+q<=32` slots. Pad with arbitrary distinct records from `Z_lo` if
needed. The number of basis pairs represented only once is

```text
t-q<=6.                                               (6)
```

For a twice-represented fixed pair, disjointness of its two exception sets
puts the intersection of its selected supports inside `H_p`. For a
singly represented pair, its selected support differs from `H_p` on at
most `387` points. Equations (4)--(6) therefore give, for the complete
selected support intersection `C`,

```text
C subset J_2 union (at most six exception sets),
|C| <= (K-4923)+6*387 = K-2601.                       (7)
```

## An off-line record exists

For a pair `p=(a,b)`, every owned explanation is

```text
h_gamma=a+gamma*b.
```

Take any `p_i!=p_0`. If two distinct records owned by `p_i` both lay on
the parameterized line of `p_0`, then

```text
a_i+gamma_j b_i=a_0+gamma_j b_0,     j=1,2.
```

Subtracting the two identities gives `b_i=b_0`, and then `a_i=a_0`, a
contradiction. Hence every distinct heavy pair has an owned record outside
the `p_0` line. Choose the record from `p_1` to have this property.

## Eighteen roots pin the residual slope degree

Cancel `C` using the proved adapter. Let `L_C` be its locator and let `A,B`
be the degree-below-`K` interpolants of the received columns on `C`. On `C`,
the eighteen `p_0` explanations satisfy

```text
a_0+gamma b_0=A+gamma B.
```

Two distinct dense-pair slopes imply separately that `L_C` divides
`a_0-A` and `b_0-B`. Put

```text
a_0'=(a_0-A)/L_C,       b_0'=(b_0-B)/L_C.
```

The eighteen shortened explanations are exactly

```text
h_gamma'=a_0'+gamma*b_0'.                            (8)
```

The selected off-line explanation remains off this line: equality after
division would multiply back to the excluded original polynomial identity.

Let `H'(X,Z)` be the unique coefficientwise interpolation of the `32`
shortened explanations, with `deg_Z H'<=31`. If `deg_Z H'<=17`, then

```text
H'(X,Z)-a_0'(X)-Z b_0'(X)
```

has degree at most `17` in `Z` and vanishes at the eighteen distinct slopes
in (8). It is therefore identically zero, contradicting the selected
off-line record. Thus

```text
18<=deg_Z H'<=31.                                    (9)
```

Subtracting the residual received line, which is affine in `Z`, does not
change a degree at least two. Hence the residual slope-error polynomial has
the same degree. The cancellation adapter preserves support-wise MCA
badness, slopes, and chronology. This proves the compiler.
