# Sharp rate-half FPC5 fixed-agreement shortening

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Fix one official sharp rate-half `M=4,t=2` source and one touched pair. Let
`S_0` be the union of the entire background and the two touched petals. Then

```text
|S_0|=(ell-3)+2ell=3ell-3.                            (SH1)
```

Let `Q_0` be the unique polynomial of degree below `|S_0|` interpolating the
received word on `S_0`, and let `L_(S_0)` be its locator. Every exact
contributor codeword `P`, of degree below `k=5ell-4`, has a unique form

```text
P=Q_0+L_(S_0)T,       deg T<2ell-1.                   (SH2)
```

On the disjoint core `C`, define the received word

```text
v(x)=(U(x)-Q_0(x))/L_(S_0)(x).                        (SH3)
```

The contributor map `P -> T` is injective into the Reed-Solomon list

```text
RS[K,C,2ell-1] around v
at agreement 3ell-2 and radius 2ell-3,                (SH4)
```

because its exact core defect has size `2ell-3` inside
`|C|=5ell-5`. In finite parameter form,

```text
N=5ell-5,       K_0=2ell-1,       A=3ell-2,
E=N-A=2ell-3=floor(2(N-K_0)/3).                       (SH5)
```

All primitive, cofactor, untouched-petal, and first-owner conditions remain
filters on this list. Thus any uniform list-size theorem for these
source-core evaluation sets at `(SH5)` immediately pays the sharp FPC5
cell, while a large sharp cell produces an equally large witness list for
this shortened RS instance.

## Balanced determinant specialization

The shortened exact shell lies in the scope of
`l1_balanced_pencil_anchor_determinant_atlas` with

```text
n'=5ell-5,       k'=2ell-1,       m'=3ell-2,
w=m'-k'=ell-1,
omega=n'-m'=2ell-3,
s=n'-2m'+k'=ell-2.                                   (SH6)
```

Fix one exact contributor as anchor, with defect locator `F_0`. For another
exact contributor put

```text
D=gcd(F_0,F),       deg D=ell-3-j,       0<=j<=ell-3. (SH7)
```

The atlas gives an injective determinant coordinate of degree at most
`ell-3`, recovers `D` by one gcd, and pays every fixed owner `D` by

```text
|C_D| <= min {
  floor( binom(3ell-2,j+1) / binom(ell+j,j+1) ),
  max_(1<=r<=j+1)
    floor( binom(3ell-2,r) / (ell+j-r+1) )
}.                                                    (SH8)
```

In particular, the maximal common-error stratum `j=0` has

```text
|C_D|<=floor((3ell-2)/ell)=2.                         (SH9)
```

This pays coefficient multiplicity and every fixed common-error owner. It
does not bound how many different divisors `D|F_0` occur; summing all such
owners can still be exponential. The remaining sharp obstruction is
therefore an aggregate gcd-owner coalescence for the marked cofactor family,
not an unresolved fixed-pencil count.

## Scope

This is an injection, not a converse: an arbitrary word in the shortened
list need not satisfy the FPC5 cofactor or exactness guards. No polynomial
list-size bound at `(SH5)` is asserted. Asymptotically the agreement
fraction is `3/5`, below the ordinary Johnson agreement `sqrt(2/5)`, so the
standard Johnson theorem does not close this route. The determinant
specialization proves only the fixed-owner bounds `(SH8)--(SH9)`; it does
not license a union bound over the divisors of `F_0`.
