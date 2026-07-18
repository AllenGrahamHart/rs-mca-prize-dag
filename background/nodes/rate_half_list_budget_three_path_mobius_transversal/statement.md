# Budget-three path Mobius transversal

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Take the canonical path-plus-singleton row of the split-fiber atlas. Thus the
singleton has label `3`, the two edge blocks are

```text
E_02={r},       E_12={s},       S={w},
```

where `r,s,w` are distinct points of `D`; there is no full block. Put

```text
e_02=X-r,       e_12=X-s.
```

Every quotient except possibly `q_23` is a nonzero constant. The `012` and
`013` triangle identities are exactly

```text
q_01 A_2+q_12 e_12 A_0=q_02 e_02 A_1,             (PM1)
q_01 A_3+q_13 A_0=q_03 A_1.                       (PM2)
```

Define four monic degree-`d` split factors

```text
P_0=e_12 A_0,  P_1=e_02 A_1,  P_2=A_2,  P_3=(X-w)A_3.
```

They are pairwise coprime and partition the domain polynomial:

```text
Lambda_D=P_0P_1P_2P_3.                            (PM3)
```

The first three are distinct members of one constant pencil by `(PM1)`.
Let

```text
theta=P_1/P_0,       c=q_13/q_03,
tau=q_12/q_02.
```

Their root fibers and the complementary block are

```text
theta=infinity on roots(P_0),
theta=0        on roots(P_1),
theta=tau      on roots(P_2),
theta=c (X-r)/(X-s) on T_3.                       (PM4)
```

The last map is nonconstant and injective on `T_3`. The only other root of
`P_3` is `w`. Therefore every further constant-pencil member has at most two
roots in `P_3`, and for `d>=3` the degree-`d` pencil has exactly the three
fully `D`-split members `P_0,P_1,P_2`.

There is a second coupled pencil of degree `d-1`: `A_0,A_1,A_3` are three
distinct constant-pencil members by `(PM2)`. On the remaining large block,

```text
A_1/A_0=tau (X-s)/(X-r) on T_2,                   (PM5)
```

which is again injective. Outside `T_2`, only `r,s,w` remain available after
the three existing fibers are removed. A fourth member can consequently have
at most four domain roots. For `d>=6`, this pencil also has exactly three
fully `D`-split degree-`d-1` members.

Thus every large-scale path witness is a coupled pair of primitive
three-member pencils with injective Mobius transversals, not a four-member
quotient pencil. This class is not excluded here, and no adjacent crossing is
promoted.

An exact `RS[F_17,F_17^*,8]` certificate shows that the path incidence type
survives at `d=4` on a power-of-two multiplicative domain while the first
pencil has exactly these three members. Therefore disappearance of the fourth
member is not an exclusion of the path itself. The certificate is a small
characteristic-specific route fence and has no official-scale transport.
