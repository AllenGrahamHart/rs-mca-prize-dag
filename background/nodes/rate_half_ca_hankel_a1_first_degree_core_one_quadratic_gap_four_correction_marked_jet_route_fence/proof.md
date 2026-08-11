# Proof

The Pade regular-factor theorem gives

```text
D_1=c g_*S_B^2
```

in the double-root arm, while the marked row has

```text
Q(-;x_*)=c' g_*S_B^3.
```

Substitution into `det(M_1+tau nu nu^T)=tau D_1Q(-;x)^2` proves
`(MJF1)`. In the two-simple arm, use

```text
D_1=c G_1G_2S_1S_2,
Q(-;x_i)=c_iG_i^2S_i^3
```

to obtain `(MJF2)`.

It remains to prove that these orders are abstractly realizable. Direct
multiplication gives

```text
L_eta(z)(1,z,...,z^eta)^T=0.                       (1)
```

The bidiagonal matrix has full row rank over `F(z)`, so the symmetric block
`K_eta` has generic rank `2eta` and the vector in `(MJF4)` spans its kernel.
Every maximal minor complementary to that kernel is a unit up to sign;
hence

```text
adj K_eta=c q q^T,       c!=0.                     (2)
```

For a block diagonal direct sum with a generically invertible regular block
`R(z)`, equation `(2)` becomes

```text
adj(K_eta direct_sum R)=c det(R) q q^T.            (3)
```

The rank-one determinant identity now gives

```text
det(M+tau vv^T)=c tau det(R)(v^Tq)^2.              (4)
```

For

```text
R_8=[[0,z],[z,1]],       det R_8=-z^2,
R_7=[z],                 det R_7=z,
v^Tq=z^3,
```

equation `(4)` is respectively a nonzero scalar times `tau z^8` and
`tau z^7`. This proves `(MJF5)--(MJF6)` and the route fence. QED.
