# KoalaBear c2 (1,1,2) near positive projective-boundary exclusion

- **status:** PROVED
- **scope:** the positive-sign near-aligned homogeneous endpoint boundary
- **requires:**
  `rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair` and
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate`
- **consumer:** `rate_half_band_closure` (evidence edge)

Normalize the common internal endpoint to `a=2` and orient the boundary as

```text
eta=infinity,       ell=d,       w=tau(eta)=0,
q_hom=Y(T-dY),      Omega={xi,d}.
```

The three relative `xi` orbits have representatives `2`, `1/2`, and `b` in
`J_0={2,1/2,b,1/b}`. The repaired positive odd vector and internal label are

```text
V(T,W)=(-d,1+W,-dW),       z=(d-2)/(2-4d).
```

The two equations `U(T,0) in <q_hom>` and the three internal-star equations
determine `U` uniquely in each internal template. The projective q-slice is
the product of the residual at `T=d` and the residual at `T=infinity`, the
latter being the `T^4` coefficient of `U^2-WV^2`.

All seven exhaustive deployed-field saturations are unit:

```text
fixed-moving:  xi=2, 1/2, b                         (3)
moving-moving: xi=2, 1/2 after s=b+1/b descent      (2)
moving-moving: xi=b, two constant-ratio signs       (2).
```

Thus no positive near-aligned projective-boundary form passes the necessary
q-slice identity. Together with the 18 affine-positive chart deletions and
the near-negative theorem, the complete near-aligned source-line branch is
empty.

This does not delete the aligned positive unramified branch, perform later
packet/source-row assembly, or close the rate-half target.
