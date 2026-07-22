# Claim contract

- **claim id:** `xr_tangent_support_mismatch_bridge`
- **status:** PROVED
- **scope:** all received pairs at the six clean-rate candidates
- **generic route:** P-A1 high-core `8n^3` plus P-B low-core `8n^3`
- **nongeneric route:** remove only `q_z=0` genuine tangents and route every
  retained `q_z!=0` mismatch to P-A2's combined `16n^3` clause
- **proved mismatch scope:** every retained selected ray is transverse on its
  own error support, even if another joint explanation support exists
- **consumer:** `xr_smallcore_spread_count`
- **nonclaim:** this node proves neither generic `8n^3` clause nor the
  nongeneric combined `16n^3` clause
- **falsifier:** a received pair outside the generic/nongeneric dichotomy, a
  retained selected mismatch which is not support-locally transverse, or a
  slope not routed to its stated clause
