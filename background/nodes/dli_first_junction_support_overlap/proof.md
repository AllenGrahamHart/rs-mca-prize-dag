# Proof

Write a level-zero subset vector in antipodal pairs as
`(a_i,b_i)`, where `a_i,b_i` are in `{0,1}` and the second coordinate is at
`i+h`. Since `zeta^h=-1`, set

```text
e_i=a_i+b_i,             o_i=a_i-b_i.
```

The even moment `2r` is `sum_i e_i y_i^r`; the odd moment `2r+1` is
`sum_i o_i x_i y_i^r`. The moments `1,...,2L` therefore split into the
even equations `1<=r<=L` and the odd equations `0<=r<L`.

Let `S` be the indices at which exactly one member of the antipodal pair is
selected. Equivalently, `e_i=1` and `o_i` is nonzero exactly on `S`. Once
`S` is fixed, an admissible even vector and an admissible odd vector recover
`a_i=(e_i+o_i)/2` and `b_i=(e_i-o_i)/2` uniquely. This proves the first
identity in (1). At `S=emptyset`, the odd vector is uniquely zero and the
even vector has entries in `{0,2}`; division by two is precisely the first
saturated-column census. Hence `C_1=E_emptyset`.

At level one, an entry `e_i` has weight `binom(2,e_i)`. Its weight is two
exactly on `S`, giving `Z_1=sum_S 2^|S|E_S`. At junction zero, an entry
`o_i` has weight `binom(2,1+o_i)`. Its weight is two exactly off `S`, giving
`B_0=sum_S 2^(h-|S|)O_S`. Thus `p` and `q` sum to one.

First-owner deletion removes exactly the antipodally invariant vectors,
which are the `S=emptyset` term. Also

```text
(2^|S|E_S)(2^(h-|S|)O_S)=2^h E_SO_S.
```

Substitution into the primitive first-junction ratio proves (2). Multiplying
(2) by the displayed `K_tail` cancels `Z_1` and gives

```text
2^(nm)(Z_0-C_1)/(Z_m product_(0<=j<m) B_j),
```

which is the proved primitive telescoping formula, so (3) follows.

For (4), the complete sum of the `h`-th roots is zero in every degree
`1<=r<h`. For an even vector counted by `E_S`, put `epsilon_i=e_i-1`.
It vanishes on `S`, is a sign on `S^c`, and

```text
sum_i e_i y_i^r = sum_i epsilon_i y_i^r + sum_i y_i^r
                 = sum_i epsilon_i y_i^r.
```

This is a bijection and proves (4).

Finally, on a nonempty `S` of size at most `L`, the odd constraint matrix is
the Vandermonde matrix `(y_i^r)` for `0<=r<L`, followed by nonzero column
scalings `x_i`. It has full column rank, so it has no all-nonzero sign vector
in its kernel. The same argument applied to `(y_i^r)` for `1<=r<=L`, with
nonzero column scalings `y_i`, proves the claim for a nonempty `S^c` of size
at most `L`. This establishes (5), including why the empty-support cases
must be excluded.

