# es_ternary_suppression_instruments

- **status:** PROVED (the instruments; the two open conjectural
  residuals are stated, not claimed)
- **minted:** 2026-08-06 (mint-4, rounds 17-18), coordinator-audited.
- **provenance:** notes/pilots_20260806/es_coprimality/ (143,974/0)
  + notes/pilots_20260806/efloor_sparsity/ (56,542/0), both
  coordinator-replayed.

## Statement

THE PROVED SUPPRESSION INSTRUMENTS for the (ES)-family counting
questions (0/1 and {0,±1} vectors in p-ary codes from cyclotomic
windows), with the exceptional class exactly characterized.

**THEOREM CS (ideal Galois multiplicity).** n = 2^m, p odd, S with
x_1 != 0: if p | N(I_S) then p^{|Z_w^odd|} divides |N(x_1)|, while
|N(x_1)|^2 <= (r' - a_{n/2}(S))^{n/2} (CS2, SHARP — AM-GM equality
attained); hence ceil((w-1)/2)·log2 p <= (n/4)·log2 r'.
CONSEQUENCE (unconditional): the (ES) crossing instance HOLDS
wherever ceil((w-1)/2)·log2 p > (n/4)·log2 r' — at 256-bit p,
71.16% of the bracket (every w > w* = 2^37.3131, incl. 2^38, 2^39);
scaling with log2 p (39.57% at 128 bits). Complete over all S via
the three-way dichotomy (strat 0 -> CS; middle strata -> LEMMA
STRAT + CS-TOWER, margins widening; deep strata -> LEMMA Z
structural).

**LEMMA STRAT.** strat(S) = a >= 1 reduces (n, r', w) exactly to
(n/2^a, r'/2^a, floor((w-1)/2^a)+1); the binding stratum is the
largest a with w_a = 2 (principal, non-coprimality generic).

**LEMMA TWO.** x_s = r' mod (1 - zeta) for every s, so even r'
forces 2 | N(I_S) — the coprimality invariant of record is
N_odd(I_S) (the naive N = 1 conjecture is FALSE at every prize row).

**THEOREM SP-COVER / LEMMA COS / THEOREM SP-UNIFORM.** Full
<p>-coset coverage of the odd window forces periodicity (engine:
LEMMA AB — A - B is a TERNARY vector; F_3 is why p = 3 is
extremal); w_cov(p, 2^m) is m-independent for m >= v_2(p^2-1) and
<= 2^{v_2(p^2-1)}; hence p | N_odd(I_S) with strat(S) = 0 forces
p > sqrt(w+1). p = 3 is dead for all w >= 6 at every n. THE
BAD-PRIME RANGE IS TWO-SIDED: sqrt(w+1) < p <= the CS3 ceiling.
THEOREM SP-TERNARY: a second, per-(n,p,w)-certified exclusion
mechanism.

**The adversarial nulls (banked as evidence, not proof):** the
densest floor family (F1 quarter-shift, LEMMA QS: 49% of floor mass
in 0.42% of sets at 116x density) dies at one step of w and is
exponentially small; exact all-characteristic censuses at n = 64
(a = 0 class EMPTY for w >= 3 at r' <= 4) and n = 128; the
quantization law reproduced; round-16's unreached-n = 64 flag
CLOSED.

**THE HONEST STRUCTURAL LIMITS (proved):** (E-1) given CS, E_floor
= {N_odd > 1} exactly on strat = 0 — the CC decomposition is a
RESTATEMENT, not a reduction; (E-2) CC-sparsity IS the (ES) shape
again, at half length over the ternary alphabet — not a smaller
lemma; (E-3) the official row gate v_2(q-1) >= 41 is exactly
SP-COVER's blind spot (needs w >= 2^42 vs bracket cap 2^39) — the
official primes sit PROVABLY in the gap between the two closed ends
(2^4.69 wide in w); the SPD union-bound shape is PROVED VACUOUS in
every regime (character sums + BCH cannot reach the middle).

## Falsifier

An S violating CS's divisibility; an a = 0 bad prime <= sqrt(w+1);
a floor family with non-vanishing density (refutes CC-sparsity); a
CS-covered row carrying an accident.

## NOT claimed

CC-sparsity / pair-coprimality (open — and by E-2 exactly as hard
as the original); the middle of the prime range; w = 3 (CS
degenerates to the banked M3 there); the band rows (outside CS's
window hypotheses).
