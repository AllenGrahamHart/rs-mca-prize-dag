# Proof

## Characteristic-zero full-fiber classification

Let `P,Q` be disjoint `h`-subsets of `mu_n(C)` with equal first `h-1`
elementary symmetric functions. Newton identities give equality of their
first `h-1` power sums. Choose a primitive `n`th root `zeta` and encode the
first-moment difference by

```text
R(Z)=sum_(zeta^e in P)Z^e-sum_(zeta^e in Q)Z^e,
deg R<n.                                             (1)
```

Since `R(zeta)=0` and `n` is a power of two, the cyclotomic polynomial
`Phi_n(Z)=Z^(n/2)+1` divides `R`. Thus the coefficients of `R` at `e` and
`e+n/2` are equal. Disjointness then says that `P` and `Q` are each unions of
antipodal pairs. In particular `h` is even.

Squaring each antipodal pair gives disjoint `(h/2)`-subsets `P',Q'` of
`mu_(n/2)`. For `1<=r<=h/2-1`, the original equality at power `2r` gives

```text
2 sum_(y in P')y^r=2 sum_(y in Q')y^r.              (2)
```

Newton identities recover equality of the first `h/2-1` elementary
symmetric functions. The same argument therefore repeats.

Write `h=2^v u` with `u` odd. After `v` descents, an odd-width trade remains
unless `u=1`; but its first moment would again force antipodal pairing, a
contradiction. Hence `h=2^v`. At the final level both sides are singletons,
so the original supports are their full inverse images under `x -> x^h`.
They are full `mu_h` fibers. Conversely two disjoint full fibers have
locators `X^h-alpha` and `X^h-beta` and agree in every nonconstant
coefficient.

For a near-square pair the two locators are `S-a` and `S+a`. They are full
fibers exactly when `S=X^h+s_0`, proving `(NFS3)` and reproducing the content
of the proved `x24_char0_dyadic_descent` theorem at this interface.

## Selector and repeated-squaring schemes

Over a field, `(NFS4)` has a solution in the `z_j` exactly when at least one
intermediate coefficient `s_j` is nonzero. Thus its projection is precisely
the complement of `(NFS3)`. The individual equations `u_js_j=1` give the
stated `h-1`-chart cover.

The polynomial `D=S^2-a^2` is monic of degree `2h`. Monic Euclidean division
uniquely determines

```text
V_t^2=DQ_t+V_(t+1),
deg Q_t<=2h-2,       deg V_(t+1)<2h.                 (3)
```

On an official row, `X^n-1` is squarefree. Thus `(NFS2)` forces `a!=0`:
otherwise the positive-degree square `S^2` would divide a squarefree
polynomial. The factors `S-a,S+a` are therefore coprime and split over the
domain, so the divisor solutions are exactly the near-square support pairs.

This determination is triangular and survives arbitrary base change.
Starting with `V_0=X` gives `V_t=X^(2^t) mod D`; because `n=2^s`, the terminal
condition `V_s=1` is equivalent to `(NFS2)`. Hence the recurrence scheme is
isomorphic over `Z` to the divisor scheme.

Let `r_0=floor(log_2(2h-1))`. Since `2^r_0<2h`, the first `r_0` remainders
are fixed monomials and their quotients vanish. There remain `k=s-r_0`
recurrences. Their `k-1` intermediate remainders and `k` quotients contribute

```text
(k-1)(2h)+k(2h-1)=k(4h-1)-2h                       (4)
```

variables. The coefficients of `S`, `a`, and the `h-1` selectors contribute
`h+1+h-1=2h`, proving the variable count in `(NFS7)`. Each recurrence has
degree at most `4h-2` in `X`, so it gives `4h-1` coefficient equations. The
selector adds one. Coefficients of `D` are quadratic in the base variables;
therefore every recurrence coefficient has total variable degree at most
three, while the selector has degree two.

For one chart, replace the `h-1` selectors by one inverse. The base count
becomes `h+2`, giving

```text
h+2+k(4h-1)-2h=k(4h-1)-h+2,                         (5)
```

and the equation count is unchanged. Direct substitution at `s=13` proves
`(NFS9)`.

Finally, a characteristic-zero point of either selector presentation would
give a non-full-fiber characteristic-zero trade, contradicting the first
part of the proof. Hence each defining ideal is the unit ideal over `Qbar`.
Hilbert's Nullstellensatz and denominator clearing produce nonzero integer
identities. Every finite-characteristic solution reduces those identities to
zero, so its characteristic divides the corresponding certified integer.
QED.
