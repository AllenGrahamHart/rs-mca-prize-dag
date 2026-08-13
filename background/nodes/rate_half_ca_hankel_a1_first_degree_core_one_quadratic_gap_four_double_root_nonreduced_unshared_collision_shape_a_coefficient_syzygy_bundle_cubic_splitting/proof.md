# Proof

Let `S=F[U,V]`. Basepoint-freeness of the parameter coefficient map means
that the forms in `V subset S_m` generate `O_P1(m)`. After base change to an
algebraic closure, their evaluation sequence is `(CSB2)`. The kernel has
rank `r-1` and degree `-m`. Grothendieck splitting gives integers `mu_i`,
and minimality of the coefficient presentation makes every `mu_i` positive.
Thus

```text
sum_i mu_i=m.                                      (1)
```

Twist the evaluation sequence by `O(2)`. Its global-section multiplication
map is

```text
S_2 tensor V -> S_(m+2).                           (2)
```

The three center pair-products `q_alpha,q_beta,q_theta` form a basis of
`S_2`: they are three independent quadratics because the center forms are
pairwise nonproportional. The exact generation theorem

```text
S_(m+2)=q_alpha V+q_beta V+q_theta V               (3)
```

therefore says that `(2)` is surjective. The cohomology sequence gives

```text
H^1(E(2))=0.                                       (4)
```

For a summand `O(2-mu_i)` on `P^1`, first cohomology vanishes exactly when
`mu_i<=3`. Positivity then proves `(CSB3)`.

Counting the summands and their degrees gives the first two equations in
`(CSB4)`. The kernel of `(2)` is `H^0(E(2))`, while rank-nullity and `(3)`
give

```text
dim ker(2)=3r-(m+3)=3r-(e+1).                     (5)
```

An `O(-1)` summand contributes two sections after twisting by two, an
`O(-2)` summand contributes one, and an `O(-3)` summand contributes none.
This proves the third equation in `(CSB4)`.

It remains to identify `J`. A section of `E(1)` is a linear syzygy among a
basis of the forms in `V`. Such a syzygy is equivalent to one
`h in S_(m-1)` for which `S_1h subset V`: in coordinates `U,V`, the pair
`Uh,Vh` gives the relation

```text
V(Uh)-U(Vh)=0,                                     (6)
```

and conversely coprimality of `U,V` recovers `h` from any linear syzygy.
Since the three center forms span `S_1`, this is exactly the space `J`.
Now

```text
h^0(E(1))=c_1,                                     (7)
```

which proves `(CSB5)`.

Solving `(CSB4)` gives `(CSB6)`; its bounds are precisely nonnegativity of
`c_2,c_3`. At the minimum rank, `(5)` equals two, so
`2c_1+c_2=2`. The two nonnegative solutions and the resulting values of
`c_3` are exactly `(CSB8)`. Finally the Gram router gives

```text
rank K_Gram<=dim J=c_1,
rank K_Gram>=max(0,2r-(n+2)),                      (8)
```

proving `(CSB9)` and the nonzero-Gram assertion. QED.
