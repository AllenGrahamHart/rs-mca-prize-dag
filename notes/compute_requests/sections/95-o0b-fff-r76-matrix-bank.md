## Preregistered O0b `FFF` `R76` matrix bank

- **decision:** construct the complete 16-by-16 rational multiplication
  matrix for `R76=Res_E(q7,q6)` and serialize every entry before any
  determinant attempt
- **scope:** immutable exact input for denominator clearing, polynomial
  determinant extraction, and exceptional-root enumeration
- **source multiplication-bank SHA-256:**
  `3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e`
- **source q7-coefficient SHA-256:**
  `37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d`
- **source direct-resultant program SHA-256:**
  `ac73c2251e90e6a84b45574dd171474c682586ff56415206d3453f355d49e33f`
- **program core SHA-256:**
  `18aa94db11be3b92a581fa51df5d2fb63f34c7055772d4e6f538d2275e467a5e`
- **launcher SHA-256:**
  `f356da0abb6afdd865910667b41ab680fe35965947c181d6bdec299c2a648875`
- **outcome-neutral checker SHA-256:**
  `dfde6997f96724f58113efd556e11f8275688241f1b546becbe9ef163480eefa`
- **generated Julia SHA-256:**
  `058ced61d9dea9c876f4add5a3d5bbbd26ab85abdac960062193d7c66cdbd5ca`
- **output ledger:** all 256 `(row,column,numerator,denominator)` records,
  plus the deduplicated denominator list and canonical hashes
- **cross-check:** reconstruct the finite witness at `t=2` and require
  determinant `244686406` before symbolic matrix construction
- **nonclaim:** this bank does not take the determinant or enumerate roots
- **envelope:** one deterministic task, one CPU, 24 GiB, 1,800-second Julia
  child wall and 1,860-second container wall; projected cost below `$0.25`
- **local safety:** one RAM-guarded Modal client under a 1,920-second external
  hard stop; no local CAS

Launch command:

```text
RAMGUARD_TIMEOUT=34m tools/ramguard modal -- \
  timeout --signal=TERM --kill-after=15s 1920s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_matrix_bank_modal.py
```

**Outcome:** `COMPLETE`. Modal app `ap-MUI78JcsnhTmx76IIDm0mq` serialized all
256 nonzero rational entries of the symbolic `R76` multiplication matrix.
There are 184 distinct reduced denominators. Numerator degrees range from
1105 to 1387; denominator degrees range from 975 to 1256. Matrix-ledger
SHA-256:
`24a8cc69a613bae3d367a087b524979de2bb8ec64174f97a2155c5227b7883f4`;
denominator-ledger SHA-256:
`b9623adc3fe54844a3a61c3a4d06a80f51fab713f6813e9599c1038287f280cc`;
result SHA-256:
`701f4a255f2f573b4f50d7bbf3ea14b80ae8562ae09d93f96a8409cb45babbfb`.
The checker rejects all five hostile mutations.
