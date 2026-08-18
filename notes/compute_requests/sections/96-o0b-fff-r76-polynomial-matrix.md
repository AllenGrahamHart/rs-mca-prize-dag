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
  preregistered `fc6aefbd81fb4be89ef27edd86b78841afd75648308b9a4f4da879e1d8b871fe`;
  canonical-order repair
  `b43b8f72f1020f26deee5d67cb0be3384a9b2c738cb93004bf633c790d6732bb`
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

**Outcome:** `COMPLETE`. Modal app `ap-TtH5bFr7Z3uWIjmWgiukkm` produced
sixteen column LCMs of degrees

```text
1130,1151,1148,1155,1257,1152,1045,1044,
1041,1021,1042,1039,1154,1046,1043,1150.
```

All 256 cleared matrix entries are nonzero, with degrees `1151..1388`.
At `t=2`, the column-scaling factor is `1089253482` and

```text
1087830147 = 244686406 * 1089253482 mod 2130706433,
```

which verifies the determinant-clearing identity. Column-LCM SHA-256:
`eeafedd9b32a98a5c8e5b0c85af77d9a329256590baf292e91dceb4b6a97d6ad`;
polynomial-matrix SHA-256:
`15749ad35ba394a9dce27a8c759f0203746233a2fb354efcc3655d44ea205de4`;
result SHA-256:
`ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae`.
The preregistered checker compared parsed dictionaries in serialization
order; compact sorted JSON changed that order. The repaired checker
canonicalizes fields explicitly and rejects all five hostile mutations. No
compute source or result value changed.
