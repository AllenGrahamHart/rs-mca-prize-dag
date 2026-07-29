# L1 Mersenne HNF m=8 order-one cubic three-color remainder router

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion`,
  `l1_mersenne_hnf_m8_order_one_conic_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** cubic colored interpolants using exactly three colors on the
  four official `(m,h)=(8,7)` rows

Fix a primitive eighth root `omega`. Up to simultaneous multiplication of
all colors by a power of `omega`, every unordered three-color set has one of
the seven exponent representatives

```text
{0,1,2}, {0,1,3}, {0,1,4}, {0,1,5},
{0,1,6}, {0,2,4}, {0,2,5}.                          (TCR1)
```

For one representative `T`, define

```text
Q_T(X)=product_(j in T)(X-omega^j).                  (TCR2)
```

Let `L_(r,d)` be the monic degree-six reduced h=7 HNF polynomial, and write

```text
E(W)=e_3W^3+e_2W^2+e_1W+e_0,       e_3!=0.          (TCR3)
```

Every packet in scope lies on one of the seven bounded systems

```text
35d^2r^2+14d(11d^2+27d+27)r
 +120(d^4+4d^3+7d^2+6d+3)=0,

rem_(L_(r,d)) Q_T(E(W))=0,
Res_W(L_(r,d),E(W)-omega^j)=0       for j in T.      (TCR4)
```

The remainder equation means its six coefficients vanish. The exact
profiles are only `3+2+1` and `2+2+2`; they can be separated by the gcd
degrees of `L` and the three fibers `E-omega^j`. For an official row adjoin

```text
d^(p+1)=zeta,       zeta in mu_8,                    (TCR5)
```

and saturate by the inherited nonzero factors, `e_3`, and the next
subresultants fixing the requested profile. A unit saturation of all seven
color orbits and both profiles closes the complete three-color cubic
chamber.

No unit verdict, cyclotomic converse, inner lift, four-or-more-color cubic
packet, or higher color degree is asserted here.
