# (OUT-m) as an aggregate identity, and its (DEG-m) corollary

- **status:** **POSED** (both (OUT-m) and (DEG-m); (DEG-m) inherits);
  node-level CONJECTURE (the DAG-schema bucket for POSED).
- **closure:** a constraint on the configuration space — **not** progress on
  the residual direction
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/outm_identity_degm/`, coordinator
  line-audited; **the D11 rename is applied here** — the quantity the
  round-35 addendum called `deg_H` is `deg_Sh` in this and every wired
  document (see the symbol-collision section). No proof.md by design:
  POSED is the status and a proof file would overstate it.

## (OUT-m), with the coordinator's corrections applied

At a minimising pair union with (SAT1)-(SAT4), `T = rho+2`, `a = 7m-1`,
writing `X'_g = |S_gamma ^ (S_g D S_h)|` and
`X''_g = |S_gamma ^ (S_g ^ S_h)|`:

```text
X'_gamma + 2 X''_gamma >= m - 1 - eps_gamma,                       (OUT-m)
```

where `eps_gamma` is the total saturation deficiency on `S_gamma`.

**TWO CORRECTIONS ARE PART OF THE STATEMENT** (the original rider was FALSE):

1. The aggregate rider "`sum_gamma eps_gamma <= 1+O`" is **FALSE**. A
   deficient point outside `W` charges every type-2 block through it, so the
   correct aggregate is **`(m-1)(1+O)`**. The pilot's own witness (deficient
   point = the outside pair) has `sum eps = 2 > 1+O = 1`.
2. The corollary "`X_gamma = 0` is impossible" requires `1+O < m-1`, i.e.
   **`O <= m-3`** — satisfied at `m = 3, O = 0`, but **NOT free in general**,
   and **VACUOUS at `m = 2`**.

## (OUT-ID) The refinement: an exact identity

```text
sum_gamma eps~_gamma = sum_x def(x) * t_x,                        (OUT-ID)
```

with `t_x` the number of type-2 blocks through `x`, charging

```text
m-1  per unit at OUTSIDE points,
m-2  at SYMMETRIC-DIFFERENCE points,
m-3  at MIDDLE points.
```

It is a **trivial double count once stated** (coordinator-verified), and the
verifier confirms it on `200` synthetic incidence structures at
`m = 3,4,5,6,8`, including degenerate cases.

Consequences the verifier also checks:

- the aggregate `(m-1)(1+O)` is attained **ONLY by outside deficiency**;
- the `m=3` witness attains it exactly (`sum = 2 = (m-1)(1+O)`), reproducing
  the round-34 catch (`2 > 1`);
- the `m=2` exhibit, whose deficient point is INSIDE `W`, charges `0`.

## (DEG-m), inheriting POSED status

In sigma-designs `X' = 2 deg_Sh`, so

```text
deg_Sh(gamma) + X''_gamma >= ceil((m - 1 - eps~)/2),              (DEG-m)
```

with the **exact middle budget**

```text
sum_gamma X''_gamma = (m-1)(m-2)          (= 2 at m=3, 6 at m=4).
```

**At `m >= 4` a degree-1 slope REQUIRES middle support** — a constraint round
34's DFS never imposed, so its ceiling was measured on a relaxation. At
`m = 3` the floor is `1` and a degree-1 slope needs none. Both selection
certificates survive the tightening.

## Completion-level record (rounds 34-36)

- (DEG-m) has **ZERO selection power**: tightened and relaxed 2-sharing
  ceilings are **BIT-IDENTICAL** (`7/12`, two fields).
- It is **decisive at completion**: every ceiling configuration has
  `n_1 = 9` against a completeness bound of `4`, so **the 2-sharing `m=4`
  negative upgrades from a ceiling to dead-objects-at-the-ceiling** (two
  fields).
- (OUT-m) killed `X = 0` slope-padding and two of the pilot's own designs.

## SYMBOL COLLISION — RESOLVED BY RENAME (D11, coordinator ruling)

`deg_H` already names the bipartite non-incidence degree in the PROVED node
`rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction`
— two different objects, one symbol, inside the same `rate_half` family.
[RESOLVED at wiring, 2026-08-11: per the round-37 D11 ruling, (DEG-m)'s
quantity is renamed **`deg_Sh`** (the sigma-design slope degree) in this
node and in all future wired documents. The A1 addenda retain the original
symbol with this node as the disambiguation of record; the PROVED a1_core
node keeps `deg_H` unchanged.]

## Scope

- Everything is (SAT3)-conditional and lives at `T = rho+2`, a class that
  three independent instruments expect EMPTY at `m >= 2`.
- The `m=3` and `m=2` numbers are single witnesses, not distributions.
- The verifier checks the **arithmetic and the double count**, NOT the
  geometry: it does not re-derive the placement argument, and it does not
  re-run any DFS. **ZERO POWER over whether the configurations exist.**
- `(OUT-m)` is a constraint on the configuration space; the source is
  explicit that it is **not progress on residual (ii)'s direction**.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:3329-3350`
  ((OUT-m) POSED with the two coordinator corrections; round 34 bank 3,
  pilot `r34_bivcurve_m34`).
- Refinement to (OUT-ID) and (DEG-m): ibid. :3752-3771 (round 35 bank 3,
  pilot `r35_bivcurve_m4`; coordinator hand-checks at :3686-3690).
- Symbol collision: ibid. :3767-3771.
- Completion-level record: ibid., section "Round-36 (SHARE3-4) addendum"
  (the (DEG-m) completion bullet; line refs in that region drift with
  inline markers — anchor to the title).

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_bivcurve_out_m_identity_and_deg_m/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_bivcurve_out_m_identity_and_deg_m/verify_audit.py
```
