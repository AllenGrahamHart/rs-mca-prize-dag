# Proof

For a relation supported on every block of its minimal Maxwell core, the
collision-defect identity gives

```text
-e=Delta=D_0+2C<=0,       C=(t-2)I+sigma+H>=0.       (1)
```

Hence `D_0<=0`. The case `D_0=0` is covered by the zero-baseline arithmetic
router, including its official-row rank floors. It remains to derive a
uniform floor when `D_0<0`.

Write

```text
B_t(D)=t h+(t-2)(t-1)D.
```

Then `D_0<0` says

```text
2(t-2)Z>B_t(D).                                     (2)
```

Every zero fiber has size at most `d=D-1`, so `Z<=t(D-1)`. Combining this
with `(2)` gives

```text
t h+2t(t-2)<(t-2)(t+1)D.                           (3)
```

The least integer satisfying `(3)` and the residual-shell condition `D>=3`
is exactly `D_-(h,t)` in `(GF2)`.

For a fixed `D`, strict inequality `(2)` forces

```text
Z>=floor(B_t(D)/(2(t-2)))+1.                        (4)
```

The pairwise zero-fiber inequality `z_i+z_j>=D` independently gives the
sharp total-mass floor from the shell router,

```text
Z>=M_t(D).
```

At `D=D_-`, these are exactly the two terms defining `Z_-`. Both are
compatible with the degree capacity: `(3)` proves this for `(4)`, while the
explicit parity formulas give `M_t(D)<=t(D-1)` for every `D>=3`.

The active zero fibers are disjoint in `X`, so `Z<=a+D`. The shell condition
`d<=a-1` gives `a>=D`, and `t<=a+2` gives `a>=t-2`. Therefore

```text
a>=Z-D.                                             (5)
```

The pair-mass floor already makes `(5)` dominate the two other shell terms.
Indeed, if `D` is even then `M_t(D)-D=(t-2)D/2`; if `D` is odd then
`M_t(D)-D=(t-2)(D+1)/2`. Since `t>=4` and `D>=3`, either expression is at
least both `D` and `t-2`.

After substituting either lower bound for `Z`, the quantity `Z-D` is
nondecreasing in integer `D`. For the strict-baseline term this follows
because increasing `D` raises its floor by at least one before subtracting
the one-unit increase in `D`. For the pair-mass term, the even-to-odd step
raises `M_t(D)-D` by `t-2` and the odd-to-even step leaves it unchanged. Thus
the minimum occurs at `D_-`, proving `(GF4)`.

The official RowC ranges use `t<=a+2<=k+2`. The prize ranges use the exact
minimal-core caps `384,448,960`. Evaluating `(GF2)--(GF3)` over these finite
ranges gives the table; the verifier replays every arity with integer
arithmetic. Comparing with the proved zero-baseline floors and using `(1)`
gives the all-baseline floor. QED.
