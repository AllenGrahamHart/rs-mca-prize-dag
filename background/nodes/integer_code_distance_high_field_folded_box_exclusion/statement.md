# Integer-code high-field folded-box exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `integer_code_distance_cert`

Let `p` be an odd prime with `p=1 mod 128`, and let `zeta in F_p` have
exact order `128`. For

```text
K_p={v in Z^128 : sum_(j=0)^127 v_j zeta^j=0 mod p},
```

suppose

```text
p>253^32.                                             (HFB1)
```

Then every ternary vector in `K_p` is an antipodal cyclotomic relation:

```text
K_p intersect {-1,0,1}^128
  ={v in {-1,0,1}^128 : v_i=v_(i+64), 0<=i<64}.      (HFB2)
```

Thus the complete folded box has no nonzero non-cyclotomic kernel vector,
with no support restriction. This pays the order-128 high-characteristic
branch of `integer_code_distance_cert`.

The theorem makes no assertion for `p<=253^32`, for quotient orders other
than `128`, or for the separate requirement that a certified value-set cell
have cardinality above its row budget.
