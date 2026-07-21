# Claim contract

- **claim id:** `xr_higher_rank_rank_two_shell_maxwell_router`
- **mathematical statement:** every uniform rank-two shell obeys the exact
  zero-fiber mass/arity ladder `(SR2)--(SR4)` and the active block family
  obeys the Maxwell deficit lower bound `(SR5)`
- **scope:** every uniform `u=v=0` high-core P-A selector cell and every
  affine kernel rank `a`
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependencies:** arbitrary-rank uniform split-pencil reduction and
  collapsed minimum-face exclusion
- **new open content:** proper local-circuit ownership and count, shells where
  `D_min<=0`, trade rank at least three, and nonuniform cells
- **falsifier:** a rank-two trade violating the zero-fiber constraints, row
  ceiling, or `(SR5)`, or a full Maxwell core in a printed positive-deficit
  range
- **nonclaims:** positivity outside the printed ranges, payment of proper
  local relations, or an aggregate slope bound
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_higher_rank_rank_two_shell_maxwell_router/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / exact
  primitive-circuit deficit ledger
