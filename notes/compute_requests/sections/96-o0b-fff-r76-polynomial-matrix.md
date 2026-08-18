## Preregistered O0b `FFF` `R76` polynomial matrix

- **decision:** clear the rational `R76` matrix denominators column by column
  and bank the resulting 16-by-16 matrix over `GF(2130706433)[t]`
- **source rational-matrix SHA-256:**
  `701f4a255f2f573b4f50d7bbf3ea14b80ae8562ae09d93f96a8409cb45babbfb`
- **source matrix-ledger SHA-256:**
  `24a8cc69a613bae3d367a087b524979de2bb8ec64174f97a2155c5227b7883f4`
- **program core SHA-256:**
  `af82fe9bc2a9d9e72d85687f72e576ad72b11d1d622d6a83b5c431ec761c207f`
- **launcher SHA-256:**
  `3ab05f25c122fce9882b8c1a2a44a02b38cf63eb35bee3d41338c290a1af0000`
- **outcome-neutral checker SHA-256:**
  `fc6aefbd81fb4be89ef27edd86b78841afd75648308b9a4f4da879e1d8b871fe`
- **generated Julia SHA-256:**
  `a915cb5544a24b2d22af6c35777b800bebbc55fd42de76d5fc7cc3822c8fff2a`
- **construction:** for column `j`, compute the exact LCM `L_j` of its
  sixteen reduced denominators and set `P_ij=num_ij*(L_j/den_ij)`
- **output ledger:** sixteen `L_j` coefficient arrays, 256 polynomial-matrix
  coefficient arrays, degree profiles, and canonical hashes
- **witness identity:** at `t=2`, require
  `det(P)=244686406*product_j L_j` in the prime field
- **nonclaim:** this bank does not take `det(P)` or enumerate its roots
- **envelope:** one deterministic task, one CPU, 16 GiB, 600-second Julia
  child wall and 660-second container wall; projected cost below `$0.10`
- **local safety:** one RAM-guarded Modal client under a 720-second external
  hard stop; no local CAS

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 720s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_modal.py
```

**Outcome:** pending.
