# Pro dossier — Brief 5 (f2_growing_order_myerson) — received 2026-08-01

> **Provenance:** GPT Pro response to
> `notes/pro_briefs_20260801/BRIEF_5_f2_growing_order_myerson.md`, relayed
> by the maintainer (final dossier of the six-brief cycle). Companion
> script: `verify_brief5_f2_myerson_program_arithmetic.py` (this
> directory; replayed under ramguard 2026-08-01, full PASS).
> **Fable audit:** `BRIEF5_DOSSIER_AUDIT.md`. Planning only; no DAG change.
> Minor erratum: Appendix C lists `f2_conditional_close` under
> background/; it lives in critical/.

## Executive decision (Pro's)

CONDITIONAL GO with a **mandatory interface repair first**: the node's
"growing-order Myerson max-to-mean" wording is historically accurate but
executably wrong. The magnitude theory (diagonalization, moments,
second-moment denominator, prime-power transfer) is largely BANKED; the
live residue is the **signed weighted parity alignment**: the correlation
of the sign field `epsilon_c = (-1)^(K_c + U_c)` (with the load-bearing
carry term) against the weight field `exp(S_c)`, after corrected
structural-drift subtraction. Recommended: mint a consumer-exact sibling
`f2_weighted_parity_alignment` with an equivalence/implication wrapper.

## The route fence that redefines the target (verified exactly)

**Balanced signs + constant max/mean do NOT imply weighted alignment:**
N/2 signs +1 at weight 3, N/2 signs -1 at weight 1 gives zero sign mean,
max/mean = 3/2, yet normalized alignment sqrt(N/5) — 18.84 bits > 2^15 at
N = 2^40. Every sign-only or magnitude-only theorem is insufficient; this
counterexample is a required-to-trip mutation in every future verifier.

## The strategic simplification (verified exactly)

The sixteen moving rungs (2^25..2^40) sum to 2^41 - 2^25. Even under the
most pessimistic log-additive composition, a per-rung exponent `n_r/3`
spends 732,996,567,040 bits — inside the 1.05e12 allowance with 317G bits
of slack — while `n_r/2` fails by 49.5G bits (threshold theta* =
0.4774920...). **Square-root cancellation may be unnecessary**: the
consumer-exact target F2-ALIGN-1/3 (`R <= 2^(n_r/3)` per rung) is
exponentially weaker than the campaign's 2^o(n) ambition — pending the
seam theorem PP5.0, which must freeze the actual composition law (add /
Cauchy / multiply). Under an orthogonal additive partition, even 19n/20
per top sector would fit. Also fenced: bare `2^o(n)` is NOT a finite
certificate (a 2^(10^15 + sqrt(n)) counterexample beats the label and
busts the allowance).

## Other verified content

- Notation hazard pinned: ambient N = 2^41 vs moving-top n = 2^40.
- Structural drift is level-dependent: `M_j = 2^ceil(log2(j+1))` —
  2^(n/4) is valid ONLY at j = 2,3; j = 4 needs n/8 (mutation-tested).
- Orbit invariance is a quotient, not an average: lifting by orbit size L
  multiplies alignment by sqrt(L) (~2^28 at the proxy); the correct model
  is one sign per orbit.
- Annealed fence: absolute values lose n·log2(4/pi) ~ 383G bits.
- Block calibration: one certified parity-contraction bit per 43 moving
  coordinates clears the campaign proxy; one per 44 misses. The local
  target is startlingly weak.
- **Literature (post-dates our 2026-07-27 sweep):** the June 2026
  revision of Cornelissen-Hokken-Ringeling (Gaussian-period Mahler
  measures, Wasserstein methods) — its fixed-k error is ~2^50.79 at the
  tower proxy k ~ p^0.77 (vacuous; effective only at genuinely small k,
  verified both ways), and it treats Mahler MAGNITUDE, not signed parity.
  Method lead only (Wasserstein comparison, random walks, cyclovariety
  geometry). Kowalski-Untrau and Bonolis-Kowalski-Woo: possible
  exceptional-stratum tools, each requiring a printed
  growing-parameter complexity ledger before import.

## Architecture (compressed)

Exact seam (PP5.0, gate for everything) -> four-path exact toy compiler ->
first-descent normal form over F_(p^2) (orientation variables on conjugate
pairs; trace-real equations paid, moving equations open) -> **carry
compression audit** (K couples all pairs through the mod-2p partial sum;
the first scientific question is whether the pair grammar compresses it to
a bounded descriptor — a negative answer is itself a valuable route fence)
-> block transfer matrices with local weighted contraction OR canonical
exceptional owners (doubling-zero, structural coset, high-energy branch,
cyclotomic-norm, low-degree relation; raw-K2 only after a typed bridge) ->
first-descent theorem -> functorial tower transport -> exact 16-rung
assembly. Alternative routes: exact sign-reversing pairing (pilot before
trusting); lattice-parity chambers (Ehrhart mod 2, complexity-fenced);
local Dedekind reciprocity (child-to-child, not global size bounds).
Twelve closed method classes inherited from the campaign as the death
ledger. Work packages PP5.0-PP5.16, gates G5.0-G5.9, mutation battery.

## Full text

Preserved at the maintainer's thread and session record; this summary +
audit + replay script are the load-bearing extract.
