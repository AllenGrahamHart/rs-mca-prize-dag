# Fable audit of the RowC window pilot — 2026-08-02

**Verdict: ACCEPTED — V1, and the mechanism is the best kind: the
row's own banked consumption arithmetic was already a q-floor nobody
had read as one.** Replayed the interpolation self-test (2772/2772)
and the threshold ladder. Hand-checks: the floor logic (the gate's
left side is pure (n,k,A) combinatorics, B* grows with q — a lower
bound on q, immediate once said); the RowC 1/4 arithmetic (floor
2^229.76 vs ceiling 2^200.11, +29.65 bits); the prize q_FLOOR = 2^255
exactly reproducing the banked 0.9-bit pin slack from an independent
direction; the Poisson identity (the (u,v) -> (w_z, w_z') bijection
making different-slope witness events exactly independent — clean);
the V3 refutation's Cauchy-Schwarz step.

Adopted (with the ratified q-scope decision as context):
1. **THE ADJUDICATION (mine, and I make it): the consumption gate IS
   a hypothesis of the row family.** The ratified (P1) ruling says
   family-uniform certificates govern; the consumption gate is what
   MAKES a field a row candidate (it is the row's own definition of
   viability — a field failing it cannot host the MCA budget at
   all). Reading it otherwise would have P-B quantify over fields
   where the row's arithmetic is already broken. VERDICT V1 STANDS.
   The scope-cut wording is adopted into the coordinated edit
   (the P-B node gains the explicit field hypothesis; the pins
   satisfy it; the bare-band counterexamples are recorded as the
   reason the hypothesis is necessary — V2 documented as the
   pilot recommends). Final wording rides with the edit bundle for
   user visibility.
2. **(H3) DISCHARGED at all six rows; the FRAGILE flag RETIRED**
   (real slack 110 bits). The (PB-SUPPLY) skeleton simplifies:
   P-B = the field hypothesis + (H4) restricted (non-split-fibre
   planting), and **every admissible live slope is planted** —
   composing with the design ceiling (<= 960 designable) and the
   self-collision lemma. P-B's remaining content is now entirely
   the adversarial-planting question, with the random side CLOSED.
3. **Mint queue**: the q-floor theorem (+ its cell decomposition),
   the Poisson/variance identities, the bare-band documentation
   (as the necessity witness for the field hypothesis).
4. The exact cross-check discipline was excellent (q_supply_max =
   L3 - 1 against the banked ledger; the 0.9-bit prize slack
   re-derived).

Caveats endorsed: probabilistic certificate (no explicit RowC pair);
PNT-in-AP on prize bands (RowC independent); gauge-invariant gate
restatement pending (the standing pb_h4_hunt item); (H4) untouched.
