# Proof

The seven outside records in canonical order are

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf.
```

At `xi=5`, write `m=bf`, `x=b`, and `y=f`. At `xi=6`, write
`m=sigma_c cf`, `x=c`, and `y=sigma_c f`. In both cases the source
squared-sum record is `s=(x+y)^2` and `m=xy`. Guarded sources have `x!=0`,
so every target lift obeys

```text
x^2 ((x+m/x)^2-s) = (x^2+m)^2-s x^2 = 0.
```

The compiler evaluates this necessary condition in the exact cell-4 tower:
a quadratic relation for `t` over `F_p(r)`, a palindromic quadratic for `b`,
and linear recovery of `c`. It norms first through the `b` relation and
then through the `t` relation. The candidate parameter set is the union of
all deployed-field roots of the compatibility-norm numerator and every
numerator and denominator introduced by tower inversion.

Every candidate `r` is lifted through the original base and `b` relations,
then through linear `c` recovery when a route-open `b` exists. Across all
eight source-sign/endpoint rows there are 56 candidate parameters. Forty
terminate immediately on established `r` guards; eight of the remaining
base lifts terminate on `t` guards; the other eight have a quadratic `b`
relation with nonsquare discriminant. Thus no candidate reaches a guarded
source point. There is no free lift and no unresolved branch.

The independent verifier reconstructs all roots of each degree-42 norm and
all five inverse guards, proves the seven-root candidate union in every row,
solves every base quadratic, and checks every no-`b` discriminant. Therefore
no source compatible with either endpoint role exists. Since compatibility
precedes all matching and target-sign equations, all 480 raw cases are
empty. QED.
