# XR maximal selected window-divisor count (SL-2-RES)

- **status:** TARGET
- **consumer:** `xr_band_high_window_exclusion`
- **scope:** the three prize rows and high band-proper depths

Fix a globally generic received pair `(u,v)` after the ratified strip
order, and a depth

```text
ceil(h/2) <= d <= h-2,    r'=n-k-d.
```

Let `R_d(u,v)` be the set of monic squarefree split divisors
`E_T|X^n-1` of degree `r'` satisfying all of the following.

1. The top `d` coefficients of both `uE_T mod (X^n-1)` and
   `vE_T mod (X^n-1)` vanish.
2. The uniquely reconstructed codeword pair has full joint agreement
   set exactly `H\T`, of size `k+d`.
3. That maximal pair has at least two selected live slopes under the
   support-wise first-match selector.
4. It survives the generic strip order. In particular, common-class
   quotient-periodic systems are owned by P3, the pinned large-scale
   coset class is excluded by BP parity, and the large sub-depth
   individually periodic scales are excluded by liveness L.

Then

```text
25 |R_d(u,v)| <= 17 n^2.                              (SL2-RES)
```

The window lemma gives a bijection `R_d(u,v)` with the selected maximal
depth-`d` pairs counted by `N_d`. The word "residual" does not mean
only non-coset locators: small-scale mixed-class quotient patterns and
all other aperiodic systems remain unless a proved strip or liveness
exclusion applies.

## Falsifier

One prize row, one displayed depth, and a fully auditable family of
more than `17n^2/25` distinct locators satisfying all four clauses.
A raw divisor family lacking maximality or selected liveness is not a
falsifier.
