# Audit

- Recomputed the leading coefficient `4(t+3r)delta_4 tau_t` directly.
- Separated the floor case `t=2` from the higher cases `t=2 mod 3`, `t>=5`.
- Checked the exact integer endpoint and interval cardinality under RAMguard.
- The theorem does not extrapolate the degree bound past the point where
  `7t` reaches `v`.
