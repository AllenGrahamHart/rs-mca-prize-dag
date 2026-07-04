# tr_joint_telescope

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/gap1_terminal_reserve.md']

## Statement

Simultaneous K_M-stability across an active character set R is agreement with the JOINT stabilizer subcode — if the product over R telescopes into a single instance at the joint scale, Conjecture TR's jointness is STRUCTURAL (a tower statement, #212's machinery) rather than analytic, and the q^{M-1} per-leaf over-aggregation that M4 identified disappears by construction. E29's measurement then calibrates constants instead of deciding existence. AMENDED PER E34 (15/15, 519 cells): replace R by its congruence-class CLOSURE mod D = gcd(M, {r - r'}): the joint stabilizer is K_D, all of R lies in one class r0 mod D, and the joint-stabilizer subcode is a SINGLE character-r0 isotypic instance at scale D (Lemma J1); joint data is contained in telescoped data always, with EQUALITY iff |R| = M/D (Lemma J2). Census: containment in all 519 cells (falsifier never fired); equality on all 343 full-class cells — the q^{M-1} over-aggregation vanishes BY CONSTRUCTION. E29 demotes to constants calibration.

## Attack surface

compose #212's per-character confinement with the tower recursion at the joint subgroup; the F_13 toy (already instrumented in the M4 verifier) tests telescoping exactly

## Falsifier

the F_13 joint product strictly exceeding every telescoped bound (mechanical check)

## Ledger (migrated notes)

Scoping caveat (honest): E34's identity is in the linear-model counts (E6/M4 convention); LIFTING it to the aligned A_r sets is face 1's residual statement — small, named, and toy-instrumented by the same verifier. | LIFTED AND PROVED (tr_lifting_lemma.md, 21/21 over 330 cells with real codeword enumeration): LL1 is a POINTWISE identity for every codeword — the agreement condition never has to decompose, it merely filters the domain — so telescoping commutes with alignment exactly on stable sets (LL2). Count transfer holds iff the tower is NON-DEGENERATE ([K(gamma):K] = M/D); degenerate towers lose it (CONDITIONAL there, with an engineered collision witness word W5 — 10 degenerate cells verified). Genuine-instance containment is one-directional (harmless direction). Exact stability is load-bearing; weakest repair stated. Face 1's jointness face is CLOSED. | QA.24 (#19, 28/28 replayed): degenerate towers are NOT absent — all 153 nontrivial (row, M) triples admit correction cases, including all 50 M > t consumer triples. The F2 correction column is emitted (mechanical bookkeeping, not a gap): TR's count transfer carries the correction column everywhere rather than assuming non-degeneracy.
