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

---

# PILOT APPENDIX — registrations Q0-Q6 (appended BEFORE any computation)

Opus pilot, round 17, 2026-08-06. Everything below is registered in
advance of running a single line of code in this pilot dir.

## Q0. Notation, pinned

`n = 2^m`, `h = n/2 = phi(n) = [K:Q]`, `K = Q(zeta_n)`, `O_K = Z[zeta_n]`,
`Phi_n(X) = X^h + 1`.  `S <= Z/n`, `|S| = r'`.  For `s in Z/n`,

```text
x_s = sum_{i in S} zeta^{s i}  in  O_K,     I_S = (x_1, ..., x_{w-1}) <= O_K.
```

`N(I_S) = [O_K : I_S]` (absolute ideal norm; `N(0) = 0`, `N(O_K) = 1`).
`delta = ord_n(p)`.  `Z_w = Z_w(n,p)` = the p-cyclotomic closure of
`{1,...,w-1}` mod `n` (`es_lib.py:339-347`).  NEW notation registered here:

```text
Z_w^odd  :=  { s in Z_w : s odd }   =  the <p>-closure of {s odd, 1<=s<=w-1}
                                        inside (Z/n)^*.
a_{n/2}(S) := #{ (i,j) in S x S : i - j = n/2 mod n }.
strat(S)  := max { a >= 0 : S + n/2^a = S }   (the stratum index; a=0 always).
```

## Q1. (K1) THE COPRIMALITY CONJECTURE — registered in three tiers

**Tier 0 (BANKED, cited not claimed).** `N(I_S) = 0` iff `S` is a
`mu_M`-coset union, `M` = least power of two `>= w`.  This is LEMMA Z,
`critical/nodes/b1_char0_giant_coset_theorem/node.json:9`.

**Tier 1 — THEOREM CS (registered as a claim TO BE PROVED).**
Let `p` be an odd prime, `S` with `x_1 != 0`.  If `p | N(I_S)` then

```text
p^{|Z_w^odd|}  divides  |N_{K/Q}(x_1)|                                (CS1)
|N_{K/Q}(x_1)| <= (r' - a_{n/2}(S))^{n/4}                             (CS2)
==>   |Z_w^odd| * log2 p  <=  (n/4) * log2( r' - a_{n/2}(S) ).        (CS3)
```

Contrapositive (**the coprimality corollary**): if `|Z_w^odd| log2 p >
(n/4) log2 r'` then `p` divides `N(I_S)` for NO `S` with `x_1 != 0`.

**Tier 1b — LEMMA STRAT (registered as a claim TO BE PROVED).**
If `strat(S) = a >= 1` then `x_s = 0` for `2^a` not dividing `s`, and
`x_{2^a t} = 2^a * iota(p_t(S'))` where `S' <= Z/(n/2^a)` is the reduced
set (`|S'| = r'/2^a`) and `iota : Q(zeta_{n/2^a}) -> K`.  Hence
`I_S = 2^a * iota(I_{S'}) O_K` and the ODD bad primes of `(n,r',w,S)` are
exactly the odd bad primes of `(n/2^a, r'/2^a, w', S')` with
`w' = floor((w-1)/2^a) + 1`.

**Tier 2 — THE CONJECTURE PROPER (CC).**  For `w >= 3`:

> `N(I_S) = 1` for every `S <= Z/n` outside the exceptional class
> `E(n,r',w) := E_strat ∪ E_floor`, where `E_strat = {S : strat(S) >= 1}`
> and `E_floor = {S : some p with |Z_w^odd(p)| log2 p <= (n/4) log2 r'
> divides N(I_S)}`.  Tier 1 makes `E_strat ∪ E_floor` PROVABLY exhaustive;
> CC is the assertion that `E_floor` is additionally SPARSE, with density
> `-> 0` as `w` grows at fixed `(n, r'/n)`.

**Which strata carry the exceptional class (registered prediction):**
`E_strat` is carried by `1 <= a < log2 M`; at `a >= log2 M` LEMMA Z takes
over and `N(I_S) = 0` (structural, not exceptional).  Within `E_strat` the
binding stratum is the one whose reduced instance has `w' = 2` (a single
generator, so `N(I_S') = |N(x'_1)| >> 1`).

**How (ES) follows (the K1 requirement).**  `N(I_S) = 1` means `I_S = O_K`,
so NO prime of `O_K` contains every `x_s`, so `S` is a solution in NO
characteristic whatsoever.  If CC holds at a row and the row's `p` is above
the floor (CS3) and the row's `S` are non-stratified, then the only
solutions are the LEMMA Z periodic ones -- which is exactly the (ES)
crossing instance.  Registered as the conditional to be banked in (K5).

## Q2. (K2) Proof-attempt order, with pre-named verdicts

Tools tested in the mandated order (a) resultant, (b) Galois-orbit
counting, (c) Lam-Leung.  I register in advance that I expect **(b) to be
the one that works** -- (CS1) is a Galois-orbit count -- and that (c) is
expected DEAD on subtraction grounds (see Q6).

## Q3. Registered falsifiers (any hit retracts the named item IN FULL)

- **Phi1.** Every round-16 census accident with `x_1 != 0` satisfies
  `p^{|Z_w^odd|} | N(x_1)` EXACTLY.  One violation retracts THEOREM CS.
- **Phi2.** Every such accident satisfies (CS3).  One violation retracts.
- **Phi3.** For every `S` with `strat(S) = a >= 1`, LEMMA STRAT's identity
  and the odd-bad-prime equality hold exactly.  One violation retracts.
- **Phi4 (independence).** `N(I_S)` computed by Smith/Hermite normal form
  of the `h x (w-1)h` multiplication matrix has prime support EQUAL to the
  census bad-prime set, on every fixture tested.  A mismatch retracts BOTH
  the census reading and my own -- machinery bug, nothing reported.
- **Phi5 (the mandate's own falsifier).** If the coprimality rate does not
  tend to 1 in `w`, or if exceptional mass is not concentrated on
  `E_strat ∪ E_floor`, the mechanism is NOT the suppressor -- report the
  refutation.
- **Phi6.** All five round-16 witnesses must lie in `E(n,r',w)`.  A witness
  outside it retracts the characterization regardless of elegance.

## Q4. Registered numeric predictions (scored either way)

- **R1.** At `n = 32`, `w >= 3`, the non-coprime orbits are either
  `strat >= 1` or carry only primes `p` obeying (CS3).
- **R2.** The coprimality rate at fixed `(n, r')` is NON-DECREASING in `w`.
- **R3.** At the crossing row `(n,r',w) = (32,8,8)` the rate is exactly
  `1.000` on all non-periodic orbits (round-16 measured zero accidents;
  I predict THEOREM CS explains it for every `p` above the floor, and
  that the floor at that row is `p <= 64` at `delta = 1`).
- **R4.** `w = 2` is the degenerate case: rate near 0, because `I_S` is
  principal.  The collapse is a `w >= 3` phenomenon.

## Q5. AK-UNIT SELF-CHECK (registered before use)

`THEOREM AK-UNIT` (`notes/pilots_20260806/es_axkatz_transfer/REPORT.md:44`)
excludes any route whose conclusion is a congruence/divisibility statement
about the COUNT `|W_w|`.  THEOREM CS concludes a divisibility statement
about `N_{K/Q}(x_1)` -- an algebraic-integer norm attached to an
INDIVIDUAL set `S`, not to the count -- and it is used only to contradict
an ARCHIMEDEAN size bound (CS2).  The output is "`S` is not a solution",
per set; the count statement is then a consequence of quantifying over
`S`, never a congruence.  I register that if any step of my route ends in
a statement of the form `p | |W_w|` or `|W_w| = c mod p`, the route is
VOID and I report it as such.

## Q6. Subtraction registered IN ADVANCE (from my prior-art sweep)

Conceded as banked, cited not claimed: (i) NG1/NG2 norm gate
(`notes/U1_OFFICIAL_ROW_NORM_GATE_TABLE.md:19-31`); (ii) the archimedean
`weight^{n/4}` ceiling (`f3_h3_low_distance_ideal_star_router
/statement.md:43-48`); (iii) `p | N(J)` from `J <= ker(O -> F_q)` + Smith
(`dli_wcl_ell2_weight5_pair_ideal_index_obstruction/proof.md:36-52`);
(iv) the alignment biconditional
(`f3_h3_ideal_star_prime_alignment_criterion/statement.md:12-18`);
(v) the halving resultant recursion
(`dli_wcl_ell2_weight6_recursive_norm_exclusion/proof.md:77-80`);
(vi) the odd-dilation COLLAPSE identity; (vii) LEMMA Z; (viii) Lam-Leung
at `n = 2^m` is EXHAUSTED (`S5_LAM_LEUNG_TRANSPORT.md:1,12-35`).
What I claim as new is ONLY the exponent `|Z_w^odd|` in (CS1) -- the
Galois multiplicity supplied by the window -- and LEMMA STRAT.
Round-16's registered M3 (`es_boundary_adversary/PREREG.md:165-176`) has
exponent `delta` (ONE prime); I register that my contribution is precisely
the upgrade `delta -> |Z_w^odd|`, and that if that upgrade is found banked
anywhere I withdraw it.
