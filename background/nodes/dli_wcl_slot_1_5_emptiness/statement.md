# WCL slot (1,5) emptiness

- **status:** TARGET (minted 2026-07-19 at the WCL amber ceremony)
- **consumer:** `dli_wcl_zone_coverage` (req)

At every official row (q < 2^256, v_2(q-1) >= 41), no reduced signed
weight-5 polynomial vanishes at an order-512 root (the ell=1 window slot
per the ratified schedule r2 / raw ledger; bookkeeping of record:
../dli_wcl_zone_coverage/official_terminal_attack.md). Zero-event
obligation. Evidence: the streaming terminal weight-five sweep (partial,
pilot max_v2 = 17-21); the first-64-primes MITM survival record.
FALSIFIER: one official-admissible prime with such a vanisher.
