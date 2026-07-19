# Proof

The evaluation map from `K_E` to any four coordinates `T` is an isomorphism.
Hence the kernel of restriction `C_E -> F^T` is one-dimensional. The word
`r_T=q-I_Tq` belongs to that kernel and has nonzero image in `C_E/K_E`, so it
spans the kernel. Since `c` agrees with `U` on `T`, the first assertion
follows.

Let `c'=c+lambda r_T` be another selected member on the line. Its quotient
class differs from that of `c`, so `lambda!=0`. The P-A intersection cap is
four, while both members agree on `T`; they therefore have no other common
agreement coordinate. In particular `r_T` is nonzero on `A\T`.

At any coordinate outside `T`, the residual of `c'` is

```text
U-c'=z-lambda r_T.
```

The member `c'` has at least `m` agreements, exactly the four in `T` shared
with `c`, and therefore at least `h=m-4` agreements in `E\A`. On each of
those coordinates, `r_T` is nonzero and

```text
z(x)/r_T(x)=lambda.
```

Different line members have different quotient classes and hence different
values of `lambda`; their ratio fibers are disjoint. Thus a line containing
`r` selected members supplies at least `r-1` distinct fibers, each of size at
least `h`.

It remains to identify the minor. Form the `6 x |E|` matrix `M` whose rows
are the words

```text
1, x, x^2, x^3, q, U.
```

Replacing the `q` row by `r_T` subtracts a combination of the first four
rows. Replacing the `U` row by `z=U-c` subtracts a combination of those rows
and the `q` row. Neither operation changes a maximal minor. For the columns
`T union {x,y}`, the last two transformed rows vanish on `T`, so block
elimination gives

```text
det M[T,x,y]
 = det V_T (r_T(x) z(y)-r_T(y) z(x)),
```

where `V_T` is the nonzero four-by-four Vandermonde matrix on `T`. Hence the
minor vanishes exactly when the two ratios agree, provided the displayed
denominators are nonzero.

Each heavy fiber contributes `C(h,2)` distinct pairs `{x,y}`. Pairs from
different fibers or different four-sets `T` give different records. Applying
the rich-line hierarchy therefore gives `d_r(r-1)C(h,2)` records per retained
member. Exact substitution and maximization over the line threshold produce
the table.
