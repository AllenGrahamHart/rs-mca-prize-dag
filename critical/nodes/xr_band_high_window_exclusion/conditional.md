# Conditional Proof

Assume `xr_band_maximal_window_divisor_count`.

By `xr_window_system_descent`, every depth-`d` joint codeword pair has
a degree-`n-k-d` locator satisfying both window systems. By
`xr_window_divisor_maximality_filter`, imposing exact full core
`H\T` and the support-wise `L_P>=2` predicate makes this correspondence
bijective with the pairs counted by `N_d`; raw locators over deeper
pairs are excluded. The residual's strip clause removes only classes
already proved empty or nongeneric and retains every other survivor.
Therefore

```text
N_d = |R_d(u,v)| <= 17n^2/25
```

at each prize row and high band-proper depth. This is SL-2. QED
conditional on the residual count.
