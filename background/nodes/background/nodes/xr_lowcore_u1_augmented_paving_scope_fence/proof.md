# Proof

The rank-five extension-list reduction gives, after deleting loops and
scaling coordinates,

```text
W subset F[X]_{<=4},       dim W=4,
```

with no common root on the evaluation domain.  Fix a four-set `T` in that
domain and let `L_T` be its monic locator.  The space

```text
W_T=span{1,X,X^2,L_T}
```

has dimension four and has no common evaluation root because it contains
`1`.  On `T`, however, `L_T` vanishes and the other three generators have
rank three by Vandermonde independence.  Hence `rank(W_T|T)=3`.

This example is compatible with the original RS kernel slice.  In the
`u=1`, rank-four normalization the persistent-root locator has degree
`g=k-5`.  Multiplication by it sends every member of `W_T` to degree at most
`k-1`, producing a four-dimensional RS subcode with exactly the required
normalized form.  The printed all-pair weighted-RS theorem instead takes a
`GRS_4` kernel, equivalently four independent rows on every four-set.  The
extension-list reduction therefore does not establish that theorem's kernel
hypothesis on the generic branch.

For the arithmetic fence, suppose additionally that the normalized kernel is
MDS and grant every other hypothesis needed for the strongest deep-hole
specialization.  The theorem has kernel dimension `kappa=4`.  If the chart
has length `N` and every retained word has at least `m` agreements, its
support weight is at most `t=N-m`.  At maximal direction distance
`d=N-kappa`, the local charge is

```text
Lambda_d(t)=C(N-t,kappa+1)=C(m,5).
```

The ambient numerator is at most `C(N,5)`.  The three `u=1,v=0` RowC charts
have `(N,m)=(773,10),(901,10),(965,8)`, giving the three displayed integer
ceilings.  Each is above `B=8*1024^3`.

Finally, on the closest row the local charge is `252`.  Since `beta_5(A)` is
an integer,

```text
floor(beta_5(A)/252) <= B
```

holds exactly when `beta_5(A)<=252(B+1)-1`.  Subtracting this threshold from
`C(773,5)=2,270,319,562,049` gives `105,656,044,614`, whose ratio to the
ambient numerator is `4.6537961606...%`.  This proves `(AP1)` and `(AP2)` and
the stated nonpromotion.
