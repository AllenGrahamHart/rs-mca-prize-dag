# Pro dossier — Brief 1 (dli_c1r3_gated_envelope_bound / C1'-r3) — received 2026-08-01

> **Provenance:** GPT Pro response to
> `notes/pro_briefs_20260801/BRIEF_1_dli_c1r3_gated_envelope.md`, relayed by
> the maintainer (same thread as the Brief-4 dossier). Pro audited our
> mirror at `026d8be7`. Companion script:
> `verify_brief1_c1r3_program_arithmetic.py` (this directory; replayed under
> ramguard 2026-08-01, full PASS including an exhaustive toy-row two-engine
> check of the core identities).
> **Fable audit:** `BRIEF1_DOSSIER_AUDIT.md` — read first; the brief's
> "route 3" (row census) is REFUTED and the correction is recorded there.
> Planning document only — not a proof, no DAG status change.

## Executive decision (Pro's)

Brief 1 is the second-best conversion target — but only after replacing the
brief's most concrete route. **There is no useful finite official-row
census:** `official_row_primes_pinning` (PROVED) pins universal
quantification over admissible fields; even under the `q < 2^256` cap the
progression `q = 1 + k*2^41` has `2^215 - 1` candidates, and the round-2
exact DP is `Theta(q)` in state (>= 2^44 bytes at the smallest official
scale). Conditional GO with the route replaced by a consumer-exact
zero-window theorem.

## The proposed new core

**C1-ZERO / SWIF-4 (official zero-window inverse flatness).** On an
official schedule row (`N = 256L`, `L` in the corrected 34-level dyadic
schedule, `q < 2^256`, `2^41 | q-1`): if the Boolean subset-sum map has
`L^2` fibre discrepancy `V(q,L) > 4*2^N`, then the cyclotomic ideal
`I_(q,L) = p_1 p_3 ... p_(2L-1)` contains a reduced primitive signed vector
of weight in `[L+1, L+7]`.

Composition: **Newton short-window exclusion (banked) empties the window at
every `L >= 8`; the ten `dli_wcl_slot_*_emptiness` TARGETs empty it at
`L in {1,2,4}`. Hence ten slots + C1-ZERO ==> the consumer**
(`dli_marginal_baseline100_coverage`), with `W_ext = 0` — stronger than the
`W <= 1/32` the consumer's assembly uses. The broad C1'-r3 (arbitrary
aspect `N >= 16L`, linear `W_ext` correction, short-relation clusters)
remains a stronger successor, NOT on the critical path.

Pro independently derived the ten-cell residual from Newton + banked
exclusions and it matches our board's ten slot TARGETs cell-for-cell.

## Exact equivalent forms (all verified here on an exhaustive toy row)

With `Z = sum_(d in ternary kernel) 2^(-w(d))` and `r = q^L/2^N`:

```text
E = r Z                                  (relation partition function)
E - 1 = r (Z - 1/r)                      (baseline subtraction, load-bearing)
sum_s (m_s - 2^N/q^L)^2 = 2^N (Z - 1/r)  (Boolean fibre variance)
C1'-r3  <=>  V(q,L) <= 4*2^N (1+W_ext)   (VAR-C1)
        <=>  chi^2(mu||uniform) <= 4r(1+W_ext)
```

Plus the lattice form: the Boolean cube reduced modulo the completely split
cyclotomic ideal `I_(q,L)` (norm `q^L`) in `Z[X]/(X^N+1)`; sparse ideal
vectors are the ledger.

## The 256-basis factorisation (new; verified at L=1,2,4 on exact fields)

On official levels `N = 256L`: writing `y = a + 256b` and `theta = omega^256`
(exact order `2L`), the `a`-th column block is `A_a = D_a F` with `F` the
odd-power Vandermonde of `theta` — **all 256 blocks are bases** of `F_q^L`.
Consequences: each block Fourier marginal `C_a = A_a^T lambda` is EXACTLY
iid-uniform; the blocks are coupled by one deterministic orbit
`C_a = M^a C_0`, `M = F^T D_1 F^(-T)`. "iid saturation" now has exact
content: all excess is cross-block dependence, and short signed relations
are its low-complexity certificates. C1 is a 256-step finite-orbit mixing
problem.

## Consumer arithmetic (verified)

`E_j <= 41/8` per level; `(41/8)^34 < 2^100` via `41^34 < 2^202`; the
assembly tolerates allowance 6 and fails at 7 (C1 uses 4). The delicate
part is flatness, not the final product.

## Program architecture (phases; details in the source dossier)

Phase 0 (cheap, bank first): scope-reduction node; variance-equivalence
node; cyclotomic-ideal interface; 256-block factorisation node.
Phase 1 (falsifier-first): small exact SWIF census (complete split-prime
bands, all embedding orbits, engineered dense-relation primes, multi-orbit
stacks); synthetic route-cut suite over matrix classes (full-rank -> MDS ->
256 bases -> operator powers -> exact cyclotomic orbit) to locate the
genuinely necessary hypotheses. **Gate: do not launch a fleet unless SWIF-4
survives every exact class-5 test.**
Phase 2-3: finite block-profile grammar (completeness theorem mandatory);
generic-profile iid box-count theorem (uniform in q); singular-profile ->
short-relation extractor (the algebraic heart); layer-cake/dyadic
composition to `4r`.
Candidate engines: finite-orbit flattening, discrete Brascamp-Lieb box
counting, entropic BSG/quasicube, lattice smoothing/transference, dyadic
large-spectrum comparison; fixed-order algebra at L in {1,2,4} + uniform
theorem at L >= 8. Pressure route stays a fallback, not disguised C1.

## Death ledger additions (route fences, accepted)

No official-prime enumeration; no q-sized DP promotion; no analogue-gate
(v2>=20) transport by extrapolation; no uniform v2-surplus argument (the
top level 2N = 2^41 has ZERO surplus over the ambient split); no
minimum-distance/MDS-weight-enumerator route (bounded alphabet is
essential); no per-frequency uniform bound (refuted); no density-one prime
theorem (one exceptional admissible field defeats the consumer); work with
`Z - 1/r`, never `Z - 1`.

## Full text

Complete dossier (25 sections + appendices A-E: source map, drift rule,
death ledger, consumer scope, four equivalent forms, 256-basis proofs,
falsification-round inventory, 20-item stress test, three-level scope
surgery, SWIF-4, spectrum-owner interface for full C1, phase architecture,
engine candidates, finite witness-type indexing, layer-cake budgets,
falsifier suite, pilot designs, certificate schemas, complexity contract,
node contracts, go/no-go gates 0-7, risk register, work packages A-F,
8 questions for Fable) preserved at the maintainer's thread and in the
session record. This summary + the audit + the replay script are the
load-bearing extract.
