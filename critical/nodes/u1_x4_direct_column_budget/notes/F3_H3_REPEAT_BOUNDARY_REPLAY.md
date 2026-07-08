# F3 h=3 repeat-boundary replay

Status: REPLAY HARNESS FOR THE REPEAT-BOUNDARY CHAIN.

This packet provides a focused replay for the h=3 repeat-boundary work.  It is
separate from the default aggregate replay so the large F3 replay does not grow
past its current laptop-safe margin.

## Scope

The harness runs:

- the h=2 affine coset-pair Stepanov corollary;
- the h=3 moment bookkeeping identity;
- the repeat-residue boundary compiler;
- the repeat-boundary line compiler;
- the shifted reciprocal edge normal form;
- the active-edge cubic gcd normal form;
- the pair-intersection compiler;
- the lambda-fiber ledger;
- the LP4 Stepanov compiler;
- the q0 cell payment;
- the fixed-fiber cap;
- the `S_3` support symmetry;
- the LP4 rank guardrail;
- the combined support compiler;
- the boundary-style support evidence and zero-support falsifier;
- the forced-point support reduction;
- the forced-fiber Stepanov compiler;
- the elementary forced-fiber degree bound;
- the forced-cover crossover table;
- the coordinate-cover ledger;
- the coordinate-hitting ledger;
- the forced-coordinate-2 normal form;
- the hitting exception scan;
- the singleton-hitting stress scan;
- the star-obstruction compiler;
- the star-obstruction taxonomy.

It does not run the older h=3 rank/bridge aggregate and it does not launch
Modal.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_boundary_replay.py
```

Expected digest:

```text
F3_H3_REPEAT_BOUNDARY_REPLAY_PASS
```
