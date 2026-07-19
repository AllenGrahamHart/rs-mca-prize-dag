# Budget-three multideletion multifiber exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_multifiber_vandermonde_exclusion`

Let `F` be a field. Fix `s,m>=1`. For `i=1,...,t`, let

```text
B_i(X)=product_(c in C_i)(X^m-c),       |C_i|=s,       (MME1)
```

and let `R_i` be a nonempty set of `ell_i` roots of `B_i`. Assume the sets
`R_i` are pairwise disjoint and all their elements are nonzero. Put

```text
P_i(X)=product_(r in R_i)(X-r),
A_i(X)=B_i(X)/P_i(X),
ell_0=min_i ell_i,       L=sum_i ell_i.                (MME2)
```

If

```text
m>L-ell_0,                                            (MME3)
```

then

```text
A_1,...,A_t are linearly independent over F.          (MME4)
```

For the nine linear budget-three chambers, the exceptional-root profiles in
their required constant relations give:

```text
chamber                         (ell_i)          sufficient m
4-cycle                         (1,1,1,1)             4
path tight triangle             (1,1,1)               3
linear K_4-e                    (2,2,1,1)             6
K_4                             (2,2,2,2)             7
triangle plus singleton         (1,1,1,2)             5.       (MME5)
```

Consequently, at the prize-max `d=2^39`, every direct construction in which
the completed size-`d` blocks are equal unions of fibers of one monomial
quotient map is excluded in all nine linear chambers whenever the
power-of-two fiber size satisfies

```text
m>=8.                                                     (MME6)
```

Together with the one-root theorem, cycle/path chambers are already excluded
for `m>=4`. The unresolved direct equal-fiber sizes are therefore `1,2` for
cycle/path and `1,2,4` for the other three linear chambers. Mixed quotient
maps, partial fibers, primitive locators, and all four quadratic-scroll
chambers remain outside this theorem.
