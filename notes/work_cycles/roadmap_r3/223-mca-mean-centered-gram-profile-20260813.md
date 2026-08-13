# Cycle 223: MCA mean-centered Gram profile (2026-08-13)

The first post-Johnson Gram rung centered at the intersection ceiling.  A
stronger positive-semidefinite version instead centers the incidence columns
at their mean.

For equal-size `A)-blocks in an `n)-set with intersections at most `c`,
put

```text
p=A^2/n,
g=nc-A^2,
T=(n-A)^2-(n-1)g.
```

The matrix

```text
H=B(I-J/n)B^T
```

is PSD of rank at most `n-1`.  Its off-diagonal entries lie in
`[-p,c-p]`; when `2A^2>=nc`, the endpoint chord for the square has
nonpositive slope.  Positivity of `1^T H 1` and trace-rank give

```text
L <= floor((n-1)n^2(A-c)/(A*T))
```

whenever `g>=0` and `T>0`.

For the MCA profile, each deficit threshold uses either its positive-Johnson
cap or this mean-centered cap.  Raw caps need not be monotone across the
transition, so the theorem uses the proved suffix closure

```text
B_h=min_(h<=v<=e) C_v
```

before applying the exact `floor(e/h)` owner weights.

Exact evaluation pays 46 additional official supports:

```text
KoalaBear:   e<=64047, endpoint profile 181731868;
Mersenne-31: e<=65454, endpoint profile  16101127.
```

At KoalaBear `e=64048`, `T=-1499457466`.  At Mersenne `e=65455`,
all caps remain legal but the exact profile is
`17120123>16777215`.

```text
start:                   c2bbbaa86
canonical prize:         c8d48cd4b (no newer Fable commit)
result:                  NARROWED; one PROVED field-general compiler
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 64048<=e<=1044238;
                         Mersenne 65455<=e<=1044241
delta-star movement:     none
compute:                 exact local integer arithmetic under RAMguard;
                         no Modal
next route action:       strengthen the post-Johnson profile beyond its
                         PSD chord wall or exploit full-lift near-MDS
                         extension structure
```
