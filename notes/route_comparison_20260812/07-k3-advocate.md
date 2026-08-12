# K3/SEM-QBC route: strongest honest attack plan

## 1. SEM-QBC candidate statement

SEM-QBC is a **definition+theorem package**, not a bare theorem: the frozen Q/BC predicates are opaque strings (`BAD_SLOPE_NOT_EARLIER_AND_HAS_ACTIVE_V4_*_CERTIFICATE`, #1158 §2), so no candidate exists to prove correct until executable predicates are fixed — and the (COV) anti-tautology clause puts proof obligations on the definitions themselves.

**Package SEM-QBC.** For each received line r and witness space W_r(m):

- **D1.** Executable P_Q(r,w): a typed prefix-family relation at K=k (scope = GF:4997–5013's Q-theorem family).
- **D2.** Executable P_BC(r,w): the cycle-19 active shifted-lattice certificate (K=k+1=1048577, ω=981104, w=67471, d1≥w+1; schema retains line, slope, support locator, explaining data, reduced basis, earlier-owner trace, balanced profile — `19-active-bc-semantic-gap-20260810.md:38-49`).
- **Theorem (SEM-QBC).** Q_frozen(r)=π_γ{w:P_Q}, and Z_BC(r)=π_γ{w:P_BC}∖(Z_paid(r)∪π_γ{w:P_Q}), uniformly over received lines, satisfying #1159 §6's six conditions (verified verbatim in the pr1163 source).

**Package Rec_2_4.** Rec_{2,4}(r,γ,c,e)=ValidBC(r,γ,c)∧End_{2,4}(r,γ,c,e), with End carrying the actual Q=6,s=6,u=2 record, plus selector/(FIB)/fence theorems, selector taken on the complete realizable tuple.

**Honest repose of (COV):** as posed ("coverage against the independently defined frozen cell") it is unposeable — no source defines Z_BC^(2,4). Repose: define the frozen cell by the row manifest's first-match order (GF:4767) and prove π_γ{P_BC} equals the complement of (earlier owners ∪ π_γ{P_Q}) within active bad slopes. Anti-tautology is preserved because P_Q and the earlier-owner list are independently executable — this is the only formulation that can ever be non-circular.

## 2. Sub-lemma decomposition

1. **L1 (soundness).** Certificate reconstructs an actual witness: identical pair, slope, original support, deg<k explanation.
2. **L2 (K-adapter).** Exact adapter K=k+1 prefix envelope → deg<k lattice **including the boundary** d1^(k)=d1^(k+1)=67473 (boundary-vs-first-interior collision, #1159 Thm 4.1). Hard: one extra interior coefficient appears/disappears; owner assignment must survive.
3. **L3 (slope-global Q exclusion).** For every BC-selected slope, *no* Q witness exists — universal over all witnesses, not a tag on the chosen one. Genuinely new: needs a witness-level Q/BC dichotomy per slope.
4. **L4 (coverage).** The reposed (COV) above.
5. **L5 (support preservation).** Size-≥m source support; exact-m subsupport keeps every downstream guard.
6. **L6 (fences).** All-Z_BC fence + complement fence: every BC slope not routed to (2,4,2) → earlier owner / separately paid component / explicit U_new.
7. **T5 (endpoint realization) — HARDEST.** Same-record Q=6,s=6,u=2 realization of each compiled witness. Why hardest: the 256-assignment audit proved *logical independence* (31 assignments: nonempty Z_BC, empty endpoint set — cycle 19:18-26), so no partition algebra suffices; it must be constructive, and #1158 refuted the direct coordinate identification — only the disclosed conjugated fold gτg⁻¹(T)=−T survives, and using it requires a new record-transport theorem (line, support, owner, chronology, guards).
8. **T6 (FIB).** Section s_r, exact fiber constants M_t; exact route preimage multiplicities, not label counts.
9. **T7 (reconstruction invariants + totality).**

## 3. Reuse map

- **Cycle-19 compiler [PROVED]** → D2 entirely, L1 substantially, witness half of T6 (unit fibers by lex minimization).
- **#1130 source-pencil compiler** (per supplied endpoint record) → everything downstream of T5: once realized, compilation is proved.
- **#1132 order-two classification** → target-typing for L6/T5 (never as slope bridge — R-2).
- **thm:partial-relative for any 32 actual slopes** (#1159 §5) → L4 coverage arguments.
- **#1160 2w charge + repair 5** → L3/L4/L5 same-witness semantics and mandatory regression.
- **Adapter exchange-graph** (`shortening_adapter_staircase_import/proof.md:3-41`) → L5.
- **Raw workboards** (25,200 systems/0 survivors; cell-5/11 105-label closures) + **Scott replays #1153/#1157** → convert through the wired conditional chain (positive payment → orientation → allocation → ledger) with zero re-derivation, plus independent_review evidence.

## 4. Depth estimate: 20–26 coordinator-audited packets

Bridge: D1+D2+L1 re-issue as typed relations with a parsing verifier (fixing #1159 §5(ii)-(iii)) ≈ 1; L2 ≈ 2; L3 ≈ 2; L4 ≈ 1; L5 ≈ 1; L6 ≈ 1; T5 ≈ 3 (incl. conjugacy-transport theorem); T6/T7 ≈ 1. Subtotal ≈ 9–12. Downstream (already wired, statuses TARGET): eleven-route payment ≈ 4–6 (433-1b→O0b residual = 408 rows/42,840 labels ≈ 1–2; ten remaining routes batch); source-line/source-cover/trivial-stabilizer ≈ 3; allocation definition (sibling U_Q/U_new atoms — the joint floor cannot isolate U_BC) ≈ 2–3; assembly+ledger arithmetic ≈ 1; independent review ≈ 1–2. Honest reading: heavy total, but ~8 packets are risk-free conversions of banked assets; the novel-math risk concentrates in exactly L2, L3, T5 (≈5 packets).

## 5. Three cheap decisive falsifier probes

1. **Boundary-record adjudication (kills L2).** Run the candidate K-adapter by hand on the one actual deployed d1=67473 record from #1159. If mapping the K=k+1 boundary certificate to a deg<k witness changes the owner (the extra interior coefficient cannot be absorbed), condition (4) is dead as posed. One record, pure algebra, <1 packet.
2. **Two-witness Q-collision search (kills L3).** Exhaustively enumerate a small-field model (GF(17) atom scale, `tools/ramguard tiny`) for one slope carrying both a BC certificate and a Q witness. A hit falsifies slope-global exclusion for the entire lexicographic-selector class (#1158's stated unsafety) and forces a priority-repair theorem; a proven small-field dichotomy is the template.
3. **#1160-line rejection regression (kills D2/L4/L6 semantics).** Feed the 67,472-slope globally-affine line through P_BC. Its balanced set is empty (SOURCE-STATED), so P_BC must reject every slope; one acceptance kills the definitions at deployed scale. Doubles as the mandatory #1160 regression.

A route killable this cheaply is a feature: all three probes run before any theorem-writing.

## 6. Upstream-bankable PR shape

Stack on **#1152** (the living K3 export): (i) SEM-QBC typed executable relations + a verifier that parses and checks **one actual certificate** (directly answering #1159 §5(iii)); (ii) L1–L6 theorem files with probes 1–3 as committed regressions; (iii) Rec_2_4 + selector/(FIB)/fence; (iv) transport of the two banked raw zeros (433-1a→O0b, 433-1b→O0a) from `distinct_affine_slope_payment=null` to literal **0** — satisfying cycle-12's promotion test ("prove a source-bound transport into one frozen first-match cell; then… an exhaustive zero residual") and delivering the K3 campaign's **first nonzero-information ledger movement**, the exact success condition B that #1157 says the route currently terminates without.