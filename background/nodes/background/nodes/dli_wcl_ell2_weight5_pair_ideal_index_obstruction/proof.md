# Proof

The pair-quadratic router gives the final product as `B=C/v`. Its two
membership equations are

```text
B^M=1, D_M(v,B)=2.
```

The legal-pair guards make `u` nonzero. If `v=0`, then `u=-1` and
`C=u(v-A)=A` is nonzero, so the first cleared equation below cannot vanish.
Thus no genuine or cleared solution is lost by multiplying by powers of
`v`.

The first membership equation clears to

```text
F=C^M-v^M=0.
```

For the second, the Dickson identity

```text
D_(2m)(v,B)=D_m(v,B)^2-2B^m
```

gives, after multiplication by `v^(2m)`,

```text
E_(2m)=E_m^2-2C^m v^m.
```

This is exactly the stated division-free recurrence, and `D_M=2` clears to
`G=E_M-2v^M=0`.

Now let a split prime row evaluate `zeta_M` at an exact order-`M` element
`omega` in `F_q`. If the fixed pair supports a router solution, evaluation at
`omega` kills both `F` and `G`. Hence the ideal

```text
J=F O_M+G O_M
```

lies in the kernel of the surjective ring map `O_M -> F_q`. Therefore
`O_M/J` has a quotient of cardinality `q`. If `J` has finite index, Lagrange's
theorem gives `q | [O_M:J]`.

The columns of the block multiplication matrix `L_(i,j)` are precisely the
coordinates of generators of `J` as an additive lattice. Full rational row
rank is equivalent to finite index. The Smith normal form, or equivalently
the determinantal-divisor theorem, identifies that index with the gcd of the
maximal minors. This proves the divisibility obstruction.

Finally, an odd dilation `zeta_M -> zeta_M^a` is an automorphism of `O_M`.
It carries the pair ideal for `(i,j)` isomorphically to the pair ideal for
`(ai,aj)` and preserves additive index. One representative per odd-dilation
orbit therefore suffices.

For context only, the Modal route probe computes every pair orbit through
`M=128`. The exact orbit counts are `14,36,82,176`; all 308 Smith indices
factor over just 12 primes, with maximum `v_2(p-1)=8`. Integer Smith form is
not the production algorithm: sampled `M=256` workers reached the 600-second
bound. These measurements select the ideal route but prove no `M=1024`
exclusion.
