# Proof

Put `H=38385`, `d=H+4`, and `D=H+d=2H+4=76774`. Work in
`A_t=F[X]_(<=t)`. Choose coprime squarefree split polynomials `L_1,L_2` of
degree `H` with disjoint roots in the actual evaluation set.

Consider pairs

```text
(V_1,V_2) in Gr(5,A_d)^2
```

such that

```text
V_1 intersect L_2 A_4=0,
V_2 intersect L_1 A_4=0,
gcd(V_1)=gcd(V_2)=1.                                  (1)
```

The first two conditions make `L_1V_1+L_2V_2` direct. They also make the
map from pairs to ten-spaces injective: intersecting the image with
`L_iA_d` recovers exactly `L_iV_i`.

The Grassmannian `Gr(5,A_d)` has dimension

```text
5((d+1)-5)=5H,
```

so the pair family has dimension `10H=383850`; the excluded conditions in
(1) are proper closed subsets.

Now count all possible product presentations inside `A_D`. If `P` and `B`
have maximal degrees `a` and `b`, respectively, then `a>=1`, `b>=4`, and
`a+b<=D`, because a product of maximal-degree elements belongs to `A_D`.
For fixed `(a,b)` the parameter-space dimension is at most

```text
dim Gr(2,A_a)+dim Gr(5,A_b)
=2(a-1)+5(b-4)
<=5D-25
=10H-5=383845.                                        (2)
```

There are only finitely many degree pairs. Hence the union of all product
loci has dimension at most `10H-5`, strictly below the family in (1).
Choose a pair outside that union and set

```text
C'=L_1V_1 direct_sum L_2V_2.
```

The gcd conditions and coprimality of `L_1,L_2` give `gcd(C')=1`, so there
is no global common zero. Every two- or three-subspace of `L_iV_i` vanishes
on the `H` roots of `L_i`. The two block families span their blocks and hence
span `C'`.

For an explicit finite-field count, write `q=|F|`. The Gaussian bounds

```text
q^(5H) <= |Gr(5,A_d)| <= 4q^(5H)
```

hold for `q>=2`. For one fixed five-space, the subspaces meeting it
nontrivially number at most `8q^(4H+4)`. Five-spaces with nontrivial gcd
number at most `5q^(5H-4)`. Thus, for official-size `q`, admissible pairs in
(1) number more than `(1/2)q^(10H)`.

On the other hand, summing the Gaussian upper bounds over all degree pairs
in (2) gives at most

```text
16(D+1)^2 q^(10H-5)
```

product-presentable images. The official field has `q>=n=2097152`, and

```text
q^5 > 32(D+1)^2,
```

so the latter count is below `(1/2)q^(10H)`. This supplies the finite-field
choice claimed above.

Finally, the number of rich containers available from the two blocks is

```text
4 * GaussianBinomial(5,2;q) >= 4q^6 > 16384884,
```

and `D<K=1048576`. All required containers therefore live inside the
deployed Reed--Solomon polynomial degree bound.
