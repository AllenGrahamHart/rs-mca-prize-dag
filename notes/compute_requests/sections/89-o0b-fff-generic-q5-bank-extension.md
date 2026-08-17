## Preregistered O0b `FFF` generic `q5` bank extension

- **decision:** form the exact 24-term generic quadratic from the three
  completed coefficient representatives and adjoin it to the base basis
- **scope:** certify the first finite extension in the incremental route
- **source generic SHA-256:**
  `c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e`
- **source coefficient frontier SHA-256:**
  `29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c`
- **source C1 resume SHA-256:**
  `899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c`
- **program core SHA-256:**
  `fdf8a466238f47623c2ae27771aeb6453a2eece3b736d4793b689d63ad1851ad`
- **launcher SHA-256:**
  `23fd894379f41f34f6891b68b25b6094a98fbd59a445961052b55b794a7c957c`
- **outcome-neutral checker SHA-256:**
  `d4accdf4176b4dfec0660b00298141017504604d33b2cbb9f368981fb297c093`
- **generated Julia SHA-256:**
  `1b0c106ffcc473e138113ed8fd3c48d071dbf6ec66cc802be7f867cc5ea43bc3`
- **output ledger:** input term count, certified basis and quotient profile,
  complete output coefficient denominator ledger
- **envelope:** one deterministic task, one CPU, 8 GiB, 360-second Julia
  child wall and 420-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 480-second external
  hard stop; no local CAS

The coefficient normal forms are already exact modulo the base ideal, so
adjoining their quadratic generates the same generic extension as adjoining
raw `q5`. Transformation denominators remain open.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 480s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-h3NTK3YvbAxOLtnLf7sLZ4` adjoined the exact 24-term quadratic and
certified a nonunit, dimension-zero basis of size 16 with quotient dimension
16. Basis SHA-256:
`bd4b2bf32d58c5f344d8d244eb2632646f0a7ca807bbefc5cf1c9c3737d6ab3b`.
The 192 output coefficient entries contain 100 distinct denominators, whose
ledger SHA-256 is
`125dfc37ef1bf4d8b093b66624408be8120299cc978ecef399f28cfb1df4ccdc`.
Result SHA-256:
`b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c`.
The checker verifies the complete basis and rejects all four hostile
mutations. Continue with coefficient-wise `q7` over this finite extension.
