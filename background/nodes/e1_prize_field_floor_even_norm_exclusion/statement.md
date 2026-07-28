# E1 prize-field-floor even-norm exclusion

- **status:** PROVED
- **closure:** proof plus exact arithmetic
- **scope:** the three prize-envelope clean anchors
- **dependencies:** `e1_pair_feasible_prime_field_reduction`,
  `e1_collision_square_mass_reparametrization`,
  `e1_prime_field_l2_norm_collision_radius`

Let `p` be the prime field characteristic on a pair-feasible prize-envelope
clean anchor. Its exact budget interval has lower endpoint

```text
p_min=B_P 2^128,
B_P=317494674775468773183020924238786383963 > 2^127.
```

Every nonzero folded E1 class difference has even absolute cyclotomic norm.
Consequently no such difference can collide modulo `p` in either range

```text
N=256 and S<=16,
N=512 and S<=4.
```

Indeed, in both cases the L2 norm theorem gives

```text
0<R=|Norm(alpha)|<=2^256<2p.
```

If `p|R`, then `R=p`, contradicting that `R` is even and `p` is odd.

Thus the first norm-unresolved square-mass profiles on prize rows are sharpened
to `S>=18` at `N=256` and `S>=6` at `N=512`. The RowC rows retain their
previous floors `S>=16` and `S>=4`; this theorem makes no claim about them.
