# Proof

Fix an `(H_C)` residual core and its coefficientwise interpolant

```text
H(X,Z)=sum_(j=0)^31 H_j(X)Z^j.
```

For a correction space `W` of dimension `s`, choose a basis
`P_1,...,P_s`. A rich correction `P=sum c_jP_j` obeys at coordinate `x`

```text
F_x(Z,c)=E_x(Z)+sum_j c_jP_j(x)=0.
```

This is a hypersurface of class at most `31H_Z+H_W` on
`P^1 x P^s`.

## Proper-intersection compiler

In the Chow ring, `H_Z^2=0` and `H_W^(s+1)=0`, so

```text
(31H_Z+H_W)^(s+1)=31(s+1)H_Z H_W^s.
```

Thus a proper intersection of `s+1` coordinate hypersurfaces has degree at
most `31(s+1)`. Every rich point lies on at least `m'` coordinate
hypersurfaces and contributes at least `C(m',s+1)` incidences. Summing over
the `C(n',s+1)` coordinate subsets gives

```text
N_W C(m',s+1) <= 31(s+1) C(n',s+1).
```

For fixed `s`, the binomial ratio is

```text
product_(i=0)^s (R+K'-i)/(d+K'-i).
```

Each factor decreases with `K'` because `R>d`. Since `s<=K'` and the
full-rank relative branch has `K'>=10`, the worst admissible endpoint is
`K'=max(10,s)`. Exact evaluation pays `s=1..11`; at `s=11,K'=11` the cap is
`73766883380602812`. The first adjacent formula at `s=12,K'=12` is
`1241731241521316220`, above budget.

If properness fails on a set `T` of `s+1` coordinates, inspect the evaluation
rank on `W`. Rank below `s` gives a nonzero word in `W` vanishing on the same
evaluation flat. At rank `s`, choose an evaluation basis `B subset T`. The
equations on `B` determine a unique polynomial correction curve

```text
P_B(Z) in W tensor F[Z]_(<=31).
```

A positive-dimensional common intersection forces every remaining equation
in `T` to vanish identically on that curve. These are respectively the
evaluation rank-flat and exact polynomial clone alternatives.

## Clone-tolerant compiler

Put `V=span(W,H_2,...,H_31)` and write `d_1(V)=R+a`, with `a>=1` by the RS
minimum distance. Strict growth of generalized weights gives, for every
`j`-dimensional `U<=W`,

```text
|supp(U)| >= R+a+j-1.
```

At most `n'-m'=R-d` support coordinates lie outside a rich size-`m'`
agreement set. Therefore

```text
d_j(W restricted to S) >= d+a+j-1.
```

Greedy basis selection supplies at least `(d+a)_rise_s/s!` unordered
evaluation bases inside each rich support.

For one such basis, solve its equations to obtain `P_B(Z)`. Let `C_B` be
the coordinates whose equation vanishes identically on this curve. If `W`
does not absorb all `H_j`, some coefficient of `H+P_B` of slope degree at
least two is a nonzero word of `V`. It has support at least `R+a`, so

```text
|C_B| <= K'-a.
```

Outside `C_B`, each coordinate supplies a nonzero degree-at-most-31 equation
in `Z`. Root capacity along the curve gives

```text
N(B) <= floor(31(n'-|C_B|)/(m'-|C_B|))
     <= M_a,
M_a=floor(31(R+a)/(d+a)).
```

There are at most `C(n',s)` evaluation bases globally. Double counting
rich-point/basis incidences yields

```text
N_W <= floor(M_a n'_fall_s/(d+a)_rise_s).
```

For fixed `s`, this decreases when `n'` decreases. It also decreases as `a`
increases: both `(R+a)/(d+a)` and every reciprocal denominator factor do.
The worst endpoint is therefore `n'=2097152,a=1`. Exact evaluation pays
through `s=9`, with cap `13013823503882165`; the adjacent `s=10` value is
`404431535289439486`.

Combine the two contrapositives. An over-budget space of dimension at most
11 is nonproper and hence supplies a rank-flat or clone component. If its
dimension is at most nine and it does not absorb the high core, the
clone-tolerant compiler already pays it, so every such survivor must absorb
the high coefficients. This proves all alternatives.
