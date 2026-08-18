# Proof

## Minimal field

Choose a nonzero Plucker coordinate for each of the two Grassmannian points
`P,Q`, and a nonzero polynomial coefficient for `[g]`. Let `T_g` be the
tuple of all ratios to those chosen coordinates. Changing the chosen
coordinates changes generators but not the field they generate. Define

```text
K_g=B(T_g).
```

The tuple has coordinates in `F`, so `B<=K_g<=F`; it is visibly a field of
definition for `x_g`. Conversely, every field of definition contains all
projective coordinate ratios, hence contains `K_g`. Thus `K_g` is the
unique minimal field of definition.

Finite subfields of a degree-six extension correspond to divisors of six.
Consequently `[K_g:B]` lies in `{1,2,3,6}`, proving `(MF1)`. This is the
projective-ratio form of the minimal-field argument: it does not select the
degree-one branch.

## Heavy stratum

First-match ownership partitions the retained mass by used projective
factor, and hence by the four possible values of `[K_g:B]`. Integer
pigeonhole gives

```text
max_e M_e >= ceil(9965407986/4)=2491351997.
```

The chronology-safe cap for one fixed factor is `R_2=248644099`. Since

```text
10 R_2=2486440990<2491351997,
```

the selected field-degree stratum contains at least 11 distinct projective
factors. This proves `(MF2)` and `(MF3)`.

## Countermodel to automatic descent

Let `p>41`. The union of the proper subfields `F_(p^2)` and `F_(p^3)` in
`F_(p^6)` has fewer than `p^6` elements, so choose `alpha` outside it. Then
`alpha` has degree six over `B=F_p`; in particular `alpha^p!=alpha`.

Set `r=X^2+alpha X`, `P=<1,r>`, and `Q=<1,X^4>` over `F`. Both spaces
contain `1`, so they have no common zero. The four products

```text
1, r, X^4, rX^4
```

have distinct leading degrees `0,2,4,6`; they are independent and all have
degree below seven. Multiplication `P tensor Q` therefore has rank four.

Coefficient Frobenius `sigma` sends `r` to
`sigma(r)=X^2+alpha^p X`. If `sigma(r)` lay in `P`, degree
and constant-coefficient comparison would write it as `r+c`; the `X`
coefficient would force `alpha^p=alpha`, a contradiction. Thus `P` is not
Frobenius-stable and is not `B`-defined. The same argument proves that the
product four-space `V=<1,r,X^4,rX^4>` is not stable: an element of `V` with
degree at most two lies in `<1,r>`, so `sigma(r) in V` would give the same
contradiction.

Choose 41 distinct nonzero `t in B` and put `g_t=1+t r`. Equality of two
projective classes forces the projective scalar to be one by comparing
constant terms, and then forces the two values of `t` to agree. Hence these
are 41 distinct factors. Assign mass `R_2` to forty factors and

```text
9965407986-40 R_2=19644026
```

to the last. Every mass respects the fixed-factor cap, and every combined
datum `(P,Q,[g_t])` has minimal field `F` because it contains the
degree-six field of definition of `P`.

This packet satisfies the field-internal base-free `2 x 2` product and
factor-count arithmetic while failing base descent. Therefore descent is
not a consequence of those interfaces alone. Any valid degree-one theorem
must use additional MCA semantics. QED.
