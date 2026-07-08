# F3 flip interim report

Status: IN-PROGRESS REPORT, NOT A FLIP DOSSIER.

This is the current evidence map for the F3 flip brief.  It records what is
proved, what is only conditionally compiled, and what still blocks promotion of
`u1_x4_direct_column_budget` to `PROVED`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```

The replay runs only lightweight local verifiers.  It does not launch Modal.

## Current claims

### h=2

The h=2 stratum is closed by the external Cochrane-Pinner input already cited in
the node.  The in-house rich-coset reconstruction remains valuable because it
now has explicit constants:

```text
E(H) <= 22111 h^(5/2)
```

This in-house chain covers official powers of two from `2^23` upward.  Without
the external import, the remaining finite midrange is exactly `2^19..2^22`;
`2^13..2^18` are the rows estimated as feasible for exact certificates under
the `<2000` shard policy.

### h=3

The char-zero classification and norm-gate mechanism are banked.  The current
hyperbola identity is now locally replayed: same-fiber pairs of
`F(T)=T^3+aT^2+bT+c` satisfy `G_F(u,v)=XY-Delta` after the explicit
`omega`-coordinate change.  The per-row compiler consumes the corrected
activation statement:

```text
H3-ACT(C): A_3(n,p) <= C n
```

where `A_3(n,p)` counts actual non-toral common-root activations at primitive
`n`th roots, not rational norm-gcd coincidences.  If `C=16`, then

```text
T_3 < n^3 for every n >= 17.
```

The `n=96` all-core aggregate has maximum oriented per-prime activation count
`92 < 96`, which is evidence at the right scale but not a proof.  The remaining
h=3 proof debt is exact:

```text
RC-RED(C_red) + RC-NV    => rich-curve Stepanov theorem
rich-curve theorem      => H3-ACT(C)
H3-ACT(C)               => T_3 < n^3
```

The rational norm-coprimality version should not be used; it is already
refuted by the random norm sample.

### h=4

The structural dichotomy is already proved in the DAG:

```text
h4_terminal_dichotomy: PROVED
x83_uniform_square_shift_obstruction_gate: PROVED
```

So h=4 has no hidden third mechanism.  The live work is certificate/norm-gate
exclusion, not a new classification theorem.

### h=5

The h=5 structural classification is reduced.  Since `5` is not a power of two,
`x24_char0_dyadic_descent` excludes char-zero dyadic trades, and
`x83_uniform_square_shift_obstruction_gate` says every finite-row h=5 survivor
must be a p-specific norm-gate event.  Thus h=5 no longer has an unlocalized
classification gap; it has a norm-gate exclusion/certificate gap.

The h=5 row evidence is strong but not a theorem.  Complete zero certificates
exist for:

```text
n=32: 7 primes
n=64: 5 primes
n=96: boundary prime 9601
n=128: boundary prime 17921 plus 6 nearby primes
```

The missing h=5 theorem is exactly a symbolic norm-gate incompatibility or a
maintainable per-row certificate family for all official `p = 1 mod n`,
`p >= n^2` rows.

### h=6 and h=7

The local replay verifies the banked h=6 and h=7 certificates.  The h=6
extra-prime row at `p=4993` has six anchored nontoral witnesses under the coarse
classifier, but the square-lift analysis classifies them as paid h=3 lifts.
They do not threaten the direct-column budget.

### h=8

The h=8 n=32 row is complete at six primes.  The h=8 n=64 rows remain partial:

```text
boundary_n64_h8_p193
q3_n64_h8
```

The x83 radius-three shells at `p=4289` and `p=262337` are complete and have
`full_zero = 0`.  The support-to-trade reduction is proved on banked rows: a
support-level x83 certificate is enough to recover the trade split.

The honest h=8 residual is:

```text
certify every non-antipodal h=8 n=64 x83 support, or build an external/sharded
signature join that avoids the blind binom(63,7) left table.
```

## Promotion blocker

`u1_x4_direct_column_budget` cannot be promoted from `TARGET` to `PROVED` yet.
The concrete blockers are:

1. h=3: prove `H3-ACT(C)` through `RC-RED` and `RC-NV`, or replace it with a
   complete official-row certificate family.
2. h=5: exclude or certify the p-specific x83 norm-gate branch uniformly.
3. h=8: close the n=64 non-antipodal x83 support branch.

Everything else currently looks like arithmetic/certificate engineering rather
than an unlocalized mathematical unknown.
