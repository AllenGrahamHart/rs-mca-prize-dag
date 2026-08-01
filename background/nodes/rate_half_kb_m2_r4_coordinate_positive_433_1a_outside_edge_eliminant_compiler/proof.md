# Proof

The paired-product interface gives the product equation and squared Vieta
sum equation

```text
A_0(w)-pA_2(w)=0,
wB_1(w)^2-s^2A_2(w)^2=0.
```

Expansion gives `(KBPQE-2)--(KBPQE-3)`.

Assume `A!=0`.  Modulo `P`,

```text
w^2=(-Bw-C)/A,
w^3=((B^2-AC)w+BC)/A^2,
w^4=((-B^3+2ABC)w-B^2C+AC^2)/A^3.
```

Thus the pseudo-remainder of `A^3Q` is `R_1w+R_0`.  Taking its norm in the
quadratic algebra cut out by `P` gives
`A R_0^2-B R_0R_1+C R_1^2`.  The root formula for the resultant identifies
this norm with `A^3 Res(P,Q)`, proving `(KBPQE-4)`.

If `A=0,B!=0`, substitution of the unique root `-C/B` into `Q` and
multiplication by `B^4` gives `(KBPQE-5)`.  If `A=B=C=0`, then the product
polynomial vanishes identically.  Leading support at the five common labels
would make their products all equal to `p`.  But `b` and `-b` both occur,
and they are distinct because the field is odd and `b!=0`.  Hence
`A=B=0` forces `C!=0`, so no product root exists.

Every actual outside source label is a common root of `P,Q`, so it passes
the relevant scalar cut.  Eliminating one label forgets source-pair and
distinctness data, which are therefore retained as explicit guards and
nonclaims. QED.
