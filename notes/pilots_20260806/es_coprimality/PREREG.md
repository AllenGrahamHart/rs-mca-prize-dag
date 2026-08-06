# PRE-REGISTRATION — the COPRIMALITY MECHANISM: turn C4-c into a theorem

Round 17, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. This is the PROOF lens on
the re-posed terminal (ES-G); the sibling es_g_lanes audits the
consumers — do not read its dir.

## 0. The lead (verbatim, round-16 boundary adversary REPORT §C4-c)

> **(C4-c) Generic coprimality is the real suppressor.** Accidents
> require the ideals (x_1,…,x_{w-1}) to share a prime; for w ≥ 3 the
> gcd of norms collapses to 1 for almost every orbit. This — not
> entropy — is why the crossing shape is clean over all p, and it is
> the structural reason suppression beats the entropy prediction
> wherever it does.

And the paired frontier from the AK pilot (REPORT §A5): the decisive
invariant is the defining set's divisor profile; the open problem is a
characteristic-p analogue of vanishing-sums-of-roots-of-unity rigidity
(Lam-Leung / Conway-Jones) in the sub-balance regime. Coprimality and
rigidity are two halves of one question — this pilot works the
coprimality half.

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260806/es_boundary_adversary/REPORT.md` — the
  method (S is a solution in char p iff p | N(I_S)), the five
  witnesses (what NON-coprimality looks like), the crossing-shape
  census (n=32, r'=w=8, zero accidents over all characteristics), the
  stratum mechanism.
- `notes/pilots_20260806/es_axkatz_transfer/REPORT.md` — §A5 (the
  divisor profile D(Z)), THEOREM AK-UNIT (what any proof must NOT
  route through).
- `notes/pilots_20260804/mun_anticoncentration/REPORT.md` (recovered)
  — LEMMA Z / the char-0 classification, the MDS/RS identification,
  the F2-A2 "multi-condition ideals are generically coprime" finding
  it cites.
- `background/nodes/dli_wcl_weight3_ambient_exclusion/proof.md` and
  the weight4 sibling — the BANKED bad-prime/resultant method (this
  is prior art for the machinery; the theorem sought here is new).
- `critical/nodes/b1_char0_giant_coset_theorem` — LEMMA Z of record.

## 2. Pre-registered deliverables

- **(K1) THE COPRIMALITY CONJECTURE, stated exactly.** Formalize:
  for the window element family {x_s = p_s(S)} (power sums / the
  window forms of the (ES-G) object) over subsets S of mu_n with the
  structural (periodic) family removed, the ideals (x_1,...,x_{w-1})
  in Z[zeta_n] are coprime — i.e. N(I_S) = 1 — outside an explicitly
  characterized exceptional class. State it so that (ES-G)'s crossing
  instance FOLLOWS from it (a solution in char p needs p | N(I_S);
  N(I_S) = 1 kills every characteristic at once). State the exact
  relationship to the stratum decomposition: the conjecture should
  predict WHICH strata carry the exceptional class.
- **(K2) PROOF ATTEMPT at w = 3** (the smallest case with the
  observed collapse). Available structure: x_1 = e_1(S), x_2
  relates to e_2 via Newton; the char-0 classification (LEMMA Z)
  characterizes N(I_S) = 0; what is needed is a bound/characterization
  of when a RATIONAL PRIME divides N(I_S). Candidate tools the
  coordinator suggests testing IN THIS ORDER, each with a named
  verdict: (a) the resultant factorization the DLI/WCL nodes banked
  (does Res(Phi_n, V_1, V_2) admit a closed form whose prime support
  is characterized?); (b) Galois-orbit counting (N(I_S) = prod over
  primes above p of local conditions — when does the orbit of S under
  Gal force triviality?); (c) the Lam-Leung structure theorem in
  char 0 pushed to bounds on N(I_S) rather than just vanishing.
- **(K3) THE EXCEPTIONAL CLASS vs the five witnesses.** Whatever (K1)
  characterizes as exceptional must CONTAIN all five round-16
  witnesses (they are non-coprime by construction). Verify each
  witness's N(I_S) factorization explicitly and test whether the
  characterization predicts its witness prime.
- **(K4) Quantified evidence at reachable rows.** Measure the
  coprimality rate exactly (fraction of orbits with N(I_S) = 1) as a
  function of (n, r', w) on the reachable grid, reusing the round-16
  machinery (`notes/pilots_20260806/es_boundary_adversary/es_lib.py`
  may be READ and adapted — it is banked, not sibling-active work).
  Pre-register expected shape: rate -> 1 as w grows at fixed shape,
  with exceptional mass concentrated on low strata.
- **(K5) The conditional statement banked.** Whatever is proved,
  state the exact conditional: (K1-restricted-to-X) => (ES-G
  crossing instance at rows Y). Name what remains.

## 3. Pre-registered falsifiers / honesty clauses

- If the coprimality rate does NOT tend to 1 (or exceptional mass is
  NOT structurally characterized) on the measured grid, the mechanism
  is not the suppressor — report the refutation and what the data
  says instead.
- A proof route through any congruence/divisibility conclusion about
  the COUNT (rather than about N(I_S)) is excluded by AK-UNIT —
  self-check against it before claiming a route.
- The five witnesses are ground truth: any characterization that
  excludes one of them is WRONG regardless of its elegance.

## 4. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/es_coprimality/`.
  Never touch dag.json, node shards, tools/, or push. Do NOT read
  `notes/pilots_20260806/es_g_lanes/` (sibling this round).
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.
