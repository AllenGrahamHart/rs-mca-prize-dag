# Proof

Fix `(epsilon_1,epsilon_2)`.  Both product minors are linear in `c`.
For the first, the `c` denominator is `D=bB+A` and the other term is
`N=bA+B`.  If `D=N=0`, then

```text
bD-N=(b^2-1)B=0.
```

Target guards give `b^2!=1`, while `B=r^2-t^2!=0` is a source-label
guard.  Thus no denominator branch exists and `(KB41M-3)` follows.

Substitute `c`.  The numerator of the q weld using `AC+`, after deleting
only `b(b^2-1)(r^2-t^2)`, is exactly

```text
(rt+1)(rt-epsilon_1*i(r+t)-1).
```

This proves the exhaustive split `(KB41M-4)`.  On `Q0`, `t=-1/r`;
the denominator `r` is a source nonzero guard.  After deleting the common
factor

```text
b^2(r^2-1)^2(r^2+1),
```

the direct resultant in `b` of the remaining product and q numerators is,
up to a deployed unit,

```text
r^2(r^2+1)^2(r^2-1)^3
(r^2+epsilon_2*i)(r^2-epsilon_2*i)^3.             (1)
```

The factors `r=0` and `r^2=+/-1` are source guards.  At either root of
`r^2+epsilon_2*i`, the two routed numerators have b-gcd `b-1`; at either
root of `r^2-epsilon_2*i`, their b-gcd is `(b-1)^2`.  Target
distinctness excludes both.

On `Q1`,

```text
t=(epsilon_1*i*r+1)/(r-epsilon_1*i).
```

The denominator-zero value has `r^2=-1`, already a label collision.
Delete the common guard factor

```text
b^2(b-1)^2 r(r-epsilon_1*i)^5(r+epsilon_1*i).
```

The direct b-resultant of the two reduced numerators is

```text
r^2(r+epsilon_1*i)(r+epsilon_1*epsilon_2).         (2)
```

Here `r=0` is forbidden, `r=-epsilon_1*i` gives `r^2=-1`, and
`r=-epsilon_1 epsilon_2` gives `r^2=1`.  Thus `Q1` is empty as well.
No resultant leading coefficient was inverted, so degree-drop branches are
retained.  The argument holds in all four sign rows. QED.
