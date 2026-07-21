# XR prize first-shell primitive rank-three exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_prize_primitive_rank_two_shell_band`

Consider a uniform high-core trade on the first residual shell

```text
|X|=a+3.                                             (P3E1)
```

If its trade rank is three, then its row space is the complete dual
`GRS_a` code on `X`, of dimension three. It has at least five active rows.
For each row put

```text
Z_i=X\supp(lambda_i).
```

The in-`X` zero sets have the exact graph form

```text
|Z_i| in {1,2};
the two-sets are distinct edges of a simple graph on X;
there is at most one singleton, and it is disjoint from every edge. (P3E2)
```

After the common GRS normalization, write

```text
lambda_i(x)=P_i(x)/Lambda'_X(x),       deg P_i<=2.
```

The polynomials `P_i` span `F[T]_<3` and satisfy the exact double check

```text
sum_i P_i=0,       sum_i gamma_i P_i=0.             (P3E3)
```

Let `I` count pairs of two-set zero fibers sharing a vertex. If the active
rows are all blocks of a minimal Maxwell core, their deficit obeys

```text
Delta_G>=6+t(h-t-1)+2I                 with no singleton,
Delta_G>=2+t(h-t+1)+2I                 with one singleton. (P3E4)
```

At the prize rates, the core-size caps are `t<=384,448,960`, while
`h=2^33+1,2^33+1,2^32+1`. Both lower bounds in `(P3E4)` are positive.
Thus no rank-three trade on `(P3E1)` can be supported on every block of a
minimal prize Maxwell core.

Trade rank one is impossible, rank two is excluded on `d=2` by the preceding
prize shell band, and rank cannot exceed `|X|-a=3`. Consequently:

```text
No primitive full-core trade of any rank exists on |X|=a+3
at any prize P-A row or affine kernel rank a.        (P3E5)
```

Proper local first-shell circuits remain possible. This theorem does not pay
their ownership or count, treat RowC primitive rank three, handle shell
`a+4` or higher, or promote the consumer.
