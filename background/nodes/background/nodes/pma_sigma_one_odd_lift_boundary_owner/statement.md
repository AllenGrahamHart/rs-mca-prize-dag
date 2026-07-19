# PMA sigma-one odd-lift boundary owner

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **role:** global owner for the first two exact scale-two odd-lift levels

## Statement

Let `n=2^j`, `13<=j<=44`, let `k` be one of the four official even
dimensions, and put `N=n/2`.  Write `pi(x)=x^2` on the cyclic evaluation
domain.  Suppose the nonzero source word has a scale-two split factorization

```text
U(x)=(x-a)V(pi(x))
```

for some `a` in the domain.  Let `QOWN_odd2(U)` consist of degree-`<k`
codewords of the form

```text
P(x)=(x-a)G(pi(x))
```

whose exact agreement set contains `a` but not `-a` and has size `k+1` or
`k+3`.  Then the source factor `a` is unique and

```text
#QOWN_odd2(U)
 <= binom(N-1,k/2)+binom(N-1,k/2+1)
  = binom(N,k/2+1)
  < 3 Q_2(k+2),                                      (ODD2)

Q_2(k+2)=binom(N-1,k/2+1).
```

Apply this owner after the exact-periodic and growing dyadic near-coset
owners.  On every official finite row,

```text
#(QOWN_per union QOWN_cosgrow union QOWN_odd2)
 < 11(1+2^-690)Q_2(k+2)
 < 719(1+2^-690)Q_2(k+2).                           (ODD2-COMB)
```

The owner contains the complete binomial-scale odd-lift family identified in
catch #171 at exact agreement levels `k+1` and `k+3`.  It is selected from the
received/source word before any sunflower chart, so it has no chart
multiplicity.

## Scope

This theorem does not own odd lifts at higher exact agreement, arbitrary
one-boundary quotient closures, non-lift below-floor full-petal objects, or
the mixed/diffuse residual.  It does not revive the raw `QCLOSE` route.
