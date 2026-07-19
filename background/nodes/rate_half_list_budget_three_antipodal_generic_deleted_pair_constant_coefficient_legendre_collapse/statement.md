# Budget-three antipodal generic deleted-pair constant-coefficient Legendre collapse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_fourth_root_gap_reduction`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate`

Retain the official nonharmonic deleted-pair normalization and put

```text
E(z)=(1-z)(1-tz),       F(z)=E(z)^(-1/4),
m=2M-1,       a=4M-1,       H_n(t)=[z^n]E(z)^(-1/2). (LCC1)
```

The fourth root is the formal series with constant term one. The constant
coefficient `sigma=S(0)` from `(CCG2)` has the exact closed coefficient form

```text
sigma=2H_a(t),       a=4M-1.                         (LCC2)
```

In particular, no Euclidean division or truncated quotient is needed to
evaluate this gate. If

```text
c_j=binom(2j,j)/4^j,
```

then

```text
H_n(t)=sum_(j=0)^n c_j c_(n-j)t^j,                  (LCC3)
H_0=1,       H_1=(1+t)/2,
2(n+1)H_(n+1)=(2n+1)(1+t)H_n-2ntH_(n-1).           (LCC4)
```

Equivalently, for `t=r^4` and the ordinary Legendre polynomial `P_n`,

```text
H_n(r^4)=r^(2n)P_n((r^2+r^(-2))/2).                 (LCC5)
```

Writing `H=H_(4M-1)(t)` and `chi=r+r^(-1)`, the three necessary scalar gates
become

```text
j=0:       t H^2+(chi-1)^2=0,
j=1:       t(chi-2)^2H^2+(chi+2)^2=0,
j=2:       t chi^2H^2+(chi-4)^2=0.                  (LCC6)
```

This theorem does not prove uniform failure of `(LCC6)`. The width-two
recurrence in `(LCC4)` is a mathematical compression, but direct iteration to
the official index `4M-1=2^37-1` is not claimed to be an acceptable
official-scale algorithm.
