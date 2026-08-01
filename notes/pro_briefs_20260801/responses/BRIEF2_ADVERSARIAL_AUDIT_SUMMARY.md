# Pro's adversarial self-audit of the Brief-2 (C2'') dossier — 2026-08-01

> **Provenance:** Pro's adversarial audit of its own C2'' Bellman/owner
> dossier (same thread), relayed by the maintainer. Checker:
> `verify_adversarial_audit_brief2_c2pp.py` (replayed under ramguard, all
> six fixtures PASS). **Fable verification:** the gate-prime arithmetic
> (v_2(3*2^41) = 41), the linear identity E[prod q*1[l_i=0]] =
> q^(m-rank), the nullity ledgers, and C(33,12) were re-derived by hand.
> **Addendum recorded on `BRIEF2_DOSSIER_AUDIT.md`.** No DAG changes.

## Retired (with exact fixtures)

The spine "toy compiler -> finite descriptor -> bounded owner grammar ->
Bellman supersolution -> 2^21" is retired:

- **The 32-wise trap (the centerpiece):** at the ADMISSIBLE gate prime
  q = 3*2^41+1, the 33 moment-curve forms on F_q^32 are 32-wise
  independent — every proper subtower exactly iid — yet the full product
  is q > 2^21, via a unique circuit supported on ALL 33 junctions. A
  tower can look perfectly flat at every experimentally accessible depth
  and fail only at the last global relation. Kills: finite toy depth,
  bounded-support owner grammars, low-degree harmonics, per-junction
  chains — anything not engaging all 33 junctions at once.
- **Four-wise trap:** rank-11 system, no dependency of support <= 4,
  full ratio 2^22 — extends the pairwise trap; kills degree-4 statistics.
- **Circuit explosion:** F_37^11 moment curve — every 12-subset a
  circuit, 354,817,320 support-minimal circuits. Support-minimality
  implies neither sparsity nor enumerability.
- **Continuation amplification:** a probability-1/2 owner with 32
  mean-one future factors contributes 2^31 — future-inclusive owner
  debits contain the original problem unless owner-local data provably
  control continuation.
- **Rank/bounded descriptors:** same rank, different span, different
  transition; spans are q-dependent. Bellman existence is tautological
  (the identity descriptor always works); descriptor-collision PASS is
  one-sided (memorisation converges to zero collisions).

## Retroactive demotions on our side (recorded)

1. **The C2R2 "14.53% of reserve" margin is NOT evidence about the true
   joint ratio** — it stacks one-junction proxies, and the 4-wise trap
   realizes all-local-statistics-iid with truth 2^22. Empirical support
   for the measured proxy only.
2. **Brief-3's Track B posture inherits the demotion:** Bellman is a
   CHECKER interface everywhere (P-A2 included), not a proof engine,
   until a structural compression theorem exists.
3. **Descriptor-collision audits across briefs 2/3/4/5: FAIL is
   informative; PASS is only permission to formulate a theorem.**

## Retained

PP2.0 seam, PP2.1 true compiler, PP2.2 generic identities, exact Bellman
ground truth, first-owner partition (bookkeeping, not mechanism),
exact-rational thresholds, the mutation battery (now + the 32-wise trap
as required-to-trip).

## The replacement: global cross-junction information-nullity

Linear prototype (EXACT, verified): E[prod q*1[l_i=0]] = q^(m - rank);
the entire joint loss is q^nullity. Gibbs dual: nullity = constraint
reward not paid by entropy cost (4-wise: 33 - 11 = 22 bits; gate model:
33 log q - 32 log q). Proposed DLI seam: expand rho_j into latent
choices, form the combined constraint object per record tau, define
delta(tau) = sum local ranks - global rank, and prove
R_joint = E_pi[q^delta] (or a dominating version). C2'' becomes the
weighted nullity tail theorem sum_d q^d Pr(delta = d) <= 2^21 — at
official q even delta = 1 exceeds the reserve, so positive nullity must
be correspondingly rare. Fundamental-circuit ownership against a
canonical basis gives owner count = delta exactly (ownership as
certificate of the invariant, not its bound). NOT minted: the identity
is proven only for the abstract linear model; the DLI seam (NUL0-NUL4)
is the open construction, gated.

## Posture

Conditional exploratory GO for NUL0-NUL4 only (seam, latent expansion,
combined constraint object, rank-partition identity, compiler replay
with the 32-wise trap required-to-trip). Kill line: if the first true
multi-junction compiler cannot reproduce X/A through an exact or
dominating rank-defect partition, the C2'' strategy is RETIRED, not
rescued by descriptor refinement.

## The emerging pattern (two audits in)

Both adversarial rounds landed on the same structure: local/bounded
statistics can never see the decisive GLOBAL invariant, and the
replacement in each case is an exact global identity — doubling-cycle
products for C1, cross-junction nullity for C2''. The black hole is now
sharply characterized: each lane needs DLI/RS-specific control of ONE
global quantity, and the abstract versions of those quantities are
provably uncontrollable.
