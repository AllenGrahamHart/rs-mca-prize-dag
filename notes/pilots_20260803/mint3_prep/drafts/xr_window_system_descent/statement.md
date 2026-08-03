# xr_window_system_descent

- **status:** PROVED
- **closure:** proof
- **scope:** the LINEAR ALGEBRA of the depth-`d` window system on
  `H = mu_n` and its `mu_M`-coset descent, plus two exclusion theorems
  (L, R) about which scales can carry a live band-proper pair. **SL-2
  itself is NOT answered** — the unstructured (aperiodic) count is the
  residual `SL-2-RES`, recorded below and explicitly NOT claimed.
  LEMMA W, THEOREM D(a), THEOREM D(b) and THEOREM R are proved here in
  full. **THEOREM D(c) and THEOREM L are RECONSTRUCTED** — see the
  honesty flags and `../../AUDIT_CHECKLIST.md` F1.a-F1.h.
- **provenance:** SL-2 unstructured high-window exclusion pilot,
  `notes/pilots_20260803/sl2_unstructured/`:
  `PREREG.md:35-43` (P1 = LEMMA W), `:49-56` (P3 = THEOREM D),
  `:57-63` (P4 = the BP(1) scope catch), `:77-82` (P7 = "syndromes
  descend"), `algebra.py:12-29` (the machine-checked statements),
  `algebra.py:150-154` (the LEMMA W oracle) vs `:142-147` (the
  independent direct oracle), `descent.py:15-20` (THEOREM L, statement
  + sketch), `toeplitz.py:7-19` (THEOREM R, statement + proof),
  `FABLE_AUDIT.md:12-38` (coordinator verdict BANKED — PARTIAL).
  Mint queued at `FABLE_AUDIT.md:40-43` and
  `notes/pilots_20260802/CAMPAIGN_LEDGER.md:940-943`.
- **HONESTY FLAG 1 (read before citing) — THEOREM L has NO written
  proof of record.** `descent.py:15` cites "THEOREM L, proved in REPORT
  section 3". **There is no `REPORT.md` in that pilot directory**, and a
  repo-wide grep for `THEOREM L` returns only `descent.py`, three
  `FABLE_AUDIT.md` files, the roadmap, the campaign ledger and an
  unrelated homonym in `la_pencil_rigidity/verify.py`. The only written
  derivation anywhere is the six-line docstring `descent.py:15-20`. It
  is reconstructed in `proof.md` with **two gaps named, not papered
  over** (F1.d, F1.e).
- **HONESTY FLAG 2 — the coordinator's replay did not cover THEOREM R.**
  `FABLE_AUDIT.md:8-10` records "algebra.py + descent.py rerun clean
  (677 total checks)". 677 is the sum over **all five** scripts
  (425+114+83+15+40); the two named scripts account for **539**.
  THEOREM R lives in `toeplitz.py` (40 checks) and was accepted from the
  pilot's own checkpoint, not re-run — as were `planted.py` (83, and it
  is the file holding the single deliberate failure) and `route2.py`
  (15). `verify.py` in this node re-runs **all** of it on fresh code.
- **HONESTY FLAG 3 — the title phrase is NOT NEW; it is BANKED
  UPSTREAM IN ANOTHER LANE'S VOCABULARY.** "cores <-> monic divisors of
  `X^n - 1` on a codim <= `2d` affine subspace" appears in **no pilot
  source file** — only in `FABLE_AUDIT.md:23-26` and
  `CAMPAIGN_LEDGER.md:887-888`. Worse for novelty: the correspondence
  itself is **already PROVED and banked** (see SUBTRACTION below). This
  node states it as COROLLARY W2 **with attribution**, never as a
  discovery.

## SUBTRACTION (hard law 5) — what is BANKED and CITED, not re-derived

The single most important line of this node. The divisor
correspondence at the heart of LEMMA W is **prior art in the
locator/Hankel lane**, stated there in different words:

- `critical/nodes/counting_frame/statement.md:9` (node `counting_frame`,
  **PROVED**, in tree since 2026-07-27): "Locators of co-supports are
  squarefree degree-`j` divisors of `X^n - 1` — a FINITE set of size
  `C(n,j)`, i.e. points in `P^j` coefficient space."
- `critical/nodes/v8_ledger/statement.md:9` (**PROVED**): "bad slopes
  are charged to squarefree degree-`j` divisors of `X^n - 1`, of which
  there are exactly `C(n,j)`".
- `critical/nodes/spi_exceptional_class/proof.md:87` already **names the
  set** `D_j = { [l] in P^j : l a squarefree degree-j divisor of
  X^n - 1 }`.
- The `2d`-linear-conditions half:
  `notes/band_heart_consolidation_20260803/CONSOLIDATION.md:59-62`
  ("**2d linear conditions in the top-coefficient space of the banked
  KEY LEMMA**"), sourcing
  `background/nodes/xr_band_key_lemma_pencil_mass/statement.md`
  (KEY LEMMA: `top(I_S(w_z)) = A(S) + z B(S)`, linear in the word).

**Therefore LEMMA W is minted here as the BAND-LANE INSTANTIATION of
the banked counting frame** — the contribution is the *explicit
Toeplitz syndrome form* `(W-T)`, the `iff` in both directions against an
independent oracle, and the joint (`2d`) version — **not** the
correspondence. Anyone citing this node for the correspondence should
cite `counting_frame` instead.

**SCOPE FENCE — a banked REFUTATION applies to the neighbouring
phrasing** (`CONSOLIDATION.md:102-117`, the L-D pilot): "'`(k+d)`-sets
`Z` with `A(Z)=B(Z)=0`' is FALSE as a `<= 0.68n^2` claim (raw subsets of
one deep joint agreement set explode ...). CORRECT object: codeword
pairs whose joint agreement set has size EXACTLY `k+d` (maximal) —
which IS the ledger's `N_d`." **This node's cores are MAXIMAL joint
agreement sets (`|Z_P| = k+d` exactly), never raw subsets**, and no
counting claim is made from the correspondence. The same note records
that a prior write "failed to subtract against it (fifth-surface
rule)" — this one does not.

**THEOREM D and THEOREM L are ALREADY BANKED BY REFERENCE.** The dated
addendum at
`background/nodes/xr_mc_depth_quantization/statement.md:151-163` already
records both ("They ARE excluded by the SL-2 pilot's THEOREM L ...
THEOREM D there settles 'syndromes descend' affirmatively for the window
system"). This node supplies the **statements, proofs and a verifier**
behind that addendum; it does not claim them as unbanked findings.

**THEOREM R is the one clean novelty in the band lane** — but flag the
adjacency: `critical/nodes/f_termination_hankel/notes/pro_brief_broad.md:24-28`
already calls `ker M(Z)` "the classical key equation / **Berlekamp-Massey
kernel**", and `dag.json` `hankel_rank_profile_entropy` (**PROVED**)
carries a rank-profile dichotomy for Hankel kernels. THEOREM R is a
different statement (full rank on the *tangent-gated* class), but it is
adjacent and must be cited as such, not presented in isolation.

**The BP(1) scope question was PARTIALLY ANTICIPATED.**
`notes/pilots_20260802/band_mint_prep/AUDIT_CHECKLIST.md:175-181` (item
7) already asked to "re-scope BP(1) to 'coset-union complements with
`M = 2^ceil(log2 d)`' (the form actually used downstream)". The SL-2
pilot's catch is genuinely sharper — it **exhibits non-empty sub-depth
scales at the prize rows** — but this node must not present the scoping
issue as wholly unforeseen.

Also consumed, not re-derived (`PREREG.md:146-157`): MC-1/2/3/5 + the
KEY LEMMA; THEOREM 5, BP(1), BP(2), BP(3), the `h`-even control, MC-4's
scope; the e22 coset locator factorization; the six-row table and the
`q`-envelope; `cap_d` = `xr_band_ledger_theorems` THEOREM 3.

## Setting

`C = RS_k` (polynomials of degree `< k`) evaluated on `H = mu_n <= F_q^*`,
`n | q-1` (split); `A = k + h` is the tangent-gate agreement ceiling and
`h` the **excess** — an AMBIENT ROW parameter, never a per-word measured
ceiling (`planted.py:178-184`). Received pair `(u, v)`; a
**joint-explanation pair** `P = (f,g)` has **core**
`Z_P = {x in H : f(x) = u(x), g(x) = v(x)}` with `|Z_P| = k + d`, and `d`
is the **depth** (`PREREG.md:21-25`; definitions of record
`notes/BAND_LANE_DEFINITIONS.md:9-10`). Write `r' := n - k - d` and
`T := H \ Z` for the core complement, `|T| = r'`.

**BAND-PROPER — WHICH ONE (F1.a).** This node uses the pilot's *upper
window* `d in [ceil(h/2), h-2]` (`PREREG.md:26`, computed at
`descent.py:73`). `BAND_LANE_DEFINITIONS.md:11-12` item 2 defines "band
(proper)" more broadly as depths `[1, h-2]`. **Every band-proper
statement below means the pilot's `[ceil(h/2), h-2]`**; nothing here is
claimed on `[1, ceil(h/2)-1]`.

Words are identified with their degree-`< n` interpolants on `H`; the
**syndrome window** of `u` is `(u_k, ..., u_{n-1})`. A **coset scale** is
`M | gcd(n,k)` with `M | d`; the **item-10 pinned scale** is
`M = 2^ceil(log2 d) >= d` (`BAND_LANE_DEFINITIONS.md:43-44`); `M < d` is
**sub-depth**. `cap_d := floor((n-k-d)/(h-d))` is the **banked line cap**
(`xr_band_ledger_theorems/statement.md:38-44` THEOREM 3, at `J = k+d`,
`A = k+h`), and `L_P` counts SELECTED supports containing `Z_P`, with
`N_d = #{depth-d pairs with L_P >= 2}`
(`BAND_LANE_DEFINITIONS.md:34-36`).

## Statement

### LEMMA W (the window system for a GENERAL word) — PROVED

For `T <= H` with `|T| = r' = n-k-d` and locator
`E_T = prod_{t in T}(X - t)`:

```text
(W)  a codeword P (deg P < k) with (u - P)|_{H \ T} = 0 EXISTS
     <=>  the coefficients of  u E_T mod (X^n - 1)  in degrees
          n-d, ..., n-1  all vanish.
```

These are `d` equations, **linear in the coefficients of `E_T`**, with
coefficient matrix the `d x (r'+1)` **Toeplitz matrix** `R(u,d)` of the
syndrome window:

```text
(W-T)   sum_{i=0}^{r'} u_{(j-i) mod n} E_i = 0,     j = n-d, ..., n-1.
```

The **joint (pair) system** for `(u,v)` is the same with `2d` equations —
`d` from `u`, `d` from `v` — and a joint core is exactly a common
solution.

**COROLLARY W2 (the coordinates; DERIVED here — F1.b).** Since `T <= H`
and `X^n - 1 = prod_{x in H}(X - x)` is squarefree and split, `E_T` is a
**monic divisor of `X^n - 1` of degree `r'`**, and `T <-> E_T` is a
bijection between `r'`-subsets of `H` and such divisors. Under it,
`(W-T)` cuts out an **affine subspace of codimension `<= d`** (single
word) resp. **`<= 2d`** (joint) in the coefficient space `A^{r'}` of the
monic locator. Hence: **cores are exactly the monic degree-`r'` divisors
of `X^n - 1` lying on a codim-`<= 2d` affine subspace.**

### THEOREM D (coset descent; settles "syndromes descend") — (a),(b) PROVED; (c) RECONSTRUCTED

Let `M | gcd(n,k)` and `M | d`.

- **(a) PROVED.** `T` is a `mu_M`-coset union `<=>` `E_T(X) = G(X^M)`
  for some monic `G` of degree `r'/M`.
- **(b) PROVED.** If `E_T(X) = G(X^M)` then equation `j` of `(W-T)`
  involves **only syndrome positions `= j (mod M)`**.
- **(c) RECONSTRUCTED (F1.c).** If the syndrome window of `u` is
  supported in a **single class `rho` mod `M`**, then exactly `d/M` of
  the `d` equations are non-vacuous, and they are **literally LEMMA W's
  system for the QUOTIENT instance** `RS_{k/M}` on `mu_{n/M}` at depth
  `d/M` with word `U_s = u_{rho + sM}`. Consequently the scale-`M` cores
  upstairs are in **EXACT BIJECTION** with the cores of that quotient
  instance.

**COROLLARY D6 ("syndromes descend", definitions item 6).** The
bijection of (c) carries syndromes to syndromes, so the quotient
convention of `BAND_LANE_DEFINITIONS.md:27-31` item 6 is **CORRECT for
the window system**, and P3 (quotient-periodicity at `M | gcd(n,k)`)
formally fires on any exactly-degenerate scale-`M` adversary.
**SCOPE WORD, LOAD-BEARING:** settled *for the window system only*
(`PREREG.md:77-82`, `FABLE_AUDIT.md:26-28`) — not for the strip filter
in general. See P3-EVASION below.

### THEOREM L (liveness / parity exclusion) — RECONSTRUCTED, with two named gaps

For a **separately `M`-quotient-periodic** depth-`d` pair `(u,v)` with
**`h` ODD**:

```text
(L)   M > cap_d = floor((n-k-d)/(h-d))   =>   L_P = 0,
      i.e. the pair is NOT counted by N_d.
```

Chain as written at `descent.py:15-20`: the extra agreement of any
pencil projection beyond the core lies in `g*{0,...,m}` with
`g = gcd(M, b-a)` and `m = (n-k-d)/M`; liveness needs extra `= h-d`
EXACTLY; `M | d` and `h` odd force `g = 1`; hence `h-d <= m`, i.e.
`M <= cap_d`.

**Effect at the rows (machine-replayed here):** at all three prize rows
`(L)` closes the sub-depth scales `M = 2^21..2^31` (prize 1/4, 1/8) and
`M = 2^21..2^30` (prize 1/16) **unconditionally**. Scales `M = 2^1..2^20`
are **NOT** closed by `(L)`; they are closed only by a FIRST-MOMENT
margin, which is **heuristic-grade and labelled as such** (see NOT
claimed).

### THEOREM R (full Toeplitz rank on the gated class) — PROVED

```text
(R)   On the tangent-gated class,  rank R(u,d) = d  exactly.
```

Hypotheses carried: `n - k >= 2d`; the tangent gate (agreement
`<= A = k+h`); `d <= h-2` with `h << n-k`. **Consequence
(`toeplitz.py:21-25`):** an adversary CANNOT buy a large family by
degenerating the LINEAR part of the window system — **any blow-up must
be arithmetic**, i.e. must come from the divisor structure of
`X^n - 1`. The MC word is the illustration: its system has FULL rank
`w`, yet its solution set is the whole coset lattice.

**NAMING (F1.f).** The pilot uses "R" for two different objects:
THEOREM R (`toeplitz.py:19`, full rank `d` on the gated class) and
`algebra.py:27-29` check "R" (rank on the scale-`M` locus = PREREG P6,
the off-class rank penalty). Here **THEOREM R** always means the former;
the latter is called the **OFF-CLASS RANK PENALTY** and is recorded as
measured, not claimed.

## The BP(1) scope correction (context; consumed, not re-derived)

Banked BP(1) (`background/nodes/xr_mc_depth_quantization/statement.md:51-59`)
concludes "structured => depth a power of two" **at the pinned scale
`M = 2^ceil(log2 d) >= d`** (definitions item 10). Coset structure alone
forces only `M | d`. The pilot's F2 **FIRED**: sub-depth scales `M < d`
are **non-empty inside the band proper at all three prize rows**
(`M = 2..2^31`; the largest lands on the **quotient's cascade tier**),
and are NOT excluded by BP(1)/BP(3) (`PREREG.md:57-63, 98-101`;
`FABLE_AUDIT.md:12-18`, where the coordinator records ""The structured
half is proved excluded" was too broad — my r3.2 wording inherited it").
They ARE excluded by THEOREM L on `M >= 2^21`, and by first moment
(heuristic) below that. The corrected scope of record is the dated
addendum already applied at
`background/nodes/xr_mc_depth_quantization/statement.md:151-163`, which
this node's THEOREM D and THEOREM L are cited by. **Non-vacuity is
exhibited**, not assumed: `planted.py:160-164` / `planted.json:441-450`
realise a scale-`M=2`, `d=4` family whose item-10 scale is `4` — a
family BP(1) does not cover. The tempting misreading is killed in the
source itself (`planted.py:198-200`): `d = 4` IS a power of two here;
what matters is `M != 2^ceil(log2 d)`.

**P3-EVASION (recorded).** With `rho_u != rho_v` (`planted.py:49`), `u`
and `v` each sit in one class mod `M` but **every pencil member `w_z`
meets both classes**, so no per-word quotient-periodicity test sees the
adversary — yet the whole family is admitted by every member and the
KEY LEMMA holds on it (`planted.py:212-223`). **THEOREM L, not the strip
filter, is what excludes the descent class** (`FABLE_AUDIT.md:30-32`).

## Explicitly NOT claimed

- **SL-2 IS NOT ANSWERED.** "Can an UNSTRUCTURED (non-coset) admissible
  family reach a band-proper depth with `> 0.68 n^2` members?"
  (`PREREG.md:26-28`) is **OPEN**. The pilot pre-registered that its
  assigned falsifier F1 would NOT fire and it did not
  (`PREREG.md:91-97`): by SL-3 sub-criticality no toy can exhibit the
  blow-up, and SL-3 is itself a **conjecture**
  (`listsize_program/REPORT.md:57-58`).
- **SL-2-RES — the residual, NOT proved** (`FABLE_AUDIT.md:33-38`):
  "aperiodic band-proper core count `<= 0.68 n^2`, equivalently: how
  many monic degree-`r'` divisors of `X^n - 1` lie on a codimension-`2d`
  affine subspace?" It **must carry `h` ODD and `q >= 2^209`**, both
  load-bearing: the `h`-even control fails twice over, and the `q`-pin
  has **41.5 bits of headroom at the binding row**. (`2^209` is `ceil`
  of the measured `log2_q_critical = 208.47593052630532` at prize 1/4,
  `descent.json` `critical_field`; the number `209` is not literally in
  any pilot source.)
- **The `M <= 2^20` closure is HEURISTIC-GRADE.** Those scales are
  closed only by a first-moment **expectation**, not a certified bound
  (`descent.py:23-27`). The margins are `>= 3.09e5` bits — precisely,
  `309180.56` bits is the *minimum over the three prize rows* of the
  least-negative heuristic-scale margin (prize 1/16, `j = 20`); prize
  1/4 gives `340674.23` and prize 1/8 `897123.80`. The code's own
  partition into `proved_scales` vs `heuristic_scales`
  (`descent.py:152-178`) is carried verbatim into the verifier.
- **No count claim rests on any fixture.** Stated by the pilot up front
  (`PREREG.md:141-144`, `algebra.py:7-8`, `planted.py:33-34`).
- **THEOREM L at `h` EVEN is FALSE as an exclusion.** The `h`-even
  control (`n=20, k=8, h=6`) has `proved_scales: []` — liveness proves
  nothing there, and the BP(1) class fires *in addition*
  (`descent.json` control block; F7 as predicted, `PREREG.md:112-116`).
  `h` odd is a real hypothesis.
- **The OFF-CLASS RANK PENALTY (PREREG P6) is MEASURED, not claimed.**
  Rank strictly exceeds `2d/M` off-class on the tested toys, but the
  pre-registered "rank additivity exact on toys" was **never checked**,
  and what is checked is the single-word `d`-row system, not the joint
  `2d`-row one (F1.g).
- **Route 1 and Route 2 are PROVED NEGATIVES ABOUT THE ROUTES, not
  about SL-2** (`route2.py:28-29`): the packing bound sits `~2^1.7e12`
  above budget, and the counting/union route can only ever exclude
  families of fewer than `1/rate` members (`N < n/k = 4,8,16`).
- Nothing about the **non-coset / aperiodic** case beyond restating it
  as SL-2-RES; no bound on `|Gamma|`; no discharge of the occupancy
  lemma; nothing about `xr_graded_tangent_band_charge`'s single open
  input beyond the evidence recorded here.

## Falsifier

A `T <= H` where `(W)` fails in either direction; a `mu_M`-coset union
whose `E_T` is not a polynomial in `X^M` (or a `G(X^M)` whose root set
is not a coset union); an equation of `(W-T)` under `E_T = G(X^M)`
touching two distinct classes mod `M`; a scale-`M` core with no quotient
counterpart or vice versa; a tangent-gated `(u,d)` with
`rank R(u,d) < d`, or a word at distance `L < d` whose rank is not
exactly `L`; a separately `M`-quotient-periodic pair with `h` odd,
`M > cap_d`, and a live selected support.

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, **no reads outside this
directory** — all pins inlined, provenance in comments only). It replays
every computational claim on **fresh code** and, in three places,
**strengthens** what the source checked (each flagged in
`AUDIT_CHECKLIST.md`):

- **A** LEMMA W `<=>` an independent direct-interpolation oracle,
  exhaustively over every `T`, at four shapes — **both directions**.
- **B** the JOINT system = intersection of the two single-word systems.
  *The source hard-codes this check to `True` (`algebra.py:224`); here
  it is actually computed*, and on a fixture where the joint core set is
  **non-empty** (the source's own joint counts are 0 in all 12 trials).
- **C** COROLLARY W2: `E_T` monic, `E_T | X^n - 1`, the `T <-> E_T`
  bijection, and the codimension bound `<= 2d`.
- **D** THEOREM D(a) **in both directions** (*the source checks only
  coset-union `=>` `G(X^M)`*), D(b) class-locality, and D(c) bijection
  at fixtures where **both sides are non-empty** (*the source's D(c) is
  non-vacuous in only 2 of 14 cases*).
- **E** THEOREM R: `rank = d` on gated words; the sharpness converse
  (planting at distance `L < d` drops rank to exactly `L`); and the MC
  illustration (full rank `w`, large solution set).
- **F** THEOREM L's row arithmetic: `cap_d`, the proved/heuristic scale
  partition at all six rows + the `h`-even control, reproduced from
  inlined row parameters; asserts `proved_scales = 2^21..2^31` (prize
  1/4, 1/8), `2^21..2^30` (prize 1/16), `[]` at `h` even.
- **G** the `q`-critical arithmetic: `log2_q_critical` at the binding
  row and the `41.5`-bit headroom against the `2^250` pin.
- **H** the BP(1) scope catch: sub-depth scales exist inside the band
  proper at the prize rows and NOT at RowC, with `M != 2^ceil(log2 d)`
  exhibited — **labelled as the scope gap**, and the route-2 negatives
  recorded as MEASURED-about-the-route.
