# Coordinator note (2026-08-07, round 22): two corrections to this pilot's PROOFS.md

Round-22 f2_rlocality (coordinator-replayed, 47/0):
- PROOFS.md:441-443 ("the gap is the factor L/log2(e L) = 8.60"):
  layer error — 8.60 = DEF_INSTR(1); the binding-layer deficit is
  6.3130; at c = 1 R-locality costs nothing (THEOREM 12 of this
  very pilot proves that layer R-locally; OPT_k(1) = p^{-k} exact).
- THEOREM 10's "dies at EVERY p / position entropy H(1/L) > 1/L":
  artifact of the union bound; the exact R-local binomial moment
  cancels C(S,R) and admits a threshold at every log2 p >= 3.06;
  the route dies numerically (deficit 258.9) but the diagnosis is
  locality, not position entropy.
The structural-deficit CONCLUSION of this pilot survives and is
now floored: see the round-22 addendum on
background/nodes/f2_z1_mass_knife_edge/statement.md.
