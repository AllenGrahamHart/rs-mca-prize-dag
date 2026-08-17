## Preregistered O0b collapsed common FGLM audit

- **decision:** measure and triangularize the checked dimension-zero
  four-variable collapsed common basis
- **scope:** the 43-element `epsilon=(-1,-1)` basis containing every
  canonical admissible `FFI/FIF` base point
- **relation:** exact change of monomial order for the recorded finite scheme
- **launcher SHA-256:**
  `7d1ea7cf573830151f0c3e09ce99dd08415fe00491ce44074b50f029cd2f2022`
- **outcome-neutral checker SHA-256:**
  `3e2b9f1442dbf750e0e1ec9cb312ac4c20e3f08b19f49d5564767da14023fac1`
- **program core SHA-256:**
  `0bebc1df7b26991035541e545207c8c3f92eb17ffe136cca31e89a6bb08b9f34`
- **source basis/result SHA-256:**
  `01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d`
- **input ledger:** variables `t,r,c,b`; 43-element degree-order basis;
  print `vdim` before converting to lexicographic order
- **envelope:** one CPU, 4 GiB, 120-second Singular child wall and
  150-second container wall; projected cost below `$0.03`
- **local safety:** one RAM-guarded Modal client under a 210-second external
  hard stop; no local CAS

The pre-FGLM transcript prints the vector-space degree, so a timeout still
records the finite scheme size. Completion must preserve dimension and degree
and returns the full lexicographic basis. This is a representation theorem,
not an emptiness claim.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 210s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_modal.py
```

**Outcome:** `COMPLETE`. Modal app `ap-i9TwFIx6T8gWO23DUhKlcQ`
computed vector-space degree 65 and a 20-element lexicographic basis; result
SHA-256:
`a72b2fe045538562352b3954b016dab60c5f8fdb01a22839088e72512d61f53f`.
The outcome-neutral checker verifies dimension and degree preservation and
rejects all three hostile mutations. The custodied factor verifier gives the
first eliminant exactly as
`b^3(b-1)^4(b+1)^5(b+8244070)(b+25179288)`. Thus the printed
`b,b-1,b+1` guards leave only two possible `b` fibers,
`2122462363` and `2105527145`, before the remaining guards are reapplied.
