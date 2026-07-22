# Proof - L1 maximal background-anchor injection

The exact core-defect normal form gives a monic degree-`d` locator `F=L_D`
and `deg W<=d`. For every touched petal,

```text
W-c_jF=L_(S_j)A_j,       deg A_j<=d-a_j,               (1)
```

and `W` vanishes on `R_0`. The list threshold says

```text
r+h>=ell+d.                                             (2)
```

Fix `i in I`. Suppose two codewords in the fixed layer, with data `(F,W)`
and `(F',W')`, have the same `A_i`. Equation `(1)` gives

```text
W-W'=c_i(F-F').                                         (3)
```

For every `j!=i`, subtracting the two `j`-petal equations and using the
pairwise distinct labels shows that `F-F'` vanishes on `S_j`. On `R_0`, both
`W` and `W'` vanish, so `(3)` and `c_i!=0` show that `F-F'` vanishes there as
well. Therefore `F-F'` is divisible by a polynomial of degree

```text
r+h-a_i >= ell+d-a_i >= d.                              (4)
```

If the right side is greater than `d`, the degree bound forces `F=F'`. At
equality, monicity gives `deg(F-F')<d`, with the same conclusion. Equation
`(3)` then gives `W=W'`. Thus `(BA2)` is injective and its target has at most
`q^max(0,d-a_i+1)` elements. Choose `a_i=a_*`.

For the second injection, write `W=L_(R_0)V`; if `d<r`, the only possible
quotient is the zero polynomial. If two codewords have the same `V`, they
have the same `W`. Subtracting `(1)` pointwise on every `S_j` shows that
`F-F'` vanishes on their disjoint union, of size `h`. Since the chart is
maximal, `r<ell`, and `(2)` gives

```text
h>=ell+d-r>d.                                           (5)
```

Hence `F=F'`, and the codewords coincide. The quotient space has at most
`q^max(0,d-r+1)` elements. Taking the smaller of the two independent bounds
gives

```text
min(max(0,d-a_*+1),max(0,d-r+1))
 =max(0,d-max(r,a_*)+1),
```

which proves `(BA4)`.

For the stratum ledger, choose `R_0`, the `t` touched petals, and the `u`
missing points among their `t ell` positions. This gives at most

```text
binom(b,r) binom(M,t) binom(t ell,u)                    (6)
```

support patterns. If `a_*` is the largest petal support, averaging the
deficits gives

```text
a_*>=ell-floor(u/t).                                    (7)
```

For each `d<=ell+E`, `(BA4)` and `(7)` give

```text
max(0,d-max(r,a_*)+1)
 <=min(E+floor(u/t)+1, max(0,E+ell-r+1))=gamma.          (8)
```

There are at most `ell+E+1` nonnegative defect values. Multiplying `(6)`,
this defect count, and `q^gamma` proves `(BA5)`.
