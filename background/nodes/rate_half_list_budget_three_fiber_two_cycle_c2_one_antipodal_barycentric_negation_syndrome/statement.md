# Budget-three fiber-two c=2 one-antipodal barycentric negation syndrome

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder`

Retain `(CFL1)--(CFL8)` and define

```text
Phi(W)=product_(i=1)^4(W-w_i),
lambda_i=1/Phi'(w_i),
f(a)=lambda_i for a in A_i,       f(a)=0 for a in Omega,
u(a)=f(a)-f(-a).                                      (BNS1)
```

The outer scalars are distinct, so every `lambda_i` is nonzero.  Their exact
barycentric moments are

```text
sum_i lambda_i w_i^m=0,       0<=m<=2,
sum_i lambda_i w_i^3=1.                            (BNS2)
```

For the Fourier moments on `mu_N`, one has the sharp syndrome

```text
sum_(a in mu_N)u(a)a^j=0,       0<=j<3H,
sum_(a in mu_N)u(a)a^(3H)=-2H!=0.                 (BNS3)
```

In particular the invariant alternative in `(CFL10)` cannot occur in the
barycentric direction, and

```text
|supp u|>=3H+1=3R+4.                               (BNS4)
```

The equality case has an exact certificate.  If `|supp u|=3H+1` and

```text
Psi(T)=product_(a in supp u)(T-a),                  (BNS5)
```

then `Psi` is even and

```text
u(a)=-2H/Psi'(a),       a in supp u.                (BNS6)
```

Conversely `(BNS5)--(BNS6)` reproduce all moments in `(BNS3)` through the
first nonzero syndrome.  Thus the minimum-support alternative is reduced to
a derivative-weighted negation-stable support, while every other candidate
has strictly larger mismatch support.  This theorem does not classify those
supports or close the one-antipodal branch.
