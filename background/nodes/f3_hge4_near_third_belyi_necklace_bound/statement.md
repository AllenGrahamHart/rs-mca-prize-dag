# HGE4 near-third Belyi necklace bound

- **status:** PROVED
- **consumers:** `f3_hge4_near_third_dual_gap_exclusion`,
  `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_complement_separator_defect_normal_form`,
  `tame_central_star_belyi_necklace_bound`

Let `m=3h+e` be dyadic with `0<e<h`, and work over a field containing
`mu_m` whose characteristic is zero or greater than `4h+e`. For a primitive
ordered non-full exact-level pair, retain the notation

```text
Q=P+d,       PQR=X^m-1,
G=B-A,       deg G=e,
m(P+Q-PQG)=d^2XP'R.
```

Put

```text
U=y^hP(1/y),       V=y^hQ(1/y),       S=(U+V)/2,
gamma=y^eG(1/y)/d^2=sum_(j=0)^e gamma_jy^j,
Z=sum_(j=0)^e [-3m gamma_j/(3h+j)]y^j,
c=h+e.
```

Then `Z(0)=S(0)=1`, `deg Z=e`, `deg S=h`, and

```text
S=Z^(-1/3) mod y^c.                                (NTB1)
```

Consequently

```text
Phi=ZS^3,       Phi-1=y^cT,       deg T=2h,         (NTB2)
```

has the tame central-star passport

```text
0: 3^h 1^e,       1: c 1^(2h),       infinity: m.  (NTB3)
```

If

```text
N(c,e)=(1/c) sum_(r|gcd(c,e)) phi(r) binom(c/r,e/r),
```

then the number of primitive ordered scaling orbits satisfies

```text
E_h^prim(m,p)<=2N(h+e,e).                          (NTB4)
```

In particular,

```text
e=1: E_h^prim(m,p)<=2,
e=2: E_h^prim(m,p)<=h+2=(m+4)/3.                  (NTB5)
```

Besides sharpening both boundary debits, `(NTB4)` pays the following five
additional official exact-level cells against the `(21/2)m^2` allowance:

```text
(m,h,e)       orbit debit
(32,9,5)            286
(64,20,4)           892
(128,41,5)        59598
(256,84,4)        53020
(1024,340,4)    3333532.                           (NTB6)
```

The necklace bound is not claimed to pay every `0<e<h` cell, any `e>=h`
cell, or the complete exact-level aggregate.
