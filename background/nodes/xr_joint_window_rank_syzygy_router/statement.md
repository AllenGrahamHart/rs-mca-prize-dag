# XR joint-window rank syzygy router

- **status:** PROVED
- **consumer:** `xr_band_maximal_window_divisor_count`

For a tangent-gated received pair `(u,v)` at depth `d`, let
`R_u(d)` and `R_v(d)` be the `d x (r'+1)` Toeplitz matrices of the
window lemma, where `r'=n-k-d`, and let

```text
J_d(u,v) = [ R_u(d) ; R_v(d) ].
```

Then:

1. `d <= rank J_d <= 2d`.
2. `rank J_d<2d` if and only if there are coefficient vectors
   `a,b in F^d`, not both zero, such that for every `0<=i<=r'`,

   ```text
   sum_{s=0}^{d-1} a_s u_{n-d+s-i}
     + sum_{s=0}^{d-1} b_s v_{n-d+s-i} = 0.            (P)
   ```

   Equivalently, the syndrome pair has a degree-`<d` Padé syzygy on
   the complete window.
3. Under the tangent gate, both `a` and `b` are nonzero and they are
   not proportional. A one-sided syzygy contradicts the single-word
   rank theorem; a proportional pair is a recurrence of order `<d`
   for one scalar pencil member `u+zv`, also contradicting the gate.
4. The corresponding polynomials `A,B` therefore determine a
   nonconstant rational direction `A/B`. Thus the residual splits
   exactly into a full-joint-rank arithmetic case and a genuinely
   two-sided, nonproportional Padé-syzygy case.

No bound on either stratum is asserted.

## Falsifier

A tangent-gated pair with stacked rank below `d`, or a deficient pair
with only a one-sided or proportional syzygy.
