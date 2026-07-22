# Proof - L1 root-free rational-Q projective packing

## 1. Dimension and the affine chart

The planted descent writes every candidate uniquely as

```text
P=P_S+D R,       deg R<d,
W_1R+G=c_P Lbar.                                  (1)
```

Multiplication by nonzero `W_1` is injective, so `W_1 F[X]_<d` has dimension
`d`.  If `G` belonged to that subspace, every element of `V` would be
divisible by `W_1`.  Since `gcd(W_1,Omega')=1`, no nonzero scalar multiple of
a degree-`j` divisor of `Omega'` could lie in `V`; the exact cell would be
empty.  Nonemptiness therefore gives `dim V=d+1`.

The element `W_1` itself lies in `V` and is nonzero at every point of `H'`.
Hence the elements of `V` have no common domain root.

Every exact candidate in `(1)` gives a point of `(PC2)`.  Conversely, consider
a split-locator point in `P(V)`.  If its coefficient of `G` were zero, it
would have a representative `W_1R`.  When `deg W_1>0`, this cannot divide
`Omega'` because `gcd(W_1,Omega')=1`.  When `W_1` is constant, it has degree
at most `d-1=j-w-1<j`, so it cannot represent a degree-`j` locator.  Thus the
coefficient of `G` is nonzero, can be normalized to one, and yields a unique
`R`.  The planted descent then proves exactness.  This establishes the
bijection and the empty hyperplane at infinity.

## 2. Root-set packing

Let two distinct points correspond to `R` and `R'`.  Their codewords differ
by

```text
P-P'=D(R-R').                                      (2)
```

At a common root of their reduced locators, both codewords agree with `U`.
That root lies in `H'`, where `D` is nonzero, so `(2)` forces
`R-R'=0`.  The nonzero polynomial `R-R'` has degree at most `d-1`; therefore
the two `j`-element root sets intersect in at most `d-1` points.

No `d`-subset of `H'` can consequently lie in two root sets.  Counting pairs
`(T,Lbar)` with `|T|=d` and `T` contained in the root set of `Lbar` gives

```text
|P(V) intersect Dloc_j(H')| binom(j,d) <= binom(n',d),
```

which is `(PC3)`.  The fixed-`d` and `d=1` consequences are immediate.

Finally,

```text
binom(n',d)/binom(j,d)
  = product_(i=0)^(d-1) (n'-i)/(j-i)
  <= (n'/(j-d+1))^d.
```

If `j>=alpha n'` and `d<=alpha n'/2`, then
`j-d+1>=alpha n'/2`, proving `(PC4)`.  Its logarithm is at most
`d log(2/alpha)`, which is `o(n')` for `d=o(n')` and
`o(R log |B|)` under the stated reserve condition.
