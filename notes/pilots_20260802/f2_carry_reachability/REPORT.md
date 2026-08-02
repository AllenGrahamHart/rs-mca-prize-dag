# F2A.2 — carry reachability audit (pilot, 2026-08-02)

> **Verdict: OUTCOME-FULL.** On exact first-descent models the reachable
> carry sumset fills ALL of Z/(2p) after `log2(2p) + O(1)` conjugate
> pairs — about 36 pairs out of ~2^39 at the official shape — and the
> reachable-continuation Myhill-Nerode quotient then attains the full
> `2p ~ 2^32` width. **Bounded carry compression is formally dead**; the
> carry-DFT route is mandatory. The only exception is an exactly
> characterised measure-zero class where the question is vacuous.
> Pilot by an Opus 5 subagent under planner direction; audited and banked
> by Fable (see FABLE_AUDIT.md). No DAG change, no status flip.

## Key exact findings

1. **Delta normal form (new, exact):** with `c = a_c + b_c w`,
   `y = a_y + b_y w`, `w^2 = N`: `Tr(c y) = 2(a_c a_y + N b_c b_y)` and
   `Tr(c y^p) = 2(a_c a_y - N b_c b_y)`, so the orientation difference is
   `delta = 4 N b_c b_y (mod p)` — verified exactly on all p <= 47 rows.
2. **Frequency dichotomy (proved):** `c in F_p^*` gives delta = 0 on
   every pair (the carry is CONSTANT — a vacuous null class of density
   ~(p+1)^-j); every other c has delta != 0 mod p on EVERY pair, and
   since Z/p has no proper nontrivial subgroup there is no intermediate
   structure to be trapped in.
3. **SHARP LAW A (0/635 violations):** `c not in F_p` and
   `m >= log2(2p)+2` => the difference sumset IS Z/(2p).
4. **SHARP LAW B (0/595 violations, the operative one):** at
   `m >= 2(log2(2p)+2)` the reachable-continuation Myhill-Nerode carry
   width equals the FULL 2p. Median width/2p = 1.0000.
5. **Covering number is logarithmic:** k_full = log2(2p) + 4 exactly and
   stably from p ~ 4000 to p ~ 10^6 (information-theoretic maximum
   |S_k| = min(2^k, 2p), median ratio 1.000). Even the unconditional
   Olson / Dias da Silva-Hamidoune bound already forces >= p states.
6. **Robustness:** restricting orientations to a random affine
   GF(2)-subspace of dimension d gives reachable ~ min(2^d, 2p): only a
   descent freezing all but O(1) of ~2^39 orientation bits could bound
   the carry — impossible for a seam carrying exponential configuration
   entropy.
7. **F2A.4 seeds:** carry-DFT L1 mass = (2/pi) ln p + 0.96252283 + O(p^-2)
   (< 4 bits at official p — diagonalisation essentially free); weight
   balance median 0.9501 (not the bottleneck); generic worst-mode
   contraction >= 0.2426 bits/pair with ZERO dead modes at five sampled
   primes — kill line K2 NOT triggered; **one named resonance owner:
   mode k = p on the trace-zero line** (exact proof: s(-) = p - s(+) and
   f(p-s) = f(s), so |M_i(p)| = a_i + b_i, zero contraction) — a
   pre-registered exceptional owner for the mode-contraction theorem,
   exactly the audit's expected theorem shape.
8. The carry-DFT product identity verified ON THE REAL F_{p^2} model
   (36 cases, max rel err 2e-14), not just the invented toy.

## Honest assumptions (what could flip this)

The orientation-cube seam is the F2A.1 idealisation (danger low — the
robustness sweep covers it); single descent j=1 only (the delta normal
form generalises coordinatewise, which only increases spread); q = p^2
only (tower reachability not automatically functorial — not verified
here); the unweighted carry DP (weighted merging would be a strictly
stronger theorem); official p ~ 2^31 extrapolated on a law exactly
constant over four decades.

## Downstream

PP5.4 answered NEGATIVE and banked as the route fence the Brief-5
architecture asked for. F2A.3 (exact carry-DFT node) is the only live
carry route, entry cost quantified. F2A.4 gets its three fields and its
first exceptional owner. The b-resolved slice coefficient theorem
remains the gate and is untouched.

(Scripts: f2model.py, validate.py [10 validations, ALL PASS — re-run
independently by Fable], sweep.py [1032 rows], scaling.py [to p=1048573],
constraint_robustness.py, resonance.py, dft_mass.py, analyse.py.
Machine-readable results under results/.)
