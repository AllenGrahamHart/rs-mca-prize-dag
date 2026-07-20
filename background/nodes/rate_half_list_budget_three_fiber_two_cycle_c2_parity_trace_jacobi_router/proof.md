# Proof

Common subgroup scaling sends one antipodal denominator pair to `{1,-1}`;
the other becomes `{r,-r}`. Reversing the denominator polynomial gives
`(C2P1)`. Since every denominator root lies in `mu_N` and is a base-field
square, `tau=r^2` lies in `mu_(N/2)=mu_(8M)` and has the required square
lifts. The parity-reduction dependency, at the doubled parameter
`N=16M`, is exactly `(C2P2)`. The pure value `tau=-1` makes `Omega` a scaled
fourth-root quartet and is removed by the pure-exclusion dependency.

For any unordered pair `{A,B}` the mismatch trace is

```text
z_(A,B)=(A+B)^2/(AB).                                 (1)
```

The pairs `{1,-1}` and `{r,-r}` give zero. The pairs with equal signs give
`2+r+r^(-1)`, and those with opposite signs give `2-r-r^(-1)`. This proves
`(C2P4)` and the multiplicities.

The mismatch trace-resolvent theorem says that a selected pair has the
required completion-root PGL coupling exactly when `K` vanishes at its trace.
At zero,

```text
K(0)=-12^3 J^2,
```

so the zero-trace class passes exactly when `J=0`. The two cross classes give
the product in `(C2P5)`. Replacing `r` by `-r` exchanges its factors, while
inversion fixes `chi`; their product is even in `chi`. Equation `(C2P6)` then
shows that it belongs to the base polynomial ring in the normalized parity
parameter. This proves the exact coupling router.

It remains to identify the torsion prefilter. Since `r` is a base-field
square, choose `q` with `q^2=r`; then `q^4=tau`. The standard parity
Gegenbauer transformation gives the primary equation in the variable

```text
x=(q^2+q^(-2))/2=(r+r^(-1))/2.
```

The even Jacobi transformation sends it to `mathcalJ(w)=0`, with
`w=2x^2-1=(tau+tau^(-1))/2`. The order of `q` gives one of the two exact
Chebyshev factors in `(C2P7)`. These are precisely the denominator-only
primary/torsion factors used in the matched trace-Jacobi norm transfer; its
derivation precedes every source-specific constant equation. Therefore every
survivor satisfies `(C2P8)` and its characteristic divides the same
`R_-,R_+` pair.

The additional parity-secondary, c=2 coupling, canonical, and reconstruction
conditions can only remove roots of this shared primary/torsion gcd. Hence a
no-divisor result for both norms excludes this chamber, while a divisor is
only a candidate requiring the stated replay. QED.
