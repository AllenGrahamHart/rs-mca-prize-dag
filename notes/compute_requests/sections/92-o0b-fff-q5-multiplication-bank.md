## Preregistered O0b `FFF` `q5` multiplication bank

- **decision:** extract the 16-dimensional quotient basis, regular
  multiplication matrices for `s,x,r,c,b`, and base normal forms of `k0..k5`
- **scope:** reusable exact input for the explicit quadratic `q7` extension
  and final `q6` determinant
- **source q5 extension SHA-256:**
  `b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`
- **source generic SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **program core SHA-256:**
  `269cc2bea1efb9ee4a16d9a03e6d420df04a88907454f7899324725cdc4508b1`
- **launcher SHA-256:**
  `d1e2239314201b6f68403204b96054547484692c2f5093853412954c7ecfd08f`
- **outcome-neutral checker SHA-256:**
  `8a7770f3df90457124863fca9c4a31c5922a1d7342fd5a2a5faa29e819687f8e`
- **generated Julia SHA-256:**
  `a0e7912ef2092d9fc3a1754f9b261c808c5a6faf5d88a57fa4cc9bb9c5310e4e`
- **output ledger:** ordered quotient basis; five sparse 16-by-16 matrices;
  six kernel representatives and rational coefficient ledgers
- **internal checks:** imported basis is Groebner; quotient dimension 16;
  every variable product reduces into the basis; all five matrices commute
- **envelope:** one deterministic task, one CPU, 16 GiB, 600-second Julia
  child wall and 660-second container wall; projected cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local CAS

This bank is structural. It does not itself impose `q7` or `q6`, and all
matrix-entry denominators remain open specialization obligations.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_modal.py
```

**Outcome:** preregistered; not yet run.
