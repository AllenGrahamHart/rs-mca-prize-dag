# Proof

Write every index uniquely as `i=s+ra`, with `0<=s<r` and `0<=a<4`. Put

```text
eta=zeta^4,       omega=zeta^r.
```

Then `eta` has order `r` and `omega` has order four. For
`f=f_0+4l`, direct substitution gives

```text
sum_i X_i zeta^(fi)
 = sum_(s=0)^(r-1) zeta^(f_0s) eta^(ls)
     [sum_(a=0)^3 X_(s+ra) omega^(f_0a)].                 (1)
```

As `l` ranges from `0` to `r-1`, the outer coefficient matrix is an
invertibly scaled Fourier matrix of order `r`. Hence all frequencies in one
band vanish if and only if the bracketed local expression vanishes for every
`s`.

For `f_0=1`, the local equation is

```text
(X_s-X_(s+2r)) + omega (X_(s+r)-X_(s+3r)) = 0.            (2)
```

Each parenthesized difference belongs to `{0,+1,-1}`. Since `omega` has
exact order four in odd characteristic, it is not `0`, `+1`, or `-1`.
Equation (2) therefore forces both differences to vanish. There are four
local assignments.

For `f_0=2`, the local equation is

```text
X_s-X_(s+r)+X_(s+2r)-X_(s+3r)=0,                          (3)
```

which has `binom(4,2)=6` assignments after moving the two positive
coordinates to one side. Imposing both (2) and (3) makes all four local bits
equal, leaving two assignments.

The `r` local blocks are disjoint, so the counts tensor. Dividing by the
`16^r` binary words proves all probabilities in `(CB1)`.

The joint local conclusion says

```text
X_s=X_(s+r)=X_(s+2r)=X_(s+3r)
```

for every `s`. Thus every joint vector is invariant under shift by `r`, and
in particular by `2r=n/2`. It is nonprimitive under the DLI antipodal owner,
which proves `(CB2)`. QED.
