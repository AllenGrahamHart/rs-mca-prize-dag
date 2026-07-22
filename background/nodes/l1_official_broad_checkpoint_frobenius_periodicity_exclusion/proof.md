# Proof - L1 official broad-checkpoint Frobenius periodicity exclusion

For `1<=a<p`, equality of the power sums gives

```text
0=sum_(x in X)x^a-sum_(y in Y)y^a=gamma^a A(zeta^a).
```

At `a=0`, the same equality follows from `|X|=|Y|=p`. Hence `A` vanishes on
the initial interval in `(BFP2)`.

Every coefficient of `A` belongs to `F_p`. Therefore

```text
A(zeta^(ap^r))=A(zeta^a)^(p^r)=0,
```

which proves vanishing on `S_(n,p)`. The TSV and verifier enumerate each
orbit for exactly `ord_n(p)` steps and prove the seven rows and all printed
closure data exhaustively.

Fix one row and its printed `g`. Fourier inversion is valid because `p` does
not divide the dyadic integer `n`. Since every possibly nonzero frequency is
`k=gq`,

```text
a_(i+n/g)
 =n^(-1) sum_(g|k) A(zeta^k) zeta^(-k(i+n/g))
 =a_i.
```

Thus the coefficient word is constant on the orbits of translation by
`n/g`, each of which has exactly `g` elements. Coefficients are in
`{0,+1,-1}` and the positive and negative supports have size `p`. The table
has even `g` on every row, while `p` is odd. This contradiction proves
`(BFP3)`.

The first-checkpoint split-pencil reduction says every minimum-width pair is
exactly such an equal-moment pair, so the exclusion is valid at every depth.
Filtering the exact checkpoint atlas leaves precisely the nine rows in
`(BFP4)`.
