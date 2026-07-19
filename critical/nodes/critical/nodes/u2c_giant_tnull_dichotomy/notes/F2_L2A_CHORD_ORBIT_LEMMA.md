# F2 campaign L2a: the CHORD-ORBIT LEMMA (exact Jacobi-sum formula
# for the collision count, per mu_n-orbit)

Status: PROVED (standard multiplicative-character machinery, full
proof inline) + machine-verified exactly
(f2_l2a_chord_orbit_modal.py, digest F2_L2A_CHORD_ORBIT_PASS).

## Pre-registration

Question (re-posed after L2b's orbit discovery): give an exact formula
with printed error for N(c) = #{(x,y) in mu_n^2 : x + y = c}, hence
for the chord collision count kappa(c), manifestly constant on
mu_n-orbits, evaluable per orbit.

Success: exact identity verified at every orbit of every test row;
error term with EXACT modulus (not an O()); the L1/L2b kappa strata
reproduced from the formula.
Failure: any orbit where the identity misses; a bound instead of an
identity; mixing the field conventions (official-row reading must be
beta-normalized per catch #11).

## Setup and statement

q an odd prime, n | q-1, m = (q-1)/n the co-index (= the number of
generic chord orbits, L2b). mu_n = (F_q^x)^m is the n-element group of
n-th roots of unity. Let C_m = {chi : chi^m = eps} be the m
multiplicative characters TRIVIAL ON mu_n (note the duality: the
detecting characters have order dividing m, not n). For c != 0:

  LEMMA (chord-orbit formula).
    N(c) = ( q + 1 - 2m*1_{mu_n}(c) - m*delta + E(c) ) / m^2,
  where delta = 1_{-1 in mu_n} (= 1 iff n even, q odd),
    E(c) = sum over pairs (chi1, chi2) in C_m^2 with
           chi1, chi2, chi1*chi2 all nontrivial of
           chi1(c) chi2(c) J(chi1, chi2),
  J the Jacobi sum, |J(chi1,chi2)| = sqrt(q) EXACTLY for every such
  pair; hence |E(c)| <= (m-1)(m-2) sqrt(q).

  COROLLARY (collision count). kappa(c) = (N(c) - 1_{c/2 in mu_n})/2,
  so for every chord c not in mu_n:
    kappa(c) <= ( q + 1 + (m-1)(m-2) sqrt(q) ) / (2 m^2)  + 1/2,
  and the same formula gives the matching lower window. Both N and
  kappa are constant on mu_n-orbits (chi(uc) = chi(c) for u in mu_n,
  chi in C_m — manifest), so the formula is intrinsically a function
  on the m-element orbit space.

## Proof

Indicator: mu_n = (F_q^x)^m has annihilator C_m of size m in the
character group, so 1_{mu_n}(x) = (1/m) sum_{chi in C_m} chi(x) for
x != 0. Therefore, for c != 0,

  N(c) = sum_{x+y=c, xy != 0} 1_{mu_n}(x) 1_{mu_n}(y)
       = (1/m^2) sum_{chi1, chi2 in C_m} S(chi1, chi2, c),
  S = sum_{x+y=c, xy != 0} chi1(x) chi2(y)
    = chi1(c) chi2(c) J(chi1, chi2)          [x = cs, y = c(1-s)].

Values of J: J(eps, eps) = q - 2; J(chi, eps) = J(eps, chi) = -1 for
chi != eps (complete character sum minus the s = 1 term); for
chi != eps, J(chi, chi^{-1}) = -chi(-1) (substitute t = s/(1-s));
and for chi1, chi2, chi1chi2 all nontrivial, J = g(chi1) g(chi2) /
g(chi1 chi2) with Gauss sums of modulus sqrt(q), so |J| = sqrt(q)
exactly. Collecting:

  (eps,eps):    q - 2
  (chi,eps)+(eps,chi): -2 ( m 1_{mu_n}(c) - 1 )      [orthogonality:
                 sum_{chi in C_m} chi(c) = m 1_{mu_n}(c)]
  (chi,chi^{-1}), chi != eps: - ( m delta - 1 )      [chi(c)chi^{-1}(c)=1;
                 sum_{chi in C_m} chi(-1) = m delta]
  generic:      E(c)

Total: q - 2 + 2 - 2m 1_{mu_n}(c) + 1 - m delta + E(c), which is the
lemma. The diagonal term: the ordered count N includes x = y exactly
when c/2 in mu_n; removing it and halving gives kappa. QED.

## Remarks binding it to the campaign

1. MAIN TERM q/m^2 = q n^2/(q-1)^2 ~ n^2/q — the empirical law from
   L1 (kappa_max tracking n^2/q) is the theorem's main term.
2. The formula EXPLAINS the L2b strata: at (97,32), m = 3, exactly
   (m-1)(m-2) = 2 generic Jacobi pairs, window (95 +- 2*sqrt(97))/9 =
   [8.3, 12.7] for N, i.e. kappa in {4,5,6} — precisely the three
   observed orbits. Small m => few Jacobi terms => narrow strata.
3. OFFICIAL-ROW READING (catch #11 discipline): q in this lemma is
   the field CONTAINING mu_n as index-m subgroup. At official rows
   the beta-normalized generated field is the correct instantiation;
   m there is the generated-field co-index. FLAG carried forward.
4. What L2a does for the ladder: the chord geometry of the GENERIC
   Fourier arcs is now an m-point exact computation. The remaining
   L2 content is the per-orbit ARC-MAX bound (|E_b| in terms of the
   orbit's kappa and b) — the analytic rung, next.

## Replay

    ~/.venvs/modal/bin/modal run critical/nodes/u2c_giant_tnull_dichotomy/notes/f2_l2a_chord_orbit_modal.py

Digest: F2_L2A_CHORD_ORBIT_PASS. Gates: per-orbit exact identity
(< 1e-6), |J| = sqrt(q) exact on every generic pair, orbit constancy
of N over ALL c, kappa windows containing every measured L1/L2b
stratum, and the corollary inequality as stated.
