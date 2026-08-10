# Proof: official FPC5 prefix payment

For each official rate denominator `R` and source scale `M`, compute

```text
N=8192/R-1,
(ell,b)=divmod((R-1)8192/R+1,M).
```

The exact prefilter enumerates precisely the integer `(t,d)` cells satisfying
`(PF6)`. In each such cell put `u=d-(t-1)ell`. The syndrome-shell endpoint is

```text
H=t ell                    when u<0,
H=d+ell                    when 0<=u<=b.
```

Apply the proved constant-weight cap with `sigma=H-d` and
`w=min(d,N-d)`, minimizing over every legal shortening depth. Multiply by
one chart for `u<0` and by `binom(b,u)` charts otherwise.

For fixed `(M,t)`, sum the defect caps before applying the canonical
first-layout theorem. It gives

```text
binom(M,t) sum_d W_(M,t,d) A_(M,t,d)+M.                (1)
```

Summing `(1)` over the nonempty touched counts and then over the printed
source scales gives exactly `G_8` and `G_16`. The verifier evaluates all
binomial coefficients, shortening denominators, floors, and `(PF6)` tests as
integers. It also confirms the cell/group counts and the exact two totals.

Since the prize budget is `floor(q/2^128)`, either total `G` is paid when
`q>=2^128 G`. Direct integer comparison proves both thresholds are below
`2^256`; their bit lengths are 256 and 249.

The same replay at the four scales in `(OP5)` produces a cap greater than
`2^128-1`, the largest budget available below `2^256`. This proves only that
the present upper-bound compiler stops there. QED.
