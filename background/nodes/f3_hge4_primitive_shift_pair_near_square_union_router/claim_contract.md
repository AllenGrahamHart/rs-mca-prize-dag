# Claim contract

- **claim id:** `f3_hge4_primitive_shift_pair_near_square_union_router`
- **status:** `PROVED`
- **claim:** near-square union characterization `(NSU1)`, exact free/swap
  orbit ledger `(NSU2)`, anchored identity `(NSU3)`, HGE4 interfaces
  `(NSU4)--(NSU6)`, and candidate reduction `(NSU7)`
- **scope:** every official row and every `4<=h<=H_max`
- **dependency:** `f3_hge4_primitive_shift_pair_orbit_aggregate_router`
- **consumer:** `f3_hge4_norm_gate_count`
- **falsifier:** a primitive ordered top shift pair failing `(NSU1)`, a valid
  near-square union with another partition, or an orbit violating `(NSU2)` or
  `(NSU3)`
- **open content:** the aggregate bound `(NSU4)` or a sufficient stronger
  union-orbit estimate
- **upstream mapping:** primitive shift-pair control / exact split-pencil
  second-moment ledger
- **replay:** `python3 verify.py` and `python3 verify_audit.py`

The node supplies a complete generator reduction, not a primitive union
count.
