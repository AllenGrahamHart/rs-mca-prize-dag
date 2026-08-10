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

## Scope

This is an injection, not a converse: an arbitrary word in the shortened
list need not satisfy the FPC5 cofactor or exactness guards. No polynomial
list-size bound at `(SH5)` is asserted. Asymptotically the agreement
fraction is `3/5`, below the ordinary Johnson agreement `sqrt(2/5)`, so the
standard Johnson theorem does not close this route.
