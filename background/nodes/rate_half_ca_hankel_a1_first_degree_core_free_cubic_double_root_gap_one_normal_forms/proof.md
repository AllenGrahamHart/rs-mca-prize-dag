# Proof

At `u=1`, the cubic router gives

```text
O=e-1,
I_E=Delta-1-I_0,
c_s+c_d=2+I_0.                                       (1)
```

Let `epsilon=epsilon_s+epsilon_d`. The root rows use excess degree
`I_E+epsilon`, and each ordinary incidence uses at least two. Since
`C_tot=Delta-w`, the excess degree outside those named charges is

```text
R_out=1-w-I_0-epsilon>=0.                            (2)
```

If `I_0=0` and `R_out=1`, that one degree occurs at a supported incidence
away from both roots of `R_3`. There the scalar residual is a unit. One
excess copy gives horizontal multiplicity one or two according as the root
is new or overlaps the minimal locator, contradicting the ordinary cube
divisibility `3|m`. Thus `R_out=0`, and `(2)` gives

```text
I_0=0: w+epsilon=1.                                  (3)
```

If `I_0=1`, equation `(2)` immediately forces

```text
I_0=1: w=epsilon=R_out=0.                            (4)
```

In `(4)` the ordinary incidence spends exactly two excess degrees. It must
therefore overlap the minimal locator and has multiplicities `(b,r,m)=(1,2,3)`.

The root-row correction law gives

```text
t_s=c_s+epsilon_s mod 3,
t_d=c_d+epsilon_d mod 3.                             (5)
```

At the simple row, the vertical estimate is

```text
t_s<=c_s+epsilon_s.                                  (6)
```

At the double row, `t_d<=e-c_d` because there are only that many
distinguished incidences.

First let `I_0=0`. Equation `(1)` forces `c_s=c_d=1`. There are no new
roots outside the root rows, so

```text
t_s+t_d=C_tot-O=e-w.                                 (7)
```

If `epsilon=0`, equations `(3),(5)--(7)` give
`w=1,t_s=1,t_d=e-2`. If `epsilon=1`, it lies on exactly one root row. When
it lies on the simple row, `(5),(6)` force `t_s=2` and `(7)` gives
`t_d=e-2`. When it lies on the double row, `(5),(6)` give `t_s=1` and
`(7)` gives `t_d=e-1`. These are the first three rows of `(DGN2)`.

Now let `I_0=1`. Equation `(1)` gives `c_s+c_d=3`, while `(4)` gives
`t_s+t_d=e`. Since `c_s<=2`, equations `(5),(6)` force `t_s=c_s`.
Thus `t_d=e-c_s`; comparison with `t_d<=e-c_d` gives `c_s>=c_d`.
The only positive partition is `c_s=2,c_d=1`, proving the last row.

We identify the vertical and contact divisors. At a simple residual root,
an unaugmented new point has `(m,n,k)=(1,2,1)`, an overlapping point has
`(2,1,1)`, and the augmented new point in the second packet has
`(2,1,1)`. Exact vertical degree therefore gives the simple-row divisors in
`(DGN3)`.

At the double root, an unaugmented new point has `(m,n,k)=(1,1,1)`. In the
packets with `t_d=e-2`, the unique overlap has `(2,2,2)`; in the packet with
`t_d=e-1`, the unique augmented new point also has `(2,2,2)`. Denote that
point by `P`. This gives the double-row and contact divisors in `(DGN3)`.
The ordinary point in the last packet has contact multiplicity one as noted
above. All displayed contact degrees total `Delta`, so no other zero remains.

The sum of the two vertical fibres has class `O_C(2,0)`. Divide its divisor
by the contact divisor, whose line bundle is `O_C(-rho-1,e+1)`. This gives
`(DGN4)` and confirms that `deg L_1=1`.

For completeness, push forward along the domain projection. A positive
proper vertical subdivisor of length `j=1,2` has nilpotent modification
directions disjoint from the constant line, so

```text
pi_*O_C(A)=O direct_sum O(1-rho) direct_sum O(-rho)^(e-2),
pi_*O_C(A+B)=O direct_sum O(1-rho)^2 direct_sum O(-rho)^(e-3). (8)
```

Each bundle in `(8)` has only its canonical section. In the ordinary packet,
`Q` lies on a different domain fibre from `A+B`, so subtracting it kills that
section. This proves `(DGN5)`. QED.
