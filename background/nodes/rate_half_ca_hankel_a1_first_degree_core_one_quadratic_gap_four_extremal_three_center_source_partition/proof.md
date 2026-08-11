# Proof

At every slope `gamma in A`, the assigned center lies on `c^L`, so

```text
b(gamma)=f_gamma-c_gamma.                            (1)
```

Its support is the actual error support `S_gamma`. At the two endpoint
slopes, the joint support of `b` is therefore

```text
supp(b_0,b_1)=S_alpha union S_beta=U.                (2)
```

For every `x in U`, the coordinate `b(t)(x)` is a nonzero homogeneous
linear form on the parameter line. It can vanish at at most one of the
three distinct slopes in `A`. Thus the missing sets in `(ESP3)` are
pairwise disjoint.

Every line support is contained in `U`, the core belongs to every support,
and

```text
|U_0|=3p-2,
|S_gamma|=rho-r_gamma=2p-r_gamma.                   (3)
```

Hence

```text
|M_gamma|
 =|U_0|-(|S_gamma|-1)
 =(3p-2)-(2p-r_gamma-1)
 =p-1+r_gamma,                                      (4)
```

which proves `(ESP4)`. Summing `(4)` gives

```text
sum_(gamma in A)|M_gamma|=3p-3+d_A
                           =|U_0|-(1-d_A).           (5)
```

The sets are disjoint and `d_A` is zero or one, so `(5)` proves the two
partitions in `(ESP5)`.

Finally fix `x in M_gamma`. The nonzero linear form `b(t)(x)` vanishes at
`gamma`, so it is a nonzero scalar multiple of `ell_gamma(t)`. Multiplication
by the fixed nonzero contraction and dual-column factors `(x-s_0)v_x`
preserves this statement and gives `(ESP7)`. If `x_circ` exists, it belongs
to none of the three missing sets, so its source form is nonzero at all
three line slopes. QED.
