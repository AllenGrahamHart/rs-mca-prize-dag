# Proof

The cube map on `F_p^*` has kernel size `g`. Its restriction to the dyadic
group `H` is bijective because `gcd(3,n)=1`, so `H` lies in its image.
Therefore the full preimage `K` in `(NCE1)` is a subgroup of order `gn`.

Write `Q=F_p^*/H`. For a nonnode parameter `theta`, put

```text
A=[theta],       B=[1+theta].
```

The nodal parameter router says that the point belongs to the singular trace
`3c` exactly when

```text
A^3=1,       B=CA^2,       C=[c].                  (1)
```

Equation `(1)` implies `theta^3,(1+theta)^3 in H`, hence
`theta,1+theta in K`. Conversely, if those two elements lie in `K`, then
`A^3=B^3=1`. Put `C=BA`; since `A^(-2)=A`, this is exactly `B=CA^2`.
The natural map from the field cube roots of unity to `Q[3]` is injective,
because `H` has no nontrivial cubic torsion, and both groups have size `g`.
Thus there is a unique cube root `c` with class `C`, and `(1)` holds.
Excluding `0,-1` and the two tangent parameters gives the bijection `(NCE2)`.

Apply the Mattarei affine coset-pair theorem to the two forms `theta` and
`1+theta` on the order-`gn` subgroup `K`. It bounds all nonnode parameters by
`C_M(gn)^(2/3)`. The node `(c,c)` lies in `H^2` only for `c=1`, so there is
exactly one additional subgroup node. This proves `(NCE3)`.

For a retained target, the quotient-line fiber satisfies

```text
R(t)+1=#{z in H:1-t(1-z) in H}.                    (2)
```

The two affine forms in `(2)` are nonconstant and nonproportional because
`t notin {0,1}`. Mattarei's arbitrary Fermat coefficients permit the slope
`t` to lie outside `H`. Applying the same theorem at order `n` gives

```text
R(t)<C_M n^(2/3).                                   (3)
```

Let `N_c` be the point count on one singular trace. Before imposing any
favorable richness, class, or signed-disjointness predicate, that trace has
at most `N_c^2` ordered point pairs. Equations `(3)` and `(NCE3)` give

```text
G_sing^0+G_sing^A
 <C_M n^(2/3) sum_c N_c^2
 <=C_M n^(2/3)(sum_c N_c)^2
 <C_M n^(2/3)(C_M(gn)^(2/3)+1)^2,
```

which is `(NCE4)`.

It remains to print rational constants. Since

```text
C_M<189/100,       n^(2/3)>406,                    (4)
```

the first inequality follows after cubing from
`4*189^3>27*100^3`, and the second from
`8192^2>406^3`. If `g=1`, the class-weighted ratio in `(NCE4)` is
strictly below

```text
17(189/100)((189/100)^2+2(189/100)/406+1/406^2)
 =677422443051/5887000000
 <116.                                               (5)
```

If `g=3`, then

```text
3^(2/3)<2081/1000,       3^(4/3)<4327/1000
```

because `2081^3>9*1000^3` and `4327^3>81*1000^3`. Expanding `(NCE4)`, the
corresponding ratio is below

```text
17(189/100)[(189/100)^2(4327/1000)
 +2(189/100)(2081/1000)/406+1/406^2]
 =2927247785605377/5887000000000
 <498.                                               (6)
```

Using the larger class coefficient `17` in `(5)--(6)` proves `(NCE5)`.
QED.
