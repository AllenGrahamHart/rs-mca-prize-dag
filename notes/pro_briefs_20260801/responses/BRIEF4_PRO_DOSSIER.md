# Pro dossier — Brief 4 (xr_lowcore_spread_heart / P-B) — received 2026-08-01

> **Provenance:** GPT Pro response to
> `notes/pro_briefs_20260801/BRIEF_4_xr_lowcore_spread_heart.md`, relayed by
> the maintainer. Share link:
> <https://chatgpt.com/share/6a6ddb06-7e20-83ed-9e21-fd8e2e74c192>.
> Pro audited our mirror at commit `026d8be7`. Companion script:
> `verify_brief4_lowcore_program_arithmetic.py` (this directory; replayed
> under ramguard on 2026-08-01, PASS).
> **Fable audit:** `BRIEF4_DOSSIER_AUDIT.md` (this directory) — read that
> first; two of the brief's own suggestions are REFUTED by this dossier and
> the corrections are recorded there.
> Planning document only — not a proof, no DAG status change.

## Executive decision (Pro's, verbatim in substance)

Brief 4 is the most plausible first conversion candidate — because of the
banked exact infrastructure, not because the remaining theorem is easy. But
the stress test changes the brief's reading in one important way:

**The missing theorem is not a better per-difference packing bound. The
first indispensable new theorem is an RS-specific source of additive
energy (or an equivalent canonical bound on realized support differences).
Pure set-system combinatorics cannot provide it.**

Recommended posture: **conditional GO**; NO fleet-scale case campaign yet;
first pay two gates: (1) selector-semantics closure under puncture,
(2) an RS-specific difference-owner or energy-producer theorem with
composable constants.

## The two fences (both verified on our side)

### Fence 1 — support-only combinatorics is structurally insufficient

Ignore RS realization. Constant-weight A-subset families with the P-B
intersection cap `|S ∩ T| <= K-1` can have size at least
`Q = C(N,A) / sum_{i<H} C(A,i) C(N-A,i)` (greedy/GV). On the RowC rows:
`log2 Q = 759.32 / 495.40 / 310.02` against a budget of 33 bits.
Moreover a greedy Sidon extraction (each new point excluded by at most
`2m^3 + m^2` difference-collision equations in `Z^N`) yields a subfamily of
size ~ `Q^(1/3)` — still hundreds of bits above budget — in which **every
nonzero oriented difference occurs exactly once**. Such families have
`E_* = M(M-1)`, so no energy producer of the form
`E_* >= M^2(M-1)/N^2` can hold for abstract families.

Consequence: any P-B proof must use at least one RS-specific input
(syndrome line, degree-<K realization, first-match selector, genericity,
parity-stack coupling). Arguments using only support size, the
intersection cap, the difference identity, generic packing, or fixed-fibre
recursion are **structurally incapable** of reaching P-B. This is a
fatal-route fence, not a falsifier of P-B.

### Fence 2 — exact composition constants (the multiplicity-two obstruction)

Under the candidate producer `E_* >= M^2(M-1)/N^2` at `M > 8N^3`, the
already-banked wide (`t>=K`, multiplicity one) and near-K
(`c <= C0`) bands consume exactly `(R_C0+1)/(8N)` of the baseline:

```text
RowC 1/4    791/1024   (leaves 233/1024)
RowC 1/8    129/8192
RowC 1/16   225/8192
prize 1/4   ~0.2500
prize 1/8   ~0.0148
prize 1/16  ~0.0023
```

A difference-owner theorem with multiplicity two yields only half the
baseline via Cauchy-Schwarz — and RowC 1/4 already spends `791/1024 > 1/2`
before any open middle width. **Multiplicity <= 2 cannot close all six
rows through the simple energy composition.** Owner multiplicity ONE
(`D_* <= N^2(M-1)`), a sharpened RowC 1/4 near-K cap (6,327 -> below
4,096), or the rank-five fallback for RowC 1/4 are the live options.

### Fence 3 — naive recursion loses N^2

Applying the cubic target recursively per fibre gives
`E_mid <= 8N^3 M(M-1)`, which is a factor ~N^2 too weak against the
producer baseline at threshold. Descent termination (max depths 42/21/15
RowC, 63/31/31 prize) is necessary, NOT sufficient; the recursion needs
amortized collision ownership or a potential function, not per-fibre
cubic bounds.

## Program architecture (Pro's proposal, adopted for discussion)

- **Track A (global, all six rows):** decorated recursive family class
  `RecPB` closed under puncture (Option S2 — do NOT assume first-match
  is hereditary; that inference is currently invalid without a transport
  lemma) -> RS-specific producer theorem (owner form `D_* <= N^2(M-1)`
  preferred; weighted and direct-rectangle forms permitted) -> single
  middle-width energy ledger in one exact currency
  (`sum of band debits < producer coefficient`) -> composition theorem
  (one line, banked early as the common contract).
- **Track B (finite fallback, RowC):** the banked rank-five reduction
  (residual deficiency pairs 8/49/274; split-pencil, Maxwell cores,
  rank-two localization to 13/13/10 active coordinates) as an m2-style
  finite atlas — pays RowC 1/4 if Track A's constant fails there.
  High-rank (rho >= 3) dual trades need their own boundedness theorem
  first; `L <= 480 blocks` is finite but NOT a practical census.

Phase 0 gates before any fleet campaign: PP4.0 semantic freeze (selector,
genericity, infinity, row table, import SHAs); PP4.1 RecPB definition +
closure theorem; PP4.2 producer pilot on exhaustively enumerable small
rows (with support-only negative controls); PP4.3 the exact six-row budget
checker built BEFORE the middle theorem. Stop/go gates G0-G5 and the
pre-registered falsifier suite are in the dossier source.

## Verified constants ledger (all replayed exactly on our side)

- Six-row table (N,K,H,A,r,d): matches our rows; `A = K + N/256 + 1`
  (rates 1/4, 1/8), `A = K + N/512 + 1` (rate 1/16).
- Near-K caps: `R_c = floor(C(N-2K+2c,c)/C(H+c-1,c))`; paid prefixes
  c<=2/1/1 (RowC), c<=6/5/4 (prize); boundary values
  6,327/128/224 and 4,398,046,497,508 / 260,919,262,630 / 40,282,095,485;
  first unpaid values 411,273/14,171/40,455 (RowC).
- Descent invariants `d = N-2K`, `h = A-K` preserved by puncture:
  `(N',K',A') = (d+2c, c, c+h)`.
- Producer compatibility ceilings before middle debit:
  mu = 1/63/36 (RowC), 4 (practically <=3)/67/436 (prize).
- Distinct-support lemma (globally generic branch): verified — equal
  supports at two slopes force a joint codeword-pair explanation.
- Rank frontier imports: first open selector ranks 5,5,5 (RowC) and
  17,17,15 (prize — the corrected-of-record values, not the stale
  16,16,15). Flat-nullity census and 13/13/10 localization: match.

## Pro's summary message (§28, condensed)

P-B chosen for its developed exact interface. Critical correction to the
brief's optimistic reading: no support-only aggregation or recursion can
close P-B; the program must begin with an RS-specific
difference-compression/energy-production theorem (natural target
`D_* <= N^2(M-1)`, giving `E_* >= M^2(M-1)/N^2`). Constants matter:
RowC 1/4's banked bands consume exactly 791/1024 of that baseline, so a
multiplicity-two owner cannot compose there. Conditional GO with two
preliminary gates; single middle-width energy ledger after; rank-five
atlas as the RowC 1/4 fallback. Launching the recursive census before the
producer gate risks a structurally doomed campaign.

## Full text

The complete dossier (28 sections + appendices: exact pose and routing
pins, fibre normal form, banked-theorem inventory, stress tests I-V,
two-track architecture, phase-0 work packages PP4.0-PP4.3, node grammar
proposal, certificate/checker design, falsifier suite, pilot experiment
designs, risk register, stop/go gates G0-G5, what-not-to-do list, work
breakdown A-F, partial-result menu) is preserved at the share link above
and in the maintainer's session record. This banked summary + the
verified-constants ledger + the companion script are the load-bearing
extract; wire future nodes to THIS file and the audit note.
