# F2 campaign L3: MID-BAND DESIGN NOTE (posing, not results)

Status: DESIGN + one PROVED no-go guardrail. Pre-registers the L3
attack before any experiment/proof work, per campaign law.

## What is left after L2

By f2_weil_newton_arc_bound the bands b <= 5 and b >= n-5 are paid at
official rows. Remaining: MID-BAND block sizes, where W(q,b) explodes.
Everything below is about a fixed mid-band b.

## The exact Parseval frame

Sum_{lambda in F_q^2} |E_b(lambda)|^2 = q^2 * SP_b, where SP_b =
Sum_s N_b(s)^2 = #{(S,S') : |S|=|S'|=b, equal first t power sums} —
the shift-pair/trade census (the v13 SP identity's object; its strata
are PROVED bookkeeping). The inversion split, exact:

  N_b(0) = C(n,b)/q^2
         + (1/q^2) Sum_{structured} E_b(lambda)
         + (1/q^2) Sum_{minor} E_b(lambda).

STRUCTURED ARCS ARE EXACTLY COMPUTABLE: linear arcs (l2 = 0) are Gauss
sums; quotient arcs (l1 = 0) factor through the double cover
mu_n -> mu_{n/2} (e_b of a doubled system on mu_{n/2}); both classes
have q-1 arcs each and closed forms — no estimates needed, they enter
the assembly as exact terms (L2b data: they dominate and grow with b,
so they MUST be exact, not bounded).

## PROVED NO-GO (guardrail, banked before anyone walks the route)

Raw Parseval cannot close the mid-band: N_b(0) <= sqrt(SP_b) and
SP_b >= C(n,b) (diagonal), so the best unconditional L2 statement
gives N_b(0) <~ sqrt(C(n,b)) — at the window peak that is
exponentially above the n^3 budget. The L2 flatness of the census is
STRICTLY WEAKER than the L-infinity claim at s = 0. Any L3 proof must
use the SPECIALNESS OF THE VALUE 0 (it is the coset-union value), not
generic fiber statistics. This kills the tempting "SP small => done"
route; SP enters as an ingredient, never the whole argument.

## Candidate mechanisms for the mid-band (to be tried in this order)

M1 MOMENT LADDER: 2k-th moments Sum_s N(s)^{2k} = #{2k-tuples with
   matching power-sum ledgers} — the BGK-style amplification. The
   banked energy dichotomy (f2_effective_energy_dichotomy) bites
   exactly here: a heavy fiber at 0 forces additive structure that
   the quasicube/BSG composition prices. Explicit-k arithmetic at
   official rows decides how far the ladder reaches; L4's constants
   feed this directly.
M2 ALGEBRAIC RIGIDITY: the PROVED complementation + top-band +
   (t+1)-support rigidity lemmas constrain ker(Phi) intersected with
   {0,1}-differences; a mid-band accident pair (S,S') is a t-null
   SIGNED configuration — route through the trade-variety machinery
   (a_universal_trade_variety is already an ev-parent of u2c).
M3 SUB-BALANCE ENTROPY: the ~2% margin q^t >= 2^n (beta-normalized)
   as a counting resource: mid-band fibers average < 1; the obligation
   is a deviation bound at 0 only — combine with M1's ladder at small
   k rather than large.

Falsifier discipline: each mechanism gets its own pre-registered
experiment at the calibration rows BEFORE proof work, in the L1/L2b
harness (the machinery is built and green).

## Assembly shape (what T-WIN will look like)

extras(b) <= [exact structured terms] + [Weil-Newton, b in extreme
bands] + [mid-band via M1/M2/M3] summed over b with complementation
halving; compare to n^3 = 2^123 at official rows; replay consumer
arithmetic; flip u2c. L4 (explicit BSG constants) gates M1's numbers.
