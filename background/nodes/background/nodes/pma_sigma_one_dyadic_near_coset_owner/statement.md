# PMA sigma-one growing-defect dyadic near-coset owner

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **evidence consumer:** `pma_wide_residual`
- **role:** global owner for every dyadic quotient core within the explicit
  `n/(32 log_2 n)` miss window

## General owner

Let `H` be cyclic of order `n`, let `L|n`, and let `K_L` be its unique
subgroup of order `L`. For a received word `U` and a degree-`<k` listed
codeword `P`, put

```text
A_P={x in H:P(x)=U(x)},    |A_P|>=a>=k+1.
```

For a `K_L`-coset `B` and `e=|B\A_P|`, put

```text
q_(L,e)=max(0,k-L+e).
```

If `q_(L,e)<=n-L`, then the class with `e<=s` at fixed scale `L` has the
chart-independent bound

```text
#CORE_(L,s)(U)
 <= (n/L) sum_(e=0)^s binom(L,e) binom(n-L,q_(L,e)).    (L-CORE)
```

Ordering scales and cosets and taking the first qualifying pair makes the
owner disjoint across all scales. It records the missed core points and only
enough outside agreements to reach `k` interpolation points.

## Official finite corollary

On the 128 official dyadic `sigma=1` rows, write `n=2^j`, put

```text
s_n=floor(n/(32j)),
```

let `S_grow` be all dyadic scales `L|n` with `L>=k-s_n`, and apply the
owner after exact periodicity. Then

```text
#QOWN_cosgrow
 <= sum_(L in S_grow) (n/L) sum_(e=0)^s_n
      binom(L,e) binom(n-L,max(0,k-L+e))
 <= (j+1)(s_n+1)n^(3s_n+1)
 < 2^(7n/64)
 < Q_2(k+2).                                            (FINITE-COS)
```

Consequently

```text
#(QOWN_per union QOWN_cosgrow)
 <= 8(1+2^-690)Q_2(k+2)
 < 719(1+2^-690)Q_2(k+2).                              (COMBINED-COS)
```

Since `s_n>=19`, the index-two four-defect owner is one `L=n/2` subcell, so
the complete reciprocal-quadratic obstruction is included. More generally,
every listed codeword with an agreement core missing at most `s_n` points of
any eligible dyadic coset is removed globally before B11 and before chart
composition. In particular this pays the near-quotient portions of finite PMA
defects through `d=s_n-1` in the worst background state.

## Scope

The interpolation formula `(L-CORE)` is general under its printed size
conditions. The growing-window absorption `(FINITE-COS)` is only for the
official finite `sigma=1` grid. It does not claim that near-coset agreement
sets are periodic, revive `QCLOSE`, or pay the post-owner diffuse complement.
