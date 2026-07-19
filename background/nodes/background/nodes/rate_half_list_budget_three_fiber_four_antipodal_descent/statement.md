# Budget-three fiber-four antipodal descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_fiber_four_rank_gate`

Work in the direct equal-complete-fiber linear `K_4` branch with fiber size
four. Write the block completion degree as `d=4s`, so the domain has size
`n=4d`, and put `Y=X^4`. Assume the rank-two deleted-root component is
antipodal:

```text
P_i(X)=X^2-a_i,       b_i=a_i^2,       0<=i<=3.          (F4A1)
```

Let `H_i(Y)` be the monic degree-`s` completed-block polynomials and

```text
A_i(X)=H_i(X^4)/P_i(X).                                  (F4A2)
```

The four `P_i` are pairwise coprime, the four `A_i` are pairwise coprime,
their roots together partition the subgroup domain, and the linear `K_4`
relation has all coefficients nonzero:

```text
product_i P_i product_i A_i=X^(4d)-1,
sum_i lambda_i A_i=0,       product_i lambda_i!=0.        (F4A3)
```

Then there are monic polynomials `G_i(Y)` of degree `s-1` such that

```text
H_i(Y)=(Y-b_i)G_i(Y),
A_i(X)=(X^2+a_i)G_i(X^4),                                (F4A4)

product_i H_i(Y)=Y^d-1,
product_i G_i(Y)=(Y^d-1)/product_i(Y-b_i),                (F4A5)

sum_i lambda_i G_i(Y)=0,
sum_i lambda_i a_i G_i(Y)=0.                             (F4A6)
```

The `b_i` are four distinct elements of the order-`d` subgroup, the `G_i`
are pairwise coprime, and, for `s>=2`,

```text
dim_F span {G_0,G_1,G_2,G_3}=2.                         (F4A7)
```

Conversely, data satisfying `(F4A1)` and `(F4A4)--(F4A6)` reconstruct the
antipodal locator relation and domain factorization in `(F4A2)--(F4A3)`.

At the prize maximum, `d=2^39` and `s=2^37`. Thus the known rank-two
component descends exactly to four degree-`2^37-1` pairwise-coprime members
of one base-field pencil whose product is the order-`2^39` subgroup
polynomial with four printed roots removed. This theorem identifies the
remaining census; it does not prove that the census is empty.
