# H3 low-distance exceptional-prime router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependency:** `f3_h3_rich_fiber_norm_cutoff`

Let `n=2^s`, let `zeta=zeta_n`, and let `U_n` be the unordered pairs with
repetition `E={i,j}`, where `1<=i,j<n`. Put

```text
beta_E=(1-zeta^i)(1-zeta^j),
v_E=epsilon(i+j)e_bar(i+j)-epsilon(i)e_bar(i)-epsilon(j)e_bar(j),
```

using the half-basis notation of the rich-fiber norm-cutoff theorem. Define
the finite set

```text
C_n={odd primes ell : ell divides Norm(beta_E-beta_F)
      for some E!=F with ||v_E-v_F||_2^2<=6}.       (LDR1)
```

If `p=1 mod n` and an order-`n` subgroup row has `P(t)>=19` for some nonzero
target `t`, then

```text
p in C_n.                                           (LDR2)
```

Consequently every official row prime `p notin C_n` has empty cutoff-18 rich
locus, so `X_18=Y_18=0` and C36' holds on that row.

The candidate set can be enumerated without duplication over all raw
quadruples. Odd Galois dilation of every exponent, exchange of `E,F`, and
exchange inside either unordered pair preserve both the distance condition
and the absolute norm. One representative from each resulting orbit is
therefore complete.

This is a finite fixed-order router. It does not factor the candidate norms,
bound their number, or prove C36' at primes that survive the filter.

Raw orbit enumeration is not a viable official-order implementation. Put
`m=n/2`, `M=floor((m-1)/2)`, and `N=binom(M,2)`. There are at least

```text
L_n=N(N-1-9M)/2                                      (LDR3)
```

unordered low-distance pair-pairs before Galois quotienting, and therefore
at least `ceil(L_n/m)` Galois/exchange orbits. At `n=8192` this lower bound is
`530,590,075`. A practical certificate needs algebraic norm-template
compression before factorization.
