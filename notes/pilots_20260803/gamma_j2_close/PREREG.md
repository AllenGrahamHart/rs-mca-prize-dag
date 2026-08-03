# PRE-REGISTRATION — gamma_j2_close (Heart 7, last sub-item)
# Opus 5 proof pilot, 2026-08-03. Written BEFORE any computation in this directory.
# (A prior run of this pilot was killed mid-flight; no usable PREREG survived. Started clean.)

## 0. Task

Prove a hard cardinality bound for the j >= 2 Gamma classes of the MC shift
pencil, CONDITIONAL ON the gate inequality X := C(n,A)/q^w < 1 -- the
hypothesis the lane's pricing already assumes.

Banked state (adv_gamma_minus_h, 2026-08-02, coordinator-replayed):
  * j = 1: THEOREM Y, unconditional. -z in gamma.x0^{-(r-1)}.mu_n, so |Gamma| <= n.
  * j >= 2: REFUTED as a set claim. 18 certified gate-intact counterexamples,
    headline |Gamma| = 2.2n, 24 slopes outside -H^j.
  * j >= 2 cardinality: NOTHING proved. That is this pilot's target.

## 1. CONSUMER-REQUIRED BOUND SHAPE (stated BEFORE proving, as required)

Consumption chain (four sites, all downstream of one chain):

    Gamma confinement  ==>  Sum_P L_P <= |Gamma|  ==>  N_{h-1} <= |Gamma|/2
                       ==>  N_{h-1} . (n-A+1) <= headroom (= 13.857 n^3)

Sites:
  (A) background/nodes/xr_mc_depth_quantization/proof.md:120-123  (primary)
  (B) notes/pilots_20260802/adv_gamma_minus_h/t3_pricing.py:100-118 (bits)
  (C) critical/nodes/xr_graded_tangent_band_charge/statement.md:16-18,32
  (D) the B_tan overflow finding (band_adjudication/REPORT.md:58)

**EXACT REQUIREMENT.** Per received pair (u, v) -- i.e. PER j-class, NOT summed
over j -- the tier requirement is

    N_{h-1}  <=  2^86.2151 / 2^85.9916 / 2^85.8887      (prize 1/4, 1/8, 1/16)

and the only route from |Gamma| to N_{h-1} is N_{h-1} <= |Gamma|/2. So the
literal need is

    |Gamma_j|  <=  2 . 13n^3/(n-A+1)  =  37.2 n^2 / 31.8 n^2 / 29.6 n^2
                =  2^87.22 / 2^86.99 / 2^86.89        with n = 2^41.

Not summed over j. Not |Gamma| <= n (that is 2^46 STRONGER than needed).
Not <= n/2. `|Gamma| <= 13n^3` alone is 40 bits too weak for the tier leg
(it only clears the slacker Gamma_casc leg).

**Therefore the target of this pilot is: |Gamma_j| <= C.n with C <= 2^46,
or |Gamma_j| <= C.n^2 with C <= 29.6.** Anything in that box CLOSES heart 7
at the consumer. Number of j-classes: 1 <= j <= M-1, M = 2^33 (rows 1/4, 1/8)
/ 2^32 (row 1/16); only gcd(j,n) = 1 (odd j) survives BP(2), the rest break
the tangent gate and leave the generic branch.

## 2. THE FRAME I WILL VERIFY (derived on paper before computing)

Setting as in advlib: H = x0.mu_n, |H| = n, Omega = X^n - beta,
u <-> X^{n-1} + c X^{k+w-1}, v(x) = u(x)/x^j, A = k+w+1, r = n-k-w,
r' = r-1 = n-A. Exact-A codewords <-> monic M | Omega, deg M = r',
T = roots(M) subset H, m_s = [X^s]M. gamma := (-1)^{r+1} c = (-1)^{r'} c.

**(P1) The window system, s-form.** The w+1 window equations
alpha_i + z beta_i = 0 (i = 0..w) are equivalent to

    (beta)  m_s + z m_{s+j} = 0     for s in {0} u [r'+1-w, r'-j]
    (alpha) m_rho = -(c/z) m_{r'-j+1+rho}   for rho = 0..min(w,j)-1

i.e. the bottom-j window of M is a scalar multiple of the top-j window of M,
in the SAME order.

**(P2) The (X^j + z) factorisation (route 2 answer).** With
Ntilde := M.(X^j + z) and E_T(Y) := prod_{x in T}(1-xY) = Y^{r'} M(1/Y):

    (1 + z Y^j) E_T(Y)  ==  G(Y)  (mod Y^w),   deg G <= j-1, G(0) = 1.

Since 1 + zY^j = prod_{zeta^j = -z}(1 - zeta Y), this IS the j-fold
generalisation of the S = T u {-z} trick: S := T u {j-th roots of -z}, and
the conditions read e_t(S) = 0 for t = j..w-1 (and e_t(S) = e_t(T) for t < j,
vacuous). Coefficientwise, with lambda := (-1)^{j+1} z:

    e_u(T) = lambda^{floor(u/j)} . e_{u mod j}(T),   u = 0..w-1.

**(P3) The excess identity (the heart).** From (alpha) at rho = 0 combined
with prod(T) = (-1)^{r'} m_0:

    z  =  (-1)^j . gamma . e_{j-1}(T) / prod(T).

At j = 1, e_0 = 1 and this IS THEOREM Y (-z = gamma/prod(T)).
Also (from (P2) at u = j, needs w >= j+1):  z = (-1)^{j+1} e_j(T),
and (consistency)  e_{j-1}(T)/e_j(T) = -prod(T)/gamma.

**(P4) REDUCTION THEOREM (the pilot's main claim).** prod(T) in x0^{r'}.mu_n
ALWAYS (any r'-subset of a mu_n-coset). Hence, with

    E_j := #{ e_{j-1}(T) . mu_n  :  T admissible }   (count of mu_n-COSETS hit)

    |Gamma_j|  <=  n . E_j        UNCONDITIONALLY, every j >= 1.

j = 1 gives E_1 = 1 and recovers |Gamma| <= n. The ENTIRE j >= 2 excess is
the coset-class count of ONE symmetric function.

**(P5) Structured solutions.** T = T_MC \ {y}, y in T_MC an MC coset union:
E_T = 1/(1-yY) mod Y^w, e_u(T) = (-y)^u, so lambda = (-y)^j and
z = -y^j, i.e. z in -H^j. Recovers |Gamma ^ (-H^j)| <= n and identifies
E_j = 1 with the pure-coset case.

**(P6) RIGIDITY.** For admissible (T,z), (T',z'), write d := |T \ T'| = |T' \ T|,
M_1, M_1' the coprime parts. If d <= w-2j then
    E_{M_1} G' (1 + zY^j)  =  E_{M_1'} G (1 + z'Y^j)   (an EQUALITY),
so E_{M_1'} | G'.(1+zY^j) and E_{M_1} | G.(1+z'Y^j). Consequences:
  (a) d <= 2j-1, so: **d <= 2j-1 OR d >= w-2j+1** (dichotomy);
  (b) if T' is STRUCTURED then G' has no root of the form 1/x with x in H
      (gcd(j,n)=1), so d <= 1: every admissible T is within symmetric
      difference 2 of a structured T', or is far (d >= w-2j+1).

## 3. PRE-REGISTERED FALSIFIERS

Each is a concrete search. Firing = the corresponding claim dies, recorded.

F1 (kills P4, the reduction). A gate-intact fixture with |Gamma_j| > n . E_j.
   Search: all fixtures below, every j, exhaustive Gamma via the theory-free
   scan; compute E_j from the classifier's admissible T list.

F2 (kills the conditional close). A gate-intact fixture with **X < 1** and
   |Gamma_j| > n. This is THE falsifier for the headline conditional theorem.
   Search: sweep (n,k,w,q,beta,j) with X < 1, prefer X just under 1.

F3 (kills "E_j <= j"). A gate-intact fixture with E_j > j.
   [I do NOT predict E_j <= j; this is a hypothesis under test, registered so
   that a refutation is on the record either way.]

F4 (kills P6a, the dichotomy). Two admissible T, T' with 2j-1 < d <= w-2j.

F5 (kills P6b). An admissible T and a structured T' with 1 < d <= w-2j.

F6 (CONSUMER-SHAPE falsifier). A gate-intact fixture with X < 1 and
   E_j > 29.6 n  (equivalently |Gamma_j| > 29.6 n^2 by P4). If this cannot
   fire, the consumer is satisfied by P4 + any E_j bound in the box.

F7 (MANDATORY REPLAY of the calibration floor). Replay all 18 banked
   counterexamples. Two required outcomes:
     (i) EVERY one of the 18 must have X >= 1. If any has X < 1, the
         conditional theorem is DEAD ON ARRIVAL and this pilot reports
         OBSTRUCTED/REFUTED, not CLOSED.
     (ii) EVERY one must satisfy |Gamma| <= n . E_j (P4 is unconditional,
          so a violation kills P4 outright).

F8 (frame falsifier). Any solution of advlib.classify_mixed at any j
   violating (P1),(P2),(P3). 100% of solutions must satisfy them.

## 4. PRE-REGISTERED PREDICTIONS (falsifiable, recorded before running)

D1. F8 does not fire: (P1)-(P3) hold on 100% of solutions, all j, all fixtures.
D2. F1 does not fire: |Gamma_j| <= n.E_j on 100% of fixtures.
D3. F7(i) does not fire: all 18 counterexamples have X >= 1.
D4. E_j >= 2 occurs at j >= 2 (the excess is real) and E_j is SMALL --
    I predict max E_j <= 5 over the whole sweep at toy scale.
D5. F5 does not fire (the structured rigidity d <= 1 holds as proved).
D6. I predict F2 DOES NOT fire, but that this pilot will NOT be able to
    PROVE it, because the X < 1 first moment has only ONE free instance
    parameter (c) to average over while w factors of q are needed. Named
    obstruction, registered in advance: **the one-parameter averaging gap**.

## 4b. AMENDMENT (same session, still BEFORE any computation)

Two corrections found by re-reading the banked fixtures and the node
statement. Recorded as an amendment, not a silent edit.

**(A) (P3) as written is only valid for j <= w.** The (alpha) family runs
rho in [max(0, j-w), j-1], so rho = 0 is present only when j <= w. The
banked HEADLINE counterexample is (n=20, k=6, w=2, M=4, j=3) -- i.e. j > w --
exactly where the rho = 0 form fails. The form that is valid for EVERY j
comes from (alpha) at rho = j-1 (always present):

    m_{j-1} = -c/z    ==>    **z = (-1)^j . gamma / e_{r'-j+1}(T)**   (P3')

and since e_{r'-s}(T) = prod(T) . e_s(T^{-1}),

    e_{r'-j+1}(T) = prod(T) . e_{j-1}(T^{-1}).

So the REDUCTION THEOREM (P4) is restated with the corrected invariant:

    **E_j := #{ e_{j-1}(T^{-1}) . mu_n : T admissible }**,  |Gamma_j| <= n . E_j.

j = 1: e_0(T^{-1}) = 1, E_1 = 1, |Gamma| <= n -- THEOREM Y. Unchanged.
(For j <= w the two forms agree, because (Z4) at rho = j-1 gives
e_{j-1}(T) e_{j-1}(T^{-1}) = 1; that identity needs w >= j.)

**(B) SCOPE: at the prize rows j <= w-1, so j > w NEVER OCCURS there.**
From background/nodes/xr_mc_depth_quantization/statement.md:25-33 the MC
family needs `M | n`, `M | r'`, **`w <= M`**, and the shift class runs
**`1 <= j <= M-1`**; and statement.md:89 pins **`w = M = h-1` at the prize
rows**. Hence at every prize row j <= M-1 = w-1 < w. The banked
counterexamples sit at w=2, M=4 (w < M), which MC-3 admits in general but
which is NOT the prize-row shape.

This matters because BOTH new tools bite only for j < w:
  * (P2), the (X^j+z) factorisation, is vacuous once j >= w (the (beta)
    family is empty and G mod Y^w is unconstrained);
  * (P6) rigidity needs d <= w-2j, vacuous once j >= w/2.

New falsifier and prediction:

F9 (THE prize-regime falsifier -- now the sharpest one). A gate-intact
   fixture in the PRIZE-ROW SHAPE (w = M, hence j <= w-1) with
   |Gamma_j| > n. Search this regime hard and specifically; it is the only
   regime the consumer actually sees.

D7. I predict ALL 18 banked counterexamples have j >= w (equivalently
    w < M), i.e. NONE of them lives in the prize-row shape. If D7 holds,
    the refutation of record is real but OUT OF CONSUMER SCOPE, and the
    honest headline changes accordingly. If D7 fails -- a counterexample
    with j <= w-1 exists -- then F9 is already fired by banked data and
    the conditional theorem must carry the whole load.

## 5. Method / compute law

All computation under `tools/ramguard tiny -- python3 ...` or
`tools/ramguard local -- python3 ...` from the repo root, literal `--`.
No bare python3. No Modal, no network. Everything constructive is
machine-verified. Nothing written outside this directory. No commits.

Fixture families: prime fields q with n | q-1, q > n+1 (so -H is proper),
n in {12,14,15,16,18,20,21,22,24}, several beta exponents, j = 1..min(w, 6),
plus extension-field spot checks where the banked engine supports them.
