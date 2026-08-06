# WCL slot (1,5) emptiness

- **status:** PROVED (2026-08-06, complete norm census and independent replay)
- **consumer:** `dli_wcl_zone_coverage` (req)

At every official row (q < 2^256, v_2(q-1) >= 41), no reduced signed
weight-5 polynomial vanishes at an order-512 root (the ell=1 window slot
per the ratified schedule r2 / raw ledger; bookkeeping of record:
../dli_wcl_zone_coverage/official_terminal_attack.md).

The normalized-section extension is complete and has exactly `2,296,920`
affine-Galois classes.  Every class has a nonzero exact cyclotomic norm.  A
full independent direct-resultant replay certifies all `2,296,920` norms:
`2,296,726` easy rows and `194` hard tails.  Every factor is proved prime,
no factor meets the official gate, and the global maximum is
`v_2(p-1)=30<41`.  The proof and certificate custody are in `proof.md` and
`dependency_subdag.md`.
