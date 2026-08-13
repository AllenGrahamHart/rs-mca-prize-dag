# Claim contract

- **claim id:** `rate_half_mca_degree_guarded_shifted_lattice_witness_adapter`
- **status:** `PROVED`
- **quantifier:** every finite field, every distinct evaluation domain, and
  every `k<m<=n`
- **input:** an effective-shift exact-support lattice pair with a split monic
  complement locator and divisible numerator
- **guard:** `deg(N/W)<k`, equivalently `s_k(W,N)<=n-m`
- **output:** the identical support and a degree-`<k` explanation; with the
  support-interpolant noncontainment test, an actual MCA-bad witness
- **falsifier:** failure of any equivalence or shift-gap bound in the theorem
- **nonclaims:** no Q/BC owner equivalence, coverage, endpoint, selector,
  payment, or row closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_degree_guarded_shifted_lattice_witness_adapter/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_degree_guarded_shifted_lattice_witness_adapter/verify_audit.py`
- **upstream mapping:** discharges SEM-QBC soundness at the lattice-to-witness
  layer and the algebraic degree guard in condition 4; owner transport remains
  open
