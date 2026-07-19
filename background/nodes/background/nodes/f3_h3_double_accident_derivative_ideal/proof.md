# Proof

Write `c_u=1-zeta^u` and `d_v=1-zeta^v`. The proved nonidentity quotient
uniqueness theorem says that the characteristic-zero values
`gamma_uv=d_v/c_u`, `(u,v) in I`, are pairwise distinct. Since

```text
eta_ij=c_u c_u' (gamma_i-gamma_j),
```

every `eta_ij`, and hence every `Delta_i`, is nonzero.

## Perfect-power norm and comparison

Every odd Galois dilation sends `J_i` to the corresponding `J_ri` and
`Delta_i` to `Delta_ri`; it therefore permutes the ideals `K_i`. The product
`K_n` is Galois invariant. Exactly as in the global derivative-ideal theorem,
every odd rational prime is unramified and its primes in `O` form one Galois
orbit. The odd exponent of each rational prime in `Norm(K_n)` is consequently
divisible by `d`, proving `(JD2)`.

By construction `J_i subset K_i`. Hence

```text
product_i J_i subset product_i K_i.
```

For integral ideals, reverse inclusion of quotient lattices gives
`Norm(K_n) | Norm(product_i J_i)`. Taking odd parts and using the two perfect
`d`th-power identities proves `f_n^d | e_n^d`, and therefore `(JD3)`.

For `(JD3a)`, define `Q_n` as in the statement. Every coefficient is an
algebraic integer and every odd Galois dilation permutes its linear factors,
so `Q_n` has rational algebraic-integer coefficients and hence lies in
`Z[T]`. Its roots are the pairwise-distinct `gamma_i`. Since

```text
eta_ij=c_u c_u' (gamma_i-gamma_j),
```

the ordinary discriminant formula gives

```text
Disc(Q_n)=product_(i<j) eta_ij^2,
product_i Delta_i=(-1)^(M(M-1)/2) Disc(Q_n).             (3a)
```

Both `product_i J_i` and the principal ideal
`(product_i Delta_i)^B_n O` are contained in `K_n`. Their ideal sum is
therefore contained in `K_n`. At every odd rational prime its norm valuation
is the minimum of the two norm valuations. Taking odd parts and using Galois
invariance gives

```text
f_n^d divides gcd(e_n^d,h_n^(d B_n)).
```

Comparing rational-prime valuations proves `(JD3a)`. Notice that this global
gcd can match a rich product target to a quotient collision at a different
target; the local sum ideals defining `f_n` retain strictly more information.

## Local double-accident valuation

Fix an official prime `p`, a generator `g` of the order-`n` subgroup, and the
degree-one prime

```text
mathfrak P=(p,zeta-g).
```

Let `i=(u,v)` reduce to the quotient target `t`, and write

```text
m=P(t),       r=R(t),       q=max(m-18,0).
```

Every `c_u` is a unit at this odd prime. Thus `eta_ij` is divisible by
`mathfrak P` exactly when `gamma_j` has the same reduction `t` as `gamma_i`.
There are `r-1` such indices, so

```text
v_mathfrakP(Delta_i)>=r-1,
v_mathfrakP(Delta_i)=0 iff r=1.                          (1)
```

The global derivative-ideal proof gives

```text
v_mathfrakP(J_i)>=q.                                     (2)
```

It also gives the load-bearing converse at level zero. If `m<=18`, the
`m`th Hasse derivative is among the generators of `J_i`; modulo
`mathfrak P`, its unique term deleting all `m` colliding roots is a unit and
every other term is divisible by `mathfrak P`. Hence

```text
v_mathfrakP(J_i)=0 iff q=0.                              (3)
```

Since ideal addition takes the minimum valuation,

```text
v_mathfrakP(K_i)
 =min(v_mathfrakP(J_i), B_n v_mathfrakP(Delta_i)).       (4)
```

The proved uniform product-fiber theorem applies because an official target
here is nonzero and nonidentity:

```text
P(t)<33n^(2/3).
```

Since `P(t)` is an integer,

```text
q=(P(t)-18)_+<=ceil(33n^(2/3))-19.
```

For nonzero `t`, the second product coordinate is determined by the first, so
`P(t)<=|A|=n-1` and `q<=n-19`. Hence `q<=B_n`. Equations `(1)--(4)` show:

- if `q=0` or `r=1`, then `v_mathfrakP(K_i)=0`;
- if `q>0` and `r>=2`, then `v_mathfrakP(K_i)>=q`.

There are exactly `r` quotient lifts above a target of quotient multiplicity
`r`. Summing over all `i` therefore gives

```text
v_mathfrakP(K_n)
 >= sum_(t!=1,r>=2) q r
 >= sum_(t!=1) q(r-1)
 =Y_18.                                                  (5)
```

Moreover `(4)` is positive for some `i` exactly when `Y_18>0`.

The product ideal is Galois invariant and `p` splits completely, so every
prime above `p` has the same valuation. Equation `(5)` yields

```text
p^(dY_18) divides F_n=f_n^d,
```

which proves `(JD4)`. The positivity equivalence proves `(JD5)`.

Finally `Y_18 log p<=log f_n`. Under `(JD6)` this gives
`17Y_18<=283n^2+34n-17`; the proved double-accident reduction then gives
`17X_18<=300n^2`. QED.
