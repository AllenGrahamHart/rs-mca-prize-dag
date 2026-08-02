# Payment flag 2026-08-02: "paid" is unsourced; PROVED covers forcing + cascade only

**Status of this note: surfaced; scope-narrowing recommended, decision
with coordinator/maintainer.** Full audit:
`notes/pilots_20260802/xr_cascade_payment_audit/{REPORT,FABLE_AUDIT}.md`.

What is PROVED and untouched: the forcing lemma at core >= k+t-1 = A-1
(interpolation + two-slope inversion) and the cascade (each off-core
disagreement point upgrades exactly one slope to agreement EXACTLY A).
E27's S5/S6b/S6c replays verify exactly this algebra.

What is NOT proved: "the pair is a TANGENT-PENCIL pair — paid."
(a) T2/P2 (single-slope agreement > A) never fires on the cascade tier
— the upgrade map's own formula lands at exactly A. (b) The
coordinate-injection column's hypothesis is |T| <= n-A; the cascade
tier sits at |T| <= n-A+1, one notch outside, and even the (unbanked)
one-line extension saturates the entire B_tan slot (ratio 1.0000 on
all six rows) while a pair can carry MULTIPLE forced pencils (realized
on the F_17 witness — nothing banked bounds the pencil count). (c) The
residual target F5-OS is quantified at cores <= A-2, so the A-1 tier
sits in NEITHER column. (d) The upstream sense of "paid" is membership
in rigidity_kernel clause (i) — status CONJECTURE — and E27 itself
disclaims the netting. The pair-level payment in nondeep regime is
REFUTED in-tree (`xr_nondeep_tangent_supportwise_payment`); the deep
condition 3r <= n-k fails on all six official rows.

Also needing scope: the "multiplicity is ~n-core" clause silently
assumes ONE forced pencil (F_17: observed 8 > n-core = 6).

Compensating positive (sourced WITHOUT this node): in the globally
generic branch, pairwise cores are <= A-1 unconditionally — two
distinct-slope exact-A selected supports with core = A coincide, and
the strip forcing algebra then yields a joint A-support explanation,
i.e. the nongeneric branch. So the loss is one notch (A-2 -> A-1 as
the honest generic ceiling), not a collapse.

Consequences recorded elsewhere: the W/T band-repair fork tilts to
Route W (see the bridge and P-A1 node notes); consumer wording repairs
queued for `xr_clean_residual_any_gate/conditional.md` ("removes" ->
"classifies") and `notes/kernel_basis/WP7_WORSTWORD_VERDICT.md`. Two
proof obligations opened: the injection-extension one-liner and the
per-pair forced-pencil-count lemma (= the k-packing object).
