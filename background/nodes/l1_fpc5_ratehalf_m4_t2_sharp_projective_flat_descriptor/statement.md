# Sharp rate-half FPC5 projective-flat descriptor

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Fix one official rate-half sharp `M=4,t=2` source cell and one of its six
touched-petal pairs. Use the notation of
`l1_fpc5_ratehalf_m4_t2_codimtwo_guarded_slice`, and let `C` be the
`(k-1)`-point source core. Put

```text
N=|C|=k-1=5ell-5,       j=d=2ell-3.
```

Let `V_FW` be the guarded pair slice and let `V_F` be its locator image.
Then projection to `F` is a linear isomorphism and

```text
dim V_F=ell-1,       dim P(V_F)=r=ell-2.              (FD1)
```

If `V_F` has no degree-`j` member, the exact cell is empty. Otherwise the
monic chart

```text
A_F={F in V_F : coefficient of X^j is 1}              (FD2)
```

is an affine `r`-flat of codimension

```text
s_flat=j-r=ell-1                                      (FD3)
```

inside the affine space of all monic degree-`j` polynomials. Writing
`D_j(C)` for the monic degree-`j` squarefree polynomials split on `C`, every
exact contributor in this source/pair cell injects into

```text
A_F intersect D_j(C) = P(V_F) intersect D_j(C).       (FD4)
```

The equality identifies each projective point with its unique monic
representative. That representative determines a unique `W_F` through the
guarded projection isomorphism. The exact PMA locus is the subset satisfying

```text
gcd(F,W_F)=1,
(W_F-c_u F)(x)!=0 on every untouched petal point,
the fixed source-layout and touched-pair first-owner rules.              (FD5)
```

Thus the descriptor preserves contributor multiplicity and all remaining
guards rather than replacing the exact cell by an untyped locator count.

## Maximal common-GCD normalization

Let `G` be the monic gcd of a basis of `V_F`, and put `w=deg G`. If (FD4) is
nonempty, then `G` is squarefree and split on `C`. Division gives a linear
space

```text
V_F'=V_F/G,       dim V_F'=ell-1,       gcd(V_F')=1,                 (FD6)
```

and a bijection

```text
P(V_F) intersect D_j(C)
  <--> P(V_F') intersect D_(j-w)(C\Z(G)).              (FD7)
```

The projective dimension remains `ell-2`; the reduced monic flat has
codimension `ell-1-w`, and necessarily `w<=ell-1`. The exact guards (FD5)
remain filters attached to the reconstructed pair `(GF',W_GF')`.

## Consequence and limit

The sharp FPC5 endpoint is therefore an exact growing-dimensional instance
of the split-locator master-flatness problem: root domain `C`, locator degree
`2ell-3`, projective dimension `ell-2`, and affine codimension `ell-1`, with
explicit punctures after common-GCD division. The fixed-dimensional bound
does not pay it because `r` grows linearly with `ell`. This node supplies the
typed interface only; it proves no polynomial split-point bound and does not
declare the common-GCD branch tangent-paid.
