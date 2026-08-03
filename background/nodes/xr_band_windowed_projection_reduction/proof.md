# Proof

Fix a depth-`d` pair `P=(f,g)`. At a coordinate outside `Z_P`, the two
errors

```text
e_i  = u_i-f(x_i),       e'_i = v_i-g(x_i)
```

are not both zero because `Z_P` is the full joint-agreement set. The
projected error is `e_i+z e'_i` at a finite slope and is `e'_i` at
infinity. Every nonzero vector `(e_i,e'_i)` therefore vanishes at
exactly one point of `P^1(F_q)`. If

```text
m_P(z) = a_P(z)-(k+d),
```

then double counting the non-core coordinates gives

```text
sum_z m_P(z) = n-k-d.                                      (1)
```

An over-agreeing member has `a_P(z)>=A-1`, hence
`m_P(z)>=h-d-1`. Since `d<=h-2`, this threshold is positive, and (1)
implies

```text
|{z:a_P(z)>=A-1}| <= floor((n-k-d)/(h-d-1)) = beta_d.      (2)
```

Now fix `z`. The map `P -> pi_z(P)` is injective on depth-`d` pairs
when `2d>=h`. Indeed, if distinct pairs `P,P'` had the same projected
codeword `c`, their cores would both lie in the agreement set of `c`
with `w_z`, whose size is at most `A` by the tangent gate. Banked
`k`-packing gives `|Z_P intersect Z_P'|<=k-1`, and hence

```text
|Z_P union Z_P'| >= 2(k+d)-(k-1) = k+2d+1 > k+h=A,
```

a contradiction. This also covers `z=infinity`.

Let `b_d(z)` count the depth-`d` pairs over-agreeing at `z`. Every
other pair projects injectively to a codeword counted by `W_d(z)`, so

```text
N_d^raw <= W_d(z)+b_d(z).                                  (3)
```

Summing (3) over the `q+1` pencil members and using (2) pair by pair
gives

```text
(q+1)N_d^raw <= sum_z W_d(z)+sum_z b_d(z)
               <= sum_z W_d(z)+beta_d N_d^raw.
```

Rearranging proves `(WPR')`; positivity follows from
`beta_d<=n-k-d<n<=q`. Division proves `(WPR)`, and `(W17)` gives the
stated `17n^2/25` corollary. The selected occupancy is a subfamily of
the raw one. QED.

The six-row arithmetic and the structured/coset spectral exclusion are
separate inputs. The latter is already proved in
`xr_mc_depth_quantization`; it does not turn `(W17)` into a theorem for
arbitrary received words.
