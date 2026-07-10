# PRO BRIEF — FLOOR 2 (F2) SUMMIT, v4 (2026-07-10)

SUPERSEDES v3. Written after campaign cycles 79–86 (satellites 16–22,
log entries #88–#98) completed and TERMINATED the summit's interior
chart. v3 remains the reference for the pre-79 instruments (dictionary,
edge lemma, tower skeleton, no-gos 1–9). Every claim here is banked in
`prize/dag.json` with a machine-verified digest; verifiers live in
`prize/critical/nodes/u2c_giant_tnull_dichotomy/notes/`.

## THE PROBLEM — uniquely posed (nothing else remains)

For prime q (transfer to q = p^k PROVED — see Frame 6), mu_n <= F_q^x,
and j power-sum conditions, every census frequency term is a SIGNED
REAL:

    prod_{x in mu_n} (1 + psi(c.xbar(x)))  =  eps_c * exp(S_c)

  * S_c   = sum_x log|1 + psi(c.xbar)|  — the modulus field
  * eps_c = (-1)^{K_c + U_c}            — the PARITY FIELD, where
      s_x  = c.xbar(x) mod q,
      K_c  = (sum_x s_x)/q      (an INTEGER — the carry; equivalently
                                 the integer value of the subgroup
                                 sawtooth sum sum_x ((s_x/q)) + U_c),
      U_c  = #{x : s_x > q/2}   (half-interval count).

The census identity (integer-exact at 12+ rows):
    sum_{c != 0} eps_c exp(S_c)  =  q^j N_total - 2^n.

TARGET (the whole of u2c_giant_tnull_dichotomy reduces to this):
prove, at official-shaped rows (n a 2-power ~ 2^40, q ~ p^k with
p ~ 2^31, k ~ 2^16, j up to t ~ 7e10 conditions), the ALIGNMENT BOUND

    | sum_{c != 0} eps_c exp(S_c)  -  STRUCT DRIFT |
        <=  2^{o(n)} * sqrt( sum_{c != 0} exp(2 S_c) )

where STRUCT DRIFT = 2^{n/4}(q^j - 1) (the proved coset-union census)
and the right side is an EXACT INTEGER via the ladder identity
(Frame 5). Any 2^{o(n)} — even 2^{n/100} — beats the 2^15-per-condition
budget with astronomical room (consumer arithmetic banked in
f2_conditional_close). Equivalently: the parity field eps is
2^{o(n)}-uncorrelated with the Gaussian weight exp(S).

## THE FRAME — seven proved instruments (all exact, all verified)

1. L-FUNCTION DIAGONALIZATION (sat 16): the t-shift deviation field
   diagonalizes pointwise in Dirichlet L(1,chi) over quotient
   characters; doubling law 2 in G => field == 0.
2. MOMENT THEORY (sat 17): RMS <= 2 sqrt(f) max|L(1,chi)|
   unconditionally; measured Gaussian profile (max/RMS ~ sqrt(2 log m)).
3. ANNEALED/PHASE SPLIT (sat 18): E_c[exp S_c] = (4/pi)^{n(1+o(1))}
   at official depth — ALL absolute routes miss by n log2(4/pi) bits;
   the contract is irreducibly SIGNED (this is no-go territory: do not
   attack |S| — satellites 16/17 already max out that side).
4. SIGN QUANTIZATION (sat 19): Phi_c in pi*Z (proof: full-group power
   sums vanish); eps_c = (-1)^{K+U}; twisted-orbit invariance
   (c_i -> lambda^i c_i), effective population (q^j - 1)/n.
5. LADDER IDENTITY (sat 21): sum_{c!=0} e^{2S_c} = q^j C'' - 4^n with
   C'' the weighted signed-trade census — the alignment denominator is
   an INTEGER (bigint DP; floats provably cannot see it at n >= 64).
6. TOWER TRANSFER (sat 21): the whole frame holds verbatim at q = p^k
   (psi = e_p(Tr(.)); verified at 7^2, 5^2, 3^4) — prime-q results
   transfer to the official shape by proof, not analogy.
7. LADDER TERMINATION (sat 22): rungs >= 2 are positive-sum — the sign
   problem exists ONLY at rung 1; no induction up the alphabet ladder
   can work (no-go #10). Rung-2 struct = 18^{n/4}, exact at deep rows.

## WHAT IS MEASURED (evidence, not proof)

* Struct-subtracted alignment ratio: 0.17–11.4 across 13 exact rows,
  two decades of population, fitted slope -0.067 (sat 20) — a stable
  O(1) constant ~7, four orders below budget. Falsifier direction
  (growth with scale) tested and NEGATIVE.
* Doubly-exact row (113,16,j=3): rung-1 extras = 0 AND rung-2 census =
  struct exactly — the dichotomy holds on the nose where enumeration
  reaches.
* Prime-power rows in the same band (8.7 / 4.0 / 1.9).

## NO-GOS (fenced, with margins — full list v3 + dag)

1–9 as in v3 (Parseval; absolute Fourier; Teichmuller; extremal
classification; norm counting; trade decomposition; CMMM bridge at
official k; full-ladder Esseen; the analytic lane at official fields).
10 (NEW, sat 22): the alphabet-ladder induction — rungs >= 2 carry no
signs; the recursion is an identity mill, not a proof lane.
Plus the annealed death constant (sat 18): any bound routed through
|S| alone loses n log2(4/pi) ~ 0.3485 n bits. Do not spend effort there.

## NAMED ENTRY POINTS (in order of our current credence)

E0-VERDICTS (cycle 100 source audit): Duke-Hopkins read in full —
    its mechanism (Galois twist of a fixed algebraic number) yields
    ONLY Dirichlet characters in a; eps is measured non-character
    (sat 26), so ALL permutation-sign/Galois-twist routes are
    excluded, not just naive Zolotarev. Zagier reciprocity: cotangent
    products at linear arguments, coprime moduli — shape mismatch, no
    direct application. Unread adjacent shelf: finite-field higher
    Dedekind sums (ScienceDirect S1071579711000438).
E1. LATTICE-POINT PARITY / EHRHART MOD 2. eps_c is the parity of
    K_c + U_c — both are lattice counts attached to the rational point
    c/q and the subgroup orbit {x}: U counts orbit points in a
    half-open window; K is the lattice count under the orbit's
    "staircase". Ehrhart reciprocity and its mod-2 refinements
    (Ehrhart–Macdonald; Stanley's reciprocity; recent work on Ehrhart
    quasi-polynomial parities) compute EXACTLY such counts for dilated
    rational polytopes. The subgroup structure gives the dilation
    family. Sought: a reciprocity that pins the JOINT distribution of
    (K + U mod 2) against the window position — equidistribution of
    the parity at 2^{o(n)} discrepancy wins outright.
E2. DEDEKIND-INTEGER RECIPROCITY. K_c is the integer value of a
    generalized Dedekind (sawtooth) sum over a subgroup. Classical
    Dedekind reciprocity is an EXACT functional equation for such
    sums; Zagier's higher-dimensional reciprocity covers multi-
    argument versions (our j >= 2). Sought: reciprocity => carry
    parity equidistributes over the frequency orbits.
    LITERATURE ANCHOR (cycle 94): Borda-Munsch-Shparlinski, RNT 2024
    (arXiv 2305.04304) is the closest living work — SIZE bounds for
    Dedekind sums over small subgroups via the same L(1,chi)-over-
    subgroup-characters bridge as satellites 16-18; conditionally
    optimal (Mersenne caveat). The PARITY theory is absent from the
    literature — the summit is one step beyond this named frontier.
    Also: Madritsch-Tichy 2025 (arXiv 2509.19810) for the function
    class (floor-polynomial binary sequences), interval domains only.
    Gauss-lemma generalizations need HALF-SYSTEMS; G = -G is
    maximally non-half-system (why no classical symbol exists).
E3. PARITY FOURIER SPECTRUM — CLOSED (catch #23 cycle 88; NO-GO #11 cycle 89, digest F2_CROSS_SUPPORT_PASS: k_surgery/Q = 0.57-0.76 at 7/7 rows — the absolute pairing tail never thins, the pairing is within 1 bit of trivial sqrt(Q), and the signed value accrues diffusely; DO NOT ATTACK IN FREQUENCY SPACE — the record below is kept for the negative's derivation). The
    naive Holder chain (max|eps-hat| times L1/L2 of the weight
    spectrum) LOSES a factor sqrt(q^j): Parseval is an isometry, so
    single-domain splits reproduce only the trivial bound. Walsh
    flatness alone does NOT suffice. MEASURED (digest
    F2_PARITY_SPECTRUM_PASS): the parity spectrum is nonetheless
    spectrally near-random — W* = max_{d != 0}|eps-hat|/sqrt(q^j) =
    2.4-5.7 at j=2 rows (at/below the random +-1-field max
    sqrt(2 ln q^j)), ~3x random at j=3 (twisted-orbit multiplets).
    THE RE-POSED LANE: alignment = (1/q^j) sum_d eps-hat(d) *
    conj(E-hat(d)) — win by CROSS-SUPPORT MISALIGNMENT: E-hat's mass
    concentrates on census frequencies (moment vectors of near-null
    configurations); bound sum over THAT set of |eps-hat| — i.e.,
    prove the parity spectrum carries 2^{o(n)}-small mass ON the
    weight spectrum's heavy support. Weil applies levelwise to
    individual eps-hat(d); the new required input is the SUPPORT
    geometry of E-hat (which the census machinery describes exactly).
E4. FROBENIUS AVERAGING — CLOSED BY PROOF (NO-GO #12, cycle 90):
    (S, eps) are CONSTANT on coordinatewise-Frobenius orbits (5-line
    proof via z = x^{p^{-1}}); there is nothing to average. The
    positive residue: the invariance group (twisted scaling x
    Frobenius, order ~ n k) makes the correct random-sign baseline
    PER-ORBIT — the measured 'alignment ~7' is EXACTLY the orbit
    multiplicity sqrt(n) (all 13 rows collapse to [0.5, 1.6] around
    1; prime-power rows collapse with sqrt(n k)). REFINED MODEL: the
    parity field is random per orbit with constant ~ 1. Refined
    falsifier: per-orbit constant > ~10 sustained at 3+ scales.

## DELIVERABLES (any one)

D1. Proof of the alignment bound (any 2^{o(n)}) for growing 2-power-n
    families at prime q — the tower transfer lifts it.
D2. A counterexample family: alignment growing like 2^{cn} sustained
    at 3+ scales — fires T-FLOOR, worth as much as a proof.
D3. A reduction of E1/E2/E3 to a NAMED theorem or named open problem
    in the literature with the exact statement matched (we verify and
    integrate; a recognized-open-problem reduction re-poses the prize
    node honestly).

## RULES OF ENGAGEMENT (campaign law, non-negotiable)

Falsification before proof; one verifier per claim; exact/bigint
arithmetic for anything within 60 bits of a cancellation (floats are
PROVEN blind there — sat 21); pre-register reads before running;
every catch goes in the log verbatim. Current catch count: 22 in 86
cycles — the protocol works. Modal for anything non-trivial
(~/.venvs/modal/bin/modal). The DAG is the single source of truth.
