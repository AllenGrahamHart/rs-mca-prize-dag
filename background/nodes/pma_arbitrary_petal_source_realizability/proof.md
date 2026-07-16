# Proof - PMA arbitrary-petal maximal-source realizability

For each `i`, the polynomial `f_i=c_iL_C` has degree `k-1`, so it is a
codeword of `RS[K,L,k]`.

At every `x in C`, both `L_C(x)` and `U(x)` vanish. At every `x in T_i`,
the definition of `U` gives `U(x)=c_iL_C(x)=f_i(x)`. Therefore

```text
C union T_i subset Agr(U,f_i).                       (1)
```

If `x in B`, then `U(x)=0`, while `x notin C` gives `L_C(x)!=0`; because
`c_i!=0`, `f_i(x)!=U(x)`. If `x in T_j` with `j!=i`, then

```text
U(x)-f_i(x)=(c_j-c_i)L_C(x)!=0,
```

using distinctness of the `c_i` and again `x notin C`. There are no other
evaluation points. Hence equality holds in (1), proving

```text
Agr(U,f_i)=C union T_i,
|Agr(U,f_i)|=k-1+ell.
```

All pairwise agreement-set intersections are exactly `C`, so these listed
codewords form the prescribed sunflower. For `ell=sigma+1`, the agreement is
`k+sigma`, exactly the PMA list threshold.

The complement of the core has `n-k+1=Mell+b` points with `0<=b<ell`.
Every additional petal disjoint from the existing ones and the core would
need `ell` points, but only the `b` background points remain. Hence the
source is maximal by packing.

Finally, the construction imposed no algebraic condition on the sets `T_i`
beyond disjointness. Their monic locators can therefore have different
nonconstant coefficients. In a constant-shift pencil `P-a_i`, every
nonconstant coefficient is inherited from the same `P`; only the constant
coefficient varies. Choosing petals whose locators differ in a nonconstant
coefficient proves that maximality alone does not imply a common pencil.

The `F_17^*` instance in the statement has quadratic locator linear
coefficients

```text
0, 13, 9, 5 mod 17,
```

so it realizes this obstruction on a smooth multiplicative domain.
