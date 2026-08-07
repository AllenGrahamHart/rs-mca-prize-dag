(Coordinator-persisted verbatim from the pilot's final message, 2026-08-07.)

Sanity check done: both suites re-run clean (126 + 11 = 137 checks, 0 failures), both fail-closed controls exit 1, only the four files in my own pilot dir were written, no dag.json/node/tool edits, no git, no status flips, CAMPAIGN_LEDGER never opened.

# RED CLOSABILITY PROBES — round 21

**Both probes return NO. Neither red is closable by the named theorem, and in both cases the blocker is structural and already banked — not a missing computation.**

Artifacts (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/red_closability_probes/`): `PREREG.md` (my §P0–P8 appended before any computation), `PROOFS.md`, `probe1_verify.py`, `probe2_verify.py`.

## PROBE 1 — `integer_code_distance_cert` vs Z-1/Z-2: MISMATCH, with the scope check *passing*

The node's system is `K_p = { v in Z^{N'} : sum_x v_x zeta^x = 0 in F_p }`, `zeta in F_p` of exact order `N'` (`critical/nodes/weight_graded_mitm/proof.md:26`; identically `critical/nodes/kernel_lattice_reframing/proof.md:25`). Folding it (PROVED reduction) puts it into *exactly* Z-2's shape. Hypothesis match, term by term: **(H1) char &gt; w HOLDS. (H2) omega of exact order 2N HOLDS. (H3) distinct exponents in {0..N-1} HOLDS. (H4) FAILS.**

The brief said the shift-0 scope check "is the whole probe". It isn't — **the scope check passes cleanly**. The single exponent is `j=1`, the first odd power, so the 43 banked shifted counterexamples are irrelevant here. The probe dies one slot later, on the number of vanishing conditions:

- Z-1/Z-2 give min l1 weight `&gt;= 2*ell+1`. The node needs `&gt; 2l' = 130` at the rate-1/2 prize cell (`l' = rho N'+1 = 65`), so it needs **ell = 65**. The system supplies **ell = 1**. Deficit: 64 conditions; weight gap 128 units.
- **ell=1 is permanent, and the repo already proved it.** `background/nodes/multi_multiplier_reduction/node.json:8`, status REFUTED, verbatim: *"the k-multiplier residue matrix is an OUTER PRODUCT mod p — rank 1 for every k — so the stacked ternary kernel equals the single relation's kernel"*. That refuted node is the one that minted the phrase "the explicit k x N' system" still in this node's title. I verified rank exactly 1 for k in {1,2,3,5,10} at six cells.
- **Z-2 at ell=1 gives the node literally nothing**: its conclusion is "no nonzero c with l1 weight ≤ 2", i.e. `zeta^a != ±zeta^b`, which is immediate from `zeta` having exact order `N'` and is already assumed. I verified the floor 3 is *attained* (N'=8, p=17), so no sharpening at ell=1 can ever exceed 3.
- Positive control: on the genuine ell-condition system Z-2 holds exhaustively (7 configs), and I reproduced the banked smallest shifted counterexample (2N=12, p=13, a=1, weight 2 &lt; 3) — plus its mechanism: the shifted generator `omega^3` has exact order 4 &lt; 2N, so **the shift destroys (H2), not (H4)**.

No bounded new work closes this: it would mean manufacturing 64 further independent odd-power conditions, and the only named mechanism for that is refuted by a rank argument holding for every k.

**Two catches, both mine, both in banked material:**

- **CATCH-P1** — `critical/nodes/integer_code_distance_cert/notes/folded_certificate.md:19-20` records "N'=16, p=10177: 48 collisions, min support 5". The 48 replicates exactly (all 8 primitive roots), but **5 is the folded Hamming weight; the node's threshold is unfolded ternary support, which is 7**. I proved and verified the fold lemma (min ternary support = min folded *l1* weight) and confirmed exhaustively at that cell: supports 1–6 give 0 vectors, support 7 gives 128. The verdict at that cell is unaffected; the number is the wrong statistic for a certificate.
- **CATCH-P2** — `critical/nodes/weight_graded_mitm/proof.md:110-114` justifies its factor-`N'` search speedup by "Frobenius orbits, index multiplication by `p mod N'`". But the node's standing hypothesis is `p = 1 mod N'`, so that map is the **identity** and the orbit has size 1. Index-multiplication by a general odd `a` isn't a symmetry of `K_p` at all (explicit counterexample at N'=8, p=17, a=3). The factor-`N'` saving survives, but via **cyclic shift**, not Frobenius. Conclusion right, stated mechanism wrong — and this is a certificate node.

Bonus quantification of the residual: the PROVED high-field branch (`p &gt; 253^32`, threshold 255.4558 bits) covers only **5.02%** of the crossing lane's e=1 prime-row log-window; the four pinned Proth exhibits sit 84.5–88.5 bits below it.

## PROBE 2 — `unsafe_crossing_family_instantiation` vs THEOREM BB: BB closes **no part**

Quantifier, verbatim (`critical/nodes/unsafe_crossing_family_instantiation/statement.md:8-9`): *"For every admissible row and its proposed first-safe agreement `a_safe`, emit an exact certificate at `a_safe-1`..."*, with the counted object fixed by the falsifier at `:40` as `B_C(a_safe-1)` and by `claim_contract.md:8` as *"the exact bad-slope count convention used by `mca_grand`"*.

All four registered gates fail, and the first fails on its own:

- **(C1) WRONG FUNCTIONAL — fatal, and it fails ahead of the e=1 gap** (as I pre-registered in P6). BB bounds `L_1(a) = max_u #{c : agr(c,u) &gt;= a}` (codewords for one word); the node counts `B_C(a)` = max number of support-wise MCA-bad **slopes** on one received pair. The LIST→MCA path is a chain of CONDITIONAL nodes, not a count inequality. **Exact finite countermodel**, both counts computed exhaustively on `RS[F_5,|D|=4,k=2]`: at `a=2`, `L_1 = 6 &gt; B* = 5 &gt;= B_C = 5` — so `L_1(a) &gt; B*` does **not** imply `B_C(a) &gt; B*`. Structural reason: `B_C(a) &lt;= q` always, `L_1(a)` is bounded only by `|C|`. (I used the plain MCA-bad predicate; the support-wise refinement only removes slopes, so my `B_C` *upper* bounds are safe under the official convention. The countermodel refutes the inference, not the prize row.)
- **(C2) ROWS** — I independently re-derived BB's live-window table to four decimals. Admissible degrees are exactly `e in {1..6}`; BB covers `e in {3,4,5,6}` fully, `e=2` partially, and `e=1` not at all — and not for want of compute (`gamma_shell/REPORT.md:91`: *"Prime rows untouched, and unreachable by this method at any v"*).
- **(C3) FORM** — a list of codewords for one received word gives one slope, not `B*+1` distinct slopes; it is not a Q, V, or M payload.
- **(C4) ENDPOINT** — BB sits at `k+2^34 = 1116691496960`; the node's deployed endpoints are 1116047 and 1116023, a factor 1.0e6 apart.

**Sharper than "incomplete": on the pair-feasible branch BB's coverage is *disjoint* from the residual.** `critical/nodes/unsafe_crossing_family_instantiation/dependency_subdag.md:105-110` records that exact perfect-power interval checks *"force extension degree one"* there — precisely the row class BB provably cannot reach. `(RHL-B12)` covers none of it either: it is LIST-side and budget-scoped (`B* in {1,2}`).

I verified the lane wiring by hand in `dag.json`: the node has exactly one out-edge, to `unsafe_at_crossing` (→ `mca_unsafe` → `mca_grand`); `rate_half_list_adjacent_crossing` has exactly one, to `list_adjacency_closing` (→ `list_grand`). Different obligations. **CATCH-P3**: `notes/roadmap/LIST.md:16-17` nonetheless files this MCA node under LIST, and `notes/roadmap/MCA.md` never names it — the board mis-filing that makes "BB may have closed it" look plausible.

**No certificate is written for a closable part, because there is no closable part.** What is already closed on this node (not by BB): the finite deployed `V` slice at KoalaBear and Mersenne-31 via `identity_prefix_flexible_budget_unsafe_floor`. One lead, honestly labelled as a lead: BB's *method* (pigeonhole over a concentration class + a Cauchy–Schwarz accident lower bound) is the shape the M-route's `nu(A)` needs — different objects, no transfer banked.

**Rule note for the coordinator:** all python ran under `tools/ramguard tiny|local -- python3`, including my own draft-file patches and the PREREG append. Draft files themselves were authored with the harness file tool, which runs no shell and no python — flagging that reading of "including file patching" in case you want it tightened.

result: Both round-21 closability probes return NO with exact gaps — Z-1/Z-2 cannot touch `integer_code_distance_cert` (its system supplies ell=1 odd-power condition against the ell=65 needed, and `multi_multiplier_reduction`'s REFUTED "rank 1 for every k" proves that permanent; the shift-0 scope check actually *passes*), and THEOREM BB closes no part of `unsafe_crossing_family_instantiation` (wrong functional `L_1` vs `B_C`, refuted by an exact finite countermodel `L_1=6 &gt; B*=5 &gt;= B_C=5`, plus e=1 rows unreachable and *disjoint* from the pair-feasible residual) — 137 checks/0 failures, both fail-closed controls exit 1, no status flips, plus three catches in banked material (folded_certificate's "min support 5" is a folded-Hamming count where the node-relevant unfolded support is 7; weight_graded_mitm's factor-N' speedup is justified by a Frobenius map that is the identity when p≡1 mod N'; roadmap/LIST.md files the MCA node under LIST).
