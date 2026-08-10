# Proof

The compact-locus parent proves that, in these four rows, the complete common
system is the guarded zero set of three explicit compact equations. Exact
standard-basis reduction in the original variables gives

```text
t-epsilon_1 epsilon_2 r^2 = 0,
c^3 b+1 = 0.
```

The guard has `c != 0`; setting `u=c` therefore gives `b=-u^-3` and loses no
guarded point. Substitute these three relations into each compact equation
and clear its power of `u`. Direct polynomial gcd computation gives exactly

```text
G = r^2 (u^2-1)^2 H_epsilon(r,u)
```

with `H_epsilon` as in the statement. Division of every numerator by `G`
has zero remainder. The transformed guard excludes `r=0` and `u^2=1`.

It remains to exclude a second component on which the primitive quotients
all vanish while `H_epsilon` does not. Saturating their ideal by the complete
transformed guard gives the reduced basis `[1]` in all four sign rows. Hence
there is no such guarded component. Conversely, `H_epsilon=0` makes all
three substituted numerators zero, and the direct parameter-extended ideal
is nonunit of dimension one. The displayed guarded equation is therefore
both necessary and sufficient. QED.
