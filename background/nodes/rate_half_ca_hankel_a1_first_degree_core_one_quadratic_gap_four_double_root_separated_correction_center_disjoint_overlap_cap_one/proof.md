# Proof

Let `c^L(t)` be the affine codeword line through the three assigned centers
and put

```text
b(t)=f(t)-c^L(t),
U=S_alpha union S_beta.                             (1)
```

The exact source-partition theorem gives

```text
supp(b_0,b_1)=U.                                    (2)
```

The fixed heavy point `x_*` lies outside `U`: the nonempty form `g_*` cuts
out slopes where `x_*` is padded, every padding root lies outside
`U_0=U\{s_0}`, and `x_*!=s_0`.

For every assigned center `gamma in A={alpha,beta,theta}`, the line passes
through its assigned codeword, so

```text
b(gamma)=f_gamma-c_gamma,
S_gamma=supp b(gamma) subset U.                    (3)
```

Thus `x_*` is absent from the actual support of all three center errors.

Suppose a center `gamma` were a root of `S_B`. The row factorization

```text
Q(t,x_*)=a_Q g_*(t)S_B(t)^3                        (4)
```

makes `x_*` a root of the specialized locator `Q(gamma,X)`. By `(3)` it is
not an actual-support root, so in the double-root arm it is the padded heavy
root. Hence

```text
r_gamma=1,       g_*(gamma)=0,                     (5)
```

contradicting `gcd(g_*,S_B)=1`. Therefore no center is a correction root,
which proves `(HOD1)`.

The center factors of `g_*` are exactly the indicators `r_gamma=1`. The
three-center reduction gives

```text
deg gcd(g_*,Lambda)
 =sum_(gamma in A)r_gamma<=1.                       (6)
```

Equation `(HOD1)` now reduces `J` to `gcd(Lambda,g_*)`, and `(6)` proves
`(HOD2)`. The center-overlap factorization, separated nonvanishing, and
exact correction-order theorem give `(HOD3)`. Since no correction root is
a center, its exact order is two, proving `(HOD4)`. QED.
