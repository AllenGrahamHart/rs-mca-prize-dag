## Preregistered O0b `FFF` ratio graph

- **decision:** introduce the exact guarded ratio graph
  `a2m*x-a0m=0` before adjoining the compressed `q5,q7,q6` equations
- **scope:** a strict necessary superset of the last open canonical
  `FFF` chart
- **relation:** necessary superset; `q4` remains deliberately omitted
- **launcher SHA-256:**
  `149547f42cfe4a31ad656272d361c0cc86006c6a19f991360a79cd0881b45a74`
- **outcome-neutral checker SHA-256:**
  `fede939b35864af09999feb26964e043a84b12777ba12617ae5bfa29a189e409`
- **program core SHA-256:**
  `4375aa57ad1b1ec1aa85afd323e6bed5d4e6b7bd1c33e4ab15492a623a443898`
- **generated Singular SHA-256:**
  `5c184f0bc3d20a5293e479d8c19aa16c12fb664710af6de1fbc9000dfd628cc7`
- **source reduced-square timeout SHA-256:**
  `c4406f815ddbcc33618a91ddce56b8a51c4f2c541f746d28f2873df377d0f7ba`
- **input ledger:** variables `E,s,x,t,r,c,b`; 21-element common basis;
  graph `a2m*x-a0m`; equations and normal forms in order `q5,q7,q6`;
  16 route guards; guards `E,s,x,a0m,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

On the graph and under the already required `a2m != 0` guard, exact symbolic
identities give

```text
q5_original = a2m^4 * q5_graph
q6_original = a2m^2 * q6_graph
q7_original = q7_graph
```

Thus every admissible `FFF` point lifts to the graph subsystem and the
removed factors cannot vanish there. A checked unit basis closes `FFF`; a
checked nonunit basis supplies a compressed exact input for the omitted
`q4` step; timeout has no proof status. The launcher retains graph, normal,
and equation prefixes on timeout.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_ratio_graph_modal.py
```

**Outcome:** preregistered; not yet run.
