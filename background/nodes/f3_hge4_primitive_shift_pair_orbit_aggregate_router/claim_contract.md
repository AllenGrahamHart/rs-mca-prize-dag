# Claim contract

- **claim id:** `f3_hge4_primitive_shift_pair_orbit_aggregate_router`
- **status:** `PROVED`
- **proved content:** free scaling action `(OAR1)`, exact left-anchor factor
  `(OAR1a)`, orbit sufficient condition `(OAR2)`, per-width equivalence
  `(OAR3)`, and max-route separation `(OAR4)`
- **consumer:** `f3_hge4_norm_gate_count`
- **scope:** every official row and every `4<=h<=H_max`
- **open content:** the quadratic orbit aggregate `(OAR2)` or any sufficient
  stronger estimate such as `(OAR3)`
- **upstream mapping:** residual ray compiler / primitive exact
  falling-factorial shift-pair ledger
- **replay:** `python3 verify.py` and `python3 verify_audit.py`

The node does not claim primitive emptiness, a Q max-fiber theorem, or the
orbit bound `(OAR2)`.
