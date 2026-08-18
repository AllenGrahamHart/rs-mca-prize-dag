# Proof

At level `j`, split the level array into antipodal pairs. For a frequency
`r`, the second member contributes the factor

```text
zeta_j^(r h_j/2)=(-1)^r.
```

Thus every even frequency of `M_j` is the corresponding frequency of
`M_(j+1)`, while every odd frequency is the corresponding frequency of
`D_j`. The frequency range `1,...,t/2^j` therefore splits into the odd set
in `(H1)` and the rescaled complete range `1,...,t/2^(j+1)` at the next
level. Iterating this identity leaves the one terminal frequency in `(H2)`
and proves `(H3)`.

Each `M_(j,i)` is the sum of `2^j` disjoint original bits. For distinct
`i`, these blocks are disjoint. Hence `D_(j,i)` is the difference of two
independent `Binomial(2^j,1/2)` variables. The number of binary assignments
giving the value `d` is, by Vandermonde,

```text
sum_a binom(2^j,a) binom(2^j,a-d)
  = binom(2^(j+1),2^j+d).
```

These are exactly the `U`-induced skew weights defining `B_j`, and the total
binary sample space has size `2^n`. Therefore `P(O_j)=B_j/2^n`.

At the terminal level, each `M_(m,i)` is the sum of `t` disjoint bits and has
weight `binom(t,M_(m,i))`. Those are exactly the level-`m` weights defining
`Z_m`, which proves the second identity in `(H4)`.

By `(H3)`, the full joint event has cardinality `Z_0`. A binary vector in
that event is nonprimitive exactly when it is invariant under the first
antipodal shift. Dividing each equal pair by its common bit identifies those
vectors with the `(n/2,t/2)` subset census, of cardinality `C_1`. This proves
`(H5)`.

Finally, the denominator in `(H6)` is

```text
Z_m product_j B_j / 2^(n(m+1)),
```

while its numerator is `(Z_0-C_1)/2^n`. Their quotient is the displayed
primitive telescoping ratio. Rearranging gives `(H7)` without asserting it.

