# Budget-three fiber-two c=2 one-antipodal canonical-cell Fourier ladder

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_boundary_transfer`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_product_ratio_trace_compiler`

Retain a complete canonical candidate in the official one-antipodal chamber
and put

```text
N=2^40,       R=2^37,       H=R+1,       r=2H-3=2R-1,
Omega={1,-1,c,d},
E(z)=product_(a in Omega)(1-az),       Q=(1-z^N)/E.       (CFL1)
```

The canonical span and split outer quartic give distinct centered scalars
`w_1,...,w_4` and normalized polynomials `B,C` such that

```text
B(0)=C(0)=1,       deg B<=r,       deg C<=H-3,
sum_i w_i=0,
Q=product_(i=1)^4 G_i,
G_i=B+w_i z^H C.                                      (CFL2)
```

Every `G_i` has exact degree `r`, the four factors are pairwise coprime, and
there is a partition

```text
mu_N\Omega=A_1 disjoint_union ... disjoint_union A_4,
|A_i|=r,       G_i(z)=product_(a in A_i)(1-az).         (CFL3)
```

Write `p_(i,j)=sum_(a in A_i)a^j`.  The four cells have the exact flat
prefix

```text
p_(i,j)=-1/4 sum_(a in Omega)a^j,
1<=j<H.                                                (CFL4)
```

More generally, for `s in {0,1,2}` and scalars `lambda_i` satisfying

```text
sum_i lambda_i w_i^m=0,       0<=m<=s,                 (CFL5)
```

one has the longer annihilation ladder

```text
sum_i lambda_i p_(i,j)=0,
0<=j<(s+1)H,                                           (CFL6)
```

where `p_(i,0)=r`.  At the first endpoint,

```text
p_(i,H)=-1/4 sum_(a in Omega)a^H-Hw_i
       =-(c^H+d^H)/4-Hw_i.                            (CFL7)
```

There is also a field-exact negation consequence.  Extend the cell coloring
to `mu_N` by

```text
f_lambda(a)=lambda_i for a in A_i,
f_lambda(a)=0        for a in Omega,
u_lambda(a)=f_lambda(a)-f_lambda(-a).                 (CFL8)
```

If `(CFL5)` holds, then either `u_lambda=0` identically or

```text
|supp u_lambda|>=(s+1)H+1.                            (CFL9)
```

The support is negation-stable and hence even.  In particular,

```text
s=1:  u_lambda=0 or |supp u_lambda|>=2H+2=2R+4,
s=2:  u_lambda=0 or |supp u_lambda|>=3H+1=3R+4.       (CFL10)
```

Thus a complete one-antipodal candidate must produce either an exact
negation-invariant weighted coloring or a quantitatively large mismatch in
each nonzero moment-kernel direction.  This theorem does not classify those
colorings, prove the primary circuit empty, or prove the antipodal-free part
of `C2-PAR`.
