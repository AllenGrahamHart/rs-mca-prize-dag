## Preregistered O0b `FFF` R76 bracket bank

- **decision:** rerun the successful 61-stage progressive prefix, retain
  all five `M0`, five `M1`, and four `M2` representatives, and
  exit before final convolution
- **scope:** exact reusable quotient-ring inputs for the nine
  `R76` coefficients; no final product or equation is formed
- **launcher SHA-256:**
  `c5f6acdc04d8598b624bffe23301af808db09977071bd2edfd9d45de93c030e9`
- **outcome-neutral checker SHA-256:**
  `d208460426d0d449bd38636bf4a6e11ed94a852b29f144e468fbddf8e3e2e10b`
- **program core SHA-256:**
  `263de903e787c082d8e426519e50f5112eec7e10093109d9c57340160398949b`
- **generated Singular SHA-256:**
  `2a8614651ff141c5183ce0b69ada1c3fbeb80035f30ea9720525ebacae3486e0`
- **source progressive core SHA-256:**
  `b73c4e888dc69353bc823c787babdf7c4b8b5d2a4c7efe708ffef16604f045ca`
- **source progressive timeout SHA-256:**
  `0a2173e080a4a5029713aa8fa8feea73056a5e84b8139bc780684d5545117d95`
- **input ledger:** 61 intermediate reductions; bracket layout
  `M0[0..4],M1[0..4],M2[0..3]`; 14 outputs; expected exact zeros
  `M0[2]` and `M1[0]`; 48-element certified standard basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The generated program is identical to the successful progressive program
through all 61 intermediate reductions. It then prints and hashes the 14
brackets and exits before `M0*M0-M1*M2` is expanded. Completion creates
the sole source for deterministic chunked products; timeout retains checked
intermediate and bracket prefixes. Neither outcome closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_modal.py
```

**Outcome:** `COMPLETE`. Modal app
`ap-WkUJ6xUaL50A2ireij9cYb` completed all 61 intermediate stages and
retained all 14 bracket representatives. The two preregistered zero slots
are exact, and the 12 nonzero slots match the degree/term ledger from compute
request 79. Result SHA-256:
`08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f`.
The checker recomputes every bracket hash, accepts the exact zero pattern,
and rejects all four hostile mutations. This is the canonical source for
final `R76` product sharding; it does not close `FFF`.
