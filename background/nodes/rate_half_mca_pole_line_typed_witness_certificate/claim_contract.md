# Claim contract

- **claim id:** `rate_half_mca_pole_line_typed_witness_certificate`
- **status:** `PROVED`
- **scope:** one actual deployed KoalaBear received line and affine slope
- **output:** a parsed exact-support degree-`<k` MCA-bad witness, guarded
  lattice reconstruction, and exact minimum under both shifts
- **owner output:** none; Q, BC, and `U_new` remain unassigned
- **falsifier:** any failed source pin, field/subgroup/support identity,
  same-line witness check, noncontainment root count, or minimum proof
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_pole_line_typed_witness_certificate/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_pole_line_typed_witness_certificate/verify_audit.py`
- **upstream replay:** exact `#1159` primary checker with `--check
  --tamper-selftest --dag-root <this-worktree>`
- **upstream mapping:** imports the actual-record theorem and supplies a local
  consumer of the degree-guarded adapter; it does not duplicate SEM-QBC
