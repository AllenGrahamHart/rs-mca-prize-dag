# WIRING proposal — the DLI norm-gate mint package (4 nodes)

Prepared 2026-08-02 by the norm-gate mint-prep pilot. **Nothing here has been
applied**: `dag.json`, `background/`, `critical/` and `tools/` are untouched.
Everything below is a proposal for the coordinator to audit, adjust and wire.

All four nodes are **background** nodes (same tree as the sibling
`background/nodes/dli_c1_ternary_relation_norm_sandwich/`), each with the
three artifacts `statement.md`, `proof.md`, `verify.py`.

Destination paths (drafts to be moved as-is after audit):

```text
drafts/dli_norm_gate_forward_and_ofold/  ->  background/nodes/dli_norm_gate_forward_and_ofold/
drafts/dli_norm_gate_energy_ceiling/     ->  background/nodes/dli_norm_gate_energy_ceiling/
drafts/dli_norm_gate_splitting_law/      ->  background/nodes/dli_norm_gate_splitting_law/
drafts/dli_official_support_forcing/     ->  background/nodes/dli_official_support_forcing/
```

After moving, `tools/run_all_verifiers.py` discovers `verify*.py` under
`background/nodes/**` automatically, so `tools/verifier_manifest.json` must be
regenerated (the four `verify.py` plus the eight `statement.md`/`proof.md`
hashes). None of the four verifiers needs a Modal launcher; all run under
`tools/ramguard tiny` in under 3 seconds each.

---

## 1. `dli_norm_gate_forward_and_ofold`

```json
{
 "id": "dli_norm_gate_forward_and_ofold",
 "title": "DLI norm gate, forward direction: a block-U skew/relation solution forces q^o | Norm in Z[zeta_n], with the basis-range hypothesis load-bearing, plus the determinant-free evaluation form",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Let n=2^s>=4, h=phi(n)=n/2, Z[zeta_n]=Z[x]/(x^h+1), q an odd prime with n | q-1, and zeta in F_q of exact order n. (LN0) x^h+1 splits mod q into h distinct linear factors (x-zeta^j), j odd mod n, so q is unramified, the h primes p_j=ker(zeta_n->zeta^j) are distinct of residue degree 1 and norm q, and Gal=(Z/n)^* permutes them SIMPLY TRANSITIVELY via sigma_a^{-1}(p_j)=p_{ja}; q odd with n a power of two gives unramifiedness and n | q-1 gives residue degree 1 -- both hypotheses are used. (LN1) If alpha=sum_{i in G} eps_i zeta_n^i with G inside the BASIS RANGE [0,h) and eps in {+-1}^G satisfies alpha(zeta)=0 in F_q, then Norm(alpha) != 0 and q | Norm(alpha); the basis-range hypothesis is LOAD-BEARING (an opposite pair {i,i+h} folds to the zero element, Norm 0), and it is exactly the banked C1 reduced-signed-support clause, satisfied by construction at every junction of the DLI tower. (LN2) If in addition alpha(zeta^u)=0 for every u in U with |U|=o, then q^o | Norm(alpha) != 0; more generally v_q(Norm(alpha)) >= m(alpha) := #{j odd : alpha(zeta^j)=0}. Two independent proofs: Hensel-lifting x^h+1 over Z_q (elementary), and the o primes p_u being pairwise distinct by simple transitivity. Official instantiation: at junction j, U_j={odd u : u 2^j <= t}, so every nonzero junction-j skew has q^{L_j} | Norm != 0. (LN3) Norm(alpha) = prod_{j odd mod n} alpha(zeta^j) in F_q, so q | Norm iff m(alpha)>=1 -- the measurement is h modular evaluations, not an hxh determinant. At t=2 the junction-0 block is U_0={1} with columns zeta^i, i in Z/(n/2), so a junction-0 C2'' skew solution IS a C1 ternary relation at 2N=n; the two censuses agree byte-for-byte where they overlap. NOT claimed: any converse (q^o | Norm does not imply a U-solution), any statement outside the basis range, any upper bound on Norm, or the C1 census identification at j>0. Provenance notes/pilots_20260802/dli_norm_gate/ (LN0-LN3); formalizes the C2'' pilot's L13.",
 "refs": [
  "background/nodes/dli_norm_gate_forward_and_ofold/statement.md",
  "background/nodes/dli_norm_gate_forward_and_ofold/proof.md",
  "background/nodes/dli_norm_gate_forward_and_ofold/verify.py"
 ]
}
```

## 2. `dli_norm_gate_energy_ceiling`

```json
{
 "id": "dli_norm_gate_energy_ceiling",
 "title": "DLI norm gate, energy ceiling: 1 <= Norm <= E^(phi(n)/2) for arbitrary integer coefficient vectors (the C1 sandwich Claim 2 with w -> E, ternariness never used), and the junction router it powers",
 "status": "PROVED",
 "closure": "proof",
 "statement": "In Z[zeta_n]=Z[x]/(x^h+1), n=2^s>=4, h=phi(n)=n/2, for every NONZERO alpha=sum_{i<h} a_i zeta_n^i with integer a_i and energy E=sum_i a_i^2: (LN4) 1 <= Norm(alpha) <= E^(h/2). The proof is the banked dli_c1_ternary_relation_norm_sandwich Claim 2 verbatim with w replaced by E: conjugate-pair positivity, negacyclic Parseval sum_{j odd} |alpha(zeta^j)|^2 = h sum_i a_i^2, AM-GM over the h/2 pair values, and Norm >= 1 from irreducibility of x^h+1. Parseval is the only step where the coefficients enter, and it enters as sum_i a_i^2 -- TERNARINESS IS NEVER USED; on ternary vectors E=w and the statement is the banked one. (LN5) Consequently, at a junction with root order h_j, degree N_j=phi(h_j) and block size o=L_j, combining with q^{L_j} | Norm != 0 (dli_norm_gate_forward_and_ofold) every nonzero junction-j skew solution satisfies q^{L_j} <= Norm <= E^{N_j/2}, i.e. E >= min{E : E^{N_j/2} >= q^{L_j}}; contrapositively, if E^{N_j/2} < q^{L_j} the junction admits no nonzero skew of energy <= E, so a state whose whole admissible skew domain has sum_i c_i^2 <= E is killed. At a uniform ratio N_j = 256 L_j the criterion collapses to q <= E^128 independently of j. NOT claimed: any lower bound on Norm beyond 1, the exact maxnorm ladder (banked, and its stable-range doubling law is REFUTED in general), sufficiency of the energy condition, or the WCL fence. Provenance notes/pilots_20260802/dli_norm_gate/ (LN4, LN5).",
 "refs": [
  "background/nodes/dli_norm_gate_energy_ceiling/statement.md",
  "background/nodes/dli_norm_gate_energy_ceiling/proof.md",
  "background/nodes/dli_norm_gate_energy_ceiling/verify.py"
 ]
}
```

## 3. `dli_norm_gate_splitting_law`

```json
{
 "id": "dli_norm_gate_splitting_law",
 "title": "DLI norm-gate splitting law: phi(n) times the solution count equals sum |H_U| exactly, the ratio is mbar/phi(n) >= 1/phi(n) with equality iff multiplicity <= 1, and q^(o+1) > maxnorm forces exactness",
 "status": "PROVED",
 "closure": "proof",
 "statement": "Setting: n=2^s>=4, q odd prime with n | q-1, zeta in F_q of exact order n, W_w the ternary weight-w vectors supported in the basis range [0,phi(n)), Z(alpha)={j odd : alpha(zeta^j)=0}, H_U(alpha)={a in (Z/n)^* : a.U inside Z(alpha)} for a block U of o odd residues, Sol_U={alpha in W_w : 1 in H_U(alpha)}, D_U={alpha : H_U(alpha) nonempty}. (S1) phi(n)|Sol_U| = sum_{alpha in W_w} |H_U(alpha)| EXACTLY -- a double count using that sigma_a: zeta^i -> zeta^{ai} is a signed permutation of the basis, hence a bijection of W_w, and that Z(sigma_a alpha) = a^{-1}Z(alpha). Corollary: |Sol_U| is independent of which primitive n-th root of F_q is chosen; the equidistribution is an IDENTITY, not a Chebotarev estimate. (S2) If D_U is nonempty then |Sol_U|/|D_U| = mbar/phi(n) with mbar the mean of |H_U| over D_U, so the ratio is >= 1/phi(n) -- deviation is UPWARD ONLY -- with equality if and only if |H_U(alpha)| <= 1 for every alpha in W_w. (S3) If Stab(U)={1} and q^{o+1} > maxnorm(phi(n),w) then |H_U| <= 1 throughout, so the ratio is EXACTLY 1/phi(n): two distinct a in H_U give two distinct blocks aU inside Z(alpha), forcing m(alpha) >= o+1 and q^{o+1} <= Norm <= maxnorm. A hypothesis-free weakening replaces maxnorm by w^{phi(n)/2}. Stab(U)={1} is proved for U={1} (so the whole o=1 theory, including junction 0 at t=2 and the C1 relation lane, is unconditional) and whenever max(U)^2 < n. This DISCHARGES the C2'' pilot's L13 splitting observation from a conjecture to a theorem plus a checkable finite condition. NOT claimed: that S3's condition holds at every official junction; that Stab(U_j)={1} for official j <= 25 (a verified pattern, not a theorem -- the family U={1,3,...,2L-1} has nontrivial stabilizer exactly at L=n/4 and L=n/2); or any distributional model (the within-support variance is under-dispersed ~2x and the q-independent norm multiset does not determine rho). Provenance notes/pilots_20260802/dli_norm_gate/ (LN7 = S1-S3; 1,960-row record, 0 violations of S1/S2/S3/LN6; of the 63 rows deviating from 1/phi(n), all 54 that have a banked maxnorm fail S3's condition and the remaining 9 are n=128 rows where no maxnorm is banked, so S3 is untested there).",
 "refs": [
  "background/nodes/dli_norm_gate_splitting_law/statement.md",
  "background/nodes/dli_norm_gate_splitting_law/proof.md",
  "background/nodes/dli_norm_gate_splitting_law/verify.py"
 ]
}
```

## 4. `dli_official_support_forcing`

```json
{
 "id": "dli_official_support_forcing",
 "title": "DLI official support forcing: at the pinned 256:1 schedule a junction skew of energy E needs q <= E^128, so at every official q > 3^128 each t-null state has |S_0| = 0 or |S_0| >= 4",
 "status": "PROVED",
 "closure": "proof plus exact integer ledger",
 "statement": "At the banked official DLI production schedule (n=2^41, t=2^33, 34 blocks / 33 junctions, L_j=2^{32-j}, N_j=phi(h_j)=h_{j+1}=2^{40-j}, hence N_j=256 L_j uniformly) and any official-admissible q (odd prime, v_2(q-1)>=41, q<2^256): every NONZERO junction-j skew solution of energy E=sum_i d_i^2 satisfies q^{L_j} <= Norm <= E^{N_j/2}=(E^128)^{L_j}, i.e. q <= E^128, INDEPENDENTLY of j. Hence E >= E_min(q) := min{E : E^128 >= q}, and exactly: E_min=2 for q<=2^128, 3 for 2^128<q<=3^128=2^202.87..., and 4 for 3^128<q<=4^128=2^256 -- the last identity 4^128=2^256 being EXACTLY the official cap, so E_min<=4 throughout. At junction 0 the skew domain is {+-1}^{S_0}, so E=|S_0| exactly and the domain omits 0; therefore for every official q > 3^128 EVERY t-null state has |S_0|=0 or |S_0|>=4, and more generally any junction-j state whose whole admissible skew domain has sum_{i in S_j} c_i^2 <= 3 admits no nonzero skew. The exclusion is total at junction 0: the solution count is 0, so rho_0=0 and, in the banked exact decomposition rho_j=q^{delta_j}+Rem_j, Rem_0=-q^{delta_0} exactly. Honest pricing: a single constraint (o=1) at junction 0 excludes only E=1 -- all the strength comes from the o-fold upgrade at the fixed 256:1 ratio. NOT claimed: |S_0|>=4 for formally admissible but small q (q~2^41 gives E_min=2; the >=4 form needs q>3^128, which the production window clears by 53 bits); any bound at |S_0|>=4; any j>0 census identification; rho_j=0 at junctions with an even c_i; the 34th-block reading (ratio 128, which would give E_min=16 at the named exhibit) is recorded and NOT used. The C2'' named 256-bit exhibit q=2^256-191315023233023 has v_2(q-1)=41 and E_min=4; its primality is the banked BPSW claim, is not re-certified, and nothing above depends on it. Provenance notes/pilots_20260802/dli_norm_gate/ (LN5 at official scale) with pins from notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json; tower validation at j=0,1,2 (results/tower.json, all_hold=true, 2453 router-empty states with 0 solutions).",
 "refs": [
  "background/nodes/dli_official_support_forcing/statement.md",
  "background/nodes/dli_official_support_forcing/proof.md",
  "background/nodes/dli_official_support_forcing/verify.py"
 ]
}
```

---

## Proposed edges

### A. Internal `req` edges (all endpoints PROVED, so the green law holds)

| from | to | kind | justification |
|---|---|---|---|
| `dli_norm_gate_forward_and_ofold` | `dli_norm_gate_energy_ceiling` | `req` | the ceiling node's Claim 2 (LN5 router) uses `q^{L_j} \| Norm != 0` verbatim |
| `dli_norm_gate_forward_and_ofold` | `dli_norm_gate_splitting_law` | `req` | S3 uses the valuation bound `v_q(Norm) >= m(alpha)` |
| `dli_norm_gate_energy_ceiling` | `dli_norm_gate_splitting_law` | `req` | S3 uses `Norm >= 1` (positivity) and the hypothesis-free weakening `maxnorm <= w^(phi/2)` |
| `dli_norm_gate_forward_and_ofold` | `dli_official_support_forcing` | `req` | input (IN-1): the `q^{L_j}` lower bound |
| `dli_norm_gate_energy_ceiling` | `dli_official_support_forcing` | `req` | input (IN-2): the `E^{N_j/2}` upper bound |

*Redundancy note:* `forward_and_ofold -> official_support_forcing` is implied
by the two-step path through `energy_ceiling`. Both are stated because the
support-forcing proof cites LN2 directly, but the coordinator may prune the
direct edge without loss.

### B. Attribution edge to the banked sibling — **coordinator decision needed**

| from | to | kind | justification |
|---|---|---|---|
| `dli_c1_ternary_relation_norm_sandwich` | `dli_norm_gate_energy_ceiling` | `ref` | LN4 *is* the sandwich Claim 2 with `w -> E`; the argument is the banked one transplanted |

**FLAG.** `ref` (not `req`) is proposed deliberately: logically the general
statement IMPLIES the banked ternary special case, so a `req` edge would point
the dependency the wrong way, while the proof genuinely is the banked one and
must be attributed. If house convention treats transplanted proofs as `req`,
switch it — but then note that the implication also runs
`energy_ceiling => sandwich Claim 2`, i.e. the two are equivalent at `E = w`.

### C. `ev` edges into critical TARGETs (red-leaf law: `ev`/`ref` in-edges only)

| from | to | kind | justification |
|---|---|---|---|
| `dli_official_support_forcing` | `dli_c2pp_joint_reserve` | `ev` | at official `q` the router sets `rho_0 = 0` on every state with `1 <= \|S_0\| <= 3`, i.e. it removes junction-0 mass the reserve otherwise has to price |
| `dli_norm_gate_splitting_law` | `dli_c2pp_joint_reserve` | `ev` | discharges L13's splitting ratio (the reserve's own `1/phi(n)` input) from conjecture to identity + checkable correction; also prices the "588x invariant blindness" as low-weight census witnesses |
| `dli_norm_gate_forward_and_ofold` | `dli_c2pp_joint_reserve` | `ev` | identifies the C2'' residual as an arithmetic norm-divisibility event (L13 formalized) and pins the junction-0 = C1 dictionary |
| `dli_norm_gate_energy_ceiling` | `dli_c1r3_gated_envelope_bound` | `ev` | the exact analogue of how the banked sibling was wired (`dli_c1_ternary_relation_norm_sandwich -> dli_c1r3_gated_envelope_bound`, `ev`): the same max-norm envelope input, generalized off ternary vectors |

`dli_c2pp_joint_reserve` and `dli_c1r3_gated_envelope_bound` are both
**critical TARGETs (red leaves)**, so only `ev`/`ref` in-edges are legal —
all four edges above are `ev`, and none of the four new nodes takes a `req`
edge from any TARGET. **Coordinator must confirm** the three C2''-side `ev`
edges are wanted (three evidence edges into one red leaf may be more than the
surface wants; the minimum defensible set is
`dli_official_support_forcing -> dli_c2pp_joint_reserve` plus
`dli_norm_gate_splitting_law -> dli_c2pp_joint_reserve`).

### D. Edges deliberately NOT proposed

- **Nothing into `dli_wcl_zone_coverage` or any `dli_wcl_slot_*`.** The WCL
  norm fence (`q > w^128` unconditional, `q > c_w^64` under the C1 doubling
  law, both independent of the window index `ell`; and the decisive negative
  that no open slot with `w >= 5` is reachable) is REAL and proved-in-two-lines
  from LN2 + LN4, but it is not claimed in any of these four statements. It is
  the natural **fifth node** — see AUDIT_CHECKLIST.md item 5.
- **Nothing into `dli_marginal_baseline100_coverage`** (CONDITIONAL): it
  consumes `W_cl` and `C1'`, not the junction router.
- **No req edge out of any TARGET into these nodes** (would violate the
  red-leaf law).
