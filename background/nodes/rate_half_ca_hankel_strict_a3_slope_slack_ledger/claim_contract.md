# Claim contract

- **claim id:** `rate_half_ca_hankel_strict_a3_slope_slack_ledger`
- **mathematical statement:** every live strict-budget `A=3` generator, for
  every `m<=e<=floor((4m-1)/3)`, is a maximal-separation-rank degree-`e`
  rational normal kernel curve; every counterexample to the slope cap has the
  exact slack, saturation, clean-column, rank, and product-code ledgers
  `(SSL8)--(SSL13)`, and every sharp-cap `h=0` stratum has the low-defect
  norm-power and complementary factorizations `(SSL14)--(SSL16)` plus the
  unique component-degree chambers `(SSL17)--(SSL20)`
- **scope:** the official strict budget `B=2^39`, not the half-distance
  `A=3` or `A=1` profiles and not larger field budgets
- **dependencies:** the two-sided minimal-index theorem and the
  exceptional-slope root charge
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude every integer stratum
  `m<=e<=floor((4m-1)/3)`, `0<=h<=4(e-m)`, or construct one and move the
  rowwise MCA crossing; on `h=0`, exploit the residual-degree-at-most-`e`
  norm identity and quantized component degrees rather than restarting from
  an unrestricted biform
- **falsifier:** a live strict `A=3` pencil whose `Q_j` are dependent, whose
  supported count exceeds `4e+1`, or whose root-incidence matrix violates one
  of `(SSL10)--(SSL13)`
- **nonclaims:** no stratum is excluded, numerical survival is not used, and
  the result does not advance the high-field sparse-MCA term
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_strict_a3_slope_slack_ledger/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / strict
  Hankel-SPI slope ledger
