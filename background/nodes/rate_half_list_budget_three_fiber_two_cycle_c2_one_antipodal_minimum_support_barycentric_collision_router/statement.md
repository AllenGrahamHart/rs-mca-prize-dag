# Budget-three fiber-two c=2 one-antipodal minimum-support barycentric collision router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_support_polynomial_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`

Retain a complete canonical one-antipodal candidate and the notation of the
support-polynomial compiler.  Put

```text
Phi(T)=product_i(T-w_i)=T^4+alpha T^2-beta T+gamma,
lambda_i=1/Phi'(w_i),
O(W)=product_i(W+w_i)=W^4+alpha W^2+beta W+gamma.     (BCR1)
```

If the barycentric negation mismatch has its minimum possible support
`3H+1`, then exactly one pair of barycentric weights is equal.  For that
pair, put `s=w_i+w_j`.  Then `alpha s!=0` and

```text
s^3=-beta,
4gamma-alpha^2=2alpha s^2,                           (BCR2)
```

and hence the outer coefficients obey the codimension-one collision gate

```text
(4gamma-alpha^2)^3=8alpha^3 beta^2.                  (BCR3)
```

More precisely, the derivative collision gives the split normal form

```text
Phi(T)=(T^2-sT+s^2+alpha/2)(T^2+sT+alpha/2),
O(W)=(W^2+sW+s^2+alpha/2)(W^2-sW+alpha/2).           (BCR4)
```

Put `y=s^2/alpha`, and retain the selected completion-pair trace
`z_t=(1+t)^2/t`.  The outer invariants and completion coupling reduce to

```text
I=2alpha^2(3y+2),
J=-alpha^3(3y-4)(3y+2)^2,
32z_t(z_t-36)^2
 =(3y-4)^2(3y+2)(z_t+12)^3.                         (BCR5)
```

Thus a minimum-support survivor cannot have four distinct barycentric
weights or any triple, two-pair, or fourfold weight collision.  It lies on
the exact one-pair normal form `(BCR4)` and the normalized curve `(BCR5)`.
The theorem does not exclude that pair-collision locus or any larger-support
case.
