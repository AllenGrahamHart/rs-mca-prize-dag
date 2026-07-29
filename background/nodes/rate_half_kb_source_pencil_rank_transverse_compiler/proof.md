# Proof

## Exact per-record compiler

For a profile `(m,n,a,b)`, partition the 12 source points into `a`
unordered blocks of size `m` and `b` unordered exceptional blocks of size
`m/5`. The number is

```text
12!/((m!)^a a! ((m/5)!)^b b!).                     (KBTR-2)
```

For `m=2,3,4,6,10,12`, these counts are respectively

```text
10395,15400,5775,462,66,1,
```

whose sum is 32,099.

Put the coefficient vectors of the complete source locators and fifth
powers of exceptional locators into a matrix `S_pi`. The source-pencil
equivalence says precisely that `rank(S_pi)=2`. For a passing pencil
`<H_0,H_1>`, put the coefficient vectors of

```text
H_0^n,H_0^(n-1)H_1,...,H_1^n
```

into the `61 x (n+1)` matrix `C_(m,n)`. Substitution of a nonzero degree-`n`
binary form into the nonconstant rational function `H_0/H_1` is injective,
so `C_(m,n)` has rank `n+1`. The active condition is exactly

```text
rank([C_(m,n)|coeff(V_act)])=n+1.                   (KBTR-3)
```

For degree 12, divide `V_act-N_0^5` by `A`. The canonical pencil theorem
reduces `(KBTR-3)` to membership of the quotient in the span of
`A^4,A^3N_0,A^2N_0^2,AN_0^3,N_0^4`, a rank-five test on 49 coefficients
with 44 independent syndromes.

## Same-fiber exclusion

If `h=s composed r` has a proper right factor, then
`f=(F composed s) composed r`; iterating strictly lowers the inner degree
until the right component is indecomposable or reaches the deleted
degree-five row.

For an indecomposable separable rational map, geometric monodromy is
primitive. An irreducible bidegree-`(4,4)` component of `h(T)=h(W)` would
give its point stabilizer a suborbit of size four. For `m=2,3,4`, the
off-diagonal same-fiber divisor has bidegree `(m-1,m-1)<(4,4)`. For
`m=6,10,12`, the complete primitive-group subdegree catalogues have only
the nontrivial rows `5`, `3+6` or `9`, and `11`, respectively. None contains
four. Thus the actual component is not a same-fiber component.

## Transverse degree ledger

Let `Gamma` be the actual component and let
`C=(h x h)(Gamma)` be its irreducible non-diagonal outer image. Projection
`Gamma->P^1_T` has degree four and `h` has degree `m`, so
`Gamma->P^1_Y` has degree `4m`; the same holds in the other coordinate. If
`delta=deg(Gamma->C)` and `bideg(C)=(r_Y,r_Z)`, then

```text
delta*r_Y=4m=delta*r_Z.
```

Hence `r_Y=r_Z=r` and `delta*r=4m`. The restriction of `h x h` has degree
at most `m^2`, giving `delta<=m^2`. Since `C` is non-diagonal in the
degree-`n=60/m` outer self-correspondence, `r<=n-1`. Enumerating divisors of
`4m` under these two inequalities yields exactly the 26 rows in the
statement. QED.
