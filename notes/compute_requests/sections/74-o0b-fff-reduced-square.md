## Preregistered O0b `FFF` reduced square subsystem

- **decision:** reduce the `q5` square-subsystem polynomial explicitly modulo
  the 21-element common basis, adjoin it first, then reduce and adjoin `q7,q6`
- **scope:** the same strict necessary superset of the last open canonical
  `FFF` chart used in section 73
- **relation:** necessary superset; `q4` remains deliberately omitted and the
  retained finite pairs remain weakened to scaled resultants
- **launcher SHA-256:**
  `bf9f5478cadf7888751aa00fe227850fefc8a6d328fc39fe2c2eb2d120ae73ac`
- **outcome-neutral checker SHA-256:**
  `fe361e54601f64077c0ec202dc35560bccb5ae9cc986d0af31717724cf0de423`
- **normal-form program SHA-256:**
  `ef7169e4c2e0044ddda34b8ecdd165fcc71699b9e7afbce848a036c27ddec1b1`
- **source square core SHA-256:**
  `c5eca188068083699e94ba321858710f5225f423380a71821f9cea90135c4e72`
- **source square timeout SHA-256:**
  `cefc9fc49863ab0d20291c7cc009553bc45b8eb2946550c97c3daca154b595af`
- **generated Singular SHA-256:**
  `d1e03febe23e00b5c5867aa737827c7ce2f0c701b759399afc28bc7fc6460a73`
- **input ledger:** variables `E,s,t,r,c,b`; 21-element common basis;
  normal forms and equations in order `q5,q7,q6`; 16 route guards; guards
  `E,s,a0m,a2m`; six rank cofactors
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

Section 73 reached a dimension-two, 54-element basis after `q7` and timed
out adjoining `q5`. This run uses the same equations but computes each
new polynomial's normal form before adjoining it and starts with the observed
bottleneck. Every `FFF` solution still maps into the tested subsystem. A
checked unit basis therefore closes `FFF`; a checked nonunit result supplies
a smaller exact basis for the omitted `q4` step; timeout has no proof status.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_reduced_square_modal.py
```

**Outcome:** `INCOMPLETE_TIMEOUT`. Modal app
`ap-MhIhFWNqjNHO5cnOhY7yX9` completed the explicit `q5` normal form with
degree 90 and 4,717 terms, then timed out while adjoining that polynomial;
result SHA-256:
`c4406f815ddbcc33618a91ddce56b8a51c4f2c541f746d28f2873df377d0f7ba`.
The outcome-neutral checker accepts the retained transcript and rejects all
three hostile mutations. Whole-polynomial normal-form reduction therefore
does not remove the basis-construction bottleneck. The next architecture
decomposes the input by its low `s`-degree and reduces the coefficient
polynomials separately before rebuilding the equation.
