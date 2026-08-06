# PRE-REGISTRATION — (ES) boundary adversary: hunt the accident below balance

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. Role: the ADVERSARIAL lens on
(ES) — the sibling pilot (es_axkatz_transfer) tries to prove a
transfer; this pilot tries to BREAK the conjecture at the boundary.
Neither reads the other's drafts.

## 0. The conjecture under attack (sources of record)

(ES) ENTROPIC SUPPRESSION, the unified terminal of FOUR lanes (band
fullrank, crossing, syzygy via BC routing, u2c/dli RES): sub-balance
codimension implies only periodic divisors on the prescribed windows —
concretely at the crossing instance, the 0/1 codewords of weight r' in
the [2^41, 2^41-w+1, w] RS/cyclic codes are the periodic ones only.

Banked empirics to beat (verbatim, FABLE_AUDIT of mun_anticoncentration):

> ... suppression measured 1-2 orders EARLY (for (ES)); above-balance
> accident witness pins the boundary.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260804/mun_anticoncentration/PREREG.md` section 0 —
  the objects of record (crossing + band instances, the
  characteristic arithmetic delta in {1,2,4}).
- `notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md` — the
  four proved structural constraints on any accidental solution, the
  suppression measurements, and the above-balance witness. The
  constraints are your search-space pruners; the witness is your
  starting template.
- The five verifiers in that dir — the banked exact-count machinery;
  extend, do not rewrite.

## 2. Pre-registered claims

- **(C1)** THE HUNT: a systematic search for an ACCIDENTAL
  (non-periodic) 0/1 codeword strictly BELOW the balance boundary, at
  scaled-down parameter families chosen to respect the row arithmetic
  (delta in {1,2,4}; n | p^delta - 1; the same window shape). Search
  strategies to include at least: (a) deforming the above-balance
  witness downward parameter-by-parameter; (b) structure-guided
  construction through the four constraints (treat each as an
  equality-case analysis: what attains it?); (c) random + algebraic
  hybrid search at the largest ramguard-local-feasible rows. REGISTER
  the parameter grid and search budget in your appended section
  BEFORE running.
- **(C2)** THE CURVE: extend the suppression measurement toward the
  boundary from below — quantify "1-2 orders EARLY" as a fitted decay
  law with the boundary location as a fitted parameter, and state
  whether the fit predicts zero accidents at prize rows with margin.
- **(C3)** THE BOUNDARY: sharpen the above-balance witness — the
  MINIMAL above-balance accident over the searched families (is the
  known witness extremal?), and the exact codimension at which
  accidents switch on.
- **(C4)** Constraint feedback: any structural regularity of the
  near-boundary accidents (support structure, orbit structure under
  the p-Frobenius, divisor pattern) stated as candidate lemma(s) for
  the transfer pilot and mint-4.

## 3. Pre-registered falsifiers / honesty clauses

- A single sub-balance accident REFUTES (ES) as posed — that is a
  campaign-critical catch, not a failure: report the witness with a
  self-contained ramguard-tiny reproduction script and STOP the hunt.
  The four lanes then need the coordinator's re-pose, not yours.
- If the search space at feasible scale cannot reach the sub-balance
  regime for ANY admissible family (scope gap), report the gap
  exactly — a null result from an unreachable regime is NOT evidence
  for (ES) and must not be phrased as such.
- Fitted-curve extrapolation is EVIDENCE, never proof; label it.

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  `notes/pilots_20260806/es_boundary_adversary/`. Never touch
  dag.json, node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.

---

# PILOT-APPENDED PRE-REGISTRATION (written BEFORE any computation)

Author: Opus pilot, round 16, 2026-08-06. Everything below is registered
before a single line of arithmetic is run in this directory.

## A. Scope pins — what counts as an ADMISSIBLE scaled-down family

The prize-row arithmetic is quoted verbatim from
`notes/pilots_20260804/mun_anticoncentration/PREREG.md:41-47`:

> **Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
> `n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
> `j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`. Consequently
> `p > w` on the whole crossing bracket and `p > 2^33 > d` on every band
> depth: **Newton's identities are invertible at every one of the four
> rows**, so a vanishing PREFIX of elementary symmetric functions is
> equivalent to a vanishing prefix of power sums at all four rows.

A scaled-down row `(n, p, w, r')` is IN SCOPE iff all of:

- **(S1)** `n = 2^m` (LEMMA Z is a prime-power theorem — the exact scope
  is `verify_lemmaz.py:251-254`);
- **(S2)** `delta := ord_n(p) in {1, 2, 4}`. (For `n = 2^m` the order is
  automatically a 2-power; `delta in {8,16,...}` is recorded but flagged
  OUT OF SCOPE.)
- **(S3)** `p > w` — Newton invertibility, true at all four prize rows;
- **(S4)** window shape = the PREFIX window `p_s(S) = 0, s = 1..w-1`
  (the crossing instance of LEMMA Y / MC-1);
- **(S5)** `p > n` is TRUE at every prize row (`p >= 2^63.97 > 2^41`) and
  will be RECORDED per hit; toy rows with `p <= n` are reported with the
  caveat attached, never silently.

Distinguished sub-family: the **crossing shape** `r' + w = n/2` (from
`r' = n - k - w`, `k = n/2`). Also swept: `rho := r'/n` near `1/2`
(crossing) and small `r'` (census-feasible).

## B. Definitions registered before measurement

- `Z_w` := the p-cyclotomic closure of `{1,...,w-1}` mod `n`;
  `|Z_w|` = codimension of the code (`PREREG.md:56-61` above).
- **`Lam(n,r',w,p) := log2 C(n,r') - |Z_w| * log2 p`.**
  **Sub-balance := `Lam < 0`. The balance boundary is `Lam = 0`.**
- `M` := least power of two `>= w`; a solution is STRUCTURAL/PERIODIC iff
  it is `n/M`-periodic; structural family is nonempty iff `M | r'`, with
  count `C(n/M, r'/M)` (LEMMA Z, banked).
- **accident** := a solution `S` (|S| = r', all `p_s(S) = 0` for
  `s = 1..w-1` over `F_{p^delta}`) that is NOT `n/M`-periodic.
- **margin of an accident** := `Lam` at its row. Negative margin = the
  accident is strictly BELOW the balance boundary = (ES) refuted.

## C. Method M1 — EXACT BAD-PRIME CENSUS (decides ALL p at once)

For fixed `(n, w, r')` and a subset `S`, put `x_s = sum_{i in S} zeta^{si}`
in `Z[zeta_n]` and `I_S = (x_1, ..., x_{w-1})`. Registered claim:
the set of characteristics in which `S` or a Galois-dilate of `S` is a
solution is EXACTLY `{p prime : p | N(I_S)}`, equivalently
`{p : deg gcd(Phi_n, A_1, ..., A_{w-1}) >= 1 over F_p}` with
`A_s(X) = chi_S(X^s) mod (X^n - 1)`. Implementation: candidate primes =
prime divisors of `gcd_s Res(Phi_n, A_s)`, then each candidate CONFIRMED
by an exact gcd computation mod p. This replaces a p-sweep by a finite
exact decision over all p simultaneously.

Registered budget: `n = 16` (all `r' <= 8`, all `2 <= w <= r'`);
`n = 32` (`r' <= 8`); `n = 64` (`r' <= 5`). Orbit reduction by rotation,
complement and dilation (each verified computationally to preserve the
bad-prime set before being used as a reduction).

## D. Method M2 — MITM exhaustive solution census at rho ~ 1/2

Meet-in-the-middle on the power-sum vector: exact enumeration of ALL
solutions for a given `(n, p, delta, w)` at every weight simultaneously.
`n = 16` full `2^16`; `n = 32` via `2^16 + 2^16` halves. This removes the
`p^{w-1}` DP bottleneck of round-15's `verify_fourier.py` (which is why
that file could only reach `w = 2` and `p <= ~1400`), so arbitrary `w`
and large `p` become reachable. Sweep p over admissible primes at
`r' = n/2` and at the crossing shape; measure the suppression threshold.

## E. Method M3 — the NORM FLOOR (a proved sub-case of (ES))

Registered as a claim to be PROVED and then verified numerically:
if `S` is an accident then some `x_s != 0` in characteristic zero
(else LEMMA Z makes `S` periodic), and a prime `P | p` of `Q(zeta_n)` has
residue degree exactly `delta = ord_n(p)`, so `p^delta = N(P) <= |N(x_s)|`.
With Parseval + AM-GM over the `n/2` conjugates this gives
**`p^delta <= ( M * r'(n-r')/n )^{n/4}`**. Consequence: accidents are
IMPOSSIBLE above that bound, so the hunt only has to cover the zone
`Lam < 0` AND `p^delta <= (M r'(n-r')/n)^{n/4}`. I register in advance
that this bound is expected to be VACUOUS at the prize rows and will be
reported as such.

## F. Search budget

At most 5 `ramguard local` runs (<= 5 min each) per method, plus
`ramguard tiny` for all reproduction scripts; total compute <= ~30 min.
No Modal, no network.

## G. Registered falsifiers

- **F1 (primary).** An IN-SCOPE accident with `Lam < 0` REFUTES (ES) as
  posed. Report the witness + a self-contained `ramguard tiny`
  reproduction script and STOP the hunt.
- **F2.** An accident violating the M3 norm floor => M3 is WRONG and is
  retracted in full.
- **F3 (cross-validation).** A census bad prime that MITM does not
  reproduce at the same row (or vice versa) => machinery bug; BOTH
  results retracted rather than reported.
- **F4 (honesty).** If no admissible family reachable at feasible scale
  attains `Lam < 0`, the null result is a SCOPE GAP and must NOT be
  phrased as evidence for (ES).

## H. Registered prediction (so this pilot can be scored against itself)

I predict, before computing: sub-balance accidents DO exist at toy scale
with SMALL negative margin (because the bad-prime set of a "random" S
contains occasional large primes, and admissibility only costs a constant
factor), while the DEEPEST attainable margin grows like `O(log n)` and
not like `Theta(n)`. If instead the entire uncovered zone at `n <= 32` is
accident-free, that is strong evidence FOR (ES) and I will say so.
