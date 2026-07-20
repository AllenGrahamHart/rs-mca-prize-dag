# `A=1` exceptional-only quotient Forney-numerator normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_gap`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation`

Retain the exceptional-only face. Normalize the exceptional locator to be
monic and write

```text
A(X)=Q(0;X),       deg A=r-1,
q(z)=u+zq_1+O(z^2).                                  (QFN1)
```

Choose a minimal quotient support `T` of size `h=delta_A(h_1)` and put

```text
B_T(X)=product_(t in T)(X-t).
```

Use the unique source representations

```text
h_0=sum_(a in R_A) beta_a c(a),       beta_a!=0,
h_1=sum_(a in R_A) alpha_a c(a)+sum_(t in T) omega_t c(t),
                                             omega_t!=0.   (QFN2)
```

There is a unique polynomial `F` such that

```text
deg F=h-3,       lc(F)=Theta_2,       gcd(F,AB_T)=1, (QFN3)

omega_t=F(t)/(A(t)^2 B_T'(t))              (t in T), (QFN4)

F(a)=beta_a q_1(a) A'(a)B_T(a)          (a in R_A). (QFN5)
```

Equivalently, the quotient syndrome

```text
s_j=sum_(t in T)omega_t A(t)t^j
```

satisfies the exact key equation

```text
s_j=-sum_(a in R_A)beta_a q_1(a)a^j,       0<=j<=r, (QFN6)

s_(r+1)+sum_(a in R_A)beta_a q_1(a)a^(r+1)=Theta_2. (QFN7)
```

For `h=3`, `F=Theta_2` and `(QFN4)` is exactly the existing barycentric
triple formula. For general `h`, this theorem removes all source weights as
independent variables. The full coprimality in `(QFN3)` uses exact row
saturation: every exceptional root is simple in the parameter direction, so
`q_1(a)!=0` on `R_A`. The theorem does not classify the support polynomial
`B_T` or exclude the surviving high-distance interval.
