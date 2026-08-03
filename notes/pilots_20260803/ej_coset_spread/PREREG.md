# PRE-REGISTRATION -- ej_coset_spread (heart 7's residual = kernel item E_j)
# Opus 5 proof pilot, 2026-08-03. Written BEFORE any computation in this directory.

## 0. Task and inherited frame

H = x0 mu_n subset F_q^*, |H| = n, Omega = X^n - beta, beta = x0^n.
u <-> U = X^{n-1} + c X^{k+w-1}, v(x) = u(x)/x^j on H, w_z = u + z v.
A = k+w+1, **r := n-k-w**, **r' := n-A = r-1**, gamma := (-1)^{r'} c.
(NB two conventions collide upstream: the KEY LEMMA node's "r'" is my r.
 MC family members T_MC have size r; admissible T have size r' = r-1.)

Exact-A codewords of w_z <-> monic M | Omega, deg M = r', T = roots(M) c H,
m_s = [X^s]M, with (banked, gamma_j2_close (P1)):

  (beta)  m_s + z m_{s+j} = 0        s in {0} u [r'+1-w, r'-j]
  (alpha) m_rho = -(c/z) m_{r'-j+1+rho}   rho in [max(0,j-w), j-1]

Banked results consumed read-only: THEOREM A (window system), THEOREM C
(universal slope identity z = (-1)^j gamma / (prod(T) e_{j-1}(T^{-1}))),
THEOREM D (|Gamma_j| <= n . E_j), THEOREM E (structured => z in -H^j),
THEOREM F (rigidity, range d <= w-2j), the scope theorem (prize rows have
w = M, hence j <= w-1: the (beta) band is NON-EMPTY there).

E_j := #{ mu_n-cosets of e_{j-1}(T^{-1}) : T admissible }.
Consumer needs E_j <= 29.6 n per j-class. Trivial bound (q-1)/n ~ 2^209.
Observed max anywhere = 4.

## 1. THE FRAME I RE-DERIVED ON PAPER BEFORE COMPUTING

Write E_T(Y) := prod_{x in T}(1 - xY) = sum_t (-1)^t e_t(T) Y^t = Y^{r'} M(1/Y),
so m_{r'-t} = (-1)^t e_t(T) and m_s = (-1)^{r'-s} prod(T) e_s(T^{-1}).
Unwinding the i-indexed window equations alpha_i + z beta_i = 0, i = 0..w:

 * i = 0 gives m_0 + z m_j = 0, i.e.        (Q1)  z = (-1)^{j+1} / e_j(T^{-1})
 * i in [1,j] gives (alpha), rho = j-i;
   rho = j-1 gives m_{j-1} = -c/z, i.e.     (Q2)  z = (-1)^j gamma /(prod(T) e_{j-1}(T^{-1}))   [THEOREM C]
 * i in [j+1,w] gives the (beta) band proper, s = r'+1-i, NON-EMPTY iff j < w.

In e-coordinates the band is exactly
   (Q3)  e_t(T) = lambda e_{t-j}(T),  t = j..w-1,  lambda := (-1)^{j+1} z,
so in particular (needs w >= j+1)
   (Q4)  e_j(T) = lambda = (-1)^{j+1} z,
and (Q1)+(Q4) give
   (Q5)  e_j(T) e_j(T^{-1}) = 1.
Dividing the (alpha) equation at rho by the one at rho = j-1 gives (needs j <= w)
   (Q6)  e_rho(T^{-1}) = e_{j-1}(T^{-1}) . e_{j-1-rho}(T),  rho = 0..j-1,
whose rho = 0 case is
   (Q7)  e_{j-1}(T) e_{j-1}(T^{-1}) = 1.
(Q2)+(Q4) give the c-normalisation
   (Q8)  gamma = - prod(T) . e_{j-1}(T^{-1}) . e_j(T).
Generating-function form of the band:
   (Q9)  (1 + z Y^j) E_T(Y) = G(Y) mod Y^w,  deg G <= j-1, G(0) = 1,
         g_rho := [Y^rho] G = (-1)^rho e_rho(T);  and (Q6) says
         E_{T^{-1}}(Y) = (-1)^{j-1} e_{j-1}(T^{-1}) . G*(Y) mod Y^j, G* = reversal of G.
   (Q10) with C := H \ T (|C| = A):  E_C(Y) G(Y) = 1 + z Y^j mod Y^w.

**THE LEDGER.** The genuine constraints on the r'-subset T are:
 (w-1-j) band equations (Q3) for t = j+1..w-1;  1 equation (Q5);
 (j-1) equations (Q6) for rho = 0..j-2;  1 equation (Q8).
 Total = **w** equations over F_q on C(n,r') = C(n,A) objects.
 The first-moment count of solutions is therefore EXACTLY
 X = C(n,A)/q^w -- the banked gate index. (This identifies X's meaning.)

**CLAIM G (new, the pilot's structural headline -- to be tested, then proved).**
For zeta in mu_n, T -> zeta.T maps r'-subsets of H to r'-subsets of H, sends
z -> zeta^j z, prod(T) -> zeta^{r'} prod(T), e_{j-1}(T^{-1}) -> zeta^{-(j-1)} e_{j-1}(T^{-1}),
so (Q8) picks up zeta^{r'+1} = zeta^{r}. Hence **mu_{g} acts on the admissible
set, g := gcd(r, n)**, and Gamma_j is invariant under mu_{g'}, g' := g/gcd(j,g).
Consequences:
   (G1) |Gamma_j| >= g' . E_j.
   (G2) with THEOREM D:  g' E_j <= |Gamma_j| <= n E_j.
   (G3) At the three prize rows r = M.m with m = 191 / 223 / 479 all ODD and
        n = 2^41, M = 2^33 / 2^33 / 2^32, so **g = gcd(r,n) = M exactly**, and
        for j odd g' = M. Then N := n/M = 256/256/512 and
             |Gamma_j| / n  <=  E_j  <=  N . |Gamma_j| / n.
        **So E_j and |Gamma_j|/n are equivalent to within the factor N <= 512:
        the E_j reduction is a re-coordinatisation, NOT a strictly smaller
        object.** If CLAIM G survives, heart 7's residual is exactly as hard as
        the |Gamma_j| bound it replaced, and this must be said out loud.

**CLAIM H (sharpened rigidity).** For T, T' band-solutions with d := |T \ T'|
<= w-2j, (Q9) forces the EXACT polynomial identity
        G'(1 + z Y^j) Q = G (1 + z' Y^j) Q',   Q := E_{T\T'}, Q' := E_{T'\T},
(both sides have degree <= 2j-1+d <= w-1). Since gcd(Q,Q') = 1, Q' | G'(1+zY^j);
its d roots are 1/x with x in H, at most deg G' = j-1 of them roots of G' and at
most gcd(j,n) of them solutions of x^j = -z in H. Hence
        **(H1)  d <= (j-1) + gcd(j,n)  = j  when gcd(j,n) = 1**
(sharper than the banked d <= 2j-1), and the dichotomy
        **(H2)  d <= j  OR  d >= w-2j+1.**
If T' is structured, G' = (1 - y^j Y^j)/(1 - yY) has all roots 1/(y.zeta),
zeta^j = 1 != zeta, none of the form 1/x with x in H when gcd(j,n) = 1, so
        **(H3)  d <= gcd(j,n) = 1**, and then x^j = -z for the swapped-in point,
        i.e. **z in -H^j: the whole near-population contributes ONE coset.**
        (H4) When w >= 4j, "d <= j" is transitive (|T1 D T3| <= |T1 D T2|+|T2 D T3|
        gives d(T1,T3) <= 2j <= w-2j, so the dichotomy forces d(T1,T3) <= j):
        the band-solutions split into CLUSTERS of diameter <= j.
So **E_j <= 1 + #(far clusters)**, far = distance >= w-2j+1 from every structured T.

**CLAIM I (the species identification, upgraded from conjecture to a reduction).**
By (Q10), C = H \ T is an A-subset of H whose first w-1 power sums are
p_t(C) = p_t(Z) - p_t(W), Z = {j-th roots of -z}, W = roots of G (|W| <= j-1).
Writing C = x0.{omega^i : i in I}, I c Z/n, |I| = A, this says the DFT of the
indicator 1_I at frequencies 1..w-1 is a prescribed (2j-1)-sparse-rational
pattern. **E_j = #{achievable such patterns mod mu_n}.** This is verbatim the
structured-liveness / diffuse-shadow Fourier kernel. Registered as a reduction,
not as a bound.

## 2. PRE-REGISTERED FALSIFIERS (searches; firing = the claim dies, recorded)

F-A (identity ledger). Any admissible (T,z) at j < w violating any of
    (Q1)-(Q9). 100% must satisfy them. [kills my re-derivation]
F-B (E_j is the Gamma coset count). A fixture where
    E_j != #{ mu_n-coset classes of z : (T,z) admissible }.
    Second form: a fixture where E_j != #(Gamma_j / mu_n) with Gamma_j from the
    THEORY-FREE scan. [kills the tautology claim -- either way it is recorded]
F-C (CLAIM G, the action). An admissible T and zeta in mu_{gcd(r,n)} with
    zeta.T NOT admissible; or a Gamma_j not invariant under mu_{g'}.
F-D (G1). A fixture with |Gamma_j| < g' . E_j.
F-E (G3 arithmetic). gcd(n-k-w, n) != M at any of the three prize rows.
F-F (H1). Two band-solutions with j < d <= w-2j.
F-G (H2/H4 transitivity). T1,T2,T3 band-solutions, d(T1,T2) <= j, d(T2,T3) <= j,
    j < d(T1,T3) <= w-2j.
F-H (H3). An admissible (or band) T and a structured T' with 1 < d <= w-2j;
    or a T within d <= w-2j of a structured T' whose z is NOT in -H^j.
F-I (THE consumer falsifier). A gate-intact fixture with E_j > 29.6 n.
F-J (THEOREM D replay). Any of the gamma pilot's 179 banked rows, or any new
    row, with |Gamma_j| > n . E_j.
F-K (the prize-shape law). A gate-intact fixture in the prize shape (w = M),
    with 1 <= j <= w-1 and gcd(j,n) = 1, having E_j >= 2.
F-L (structured completeness). A structured T (= T_MC \ {y}, T_MC in the MC
    family) that is NOT admissible, at w = M.

## 3. PRE-REGISTERED PREDICTIONS

D-1. F-A does not fire.
D-2. F-B does not fire in the classifier form: E_j = #z-cosets EXACTLY.
     I therefore predict THEOREM D is essentially TIGHT-ISH from below via
     CLAIM G, and that the honest headline is "E_j is |Gamma_j| in coset
     coordinates", not "E_j is a smaller residual".
D-3. F-C, F-D, F-E do not fire (CLAIM G holds; gcd(r,n) = M at all prize rows).
D-4. F-F, F-G, F-H do not fire (CLAIM H holds, d <= j sharpening included).
D-5. F-K does not fire: E_j = 1 on every gate-intact prize-shape fixture with
     gcd(j,n) = 1. (The banked e7 row n=33,k=3,w=M=3,q=67,j=2 has E_j = 2 but
     gate_ok = FALSE; I predict the gate is what separates it.)
D-6. F-L does not fire: every structured T is admissible, so the structured
     population is |MC family| . r and always contributes exactly 1 to E_j.
D-7. **THE TOY-SCALE WALL (registered as a prediction, with exact constants).**
     Full enumeration needs C(n,A) <= B (B ~ 5e6 in Python under ramguard).
     A gate-intact excess has never been seen with X = C(n,A)/q^w < 1, and
     q >= 2n+1 always. Non-vacuous rigidity needs w >= 2j+1 >= 5 for j >= 2.
     But X >= 1 with w >= 5 forces C(n,A) >= q^5 >= (2n+1)^5 >= 25^5 = 9.8e6 > B.
     **So "X >= 1" and "w >= 2j+1" are INCOMPATIBLE at any enumerable scale:
     route (2) can never be tested against a live excess by brute force.**
     I predict this obstruction is exact, and that the only way to test the
     rigidity mechanics at w >= 5 is on the LARGER band-only family (drop (Q5),
     (Q6), (Q8)), where the population is C(n,r')/q^{w-1-j} and sporadics are
     plentiful. That is what I will do.
D-8. E_j <= 1 + (number of SPORADIC admissible T). Prediction: every fixture
     with E_j >= 2 has a sporadic admissible T.
D-9. Max E_j over the new sweep <= 4 (matching the banked max). If exceeded,
     the new max and its parameter dependence are recorded.
D-10. THE FIT. I predict E_j is NOT bounded by any function of j alone (the
     banked E_j = 4 at j = 3 already killed E_j <= j), NOR by w alone; the true
     parameter is the sporadic count, which tracks X. Pre-registered fit target:
     E_j - 1 vs #sporadic classes, and #sporadic vs X.
D-11. I predict I will NOT be able to prove E_j <= 29.6 n unconditionally, and
     that the obstruction is CLAIM I: bounding E_j is exactly the Fourier
     prescription problem (structured liveness), one factor of q^{w-1} short by
     the same one-parameter averaging gap already named upstream.

## 3b. AMENDMENT 1 -- POST-HOC, written AFTER x1_identities.py ran, flagged as
##     post-hoc, given its own OUT-OF-SAMPLE falsifier. Nothing above was edited.

x1 produced 29021 checks with 13 failures, ALL of them the single check
"Gamma cosets == classifier z-cosets", and ALL of them on fixtures whose
tangent gate is BROKEN, where the theory-free Gamma_j is EMPTY by definition
(Scan.live() returns [] when joint_max > A: no slope has max agreement exactly
A) while the classifier still finds exact-A codewords. Two consequences:

**(A1) CORRECTION of record to F-B.** The correct statement is
      #(Gamma_j / mu_n)  <=  E_j    ALWAYS,
      with EQUALITY exactly when the gate is intact. F-B is re-stated with the
      gate hypothesis; the 13 hits are re-classified as a definitional
      refinement, NOT as a falsification, and are reported as such.

**(A2) NEW POST-HOC HYPOTHESIS (S-G).** On every scanned x1 row, in the prize
      shape with j < w:   #sporadic admissible T > 0   <==>   gate BROKEN.
      Equivalently: a gate-intact fixture with j < w has ONLY structured
      admissible T, hence E_j = 1 by THEOREM E.
      Falsifier **F-M**: a gate-intact fixture with j < w and #sporadic > 0,
      OR a gate-broken fixture with j < w and #sporadic = 0.
      This was NOT predicted in advance. It is tested OUT OF SAMPLE in x4 on
      fixtures disjoint from x1's list, and the in-sample rows are reported
      separately from the out-of-sample ones.

**(A3) Recorded anomaly to explain.** The banked e7 row
      (n=33, k=3, w=M=3, q=67, j=2) has E_j = 2 with j < w -- so "j < w"
      alone does NOT force E_j = 1. Its gate is BROKEN. Under (S-G) that is
      consistent. x4 must reproduce this row and check that the gate is what
      separates it. If a gate-INTACT j < w row with E_j >= 2 is ever found,
      F-K fires and the law dies.

## 4. Method / compute law

All computation under `tools/ramguard tiny -- python3 ...` or
`tools/ramguard local -- python3 ...` from the repo root, literal `--`.
No bare python3. No Modal, no network. g2lib.py of gamma_j2_close is imported
READ-ONLY; every claim of this pilot is re-derived in ejlib.py and cross-checked
against g2lib's independent classifier AND (where affordable) against the
theory-free Scan. Nothing written outside this directory. No commits.
