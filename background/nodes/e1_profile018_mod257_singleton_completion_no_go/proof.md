# Proof

The element `3 mod 257` has order 256 and

```text
-1=3^128 mod 257.
```

Hence the 256 values `epsilon*3^e` with `0<=e<128` and
`epsilon in {+1,-1}` are exactly the 256 nonzero powers of 3, with no
repetition. This proves the completion bijection.

For the printed support

```text
S={0,1,...,15,17,78},
```

direct modular summation gives

```text
sum_(e in S) 3^e=0 mod 257.                         (1)
```

The binary support polynomial has even weight, so it vanishes at one. Its
first Hasse derivative there is

```text
sum_(e in S) e
 =0+1+...+15+17+78
 =215
 =1 mod 2.                                          (2)
```

Thus its multiplicity is exactly one. For every odd unit `u mod 256`,
Galois conjugation sends exponents to `ue mod 256`; folding an exponent above
127 back by 128 only changes its sign because `g^128=-1`. It preserves 18
distinct oriented singleton terms and local multiplicity. Applying it to
`(1)` gives the transported polynomial a root at `3^(u^-1)`. These are all
primitive roots as `u` ranges over the odd units.

Finally, direct integral negacyclic autocorrelation of the printed polynomial
has energy 1478. The family therefore demonstrates only that the local and
mod-257 gates are nonselective. It makes no claim about the proved live
window `E=5,...,12`, exact norm `514p`, or row compatibility. QED.
