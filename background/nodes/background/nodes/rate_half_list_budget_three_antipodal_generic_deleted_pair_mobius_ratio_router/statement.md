# Budget-three antipodal generic deleted-pair Möbius ratio router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_mobius_weld`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_fourier_resultant_branch_collapse`

Retain a complete canonical survivor on the maximal generic deleted-pair
stratum in its only remaining arithmetic branch. Put

```text
N=8M=2^38,       q_field=p^2,       p=1 mod 4N.       (MRR1)
```

Let `iota in F_p` satisfy `iota^2=-1`. After relabeling the two deleted
antipodal pairs and applying common source scaling, their four square-root
lifts have the exact form

```text
(a_0,a_1,a_2,a_3)=(1,iota,r,iota r),
r^(4N)=1,       r^4=t,       r^4!=1.                  (MRR2)
```

The split outer quartic has roots `(alpha,-alpha,beta,-beta)`. Set

```text
q=(beta/alpha)^2=mu/lambda in mu_N.                   (MRR3)
```

In particular `q^N=1` and `q!=1`; swapping the two outer pairs replaces `q`
by `q^(-1)`.
The Möbius matching holds if and only if at least one of the following three
equations holds:

```text
r^2(1+q)^2
 =4q(r^2-r+1)^2,                                     (MRR4)

(r-1)^4(1+q)^2
 =4q(r+1)^4,                                         (MRR5)

(r^2+1)^2(1+q)^2
 =4q(r^2-4r+1)^2.                                    (MRR6)
```

Each equation is a reciprocal quadratic in `q`. Consequently a fixed lift
ratio `r` permits at most three unordered ratios `{q,q^(-1)}`, and only those
ratios lying in `mu_N` remain admissible. No permutation search over the four
lifts or four outer roots remains.

The equations retain the harmonic case `q=-1`. It can occur in `(MRR4)` only
when `r^2-r+1=0`, cannot occur in `(MRR5)` because `r^4!=1`, and can occur in
`(MRR6)` only when `r^2-4r+1=0`.

This theorem does not prove that any of `(MRR4)--(MRR6)` is incompatible with
the half-degree square-pencil factorization or the constant-forcing ODE.
