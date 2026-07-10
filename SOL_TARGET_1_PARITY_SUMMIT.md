# STATUS: REFUTED AS WRITTEN (2026-07-10, GPT-5.6 'Sol'; replayed
# and confirmed in-repo the same day — see the appendix below and
# SOL_TARGET_1B for the corrected open conjecture). Preserved
# unedited per house discipline; do not cite the conjecture below
# without the correction.

# TARGET 1 — THE PARITY SUMMIT. Prove or falsify.

## Setup (self-contained)

Let q be an odd prime, n a power of two with n | q - 1, and
mu_n <= F_q^x the subgroup of order n. Fix j >= 2 and for
c = (c_1, ..., c_j) in F_q^j and x in mu_n write

    s_x(c) = c_1 x + c_2 x^2 + ... + c_j x^j  mod q,

with representatives in [0, q). Define

    S_c   = sum_{x in mu_n} log|1 + e^{2 pi i s_x(c)/q}|,
    K_c   = (sum_{x in mu_n} s_x(c)) / q        (an integer:
            the power sums of mu_n vanish below index n),
    U_c   = #{x in mu_n : s_x(c) > q/2},
    eps_c = (-1)^{K_c + U_c}.

(Then prod_{x}(1 + e^{2 pi i s_x(c)/q}) = eps_c e^{S_c}: every
"frequency term" is a signed real. Proof in-repo, one paragraph.)

## The conjecture

For every fixed j >= 2 there is a function delta(n) -> 0 such that
for all such (q, n) with n -> infinity:

  | sum_{c != 0} eps_c e^{S_c}  -  2^{n/4} (q^j - 1) |
      <=  2^{delta(n) n} * sqrt( sum_{c != 0} e^{2 S_c} ).

(The subtracted term is the exactly-known contribution of the
2^{n/4} "coset-union" configurations; the right side is an exact
integer via an in-repo identity. Both sides are computable.)

## PROVE OR FALSIFY.

Facts you may take as given (all machine-verified in-repo, exact
arithmetic, verifiers cited in the statement of DAG node
u2c_giant_tnull_dichotomy and its satellites):
- The identity sum_{c != 0} eps_c e^{S_c} = q^j N - 2^n, where N
  counts subsets of mu_n with vanishing power sums p_1..p_j.
- eps and S are constant on orbits of c_i -> lambda^i c_i
  (lambda in mu_n) and of coordinatewise Frobenius.
- Numerically the left/right ratio, orbit-normalized, is 0.04-1.6
  across every enumerable scale (9.4k to 9.4e9 frequency states;
  21+ rows; both j = 2 and 3): a falsification must live beyond
  enumeration or at a structured family no test found.
- The parity field eps has no nontrivial correlation with any
  additive or multiplicative character, is not a Zolotarev-type
  permutation sign, and is not covered by Gauss's lemma (the
  counting set is a subgroup orbit, not a half-system). Twelve
  fenced dead approaches are catalogued in-repo (no-gos): do not
  spend effort on absolute-value/annealed routes (they lose
  exactly n log2(4/pi) bits — proved), single-domain Fourier
  splits, or fixed-order reciprocity.
- Known-adjacent literature: Borda-Munsch-Shparlinski (RNT 2024)
  bounds SIZES of Dedekind sums over small subgroups; no parity
  theory exists. The claim generalizes "Gauss-lemma parities" from
  half-systems to subgroup orbit configurations.

A falsification means: an explicit infinite family (or a family at
3+ growing scales) where the orbit-normalized ratio grows like
2^{c n}. A proof at any delta(n) -> 0, even for j = 2 only, is a
breakthrough (it flips a prize floor via the banked conditional
close).


---

## REFUTATION APPENDIX (2026-07-10, banked after independent replay)

Sol's falsification is CORRECT and was confirmed by exact replay:
1. The centering 2^{n/4} is the structural count only for j in
   {2,3}. At j = 4 the char-0 census is mu_8-coset unions, count
   2^{n/8} (our own banked theorem b1_char0_giant_coset_theorem:
   M > t; replayed exhaustively at (q=12289, n=16): N = 4 = 2^{n/8},
   all members mu_8-unions). For deep primes (q > n^{n/2}: no
   modular accidents, our deep-regime exactness theorem) the
   mis-centering term q^j(2^{n/4} - 2^{n/8}) dominates and the
   stated ratio diverges like 2^{Omega(n log n)}. CATCH #28: the
   target's 'for every fixed j >= 2' over-generalized the j <= 3
   constant, contradicting the repo's own banked mathematics.
2. CATCH #29: the closing line ('a proof for j = 2 only flips a
   prize floor') was OVERCLAIMED — the banked conditional close
   consumes the census at ALL q-free levels up to t; no fixed-j to
   growing-t reduction is wired. Withdrawn.
3. All in-repo j <= 3 satellites, identities, and measurements are
   unaffected (they are stated and verified with j in {2,3} scope).
   The 'right side is an exact integer' phrasing is corrected in
   1B (the squared norm is the exact integer).
