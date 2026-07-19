# Claim contract

- **claim id:** `f3_h3_excess_budget_degree_tradeoff`
- **mathematical statement:** paying excess at most `E` by total quotient mass
  leaves the exact high-tail budget `(EBD2)` and forces center degree
  `(EBD3)`
- **scope:** every official H3 row and every integer `0<=E<=17`
- **consumer:** `f3_h3_mobius_excess_half`, high-excess ideal route
- **status:** `PROVED`
- **proved dependencies:** exact quotient-block mass and rich-excess
  multistar degree ladder
- **new open content:** prove one of the five Pareto high-tail estimates
- **falsifier:** a quotient profile violating `(EBD1)` or a high-tail target
  below its asserted degree threshold
- **proof route:** exact low-tail payment followed by the degree ladder
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_excess_budget_degree_tradeoff/verify.py`
- **upstream mapping:** primitive shift-pair control / truncated excess ledger
