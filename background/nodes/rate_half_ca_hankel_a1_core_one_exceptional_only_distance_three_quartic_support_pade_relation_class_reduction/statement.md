# `A=1` distance-three Pade relation-class reduction

- **status:** PROVED
- **closure:** proof plus exact official shadow certificate
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_error_pade_circuit_reduction`

Work over `K=F(U)`. For coprime polynomials `A,B in K[Z]`, not both zero,
with `max(deg A,deg B)<=t`, define the relation class

```text
H_[A:B]={gamma in Gamma:
 A(gamma)+B(gamma)q_gamma(U)=0 in K}.               (QPRC1)
```

Every identically singular Pade circuit `S`, of size `s=2(t+1)`, is
contained in one unique relation class. Conversely every `s`-subset of a
relation class is an identically singular circuit.

Distinct relation classes satisfy

```text
|H_R intersect H_R'|<=2t,                           (QPRC2)
```

and every class in an exact packet satisfies

```text
|H_R|<=e+t.                                         (QPRC3)
```

If the class sizes are `h_R`, the exact zero-circuit and shadow ledgers are

```text
D_t=sum_R binom(h_R,s),
sum_R binom(h_R,s-1)<=binom(3e,s-1).                (QPRC4)
```

Combining `(QPRC4)` with the official circuit lower bounds forces one class
of size at least

```text
172410       in the antipodal t=6 branch,
  2128       in the constant-product t=8 branch.    (QPRC5)
```

Thus a uniform relation-class bound of `172409` antipodally or `2127` for
constant product closes the corresponding degree-two branch. Equivalently,
the remaining task is to exclude a fixed factor of that size from

```text
I(Z)A(U,Z)+[U^2M_0(Z)-2UM_1(Z)+M_2(Z)]B(U,Z),       (QPRC6)
```

where `deg_Z A,deg_Z B<=t`. No official-scale enumeration of individual
circuits is needed.
