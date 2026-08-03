# Proof

The three pairing-zero blocks are proved by the required parent claims, for a
total of `3*4*4=48` raw cases.  It remains to pay pairings one and two.

For `xi=0`, deleting the first positive `DE` copy leaves the ordered residual
products

```text
de, -de, df, sigma_o ef, bf, sigma_c cf.
```

For `xi=2`, deleting the negative copy leaves

```text
de, de, df, sigma_o ef, bf, sigma_c cf.
```

In both cases canonical pairings one and two retain positions `(0,1)` as the
first pair.  Hence the proved target-free cuts and their exact root-replay
ledgers from the pairing-zero packets remain necessary without recomputing a
norm.

At each retained common point, evaluate the source missing ratio `m` and
squared-sum value `s`.  Put `de=m` for `xi=0` and `de=-m` for `xi=2`.  Since
`e=de/d`, the missing squared-sum equation becomes

```text
(d^2+de)^2-s d^2 = 0                 for xi=0,
(d^2-de)^2-s d^2 = 0                 for xi=2.
```

For every positive-`DE` source-sign/pairing row, the first quartic has no
field root at two common points and four roots at each of the other two.  The
negative-`DE` quartic has no field root at any common point.  For each
positive-`DE` root, substitute `e=de/d`.  The two paired equations remaining
after the target-free first pair are now univariate quartics in `f`.  Their
gcd has degree zero in all `64` retained `d` roots and four target lanes,
accounting for `256` exact gcd decisions and producing no target candidate.

For `xi=1`, deleting the second positive `DE` copy gives exactly the same
ordered residual product and squared-sum lists as deleting the first.  This
value-by-value equality preserves canonical pairing indices one and two, the
missing product and squared-sum equations, and all target guards.  Therefore
the `xi=0` exclusions transport to `xi=1`, paying another `32` raw cases.

Combining `48` parent pairing-zero cases, `64` newly computed cases, and `32`
transported cases proves all `144` cases in the stated block empty. QED.
