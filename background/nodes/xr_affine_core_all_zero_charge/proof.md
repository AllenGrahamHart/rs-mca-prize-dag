# Proof

The proved affine-core cogirth theorem supplies two ingredients. First, for
each `(gamma,e) in P`, the coordinate matroid of `K` restricted to the zero
set `Z_e` has rank `a`, cogirth at least `Delta-r`, and therefore at least

```text
B=C(Delta-r+a-1,a)
```

bases. Second, for every coordinate basis `T` of `K`, there is a unique
affine pencil

```text
e_T(gamma)=b_T+gamma q_T in A
```

that vanishes on `T`. Every pair for which `T subset Z_e` satisfies
`e=e_T(gamma)`.

Fix such a basis `T`. Call a coordinate in `U\T` persistent when its
coordinate polynomial in `e_T(gamma)` is identically zero, and let `p_T` be
the number of persistent coordinates. Put

```text
c=N-r-a.
```

Genericity gives `p_T<=c-1`: if at least `c` coordinates outside `T` were
persistent, then `T` together with any `c` of them would make both the
constant and direction lifts supported on at most `r` coordinates.

Let `M_T` be the number of pairs in `P` for which `T` is a basis contained in
`Z_e`. Every such error has at least `N-r` zero coordinates. After removing
the `a` coordinates of `T` and the `p_T` persistent coordinates, it therefore
has at least

```text
N-r-a-p_T=c-p_T
```

nonpersistent zeros. For a fixed nonpersistent coordinate,
`e_T(gamma)_x` is a nonzero affine polynomial in `gamma`, so it vanishes at
at most one slope. Uniqueness of `e_T(gamma)` also shows that distinct pairs
counted by `M_T` have distinct slopes. Consequently their nonpersistent zero
sets are disjoint, and

```text
M_T(c-p_T) <= N-a-p_T.
```

Since `N-a-p_T=r+(c-p_T)` and `c-p_T>=1`,

```text
M_T <= floor(1+r/(c-p_T)) <= r+1.                    (1)
```

Now count incidences `((gamma,e),T)` where `T` is a basis of `K|Z_e`.
Every pair contributes at least `B` incidences. There are at most `C(N,a)`
coordinate `a`-sets, and `(1)` permits at most `r+1` pairs over each one.
Thus

```text
|P| B <= sum_T M_T <= C(N,a)(r+1),
```

which is `(AZC)`.

For a one-per-slope selector, distinct pairs and distinct slopes coincide,
so the same bound controls the slope count at its affine rank. Substituting
the six printed XR rows gives `4,4,4,11,11,10`; the exact integer calculation
is replayed by `verify.py`.
