# L1 band complement-dimension packing

- **status:** PROVED
- **role:** pay the sublinear projective-dimension strip immediately below
  the deep Johnson range
- **consumer:** `l1_mixed_petal_amplification`

## Statement

Fix an exact shell of agreement `m>k` in the balanced band

```text
2m<=n+k-1.
```

Put

```text
w=m-k,       omega=n-m,       s=omega-w=n-2m+k>=1. (CP1)
```

The balanced shifted-lattice coefficient space has vector dimension `s+1`
and projective dimension `s`.  If `Z_m(U)` is the number of degree-below-`k`
codewords agreeing with `U` on exactly `m` coordinates, then

```text
Z_m(U) <= floor( binom(n,s) / binom(omega,s) ).       (CP2)
```

For `omega>=alpha n` and `s<=alpha n/2`,

```text
binom(n,s)/binom(omega,s) <= (2/alpha)^s.             (CP3)
```

Hence every fixed-`s` shell is polynomially paid, every `s=o(n)` strip at
linear complement density costs `exp(o(n))`, and the payment is absorbable
under reserve `R` whenever `s=o(R log |B|)`.

## Scope

This is an exact-shell packing ceiling, not a base-field-normalized BC bound.
It can be exponential for `s=Theta(n)`, including the deployed adjacent
frontier.  It does not sum finite row numerators, classify quotient owners, or
replace the deep-tail Johnson payment.
