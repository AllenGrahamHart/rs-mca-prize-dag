# Proof

Every column of `Lambda` is orthogonal to the two slope vectors
`(1)_i` and `(gamma_i)_i`. Every row is in the dual of cubic evaluation on
the coordinate domain. Hence `Lambda` is a word of the tensor product of a
dual `RS_2` slope code and a dual `GRS_4` coordinate code.

Suppose first that `r=1`. Then all nonzero rows are proportional. A nonzero
column is a dual `RS_2` word and therefore has weight at least three, so at
least three block rows are nonzero. Any two proportional nonzero rows have
the same support, of size at least five by the dual-trade theorem. Their
agreement blocks both contain that support, contradicting the pair cap four.
Thus `r!=1`.

Now assume `r=2`. The column space is a two-dimensional subcode of the dual
`RS_2` slope code. Its support is exactly the set of `t` nonzero rows. If
`t<=3`, puncturing that subcode to its support would put two independent
vectors in the kernel of a two by `t` Vandermonde matrix. Every two columns
of that matrix are independent, so its nullity is at most one for `t<=3`, a
contradiction. Hence `t>=4`.

Let `W` be the two-dimensional row space, and let `G` be its common zero set
on the coordinate domain. Put `R=|V\G|`; this is the union of the nonzero row
supports. No two selected nonzero rows are proportional, by the same
pair-cap argument used above.

For each `x` outside `G`, evaluation at `x` is a nonzero linear functional
on `W`. Its kernel is one projective point of `P(W)`. Therefore `x` can be a
zero of at most one of the `t` projectively distinct selected rows. The
noncommon zero sets of those rows are disjoint.

Every selected row has weight at most `m`, since it is supported in its
agreement block. It consequently has at least `R-m` zeros in `V\G` whenever
`R>m`. Disjointness gives

```text
t(R-m) <= R.
```

If `R<=m`, the desired bound is automatic; otherwise rearranging gives

```text
R <= t m/(t-1).
```

Since `t>=4` and `t/(t-1)` decreases with `t`, (RL1) follows. Substitution of
`m=9,9,7` and `m=10,10,8` gives the six printed coordinate caps.
