# Budget-three antipodal generic deleted-pair Fourier-resultant branch collapse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Put `N=8M=2^38` on the maximal generic deleted-pair floor. For any complete
survivor, label the inverse roots in the two cells of `(DEF3)` by `+1` and
`-1`, and label the two deleted roots `1,t` by zero. This gives

```text
S(X)=sum_(j=0)^(N-1)s_jX^j in Z[X],
s_j in {+1,-1,0},       |{j:s_j=0}|=2.               (FRC1)
```

The cells have equal size, and their flat prefix gives

```text
S(1)=0,       S(zeta^m)=0 in F_q,       1<=m<=N/4,  (FRC2)
```

for a primitive `N`th root `zeta`.

Let `p=char(F_q)`. If `p=1 mod N`, then every such packet satisfies

```text
p<4N^2.                                               (FRC3)
```

If `p=-1 mod N`, then every such packet satisfies

```text
p<2N.                                                 (FRC4)
```

Consequently the official prime-field branch and the official quadratic
branch with `p=-1 mod N` contain no complete deleted-pair survivor. The only
remaining field branch for `(DEF3)` is

```text
q=p^2,       p=1 mod N                                (FRC5)
```

and hence, by the official field collapse, `p=1 mod 2^40`, subject to the
budget interval. This theorem does not exclude that split quadratic branch or any
four-root stratum outside the deleted-pair sublocus.

Moreover, all quotient-pencil data in the remaining branch descend to the
prime field. In the notation of `(DEF3)`,

```text
t,B_0,C_0,H_lambda,H_mu,lambda,mu in F_p,             (FRC6)
```

both `-lambda` and `-mu` are squares in `F_p`, all four split outer parameters
lie in `F_p`, and the Möbius matching belongs to `PGL_2(F_p)`. Only the full
order-`2^41` evaluation domain may remain genuinely quadratic.
