# F3 h=8 n=64 x83 radius-three shell

Status: MODAL-SHARDED ADVERSARIAL SHELL, NOT A FULL H8 CERTIFICATE.

This packet extends the near-lift x83 shell attack to radius three around the
paid h=8 square-lift branch.  A radius-three shell contains
`7 * C(16,3) * C(48,3) = 67,800,320` preimage candidates per prime, so it is
sharded by paid-support/removed-triple pair and run on Modal with 60-second
worker timeouts.

## Pre-registration

Question:

```text
At the actual q3 h=8 n=64 prime p=262337, are there any x83 full-zero h=8
supports three exchanges away from the paid antipodal square-lift branch?
```

Success criterion:

- process all `67,800,320` radius-three preimage candidates at `p=262337`;
- every shard completes under the 60-second worker timeout;
- find zero full x83 obstruction vectors with nonzero square `lambda`;
- write a replayable JSON certificate and local verifier.

Failure criterion:

- any full x83-zero support is a concrete primitive/norm-gate candidate;
- any timeout/incomplete shard means the packet is not a certificate.

## Replay

Gate:

```bash
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_modal.py
```

Full certificate:

```bash
F3_H8_RADIUS3_MODE=full F3_H8_RADIUS3_PRIMES=262337 \
  ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_radius3_certificate.py
```

Expected digests:

```text
H8_N64_X83_RADIUS3_GATE_PASS
H8_N64_X83_RADIUS3_SHELL_PASS
H8_N64_X83_RADIUS3_CERTIFICATE_PASS
```

## Result

The full Modal replay reports:

```text
p=262337 radius-three shell: paid=7 pair_chunks=196
processed=67,800,320 first_obstruction_zero=320 full_zero=0
max_shard_elapsed=28.446s complete=True
H8_N64_X83_RADIUS3_SHELL_PASS
H8_N64_X83_RADIUS3_CERTIFICATE_PASS
```

Interpretation:

This is a complete adversarial check of the radius-three exchange shell around
the seven paid h=8 square-lift supports at the actual `q3_n64_h8` prime
`p=262337`.  It rules out every support at exchange distance at most three from
the paid square-lift branch at that prime.  It is still a local deformation-shell
certificate, not a full enumeration of the non-antipodal h=8 branch.
