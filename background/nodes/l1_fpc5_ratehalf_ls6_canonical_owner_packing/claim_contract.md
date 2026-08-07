# Claim contract

- **claim id:** `l1_fpc5_ratehalf_ls6_canonical_owner_packing`
- **scope:** one guarded rate-half `M=4,t=3` LS6 atom, one primitive base,
  and every distinct guarded split candidate in its determinant chart
- **unit:** candidates per exact canonical base-overlap owner
- **claim:** `(CO2)--(CO8)` in `statement.md`
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **status:** PROVED by `proof.md`
- **replay:** `tools/ramguard tiny -- python3 background/nodes/l1_fpc5_ratehalf_ls6_canonical_owner_packing/verify.py`
- **falsifier:** an owner mismatch, failure of the normalized primitive
  guard, or a fixed-owner family exceeding `(CO7)`
- **nonclaim:** no aggregate bound over different owners and no prize-row
  payment
