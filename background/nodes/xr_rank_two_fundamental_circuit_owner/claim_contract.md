# Claim contract

- **claim id:** `xr_rank_two_fundamental_circuit_owner`
- **mathematical statement:** after choosing the lexicographically first
  coefficient basis of a rank-two trade, every non-anchor block has a unique
  fundamental four/five-block circuit and those vectors form a basis of the
  complete scaling kernel as in `(FO1)--(FO4)`
- **scope:** each fixed uniform rank-two split-pencil trade
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependency:** rank-two circuit arity and Segre atlas
- **new open content:** support-embedding count, first Maxwell-core owner,
  cross-trade/cross-core deduplication, higher trade rank, and nonuniform cells
- **falsifier:** a rank-two coefficient configuration with a non-anchor that
  has no unique fundamental circuit, an owner outside arity four/five, or a
  scaling-kernel vector not reconstructed by `(FO3)`
- **nonclaims:** no count of abstract or realized Segre packets and no slope
  payment
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_rank_two_fundamental_circuit_owner/verify.py`
- **upstream mapping:** witness-exhaustive first-match atlas / residual
  balanced-core ray compiler
