# f_dih_subgroup_completeness

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e30_dim3_flat_census.md']

## Statement

Quotient-type escape mechanisms arise from Mobius symmetries of the evaluation domain; the PGL_2 stabilizer of mu_n (and of 2-power coset domains) contains the dihedral group Dih_n (rotations x -> zeta x, inversions x -> zeta/x) and generically equals it. Every subgroup of a dihedral group is cyclic or dihedral (theorem): cyclic => multiplicative pullbacks g(X^M); dihedral => Chebyshev quotients X^e g(X^M + zeta' X^-M) (twisted inversions are conjugate relabelings). THEREFORE the symmetry-quotient taxonomy {multiplicative, dihedral} is COMPLETE — no sixth quotient mechanism exists. Explains E25/E27/E30's clean fifth-shape watches structurally. Residual check (small lemma): no exotic stabilizer at special (n, q) — the stabilizer of an n-point projective set with n >= 3 is finite and contains Dih_n; rule out proper overgroups for prize domains. AMENDED (Codex P2 + verified negative controls + the Mersenne analysis): the raw all-(n,q) claim is FALSE. TAME rows: stabilizer = Dih_n PROVED (P2's tame case). WILD rows — the stabilizer explodes to PGL_2(F_{n-1}) (3-transitive, order ~n^3) exactly when the domain is projectively the subfield line P^1(F_{n-1}): requires n-1 a prime power AND F_{n-1} in F_q. For 2-power n, n-1 prime power <=> Mersenne structure: n in {4, 8, 32, 128, 2^13, 2^17, 2^19, 2^31} (exhaustive to 2^41; both negative controls verified independently: F_9/mu_4 -> 24 = S_4 by my brute force, F_49/mu_8 -> 336 = |PGL_2(F_7)|). ADMISSIBLE WILD ROWS EXIST: q = (2^m - 1)^{2s} < 2^256 with n | q - 1 automatic (q'^2 - 1 = (q'-1) 2^m for Mersenne q') at n = 2^13, 2^17, 2^19, 2^31. Row C (1023 = 3*11*31) and prize-max (2^41 - 1 composite) are TAME. At wild rows the completeness conclusion enlarges from {cyclic, dihedral} to the DICKSON subgroup lattice of PGL_2(F_{n-1}) — still finite and classical. Named condition: p2_no_wild_subfield_circle_domain (per-row tameness check, pure arithmetic).

## Attack surface

the subgroup theorem is classical; the stabilizer computation is a short PGL_2 argument; the exotic-case check is finite casework (n = 2-power, n | q-1)

## Falsifier

E36: an exotic Mobius map preserving a prize-class domain (finite enumeration per (n,q) toy class — queued with Codex, Wave 5)

## Ledger (migrated notes)

E36 (54/54, replayed green): at every checked toy prize-class domain the full PGL_2 set-stabilizer has size exactly 2n and equals the explicit dihedral group — NO exotic Mobius stabilizer. Toy casework discharged; the general algebraic lemma (all prize (n,q)) remains the route to PROVED, honestly scoped by the packet itself. | P2 (PR #14, 17/17 replayed): tame-case proof integrated; the wild exception class is the banked Mersenne analysis. PRs #10/#12/#13/#14 integrated manually onto the live branch (DAG conflicts resolved here); closing with credit comments. | SCOPE CORRECTION post-X-4b: this keystone governs the symmetry-QUOTIENT sector only — it does NOT imply cancellation-completeness (the moment-trade class cancels without symmetry). The 'explains the clean fifth-shape watches' note is retracted: those censuses were weight-<=4-blind.
