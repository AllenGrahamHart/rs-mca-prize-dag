## Preregistered O0b `FFF` exceptional admissibility replay

- **decision:** decide the nine exceptional survivors by lifting `E=e^2`,
  reimposing every original route, chart, and rank guard, and finally adding
  the omitted original finite-pair resultant `q4`
- **source cache SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **source survivor SHA-256:**
  `c066bb4f5813be4915e40a51225287cfde11284b3b3df4cabdae889778a97b88`
- **program core SHA-256:**
  `b838c8a5eaaa1b9ae3b0b51b967fc6394ddd9022095c8977721d37a630475c0b`
- **launcher SHA-256:**
  `4e5bbe8151eb111eee62df366d5b7a4f248bc82a9187455ede0a06a5da56637c`
- **outcome-neutral checker SHA-256:**
  `7575d298187363331f7a9b18179a059de0adb1849e15f123af5140dfb44d8f65`
- **generated-program ledger aggregate SHA-256:**
  `f31a3de0cfc81655e6ded937f95c34cc176e9745e492ef0e72cba44d6c3e2a14`
- **nine roots:** `0`, `1`, `16711679`, `47655010`, `451278922`,
  `1629292471`, `1893783428`, `2113994754`, `2130706432`
- **exact stage ledger:** lifted survivor ideal; sixteen sequential route
  saturations; saturation by `e,s,x,a0m,a2m`; saturation by the six-generator
  rank-cofactor ideal; original `q4` resultant
- **diagnostic contract:** record the first stage at which a singleton unit
  ideal appears; emit the full final basis for every completed non-unit
  survivor and all completed stages for every timeout
- **envelope:** nine parallel Modal containers, one CPU and 8 GiB each,
  300-second Singular child wall and 360-second container wall; projected
  aggregate cost below `$0.50`
- **local safety:** one RAM-guarded Modal client under a 420-second external
  hard stop; no local Groebner-basis or saturation computation

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 420s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_modal.py
```

**Pre-run nonclaim:** the printed survivor bases suggest that seven fibers
are boundary components killed by route guards. This is not used as a proof
until the exact saturations return. The two zero-dimensional fibers remain
wholly unresolved before this replay.
