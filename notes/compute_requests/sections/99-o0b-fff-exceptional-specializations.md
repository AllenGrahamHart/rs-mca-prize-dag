## Preregistered O0b `FFF` exceptional specializations

- **decision:** replay the original denominator-free necessary system at all
  fourteen base-field roots of the complete generic exceptional ledger; do
  not specialize any rational generic basis
- **source cache SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **source admissible-graph SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **source exceptional-root SHA-256:**
  `e845607b89e7d21159bd308cbf00f9a3fd74a25120bc4d479a607f7e9d8751a7`
- **admissible graph basis:** 48 globally valid polynomials, dimension one,
  basis SHA-256
  `7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`
- **root-polynomial SHA-256:**
  `3589dc59d90716f76248f83b667411527fda6ceaff5b845b9dc673afbc5d4592`
- **program core SHA-256:**
  `96e58d24ce0de81b2916cc250787e5862c9cd34db48ed8c37caac8a7f2369efd`
- **launcher SHA-256:**
  `03366edbd5c2fb58fc056885bc5e83428e6faa94a0df77e6e13ad3a51357b83e`
- **outcome-neutral checker SHA-256:**
  `4f181e05b7a2fa4db332551a5f35f58030e937ab9dc333e56e7621dd5b5b9623`
- **generated-program ledger aggregate SHA-256:**
  `b9862ef9b8c3ad2bfc2ea4e86eb77126e91e0fc2000002e86b93780e31b755f4`
- **equation stages:** admissible graph plus `t-root`, then the original
  finite-pair equations `q5`, `q7`, and `q6`, with a dimension and basis-size
  checkpoint after every stage; `q4` is intentionally omitted because
  emptiness of this necessary subsystem already suffices
- **acceptance:** a fiber closes only when the completed final basis is the
  singleton unit ideal; every completed non-unit fiber must emit its full
  basis, and every timeout must preserve all completed stage checkpoints
- **envelope:** fourteen parallel Modal containers, one CPU and 16 GiB each,
  600-second Singular child wall and 660-second container wall; projected
  aggregate cost below `$1.50`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local Groebner-basis computation

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_modal.py
```

**Pre-run nonclaim:** the generic `FFF` locus is empty and every possible
generic-proof failure lies over these fourteen roots, but no exceptional
fiber is closed until this denominator-free replay returns and passes its
checker.
