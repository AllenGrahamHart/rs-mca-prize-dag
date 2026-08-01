# Dated catch (2026-08-01): the M1/C2R2 accident classifier runs in binary64

Found by the Brief-2 Pro dossier's stress test; confirmed at source:
`m1_dli_m1_tower_census_modal.py:571` computes `Eck = cs[k] / cn[k]` and
compares against `theta = 2.0` in binary64. Exact fixture: with
`cs = 2^61 + 1`, `cn = an = asum = 2^60`, the exact class ratio is
`2 + 2^-60 > 2` but the float path rounds it to `2.0` and misses the
accident.

Scope of impact: the M1 and C2R2 experiments are DIAGNOSTIC instruments;
every measured cell in the banked rounds sits far from the theta boundary,
so no recorded verdict is alleged to flip. But the exact rule

```text
ACCIDENT  iff  cs[k] * an[k] > 2 * cn[k] * asum[k]
```

(integer cross-multiplication, no division) is MANDATORY for any
proof-facing compiler, descriptor-discovery run, or verdict path built on
this code. Any future reuse of `decompose_row` must replace the division
branch first.

Cross-references: `notes/pro_briefs_20260801/responses/BRIEF2_PRO_DOSSIER.md`
(Correction D), `.../BRIEF2_DOSSIER_AUDIT.md`, and the exact fixture in
`.../verify_brief2_c2pp_program_arithmetic.py` (check 6).
