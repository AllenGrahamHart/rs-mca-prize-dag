# dli B-WEAK route close — CONDITIONAL (2026-07-21, maintainer Decision 6)

The endpoint of CONJECTURE B-WEAK, `q^(-t+H) W_cen <= 2^121` at the official
rows (M5-confirmed operative constant: 21-bit joint reserve + 100-bit
aggregate; `notes/M5_CONFIRMATION_2P121.md`), is CONDITIONAL on exactly TWO
wired req predicates, neither proved:

- **(P1) C2''** — the 21-bit joint reserve at the posed /33 junction
  convention (`dli_c2pp_joint_reserve`; pose `notes/C2PP_POSED_20260710.md`;
  F-round state 2: rounds M1 + the 2026-07-13/14 round both survived).
- **(P2) the 100-bit baseline** — `A(R) = prod_L E_L <= 2^100`
  (`dli_marginal_baseline100_coverage`, itself CONDITIONAL on
  **C1'-r3** [`dli_c1r3_gated_envelope_bound`, minted this ceremony,
  twice-survived] and **WCL-ZONE-ext** [`dli_wcl_zone_coverage`,
  CONDITIONAL on its finite slot reds; extended window matches the r3
  ledger `w_max = L+7`]. Assembly arithmetic:
  `E_L <= 1 + 4(1+1/32) = 41/8`, `(41/8)^34 < 2^100`, integer comparison
  `41^34 < 2^202`).

This supersedes the M4-era three-predicate wiring (P3 = ENDPOINT-EXC was
found CIRCULAR at wave-6, catch #181, and replaced by exactly this
decomposition). The M4 exact-rational assembly verifier
(`notes/m4_assembly_verifier.py`, ten mutation controls) remains the banked
arithmetic record; the operative pins P-CONS (2^121 = 21+100, catch #40),
P-FIELD (catch #13), P-ROWS (official rows only), P-CONV (corrected display
1.554, catch #164) carry over unchanged.

## Standing watch (Decision 6)

Amber-2: any C1'-r3 row with `K'_r3 >= 2` on the EXTENDED ledger (2x the iid
asymptote) triggers re-examination; with a sustained iid-excess trend it is
a kill. The literal line `K' > 4` and the frozen falsifiers of
`notes/c1r3_program_20260719/c1r3b_falsifiers.md` stay armed. The legacy
band [1,2) is recorded, non-triggering (extreme-value plateau, c1r3b-C4).

## Pre-registered demotion criteria (none discretionary)

Downgrade CONDITIONAL -> the pre-amber state if ANY of:
1. C2'', C1'-r3, or a WCL slot family is REFUTED in a later round (the
   F-round rule is symmetric: survivals promote, kills demote).
2. The endpoint constant is re-pinned (any change to 2^121, the 21-bit
   reserve, or the 21+100 split) — the assembly re-runs and re-banks.
3. The consumer face (`x4_exactlist_staircase_split` REDUCTION_PACKET's
   half-band line or the `E_U[prod rho_j]` identity) changes — pin A0
   breaks.
4. An official row is shown to have NO accepting certificate (coverage
   refuted, not merely open).
5. Amber-2 fires together with a sustained iid-excess trend.

The conjecture node keeps its unproved character: this is a route-level
close, not a truth upgrade.
