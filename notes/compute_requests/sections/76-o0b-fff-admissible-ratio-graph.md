## Preregistered O0b `FFF` admissible ratio graph

- **decision:** construct the ratio graph in `x,t,r,c,b` and saturate
  only by the new base guards `x,a0m,a2m`
- **scope:** the admissible common-base projection required by every
  canonical `FFF` solution
- **source admissibility:** the 21-element common basis is already saturated
  by all 16 route guards and the six-cofactor rank ideal
- **launcher SHA-256:**
  `9b8eb716542e1b1530a2285aee9fc079c2b4686148a4ca6350affc6a633266e0`
- **outcome-neutral checker SHA-256:**
  `700c6c324ccdfd5c00f238cb0922b5ee674decf378152e81156d522bea53c2aa`
- **post-run stdout-tail repair checker SHA-256:**
  `6817767d7ea29bc1685447ccebce79494f36dda1b22bacf5b305981bc76923ad`
- **program core SHA-256:**
  `ca31838daef0f684d5bfffe82e0336e490707ef8acb023af6a323e0a169c7aa3`
- **generated Singular SHA-256:**
  `ca28ba87e35991836b713d32217fa842c700027dcb8b1ad6a2ec071c26a6b436`
- **source ratio-graph timeout SHA-256:**
  `9992611165f31733a3c497b27b93c39f65b621f9e3acc1489ab46c3d78e7096e`
- **input ledger:** variables `x,t,r,c,b`; 21-element dimension-one
  common basis; graph `a2m*x-a0m`; inherited 16 route guards and six
  rank cofactors; new guards `x,a0m,a2m`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

Every admissible `FFF` point has `a2m != 0`, so it maps to this graph
with `x=a0m/a2m`; `a0m != 0` also makes `x != 0`. A checked unit
basis closes `FFF` before outside equations are needed. A checked nonunit
basis is retained exactly for coefficient-wise `q5` reduction and
low-degree `s,E` resultants. Timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_modal.py
```

**Outcome:** `COMPLETE_NONUNIT`. Modal app
`ap-yefWfdW7toawtaFcRFwAG1` produced an initial graph basis of
`(dimension 1,size 53)`; saturation by `x` retained size 53,
`a0m` reduced it to size 48, and `a2m` retained size 48. The final
basis SHA-256 is
`7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`;
result SHA-256:
`5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`.

The preregistered checker rejected the otherwise valid payload because the
48-polynomial basis pushed the earlier `UNIT=0` marker outside the retained
30 kB stdout tail. The repaired checker removes only that redundant marker
test and instead requires the explicit nonunit field, dimension, basis
cardinality, and independently recomputed basis hash; it accepts the result
and rejects all three hostile mutations. The graph is nonempty, so this is
an exact input reduction rather than a chart closure.
