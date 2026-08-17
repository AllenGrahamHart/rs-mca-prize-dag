## Preregistered O0b `FFF` generic necessary subsystem

- **decision:** adjoin `q5,q7,q6` to the certified 10-polynomial generic
  base graph and compute the exact extension over `GF(p)(t)`
- **scope:** generic branch of the necessary subsystem; `q4` remains omitted,
  so emptiness is sufficient for `FFF` but a survivor is only a superset
- **source generic result SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source packet SHA-256:**
  `fbeda61593e73cdcb7bf1e2baa1ebe8b098a7025f834135b3e02d2c291d50cd9`
- **source cache SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **program core SHA-256:**
  `4fb572a9b524f9e05533c7f844f58c529470a1f4aaf25f9de3c9f62a0c61a2d7`
- **launcher SHA-256:**
  `49ea921659240e80303875708169a040c2d45fe76525b2ea0b9df3392597ad51`
- **outcome-neutral checker SHA-256:**
  `509b6b4635007702f464ae89e2225d030cbfae2bb30b86adfda035f6559bc07b`
- **generated Julia SHA-256:**
  `51c308daf9d8136fc26f29f51252a4b6b0a15f1b8ab6efda2c3e73dc3850a260`
- **input ledger:** ten certified base polynomials, quotient dimension eight,
  equations in order `q5,q7,q6`, fiber variables `E,s,x,r,c,b`
- **output ledger:** certified full basis, unit/dimension/quotient profile, and
  all output coefficient numerators and denominators
- **envelope:** one deterministic task, one CPU, 8 GiB, 300-second Julia
  child wall and 360-second container wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local CAS

The generic output alone cannot promote `FFF`. Even if it is the unit ideal,
the computation must expose or replace its transformation denominators before
specialization; output-basis denominators and the eight known basis exceptions
are retained but are not presumed complete for the unit certificate.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_system_julia_modal.py
```

**Outcome:** preregistered; not yet run.
