# Proof

On a nonincidence, the scalar-weld equation is

```text
lambda_x P_x(delta)=zeta_delta F_delta(x).
```

Division by the nonzero fiber value gives

```text
lambda_x c_(delta,x)=zeta_delta,                   (1)
```

which is `(CRC2)`. Taking the alternating product around an even cycle
telescopes every `lambda_x` and `zeta_delta`, proving the necessity of
`(CRC3)`. Specializing to a four-cycle and clearing the four nonzero
denominators gives `(CRC4)`.

Conversely, the usual spanning-tree argument proves that `(CRC3)` on all
cycles makes the edge labels a coboundary: choose one vertex scalar,
propagate `(1)` along a spanning tree, and use each fundamental-cycle
identity to verify every non-tree edge. This already proves the first
equivalence.

We now compress the cycle family. For two fibers `delta,epsilon` and a
common row neighbor `x), put

```text
q_(delta,epsilon;x)
 =c_(delta,x)/c_(epsilon,x).                       (2)
```

The four-cycle identity for common neighbors `x,y` is exactly

```text
q_(delta,epsilon;x)=q_(delta,epsilon;y).            (3)
```

Thus all rectangle identities make the value in `(CRC7)` well defined.

In the extremal profile, each fiber root polynomial has domain degree
`n=p-3), while the classified row count is `R=3p-3+d_A`. Any three
fiber root sets therefore omit at most `3n` rows, leaving at least

```text
R-3n=(3p-3+d_A)-3(p-3)=6+d_A                      (4)
```

common neighbors. Evaluate the three pair transitions at one such neighbor.
Their product is

```text
[c_delta/c_epsilon]
[c_epsilon/c_theta]
[c_theta/c_delta]=1.                               (5)
```

Hence every transition triangle holds automatically.

In the strict profile, pairwise overlap is already proved, so every
`q_(delta,epsilon)` is defined. The triangle identities are retained
explicitly.

In either case, fix a base fiber `delta_0`, choose
`zeta_(delta_0)!=0`, and define

```text
zeta_delta
 =q_(delta,delta_0)zeta_(delta_0).                 (6)
```

The transition triangles imply

```text
zeta_delta/zeta_epsilon=q_(delta,epsilon).          (7)
```

Every row has an adjacent selected fiber by the connected-rank theorem.
For one such fiber define `lambda_x` by `(CRC9)`. If both
`delta,epsilon` are adjacent to `x), equations `(2)` and `(7)` give

```text
zeta_delta/c_(delta,x)
 =zeta_epsilon/c_(epsilon,x),                       (8)
```

so the definition is independent of the chosen fiber. It satisfies `(1)`
on every edge and therefore gives a nonzero weld kernel.

The connected-rank dichotomy says that a nonzero kernel forces
`rank W=R-1` and is unique projectively; absence of a nonzero kernel forces
`rank W=R`. This proves `(CRC6)--(CRC9)` and all failure claims. QED.
