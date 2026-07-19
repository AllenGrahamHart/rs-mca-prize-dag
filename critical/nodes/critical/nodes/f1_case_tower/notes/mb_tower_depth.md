# Tower depth at KoalaBear-shaped rows (node-local, 2026-07-07)

Source: M_B seam audit, `prize/notes/correspondence/MB_VS_F1_LEDGER.md`
§5 (scripts `mb_audit.py` there). Node-local per the 2026-07-07 rule.

The node's proof prices case (iii) recursively with per-level
denominators q_K = p^d. The audit evaluated the level-d census floors
M_{p^d}(d1) = C(m',m)·C(n,m')·(p^d)^−(d1−1) at the KoalaBear row
(n = 2^21, K = 2^20, p = 2^31−2^24+1, q = p^6, deployed profiles):

    level d=1 (base):   +67.1 / +56.0 / +43.9 bits  (= upstream's PROVED
                        M_B floors, replayed to every printed digit)
    level d=2:          −2,090,740 bits
    level d=3:          −4,181,546 bits
    level d=6 (= q):    −10,453,966 bits

Consequences for this node:
1. The per-level normalization q_K = p^d is CONFIRMED against an
   external proved family: at d = 1 it reproduces upstream's floors; at
   d = 6 it reproduces the q-scale models upstream themselves refuted.
2. At KoalaBear-shaped rows the recursion is depth ONE in practice:
   intermediate levels are dead by millions of bits at the deployed
   profiles; the levels-(2,3) columns are correctly-priced guards. The
   bookkeeping fear in fork F3 of s6 ("each level multiplies
   bookkeeping") is quantitatively toothless at these rows.
3. The population the base level prices is tangent-column mass (their
   floor = C(m',m)·⌈tangent mean⌉ — the weld identity, MB_VS_F1_LEDGER
   §2), i.e. case-(i)/B-rational routing, consistent with this node's
   descent-to-minimal-field structure.
