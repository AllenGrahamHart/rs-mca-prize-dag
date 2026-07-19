# Budget-three antipodal generic canonical-span criterion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction`

Work on the maximal official generic floor and retain

```text
d=2^39,       s=2^37,       r=s-1,
h=s/2+1,      v=h-3,
E(z)=product_(i=0)^3(1-b_i z),       b_i^d=1.          (CSC1)
```

Let `A=E^(-1/4)=sum a_mz^m` and

```text
B=sum_(m=0)^r a_mz^m,
Q=(1-z^d)/E,
R=Q-B^4.                                               (CSC2)
```

The primary generic gap is equivalent to `ord_0 R=2h`. Put

```text
Rbar=z^(-2h)R,       alpha=Rbar(0),
P=(Rbar/(alpha B^2))^(1/2) mod z^h,       P(0)=1.      (CSC3)
```

Then `alpha!=0`. The secondary gap says that the coefficients of `P` in
degrees `h-2,h-1` vanish. Define the canonical polynomial

```text
Cbar=sum_(m=0)^(h-3) [z^m]P z^m                         (CSC4)
```

and

```text
S=Rbar-alpha B^2 Cbar^2,
X=z^h B Cbar^3,
Y=z^(2h) Cbar^4.                                      (CSC5)
```

Every valid generic floor-boundary solution satisfies the exact canonical
span identity

```text
S=beta X+gamma Y.                                      (CSC6)
```

The scalars are unique and are read without solving a linear system:

```text
beta=[z^h]S,
gamma=[z^(2h)](S-beta X).                              (CSC7)
```

Moreover

```text
W^4+alpha W^2+beta W+gamma=product_i(W+w_i),           (CSC8)
```

where the four distinct `w_i` are one fractional-linear image of square-root
lifts `a_i` satisfying `a_i^2=b_i`.

Conversely, if four distinct order-`d` roots satisfy the primary and secondary
gaps, `(CSC6)`, and the split/Möbius condition `(CSC8)`, then reversing `B`
and `Cbar` reconstructs the generic antipodal quotient-pencil solution.

The certifier is covariant under common subgroup scaling. If `b_i` is
replaced by `lambda b_i` with `lambda^d=1`, then

```text
E_lambda(z)=E(lambda z),       B_lambda(z)=B(lambda z),
Rbar_lambda(z)=lambda^(2h)Rbar(lambda z),
Cbar_lambda(z)=Cbar(lambda z),
(alpha,beta,gamma)_lambda
 =(lambda^(2h)alpha,lambda^(3h)beta,lambda^(4h)gamma). (CSC9)
```

Thus all accept/reject conditions are preserved, and one `b_i` may be
normalized to one. Permuting the four matched pairs is also redundant.

Thus this boundary has an exact certifier depending only on four subgroup
roots, their square-root lifts, and polynomial/series operations. There are no
free official-degree polynomial or outer-coefficient variables. This theorem
does not prove that the certifier always rejects.
