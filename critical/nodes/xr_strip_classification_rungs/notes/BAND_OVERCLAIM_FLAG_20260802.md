# Over-claim flag 2026-08-02: band removal asserted, not proved

**Status of this note: surfaced; scope-narrowing recommended, decision
with coordinator/maintainer.** Full adjudication:
`notes/pilots_20260802/xr_bridge_semantics/{REPORT,FABLE_AUDIT}.md`.

What is PROVED in this node and untouched by the flag: the forcing
algebra (`proof.md:9-20` — any distinct-slope pair with common core
`|R| >= k+1` forces a degree-<k codeword pair agreeing on >k points;
88-check toy replay incl. 4,662 nonvacuous forced pairs), the quotient
census, and the six-row integer arithmetic (69 checks).

What is NOT proved: `proof.md:20-22` ("This is exactly the
tangent/classified event removed before the generic remainder.
Consequently the generic post-strip family has pairwise cores at most
`k`."). The tangent strip's actual predicate is single-slope
over-agreement > A (`stratification_partition_thm`, P2/T2); the only
proved core-based payment is the pencil cascade at `core >= A-1`. The
band `core in [k+1, A-2]` — non-empty at every official row — is
FORCED but neither removed nor charged by anything banked. The honest
record of this open work was the archived node
`archive/retraction_xr_20260705/xr_partial_tangent_band` (cut from the
dag); `xr_smallcore_spread_count/conditional.md:66-67` still lists band
survivors as a re-surgery trigger, which is incoherent with this node's
removal claim.

Recommended repair (with the R2 bridge edit, one coordinated change):
restate item 3 as — forcing PROVED for all cores >= k+1; removal/charge
PROVED only at `r >= A-1`; the band is CLASSIFIED, not charged, and is
carried by the widened bridge partition into P-A1's obligation
(`core in [k, A-2]`, matching `F5_SKELETON.md:398` and the pinned
verifier's `J >= k` class). The node's arithmetic and replay stand.

> **[AMENDED 2026-08-02 — cascade payment audit
> (`notes/pilots_20260802/xr_cascade_payment_audit/`), coordinator-
> verified.]** The repair text above is itself over-generous: NO
> core-based CHARGE is proved at ANY threshold — `xr_pencil_cascade`'s
> "paid" is unsourced (its PROVED status covers forcing + cascade
> only; see that node's PAYMENT_UNSOURCED_FLAG note). The corrected
> restatement of item 3: forcing PROVED for all cores >= k+1; the
> generic-branch core ceiling A-1 comes from genericity + this node's
> own forcing algebra (core = A between exact-A selected supports
> forces a joint A-support explanation => nongeneric), NOT from a
> payment; the entire range [k+1, A-1] is CLASSIFIED, not charged,
> and P-A1's widened obligation becomes core in [k, A-1] (line caps
> exactly double vs A-2). Arithmetic and replay still stand.
