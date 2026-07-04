# sketch: hankel_rank_profile_entropy (Pro round 7; three parts verified)
For a saturated Hankel state P = ker(S_{i+c}) with fixed sparse cutoff W:
(1) ROW-DEFICIENT (rank M < t): binary apolarity — the apolar ideal of a
    binary form is a complete intersection (Q,R), a+b = t+j+1; row-deficiency
    forces a < t hence b > j+1, so (I_F)_j = Q * K[U,V]_{j-a}: the kernel is a
    PRINCIPAL segment P = q K[X]_{<=D-1}. After root strip: pure Vandermonde/
    MDS, no unpaid closure entropy. VERIFIED 4000/4000 (deg gcd = j+1-D).
(2) ROW-FULL WIDE (j-t+3 > 2W): by the separation + same-class collapse
    lemmas, all weight-<=W atoms lie in one rational class with one saturated
    closure: Delta_u <= 1. VERIFIED (wide states generically atom-free).
(3) ROW-FULL NARROW (j-t+3 <= 2W): dim P = j+1-t <= 2W-2 = O(W); each
    branching descent drops dim by >= 1, so <= O(W) branching states per
    path, each with <= n^W child closures.
TOTAL: #unpaid primitive saturated states <= n^{O(W^2)} for fixed W — L3,
via the entropy/Kraft argument (leaf weights prod Delta_u^{-1} sum to <= 1)
+ QF.12 budget-drop chains. Does NOT need the w>=3 many-sparse inverse; the
weight-2 routing remains useful downstream but the count is rank-profile-
driven. FORMALIZATION PENDING: the binary-apolar principal-kernel lemma
(classical Sylvester/catalecticant theory) stated referee-grade; the Kraft
bookkeeping written out. W = O(1) required (n^{O(W^2)} otherwise).
