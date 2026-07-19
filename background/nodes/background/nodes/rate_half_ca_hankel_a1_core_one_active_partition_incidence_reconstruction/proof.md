# Proof

The two-sided partition theorem gives nonzero scalars `a_gamma,b_x` such
that

```text
Q(gamma;X)=a_gamma F_gamma(X),
Q(t;x)=b_x G_x(t).                                    (1)
```

Evaluating both identities at `(x,gamma)` proves the incidence equivalence
in `(AIR1)`. On a nonincidence edge both values are nonzero, and `(1)` gives

```text
a_gamma F_gamma(x)=b_xG_x(gamma),
theta_(x,gamma)=b_x/a_gamma.                          (2)
```

This proves `(AIR4)` and telescoping proves every cycle identity `(AIR5)`.

It remains to justify that the graph interface loses no scalar information.
A saturated row has at most `e_*` roots among the clean slopes, while a clean
slope has at most `r` roots among the saturated rows. Hence the degree bounds
in `(AIR2)` hold. Using

```text
n_Z=T-D_*=4e+1-D_*,       e_*=e-b,
D_0=8e+7,                 r=2e_*+1,
c<=C_*=e-5b-1+D_*,
```

gives

```text
n_Z-2e_*=2e+2b+1-D_*>0,
n_X-2r=4e+4b+5-c
      >=3e+9b+6-D_*>0.                                (3)
```

Thus any two row vertices have a common column neighbor, and any two column
vertices have a common row neighbor. In particular `H` is connected.
Potentials satisfying `(AIR4)`, if they exist, are therefore unique up to
simultaneous scaling. Conversely, on a connected graph the standard
spanning-tree propagation constructs the potentials exactly when all cycle
products are one. This proves the equivalence of `(AIR4)` and `(AIR5)`.

We now prove the reconstruction assertion. Necessity of `(AIR6)` follows by
writing

```text
Q(t;X)=sum_(j=0)^r q_j(t)X^j,       deg q_j<=e_*.
```

The first identity in `(1)` says
`q_j(gamma)=a_gamma f_(j,gamma)` at every clean slope, which is precisely
membership in the printed Reed--Solomon evaluation code.

Conversely assume incidence consistency, the cycle identities, and
`(AIR6)`. Recover the potentials and interpolate forms `q_j(t)` of degree at
most `e_*` with the values in `(AIR6)`. Put

```text
Q_0(t;X)=sum_(j=0)^r q_j(t)X^j.                       (4)
```

Then `Q_0(gamma;X)=a_gamma F_gamma(X)` at every clean slope. Fix a saturated
row `x`. At an incident clean slope, both `Q_0(gamma;x)` and
`b_xG_x(gamma)` vanish. At a nonincident clean slope they agree by `(AIR3)`
and `(AIR4)`. They are polynomials in `t` of degree at most `e_*` and agree
at all `n_Z>e_*` clean slopes. Therefore

```text
Q_0(t;x)=b_xG_x(t),
```

which proves `(AIR7)`. The monic `F_gamma` and nonzero `a_gamma` give exact
`X`-degree `r`; `(AIR7)` gives exact parameter degree `e_*`.

Write a minimal separated expansion

```text
Q(t;X)=sum_(i=1)^s A_i(X)B_i(t),       s=sr(Q).        (5)
```

The forms `A_i` and `B_i` are linearly independent. Evaluation on `X_sat`
is injective on polynomials of degree at most `r` because `n_X>2r>r`.
Evaluation on `Z_cl` is injective through degree `e_*` because
`n_Z>2e_*>e_*`. Therefore evaluating either coefficient span, or both sides
of `(5)`, preserves dimension `s`. This proves all three rank equalities in
`(AIR8)`. The dominant-component theorem gives
`sr(Q)>=ceil((e+1)/(b+1))>=5`; when `b=0`, `Q` is the full primitive residual
generator and its coefficient forms are independent, so `sr(Q)=e+1`. This
proves `(AIR9)`.

Finally the values on more than `e_*` clean slopes determine every
coefficient form `q_j`, so another biform with the same normalized partition
data differs only by the common scalar ambiguity in the potentials. This
proves the criterion and uniqueness. QED.
