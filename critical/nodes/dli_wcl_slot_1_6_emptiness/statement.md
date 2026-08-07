# WCL slot (1,6) emptiness

- **status:** TARGET (minted 2026-07-19 at the WCL amber ceremony)
- **consumer:** `dli_wcl_zone_coverage` (req)

At every official row, no reduced signed weight-6 polynomial vanishes at
an order-512 root (ell=1 window). Zero-event obligation. Evidence note:
(1,6)-shaped relations EXIST at non-ambient primes (the engineered
weight-6 witness) — the official-admissibility gate (v_2(q-1) >= 41) is
load-bearing. FALSIFIER: one official-admissible prime with such a
vanisher.

Finite exact evidence: the first 64 certified split-prime characteristics,
`q=k*2^41+1` for prime rows with `3<=k<=996`, exhaust all normalized legal
pair/triple splits and contain no vanisher. This does not alter `TARGET`:
later characteristics and extension-field rows remain unclassified.
