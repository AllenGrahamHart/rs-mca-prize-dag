# Proof

Write

```text
P=RS_{<11}={f in F[X]:deg f<11}.
```

Then `dim P=11`, while `V'` is a hyperplane of dimension ten. Let
`L_B` be the monic locator of `B`. The kernel of evaluation from `P` to
the nine coordinates in `B` is

```text
I_B=L_B*RS_{<2}=span{L_B,XL_B},       dim I_B=2.     (1)
```

Since `rank(ev_B|V')=8`, rank-nullity gives

```text
dim ker(ev_B|V')=10-8=2.
```

This kernel is contained in (1), so equality holds and `I_B<=V'`.

Choose a nonzero functional `lambda in P^*` with `V'=ker(lambda)`.
Because `lambda` vanishes on `I_B=ker(ev_B|P)`, it factors uniquely through
evaluation on `B`. Thus there are coefficients `mu_b`, not all zero, such
that

```text
lambda(f)=sum_(b in B) mu_b f(b).                  (2)
```

Let

```text
C_B={b in B:mu_b!=0},       c=|C_B|.
```

Suppose `c=1`, supported at `b in B`. Equation (2) would make `b` an
evaluation loop of `V'`: every normalized correction `R_gamma in V'`
would vanish at `b`. The fixed chart contains at least `2578110` distinct
record slopes. For each of them the rich coordinate equation at `b` becomes

```text
E_b(gamma)+q(gamma)R_gamma(b)=E_b(gamma)=0.
```

The polynomial `E_b(Z)` is affine in `Z`, so two distinct roots make it
identically zero. Then `E_b(gamma)+q(gamma)R_gamma(b)=0` for every residual
record, placing `b` in the complete residual common support. This
contradicts maximal shortening. Hence `2<=c<=9`.
Equation (2) also shows that every polynomial vanishing on `C_B` belongs
to `V'`. This proves

```text
L_(C_B)*RS_{<11-c}<=V'
```

and its displayed dimension.

## Every eleven-set has the same circuit

Fix distinct `x,y` outside `B` and put `T=B union {x,y}`. Evaluation

```text
ev_T:P -> F^T
```

is an isomorphism: a nonzero polynomial of degree at most ten cannot vanish
at eleven distinct points. Therefore `ev_T(V')` is a rank-ten hyperplane in
`F^T`. Its unique relation is precisely

```text
sum_(b in B) mu_b f(b)+0*f(x)+0*f(y)=0.            (3)
```

The support of (3) is the fixed set `C_B`, so it is the unique circuit of
the evaluation matroid on `T`; every element of `T minus C_B` is a coloop.
In particular, neither the circuit nor its size depends on the extension
pair `{x,y}`.

Let `S` be a nine-subset of `T`, obtained by omitting a pair `D`. If
`D` is disjoint from `C_B`, then `S` still contains the unique circuit and
has rank eight. If `D` meets `C_B`, the circuit is broken and all nine
remaining columns are independent, so `S` has rank nine. There are

```text
C(11-c,2)
```

omitted pairs disjoint from `C_B`. This proves both nine-shadow counts.
Likewise a ten-subset is a basis exactly when its omitted element lies in
`C_B`, giving exactly `c` bases.

## Sharpness of every circuit size

Fix any `c in {2,...,9}`, choose `c` points of `B`, and choose nonzero
weights on them. Define `lambda` by (2) with support equal to those points
and put `V'=ker(lambda)`. Then `dim V'=10`, `I_B<=V'`, and evaluation on
`B` has rank eight. The space has no evaluation loop: otherwise its hyperplane
would equal the kernel of one coordinate-evaluation functional, making
`lambda` proportional to that functional. Evaluation functionals at
most eleven distinct points are Vandermonde-independent, while `lambda`
has support at least two. This is impossible. Thus every printed value of
`c` satisfies the complete local linear-algebra hypotheses.

For the existing eight-petal fence,

```text
V'=span{1,X,...,X^7,L_B,XL_B}.
```

Its restriction to `B` is the length-nine, dimension-eight RS evaluation
space, whose unique dual relation has full support. It is the sharp `c=9`
endpoint: `B` is its only rank-eight shadow and the other 54 shadows have
rank nine.
