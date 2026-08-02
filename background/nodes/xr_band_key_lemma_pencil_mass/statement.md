# xr_band_key_lemma_pencil_mass

- **status:** PROVED
- **closure:** proof
- **scope:** THEOREM I/I' and the KEY LEMMA are domain-agnostic
  identities (any evaluation set, any `q`); the MC construction is on
  split multiplicative-coset domains (`n | q-1`); everything is exact.
- **provenance:** list-bound-transfer pilot
  (`notes/pilots_20260802/list_bound_transfer/{REPORT,FABLE_AUDIT}.md`;
  7,792 machine checks, 0 failures; Theorem I = its section 4 THEOREM
  I/I', KEY LEMMA = its pencil support dichotomy, MC-1/2/3/5 = its
  section 2-3), queued for mint by that pilot's FABLE_AUDIT item 4.
  **Naming note (coordinator task list):** the mint brief cites
  `notes/pilots_20260802/xr_band_occupancy/` as the source path; the
  KEY LEMMA, pencil mass identity and MC family live in
  `list_bound_transfer/` — flagged in AUDIT_CHECKLIST, drafted from the
  true source. **Rename applied** per
  `notes/BAND_LANE_DEFINITIONS.md` item 5: the KEY LEMMA's "cascade
  event" is renamed to **"joint-explanation event"** throughout.

## Setting

`C = RS_k` on an evaluation set `D` of `n` distinct points of `F_q`;
received pair `(u, v)`; pencil `w_z = u + z v` for `z in F_q`,
`w_{(0:1)} = v` — `q + 1` members. `agr(c, w) = #{x in D : c(x) = w(x)}`.
For `S <= D` with `|S| = a >= k`, `I_S(w)` is the degree-`< a`
interpolant of `w` on `S`. For the MC construction, `D = H = x_0 mu_n`
(`n | q-1`, split), `A = k + h`, and definitions items 3, 5, 7 apply
(cascade tier; "below cascade" = the cascade tier is EMPTY; live slope
over all of `P^1` incl. `(0:1)`).

## Statement (all PROVED)

1. **THEOREM I (pencil mass identity).** If `v(x) != 0` for every
   `x in D`, then for EVERY function `c : D -> F_q`

   ```text
   sum_{z in F_q} agr(c, w_z) = n.
   ```

   **THEOREM I' (with zeros).** With `Z_v = {x : v(x) = 0}` and
   `e(c) = #{x in Z_v : u(x) = c(x)}`:
   `sum_{z in F_q} agr(c, w_z) = q e(c) + (n - |Z_v|)`.
   **COROLLARY I.1.** (`v` nowhere zero) `#{z in F_q : agr(c, w_z)
   >= a} <= floor(n/a)`. **COROLLARY I.2.** If `2a > n` the lists
   `{c : agr(c, w_z) >= a}`, `z in F_q`, are PAIRWISE DISJOINT.
2. **KEY LEMMA (pencil support dichotomy).** For `|S| = a >= k` the
   top `a - k` coefficients of the interpolant are LINEAR in the word:
   `top(I_S(w_z)) = A(S) + z B(S)` with `A(S) = top(I_S(u))`,
   `B(S) = top(I_S(v))`. Consequently EITHER `A(S) = B(S) = 0` — then
   `I_S(u)` and `I_S(v)` are BOTH codewords, i.e. `u|_S` and `v|_S`
   are jointly explained by a codeword pair: a **joint-explanation
   event** of size `a` (a joint pair explanation at depth `a - k`) —
   and ALL `q + 1` members' interpolants on `S` are codewords; OR at
   most ONE member `z in P^1(F_q)` has `I_S(w_z)` a codeword — in
   particular at most one member has a codeword whose agreement set
   contains `S`. **Graded consequence:** distinct pencil members share
   a common agreement `a`-set iff a joint-explanation event of size
   `a` exists there; hence "below cascade" (cascade tier empty, max
   joint pair agreement `<= A - 2`) holds iff distinct pencil members
   never share an agreement set of size `>= A - 1`.
3. **MC-1 (window classification, all `w`).** For
   `u = X^{n-1} + c X^{k+w-1}` on `H` (`c != 0`), `r' = n - k - w`:
   codewords of agreement `>= k + w` are EXACTLY indexed by
   `{T <= H : |T| = r', e_1(T) = ... = e_{w-1}(T) = 0,
   prod T = gamma}`, `gamma = (-1)^{r'+1} c`, via `T -> P_T` with
   `u - P_T` vanishing exactly off `T`; the map is injective and the
   agreement is EXACTLY `k + w`.
4. **MC-2 (ceiling).** No codeword agrees with `u` on `>= k + w + 1`
   points — so the tangent gate holds UNCONDITIONALLY on MC words
   (generalizes the crossing lane's PK1(A) to all `w`).
5. **MC-3 (the family, exact `q`-free count).** If `M | n`, `M | r'`,
   `w <= M`, `N = n/M`, `m = r'/M`, unions of `m` cosets of `mu_M`
   satisfy `e_1 = ... = e_{M-1} = 0` for free (the banked `e22`
   locator factorization), and the product condition equidistributes
   exactly: with `gcd(m, N) = 1` the family has EXACTLY `C(N,m)/N`
   members — `q`-free.
6. **MC-5 (shift pencil — no pencil exclusion).** With
   `v = u/X^j mod (X^n - beta)`, `1 <= j <= M-1` (well defined:
   `X^{M-1} | P_T`), EVERY member `w_z`, all `q+1`, admits the ENTIRE
   MC family via `P_T^{(z)} = P_T + z Q_T`; so
   `min_{z in P^1} L(w_z, k+w) >= C(N,m)/N`. The pencil does NOT
   exclude simultaneous list blow-up.

## Subtraction (hard law 5 — the mechanism is banked, the theorems are new)

The coset mechanism is OURS and banked:
`background/nodes/e22_tail_coset_locator_algebra` (the locator
factorization `G(X^M)` IS the MC mechanism);
`rate_half_cyclic_rotated_prefix_floor` (PR #1051 — MC is its
`s = 0, d = 1` boundary case with the `q^{d-1}` loss removed by exact
equidistribution); crossing PK1 (`c = 1, s = 0` boundary; MC's `w = 2`
count reproduces PK1's measured `w = 2` shell exactly; the
equidistribution step is PK1 Lemma 5). Independently present in
BCHKS25 (ePrint 2025/2055) section 7 via sumset hypotheses — MC routes
around those unconditionally. NEW here: the exact `q`-free count, the
ceiling at general `w`, the pencil theorem (MC-5), THEOREM I/I', and
the KEY LEMMA.

## Explicitly NOT claimed (context)

- **NO list bound.** This node must never be cited as a single-word or
  pencil list-size bound: the band-occupancy pilot's reduced list
  statement is FALSE (refuted by this very construction: worst-case
  lists at `tau` are `2^130`-`2^197` at the prize rows, all pencil
  members simultaneously), and the reduction route is RETIRED
  (xr_band_occupancy FABLE_AUDIT amendment). The occupancy lemma
  itself STANDS as the open target, unaffected in either direction.
- **Corollary I.3-type averaging is CIRCULAR** for bounding the pencil
  min (`|U(a)|` is exactly what a correlated-agreement theorem would
  supply) and CANNOT be repaired: MC exhibits
  `min = C(N,m)/N` under k-packing + tangent gate + non-degeneracy —
  no `poly(n)` pencil trade-off law is true. Recorded as a proved
  negative, not a route.
- **MC-4 (structured-floor completeness)** is char-0 Lam-Leung input
  and is NOT claimed here (its consumer is `xr_mc_depth_quantization`,
  where its scope is stated); accidental char-`p` excess only makes
  lists larger.
- The MC shift pencil sits exactly ONE step outside the `<= A-2`
  below-cascade reading (2-adically forced at the prize rows): its
  joint-explanation maximum is exactly `A - 1` — the cascade tier —
  which is why the band adjudication, not this node, settles where
  that mass is charged.
- The first-moment (R1) refutation's concentration step is sketched,
  not carried, in the pilot record; nothing here depends on (R1) —
  MC is the certified half.

## Falsifier

A function `c` with `sum_z agr(c, w_z) != q e(c) + (n - |Z_v|)`; an
`S` (`|S| >= k`) with two distinct pencil members having codeword
interpolants but not all `q+1`; an MC codeword at agreement
`>= k+w+1`; an MC family count `!= C(N,m)/N` at `gcd(m,N) = 1` and
large `q`; or a pencil member missing a family member's codeword.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers,
deterministic, no third-party imports, no reads outside this
directory). Checks: THEOREM I/I' exhaustively over all `q+1`... over
all `z in F_q` for census codewords AND random functions, with and
without `v`-zeros; I.1/I.2; the KEY LEMMA dichotomy over EVERY
`S` of sizes `k, k+1, k+2` at `(n,k,q) = (14,4,17)` (counts in
`{0, 1, q+1}`, `q+1` iff joint-explanation event, linearity exact);
the shared-agreement-set consequence on full per-member censuses
(sharing forces the joint-explanation event and `q+1`-member
CONTAINMENT agreement); MC-1 (exhaustive census = the indexed
`T`-set, at `q = 97, 193, 12289`), MC-2 (ceiling at every fixture),
MC-3 (coset-union family = exactly `C(8,5)/8 = 7` members, CONTAINED
in the shell; accidental excess measured `2/2/0` — vanishing at
`q = 12289 > C(16,10)`, the pilot's P5), MC-5 (all `q+1` members
admit all 7 members constructively; spot censuses `>= 7`
member-wise).
