### 2026-08-10 rate-half Haboeck-Johnson bracket

The unique-decoding transfer fence redirected the high-field safe-side search
to a direct MCA theorem. Haboeck's public Theorem 2 supplies one: at its
discrete Johnson-approaching radii, the exceptional finite-affine slope count
is bounded quadratically in `n`. The proof and same-support convention had
already been audited upstream; this cycle imported only that proved quadratic
theorem and explicitly excluded the unproved BCHKS25 linear refinement.

The exact official-row specialization uses `rho=(k-1)/n`, integerizes the
real numerator by its floor, and rounds the agreement threshold upward. For
`n=2^41`, `k=2^40`, the first strict improvement over `3n/4` is `m=9`,
available from `log2(q)>=232.650531`. Every razor row `q>2^255.9` can afford
`m=94`, proving

```text
a_RH(q) <= 1,563,215,236,073.
```

At the exact threshold

```text
q >= 330298791207625937408605578064099942258 * 2^128,
```

the bracket upgrades to `m=95` and

```text
a_RH(q) <= 1,563,128,173,124.
```

The strict field cap makes `m=96` impossible. Relative to the old `3n/4`
endpoint, the strongest gain is `86,139,268,540` agreement steps. This is
the first direct-MCA movement of the razor safe bracket in this cycle.

Burn-down: starting pins were local `6fc043995`, canonical `48a7de3c2`, and
upstream `93fba1be3`; result `NARROWED`; two PROVED nodes added, no critical
status changed, no new assumptions, no Modal spend. The exact crossing and
the adjacent unsafe half remain open. The next route-deciding question is
whether a proved beyond-Johnson MCA theorem or a far-CA structural bound can
continue from this new endpoint rather than returning immediately to the
near-capacity lower floor.
