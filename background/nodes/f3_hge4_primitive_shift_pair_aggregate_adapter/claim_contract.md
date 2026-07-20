# Claim contract

- **claim id:** `f3_hge4_primitive_shift_pair_aggregate_adapter`
- **status:** `PROVED`
- **proved content:** `(PSA1)` and the implication `(PSA3) => (PSA4)`
- **consumer:** `f3_hge4_norm_gate_count`
- **scope:** every official row and every `4<=h<=H_max`
- **open content:** the primitive shift-pair estimate `(PSA3)`
- **upstream mapping:** primitive shift-pair control in the exact
  second-moment ledger
- **replay:** `python3 verify.py` and `python3 verify_audit.py`

No bound on `SP_h^prim` is claimed. In particular, this node does not promote
the HGE4 target and does not infer primitive control from the unrestricted
prefix-fiber maximum.

