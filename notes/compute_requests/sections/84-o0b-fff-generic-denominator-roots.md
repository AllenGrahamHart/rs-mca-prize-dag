## Preregistered O0b `FFF` generic denominator roots

- **decision:** collect every deployed-field root of the 44 generic-basis
  denominators before imposing the FFF necessary subsystem
- **scope:** basis-denominator exceptions only; later generic reductions may
  add further denominator roots
- **source result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **launcher SHA-256:**
  `35abdb889ffc0e6b9770a9663a92696cee1bf3897bcf8ba13e814d9750ebd3a0`
- **outcome-neutral checker SHA-256:**
  `c99b027800ac50fbc4a5301cdd506d795db5882418ade1428f3a8c38751faaaf`
- **method:** for every denominator compute `gcd(D,t^p-t)` and factor its
  square-free field part; independently repeat on the denominator LCM and
  require equality with the per-denominator root union
- **input ledger:** 44 distinct denominators; degree range 0--42; raw degree
  sum 1,013; field `GF(2130706433)`
- **output ledger:** per-denominator roots and reconstructed linear root
  polynomial; LCM degree/hash; combined root polynomial and exact root list
- **envelope:** one CPU, 1.5 GiB, 180-second container wall; projected cost
  below `$0.03`
- **local safety:** one RAM-guarded Modal client under a 240-second external
  hard stop; no local factorization

The combined root list is exactly the finite set where the current generic
basis may fail to specialize. It has no proof status for `q5,q7,q6`, and it
does not include any denominator introduced by their future reductions.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 240s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_denominator_roots_modal.py
```

**Outcome:** preregistered; not yet run.
