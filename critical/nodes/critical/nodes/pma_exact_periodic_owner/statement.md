# PMA exact-periodic source owner

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **evidence consumer:** `pma_wide_residual`

## General theorem

Let `H` be a cyclic Reed-Solomon evaluation domain of order `n`, let
`C=RS[H,k]`, let `U:H->F`, and let `a=k+sigma<=n` with `sigma>=1`. For
`P in ImgFib_U(a)`, write

```text
A_P={x in H:U(x)=P(x)},       M(P)=|Stab_H(A_P)|.
```

Define the source-level exact-periodic predicate

```text
QOWN_per(P;U)  iff  M(P)>1.
```

For each divisor `M|n`, put `N=n/M`, `h_M=ceil(a/M)`, and
`A_M=M h_M`. If `1<M<n` and `h_M<N`, then

```text
#{P in ImgFib_U(a):M(P)=M}
  <= binom(N,h_M)
   = n/(n-A_M) * binom(N-1,h_M).                 (QOWN)
```

If `M<n` and `h_M=N`, the exact-`M` class is empty. The exact-`n` class has
size at most one. The owner is canonical: order the cosets of the unique
order-`M` subgroup and retain the first `h_M` cosets contained in `A_P`.
The pair `(M, retained cosets)` is injective on listed codewords. Exact
stabilizer makes the scale unique, so the owner is disjoint across scales and
independent of every sunflower or PMA chart.

## Official finite corollary

On the official dyadic `sigma=1` grid

```text
n=2^j,  13<=j<=44,  rho in {1/2,1/4,1/8,1/16},  k=rho n,
M_cut=(n-k)/2,
```

write

```text
Q_M(A_M)=binom(n/M-1,A_M/M),
A_M=M ceil((k+1)/M).
```

Then all exact-periodic listed codewords, globally over every source chart,
satisfy

```text
#QOWN_per
 <= 4(1+2^-690) Q_2(k+2)+3
 <= 719(1+2^-690) Q_2(k+2).                      (FINITE)
```

Thus one global first-scale line in the extended dyadic quotient-profile
ledger pays the exact-periodic class before the full-petal/mixed-petal split.
There is no chart multiplier and this line must not be charged again inside a
petal branch.

## Scope

This theorem exhausts exact stabilizer `M>1`. The downstream
`pma_quotient_closure_scope` theorem proves that the precise folded-receiver
source construction is included here. This theorem alone does not classify an
algebraically folded codeword against a nonfolded receiver or low-defect
quotient closures whose full agreement set has stabilizer one; those remain in
the direct `petal_mixed_amplification` target. The general theorem is finite and
reserve-explicit, but its scale sum must be paid by the natural
quotient-profile envelope. `(FINITE)` is only the `sigma=1` official-grid
specialization.
