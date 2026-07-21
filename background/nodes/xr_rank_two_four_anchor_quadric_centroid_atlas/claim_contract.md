# Claim contract

- **claim id:** `xr_rank_two_four_anchor_quadric_centroid_atlas`
- **mathematical statement:** relative to the canonical four anchors, every
  non-anchor coefficient is a support-three/four point on the explicit
  pulled-back Segre quadric `(QC2)`, the owner is `(QC4)`, and the complete
  trade condition is the centroid identity `(QC5)`
- **scope:** the `q=4` branch of every uniform rank-two split-pencil trade
- **consumer:** `xr_highcore_collision_count`
- **status:** `PROVED`
- **proved dependency:** canonical fundamental-circuit ownership
- **new open content:** count realized quadric-centroid configurations and
  their support embeddings, select the first core/trade, and aggregate cores
- **falsifier:** a four-anchor trade with a non-anchor off `(QC2)`, owner
  support below three or above four, or centroid different from `(QC5)`
- **nonclaims:** no abstract point count, selected-block realization theorem,
  or slope payment
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_rank_two_four_anchor_quadric_centroid_atlas/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / residual
  balanced-core ray compiler
