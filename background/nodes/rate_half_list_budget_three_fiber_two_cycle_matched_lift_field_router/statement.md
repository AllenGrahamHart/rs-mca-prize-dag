# Budget-three fiber-two matched-cycle lift field router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_boundary_transfer`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Retain a complete survivor on the matched `c=0`, generic, two-antipodal-pair
boundary of the fiber-two cycle router. Put

```text
M=2^36,       N=8M=2^39,       2N=2^40,       4N=2^41.       (CLF1)
```

The flat signed root coloring from the even factorization has a nonzero
primitive cyclotomic resultant. For `p=char(F_q)`, it gives the
parameter-uniform bounds

```text
p= 1 mod N  ==>  p<4N^2,
p=-1 mod N  ==>  p<2N.                              (CLF2)
```

Together with the maximal-row field collapse and the official budget
interval, these bounds leave exactly

```text
q_field=p^2,       p=1 mod 2N.                       (CLF3)
```

All quotient-pencil coefficients and outer roots already descend under the
weaker congruence `(CLF3)`. In the notation of the even factorization,

```text
t,B_0,C_0,H_lambda,H_mu,lambda,mu in F_p,             (CLF4)
```

both `-lambda` and `-mu` are squares in `F_p`, and

```text
q_out=mu/lambda in mu_N\{1}.                          (CLF5)
```

Normalize the four source completion roots as

```text
(1,iota,r,iota r),       iota^2=-1,
r^(4N)=1,       r^4=t!=1.                             (CLF6)
```

The completion-root Mobius matching is equivalent to at least one of

```text
r^2(1+q_out)^2
 =4q_out(r^2-r+1)^2,                                  (CLF7)

(r-1)^4(1+q_out)^2
 =4q_out(r+1)^4,                                      (CLF8)

(r^2+1)^2(1+q_out)^2
 =4q_out(r^2-4r+1)^2.                                 (CLF9)
```

There are two congruence shards modulo `4N`. If `p=1 mod 4N`, every source
lift is already in `F_p`. If

```text
p=1+2N mod 4N,                                        (CLF10)
```

then `eta=r^(2N)` is in `{+1,-1}` and `r^p=eta r`. The anti-invariant case
`eta=-1` is incompatible with each of `(CLF7)--(CLF9)`. Hence every surviving
matched source lift lies in `F_p` in both congruence shards, and the matching
lies in `PGL_2(F_p)`.

This theorem removes the extra quadratic top-lift shard at `M=2^36`. It does
not exclude the matched cycle boundary, transfer the later scalar/Jacobi/norm
routers, treat `c=1,2`, or authorize the deferred computation.
