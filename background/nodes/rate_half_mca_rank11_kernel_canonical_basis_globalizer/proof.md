# Proof

Write the residual coordinate equation as

```text
E_x(Z)+q(Z)R(x)=0,       R in W,
```

where `q` is nonzero at every retained slope. Fix a rank-`r` basis
`B subset T`, put `H=ker(ev_B)`, and choose a complement `W_0` to `H`.
Evaluation on `B` identifies `W_0` with its image.

Solving the equations on `B` gives, for every compatible slope,

```text
q(Z)R_0(Z)=U_0+Z U_1,       U_0,U_1 in W_0.        (1)
```

If only one record uses `B`, the claimed record cap is automatic. If at
least two distinct slopes use it, every remaining compatibility condition
on `B` is an affine-linear polynomial in `Z` with two roots and hence is an
identity. Thus (1) is one common quotient solution for every record over
`B`. With

```text
(A,B_1)=(a_0'+U_0,b_0'+U_1),
```

the selected explanations are

```text
h_gamma'=A+gamma B_1+q(gamma)v_gamma,
v_gamma in H.                                      (2)
```

The pair `(A,B_1)` agrees with the received pair on every coordinate of
`B`. Translate by this pair. Since nonzero scalar multiplication preserves
`H`, (2) puts the complete selected family in the fixed explanation space
`H`. Every word of `H` and both translated received columns vanish on
`B`, so exact locator division and deletion of `B` preserve slopes, exact
supports, badness, and same-support pair noncontainment. The descended
explanation space has dimension

```text
d=dim H=10-r.                                       (3)
```

If `r=0`, then `W` vanishes on `T`. The residual correction space has empty
global common support, so no such coordinate exists. Equivalently, two
selected slopes would force every degree-one `E_x` on `T` to vanish
identically, putting `T` in the common support of the complete residual
family. Hence `1<=r<=9` and `1<=d<=9`.

Now fix a rank-`r` tuple `T` whose canonical basis is `B`. Since
`rank(ev_T)=rank(ev_B)`, every coordinate in `T minus B` is a common zero
of `H`. A `d`-dimensional subspace of degree-below-`K'` polynomials has at
most `K'-d` common zeros: after dividing their gcd of degree `z`, the
quotient polynomial space has ambient dimension `K'-z>=d`. Since the `r`
basis coordinates are already common zeros, at most

```text
(K'-d)-r=K'-10                              (4)
```

additional coordinates are available. There are therefore at most
`C(K'-10,d+1)` choices for `T minus B` per record.

After cancellation, support-local transversality bounds the number of
records over `B` by `M_d` for `d<=8`. For `d=9`, use the uniform proved
margin/interleaving cap

```text
M_9=61871313426630599.
```

Multiplying this record cap by (4) gives the claimed fixed-basis incidence
capacity. Choosing one canonical basis for each tuple makes the capacities
summable without tuple overcounting.
