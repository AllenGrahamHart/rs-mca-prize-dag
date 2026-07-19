# Proof

Because `p=1 mod n`, the prime `p` splits completely in `Q(zeta_n)`. Its
degree-one primes are

```text
P_r=(p,zeta-g^r),       r mod n odd.                (1)
```

For any nonzero integral ideal `K`, the rational prime `p` divides `N(K)` if
and only if `K` is contained in at least one prime ideal above `p`. Apply this
to `K=K_(E;F,G)`.

At `P_r`, the element `pi=1-zeta` reduces to `1-g^r`, which is nonzero because
`g^r` has exact order `n>=4`. Hence division by `pi^2` is multiplication by a
unit in the residue field. Both normalized generators of `K` vanish at `P_r`
if and only if

```text
beta_F(g^r)-beta_E(g^r)=0,
beta_G(g^r)-beta_E(g^r)=0.
```

Combining this observation with `(1)` proves `(PAC1)`.

It remains to remove the quantifier over `r` for the candidate union. For an
unordered exponent pair `E`, direct substitution gives

```text
beta_E(g^r)=beta_(rE)(g).                           (2)
```

Odd dilation preserves squared vector norms, both rooted-star distances, and
distinctness of the three pairs. Therefore `(E;F,G)` is admissible if and only
if `(rE;rF,rG)` is admissible. Equation `(2)` maps every witness at `g^r` to a
witness at the fixed root `g`, and the inverse odd dilation gives the reverse
map. Taking the union over all admissible stars proves `(PAC2)`. QED.
