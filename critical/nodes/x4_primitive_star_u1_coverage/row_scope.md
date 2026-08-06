# Row scope and upstream correspondence

## Local official base rows

The local exact-slice compiler uses

```text
N=2^41,
K=rho N,  rho in {1/2,1/4,1/8,1/16},
t=t_XR=min{0<=j<=N-K : q^j>=2^128 binom(N,N-K-j)},
A=K+t.
```

The full locator-prefix map has depth `t` on `A`-subsets.  The finite local
allowance proposed by the X4 compiler is `16N^3`.  A transported quotient row
is a different tuple and must be printed by `TR`; the algebraic star-PTE
dictionary transports, but this numerical allowance and the final LIST sum
require row-specific replay.

## Upstream deployed rows

The active v13.2 LIST examples in `rs-mca` use deployed identity-scale rows
with domain size `n=2^21` and prefix parameters such as
`(m,w)=(1116046,67470)` and `(1116022,67446)`.  Its residual input
`prob:capg-active-shiftpairs` asks for a uniform maximum local primitive
degree with explicit row constants.

The correspondence is structural under

```text
upstream (n,m,w) <-> local (N,A,t).
```

It is not a numerical transport: neither upstream's row-dependent
`kappa_sp,E_sp` target nor the local `16N^3` allowance proves the other.
This node therefore uses the upstream item as a theorem-shape alignment and
possible shared proof route only.
