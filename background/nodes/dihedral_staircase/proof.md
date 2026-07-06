# dihedral_staircase proof

Let `H` be the evaluation set, `|H| = n`, and let `C` be the degree `< k`
Reed-Solomon code on `H`. For a slope `z`, write `w_z = u + z v`.
An exact aligned `j`-support is a set `R subset H`, `|R| = j`, such that
`w_z` agrees with some codeword `c_R` on `S_R = H \\ R` and disagrees from
`c_R` on every point of `R`.

The proof does not use dihedrality; it bounds all exact aligned supports.

First fix a slope `z`. If `R_1` and `R_2` are both aligned at `z`, with
codewords `c_1` and `c_2`, then
`|S_{R_1} cap S_{R_2}| >= n - 2j`. The hypothesis `k + 3j <= n` implies
`n - 2j >= k`, so `c_1` and `c_2` agree on at least `k` evaluation points.
MDS uniqueness gives `c_1 = c_2`. The exact disagreement support of the
single word `w_z - c_1` is unique, hence `R_1 = R_2`. Thus every slope has at
most one exact aligned support.

If there is at most one support total, the result is immediate. Otherwise
choose two aligned supports `R_1, R_2` at distinct slopes `z_1 != z_2`, with
codewords `c_1, c_2`. On
`I = S_{R_1} cap S_{R_2}` we have
`u + z_1 v = c_1` and `u + z_2 v = c_2`. Since `|I| >= n - 2j >= k`, the
codewords

```text
U = (z_1 c_2 - z_2 c_1) / (z_1 - z_2),
V = (c_1 - c_2) / (z_1 - z_2)
```

are the unique codeword pair agreeing with `(u,v)` on `I`.

Now let `R` be any other exact aligned support at slope `z`, with codeword
`c`. On
`J = S_R cap S_{R_1} cap S_{R_2}` we have
`c = u + z v = U + z V`. The size bound
`|J| >= n - 3j >= k` follows exactly from `k + 3j <= n`. Hence MDS uniqueness
forces `c = U + z V`.

Therefore every aligned support is the exact nonzero support of

```text
e_u + z e_v, where e_u = u - U and e_v = v - V.
```

For each point `x in H`, the value `e_u(x) + z e_v(x)` is a linear function of
`z`. If both coefficients vanish, `x` is zero for all slopes. If `e_v(x) = 0`
and `e_u(x) != 0`, `x` is nonzero for all slopes. If `e_v(x) != 0`, the zero
condition occurs at exactly one slope. Thus the zero set, and hence the exact
nonzero support, can change only at the at most `n` exceptional slopes attached
to points of `H`; all other slopes give one common support.

So the number of distinct exact aligned supports is at most `n + 1`. The
dihedral supports are a subfamily, so they satisfy the same bound.

