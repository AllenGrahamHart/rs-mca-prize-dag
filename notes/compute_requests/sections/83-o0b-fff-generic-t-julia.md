## Preregistered O0b `FFF` generic-t Julia basis

- **decision:** convert all 48 admissible graph polynomials from Singular
  compact notation and compute a deterministic, certified Groebner basis in
  `GF(2130706433)(t)[x,r,c,b]` with AbstractAlgebra/Groebner.jl
- **scope:** generic fiber plus a complete rational-coefficient denominator
  ledger; denominator roots remain open finite-fiber leaves
- **launcher SHA-256:**
  `82dc73e5e0abac1015c33a69418d3f9f026f563c052588c969aeffffe7f8c7ee`
- **outcome-neutral checker SHA-256:**
  `106406f18fdc558da9ba0697d080bbdc55cedb078513b589fc969fa70a883b50`
- **program core SHA-256:**
  `a20f75acf0bbe4654ef3467b2a0c05e0e1ec4a3d4cf50439f913abf4ae5a39d1`
- **generated Julia SHA-256:**
  `cd0c5960503ceafb2cca92e072dc2e762035ba1c540b17acb3a2752e84026b0d`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **input ledger:** parameter `t`; fiber variables `x,r,c,b`; 48
  converted source polynomials; deterministic linear algebra, one task;
  `isgroebner` assertion; quotient-basis dimension
- **output ledger:** full basis; every term coefficient serialized as
  numerator/denominator coefficient arrays in `F_p[t]`; deduplicated
  denominator list and hashes
- **envelope:** one CPU, 4 GiB, 240-second Julia child wall and
  300-second container wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The parser self-tests compact monomials such as `x2tr3` and converts all 48
source polynomials before launch. Completion requires Groebner.jl's
`isgroebner` certificate, dimension zero, positive quotient dimension, and
complete basis and coefficient ledgers. Every nonconstant denominator
remains an exceptional-fiber obligation. Timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_modal.py
```

**Outcome:** preregistered; not yet run.
