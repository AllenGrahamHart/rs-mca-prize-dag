# PROOFS — THE TERNARY MASTER STATEMENT (round 19, GENERATIVE)

Opus pilot, `notes/pilots_20260806/tern_master_statement/`. Registrations
T-A1–T-A6 appended to `PREREG.md` **before** any computation. Machine checks
in `check.py` (stages `dict char0 cs floor thresh rot newton`, plus a
permanent `failclosed` stage that exits 1 by construction): **92,263 checks,
0 FAIL**, every stage exit 0, `failclosed` exit 1. Log `VERIFY_LOG.txt`.
Library `tern_lib.py` — Python stdlib only, exact integer / finite-field
arithmetic, no floating point in any proved statement.

Toy grids are **2-POWER `n` ONLY** (CATCH-Z6), with exactly one explicitly
labelled rule-test stage at composite `2N` whose outputs are used only to
reproduce CATCH-Z6's own numbers.

---

## §0. SUBTRACTION LEDGER (hard law 5) — declared before any claim

Five surfaces swept (`critical/`, `background/`, `notes/`, `archive/`,
`experiments/` + `dag.json` + `upstream_dag/` + `formal/` + `graph/` +
`orbit/`), excluding the sibling `tern_unification_adversary/`, which was
**not read**. Verdicts:

**BANKED — the collision identity and its `2^{m-wt}` multiplicity are NOT
mine.** `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:148-155`, verbatim:

> Every difference `b - b'` lies in `T = {0,±1}^m`, and for a FIXED
> `eps in T` the number of pairs with `b - b' = eps` is `2^{m - wt(eps)}`
> (coordinates with `eps_i = ±1` are forced; the `m - wt(eps)` coordinates
> with `eps_i = 0` are free). Hence
>
> ```text
>    sum_s |F_s|^2  =  sum_{eps in T ∩ ker A} 2^{m - wt(eps)}  =  2^m · Z(L).
> ```

**BANKED — THEOREM Z-FLOOR is NOT mine.** Same file, `:130-135`, verbatim:

> **THEOREM Z-FLOOR.** For **every** `F_p`-subspace `L ⊆ F_p^m` (no MDS, no
> GRS, no genericity, no randomness),
>
> ```text
>         Z(L)  =  sum_{eps in L^perp ∩ T} 2^{-wt(eps)}   >=   2^m / p^{dim L} ,
> ```

§4 **transports** it off its instance; the inequality is cited, not claimed.

**BANKED — THEOREM CS is NOT mine.**
`notes/pilots_20260806/es_coprimality/PROOFS.md:202-225` (quoted verbatim in
§2.2). §2.2 reads its proof over the master object; the *mechanism* is the
node's.

**BANKED — the AM-GM archimedean ceiling on TERNARY vectors is NOT mine, and
it is NOT the `es_coprimality` form.**
`background/nodes/dli_c1_ternary_relation_norm_sandwich/statement.md:27-28`,
status PROVED, verbatim:

> 2. **AM-GM ceiling.** For every NONZERO ternary `f` of weight `w`:
>    `1 <= Norm(f) <= w^(N/2)`.

with `N = [K:Q]`. This is exactly (CS2) read on a ternary vector, and it was
already in the bank in the DLI lane. §2.2 cites it; the *assembly* with the
Galois multiplicity is what §2.2 supplies (and §5 CATCH-T3 prices what that
assembly is worth).

**BANKED — LEMMA AB and its multiplicity are NOT mine.**
`notes/pilots_20260806/efloor_sparsity/PROOFS.md:88-96`, verbatim:

> > **LEMMA AB.** Write `f_S = A + X^h B` with `deg A, deg B < h = n/2`, i.e.
> > `A` is the indicator of `S n [0,h)` and `B` that of `S n [h,n)` shifted.
> > Put `v := A - B in {-1,0,1}^h`. Then
> >
> > 1. `f_S = v (mod Phi_n)`, so for every **odd** `s`,
> >    `f_S(xi^s) = v(xi^s)` for any primitive `n`-th root `xi` in char `p`;
> > 2. `v = 0  <=>  S + n/2 = S  <=>  strat(S) >= 1`, for every odd `p`;
> > 3. the number of `S` with a given `v` is exactly `2^{z(v)}`, where
> >    `z(v) = #{i : v_i = 0}`.

**BANKED — the char-0 Z-basis emptiness is NOT mine.**
`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:260-265`, verbatim:

> *Verified: S9.* For `n` a 2-power the minimal polynomial of `zeta_n` is
> `X^{n/2}+1`, so `{zeta_n^a : 0 <= a < n/2}` is a **Z-basis** of `Z[zeta_n]`.
> The deployed representatives `a_i = 2i+1` are distinct elements of
> `[0, n/2)`, so `alpha = sum_i eps_i zeta_n^{a_i}` is a Z-combination of
> distinct basis elements: `alpha = 0` iff `eps = 0`. Every ternary relation is
> therefore an "accident" of `p`-divisibility.

**BANKED — LEMMA Z is NOT mine.**
`critical/nodes/b1_char0_giant_coset_theorem/node.json:9`, status PROVED:

> "Over characteristic zero: every 0/1 t-null vector on mu_n (n = 2^s) is a
> union of mu_M-cosets with M > t."

**BLIND-CONVERGENT WITH A LIVE SIBLING — the mass/census functional identity
is NOT claimed here.** `notes/pilots_20260806/tern_small_scale_laws/PREREG.md:149-159`
registers, before my own computation, exactly the identity my §1.4 records:

> - **(D3) the multiplicity dictionary (weighted mass <-> unweighted count).**
>   Put `Z(N,p,T) := sum over ALL v in CT (including v=0) of 2^{-wt(v)}`
>   (the z1 mass, `z1_ternary_mass/PROOFS.md:19`) and
>   `Sct(N,p,T) := sum over NONZERO v in CT of 2^{z(v)}`, `z(v) = #{i: v_i=0}`
>   (the efloor S-count, `efloor_sparsity/PROOFS.md:308-309`).
>   REGISTERED IDENTITY:
>   ```text
>   Sct  =  2^N * (Z - 1).
>   ```

That sibling also registers the one-framework census routine
(`tern_small_scale_laws/PREREG.md:98-118`). **I claim neither the framework
nor D3 as novel**; §1 states them because the master statement needs them,
and credits the convergence.

**NOT FOUND anywhere** (searched exhaustively, sibling excluded), and
therefore the only things §§2–4 claim as new:

1. the identification of `(r' - a_{n/2}(S))` with the ternary support size
   `wt(A-B)` (§1.3) — `a_{n/2}` occurs at 15 sites, none links it to `wt`;
2. any application of the Cauchy–Schwarz/collision floor **off** the F2
   instance (§4.1–§4.2) — every occurrence of Z-FLOOR in the repo is
   F2-lane, and the crossing lane's forcing is explicitly a different
   mechanism (`crossing_low_w/PROOFS.md:235-236`: *"**No balance is used**:
   the argument is `|domain| > |codomain|`"*);
3. the identification of I1's knife edge, I2's DSA regime boundary and I3's
   stratum-0 boundary as **one inequality** (§4.3) — the banked seam
   (`z1_ternary_mass/PROOFS.md:300-307`, CATCH-Z3) is entirely F2-internal;
4. the exact master form of CATCH-Z6 as a rank statement with a closed count
   (§2.1).

---

## §1. (M1) THE MASTER OBJECT, AND THE FOUR DICTIONARIES

### 1.1 Definition

> **DEFINITION (the ternary relation module).** For a tuple
> `P = (theta_0, ..., theta_{M-1})` of elements of `F_{p^d}^*` and a
> condition set `Lambda`,
>
> ```text
> T(P, Lambda) := { eps in {0,±1}^M : sum_{j<M} eps_j theta_j^l = 0
>                                     for every l in Lambda }.
> ```

> **DEFINITION (the target is a PARAMETER, not a conflation).** For a weight
> `omega : {0,±1}^M -> R_{>=0}`,
> `Phi_omega(P,Lambda) := sum_{eps in T(P,Lambda), eps != 0} omega(eps)`.
> The **existence** question is `Phi_1 = 0?`, the **count** question is the
> size of `Phi_1`, the **mass** question is `Phi_{2^{-U}}`. Round-18
> CATCH-Z1 (`z1_ternary_mass/PROOFS.md:482-492`) proves these come apart;
> the master statement therefore carries `omega` as a parameter and never
> substitutes one for another.

### 1.2 The canonical specialization: half-systems are negacyclic codes

> **PROPOSITION HS.** Let `n = 2h`, `xi` of exact order `n` in `F_{p^d}`,
> and `P = (xi^j)_{0<=j<h}` the **half-system**. Let `Lambda ⊆ (Z/n)^*` and
> `Lambda^* := <p>·Lambda` its Frobenius closure. Then
>
> 1. `T(P, Lambda) = T(P, Lambda^*)`;
> 2. `T(P, Lambda)` is exactly the set of **ternary words of the negacyclic
>    `F_p`-code** `C(Lambda) = {V in F_p[X]/(X^h+1) : V(xi^l) = 0,
>    l in Lambda}`, of `F_p`-codimension `g := |Lambda^*|`.

*Proof.* (1) `eps` is fixed by Frobenius entrywise (`eps_j in {0,±1} ⊆ F_p`),
so `0 = (sum_j eps_j xi^{lj})^p = sum_j eps_j xi^{(pl)j}`. (2) The generator
polynomial `G = prod_{s in Lambda^*}(X - xi^s)` is `<p>`-stable hence lies in
`F_p[X]`, has degree `|Lambda^*|`, and divides `X^h+1`; `V` lies in the code
iff `G | V`. ∎

*Verified:* `check.py cs` asserts `deg G == |Lambda^*|` in every cell
(30 cells, exact).

### 1.3 THE DICTIONARY BRIDGE (new): CS2's quantity is a ternary support size

> **LEMMA BR.** Let `n = 2h`, `S ⊆ Z/n`, `|S| = r'`, and let `v = A - B` be
> LEMMA AB's ternary vector. Then, with `a_{n/2}(S)` as defined at
> `es_coprimality/PROOFS.md:21` (`a_{n/2}(S) = #{(i,j) in SxS :
> i-j = n/2 mod n}`),
>
> ```text
>         r' - a_{n/2}(S)  =  wt(A - B)  =  wt(v).
> ```

*Proof.* `a_{n/2}(S) = #{i in S : i - h in S} = 2·#{j < h : A_j = B_j = 1}`,
and `r' = |A| + |B|`, so `r' - a_{n/2}(S) = |A| + |B| - 2|A ∩ B| =
|A Δ B| = wt(A-B)`. ∎

*Verified:* `check.py dict` — exhaustive over all `2^16` subsets at `n = 16`
and 4,000 deterministic pseudorandom subsets at `n = 32`; **69,536 checks,
0 failures.**

This is the hinge of the whole master statement: it says the archimedean
side of THEOREM CS was **already** a statement about the ternary object, and
nobody had said so. The corresponding second moment is master-level:

> **LEMMA SM.** For `eps in {0,±1}^h` and `X = sum_{j<h} eps_j zeta_n^j`,
> `sum_{c odd mod n} |sigma_c(X)|^2 = h · wt(eps)`.

*Proof.* `sum_{c odd} zeta^{cd} = (n/2)([d=0] - [d = n/2])`; for
`j, j' in [0,h)` the difference `j - j' = h` is impossible, so only the
diagonal survives and the sum is `h·sum_j eps_j^2 = h·wt(eps)`. ∎
(This reproduces `es_coprimality/PROOFS.md:278`'s
`sum_{c odd} |x_c|^2 = h(r' - a_{n/2}(S))` through LEMMA BR.)

*Verified:* `check.py dict` — exact in `Z[X]/(X^h+1)` over **all** nonzero
ternary `eps` at `n = 8` and `n = 16` (6,640 vectors, 6,640 checks, 0
failures).

### 1.4 The four dictionaries (M1 deliverable)

| | I1 (F2 mass) | I2 (crossing deep stratum) | I3 ((ES) suppression) |
|---|---|---|---|
| source node | `f2_z1_mass_knife_edge` | `crossing_dsa_refutation` | `es_ternary_suppression_instruments` |
| order `n` | `2^{e_p}` | `2L = 2^{42-v}` | `2^m` |
| `M = h` | `S = 2^{e_p-1}` | `L = 2^{41-v}` | `n/2` |
| field | `F_p`, `delta = 1` | `F_{p^{delta_a}}` | `F_{p^delta}` |
| `P` | half-system of `mu_{2^{e_p}}` | `(theta^j)_{j<L}`, `ord(theta) = 2L` | `(xi^j)_{j<h}` |
| `Lambda` | `{1,3,...,2R-1}` | `{1}` | `{odd s : 1 <= s <= w-1}` |
| `g = |Lambda^*|` | `R` | `delta_a` | `|Z_w^odd|` |
| weight `omega` | `2^{-U}` | `C(L-U, (r'_a-U)/2)` | `2^{h-U}` |
| target | `Phi <= 2^{o(h)}`? | `Phi > 0`? | `Phi = 0` / sparse? |

**All three specialize EXACTLY**, with two honest qualifications that I
report rather than paper over (registered in advance as T-A3/P1):

- **I1 is one class of four.** The banked object is `Z(L) = Z_1^C, C <= 4`
  (`f2_z1_mass_knife_edge/statement.md:14-15`); the master object is `Z_1`.
  The `C`-th power is outside `T(P,Lambda)` and is carried alongside.
- **I2's side conditions are inside the weight, not inside `T`.** THEOREM
  DSA needs `U` even and `U <= r'_a`; those are *not* conditions on
  `T(P,Lambda)`. They are absorbed exactly by LEMMA TC's weight, which is
  `0` unless they hold (`crossing_low_w/PROOFS.md:172-178`). So the
  **existence** form of I2 does NOT specialize to a bare `Phi_1 > 0`
  question; the **mass** form does, with `omega = C(L-U,(r'_a-U)/2)`. I
  report this as a genuine non-specialization of the existence reading.
- **I3 specializes only onto its ODD-condition sub-object.** LEMMA OE
  (`crossing_low_w/PROOFS.md:150-151`, verbatim: *"`p_t(S') = sum_j eps_j
  theta^{tj}` for `t` ODD, and `p_t(S') = sum_j sig_j (theta^2)^{(t/2)j}`
  for `t` EVEN"*) shows the even conditions live on `sig in {0,1,2}^h`, not
  on `eps`. They are a **different instance at half the length over a larger
  alphabet** — which is precisely CATCH E-2's self-similarity
  (`efloor_sparsity/PROOFS.md:352-360`), now with the recursion named. Every
  banked I3 instrument (SP-COVER, SP-TERNARY, LEMMA AB) uses only the odd
  conditions, so the master object covers the whole banked instrument set,
  but **not** the full predicate `p | N(I_S)`.

**The "+1" instance is the recursion itself.** The alphabet ladder
`{0,1} -> {0,1,2} -> ...` generated by LEMMA OE is exactly the `k`-ary
generalization that §2.4 shows Z-FLOOR-M covers.

**The mass/census dictionary** (blind-convergent with the sibling, §0):
I1's weight `2^{-U}` and I3's weight `2^{h-U}` are the SAME functional up
to the constant `2^h`, because both count 0/1 lifts of a ternary difference —
I1's by `z1_ternary_mass/PROOFS.md:148-155`, I3's by LEMMA AB(3).

*Verified:* `check.py floor` — the census identity
`#{S : strat(S)=0, odd conditions} == sum_{v != 0} 2^{h-wt(v)}` replayed
directly over all `2^16` subsets at `n = 16`, 16 cells, 0 failures; and the
collision identity `sum_s |F_s|^2 == sum_{v in T} 2^{h-wt(v)}` exactly in
32 cells.

---

## §2. (M2) THE SHARED SPINE, PROVED

### 2.1 (i) CHAR-0 EMPTINESS at 2-power orders — the exact master statement

> **THEOREM CZ-M.** Let `n = 2N`, `omega` of exact order `n` in
> characteristic 0, `P = (omega^j)_{j<N}` the half-system, and let `Lambda`
> contain some `l` with `gcd(l, n) = 1`. Then
>
> ```text
>   T(P, Lambda)  =  { ternary coefficient vectors of  Phi_n(X)·g(X),
>                      deg g < N - phi(n) } ,
> ```
>
> and in particular
>
> ```text
>   T(P, Lambda) = {0}   <=>   N = phi(n)   <=>   n is a power of 2 .
> ```
> Moreover the statement holds for ALL integer coefficient vectors, not
> only ternary ones, and needs no hypothesis on `Lambda` beyond one unit.

*Proof.* For `l` a unit, `j |-> lj mod n` is a bijection of `Z/n` and
`omega^{lj} = ± omega^{(lj mod N)}`, so `eps |-> eps'` is a signed
permutation and `sum_j eps_j omega^{lj} = 0` iff `sum_i eps'_i omega^i = 0`.
The map `Z[X]_{<N} -> Z[omega]`, `V |-> V(omega)`, has kernel
`{V : Phi_n | V, deg V < N} = Phi_n · Z[X]_{<N-phi(n)}`, a free module of
rank `N - phi(n)`. That rank is 0 iff `N = phi(n)`; since `phi(2N) = N` iff
`2N` is a 2-power, the last equivalence follows. ∎

**What this is worth.** The `n`-a-2-power half is exactly the banked Z-basis
argument (`f2_sl1_powersums/PROOFS.md:260-265`, §0) — **cited, not claimed**.
What is new is the *complement*: it converts CATCH-Z6
(`z1_ternary_mass/PROOFS.md:445-450`, verbatim: *"At composite `2N` there are
`p`-INDEPENDENT ternary relations... At 2-power `2N` there are **none**"*)
from an observed contamination into a **rank statement with a closed count**:
whenever `Phi_n` and its shifts have disjoint supports the count is exactly
`3^{N - phi(n)} - 1`.

*Verified:* `check.py char0` — (a) at 2-power `n in {8,16}`, **0** of the
6,640 nonzero ternary `eps` have `X = 0` (exact cyclotomic norms); (b) the
rank law over 6 orders; (c) the **RULE TEST** (composite `2N`, labelled,
never used for any official-row conclusion) reproduces CATCH-Z6's banked
numbers exactly:

| `2N` | `N` | `phi(2N)` | rank | ternary kernel vectors | banked |
|---|---|---|---|---|---|
| 12 | 6 | 4 | 2 | **8** `= 3^2-1` (min wt 3) | 8 |
| 20 | 10 | 8 | 2 | **8** `= 3^2-1` (min wt 5) | 8 |
| 24 | 12 | 8 | 4 | **80** `= 3^4-1` (min wt 3) | 80 |

### 2.2 (ii) THEOREM CS at master level — it DOES read verbatim, with an
exact hypothesis class

`es_coprimality/PROOFS.md:202-225`, verbatim:

> > **THEOREM CS.** Let `n = 2^m`, `p` an odd prime, `delta = ord_n(p)`,
> > `S <= Z/n` with `|S| = r'` and `x_1 != 0`. If `p | N(I_S)` then
> >
> > ```text
> > p^{|Z_w^odd|}  divides  |N_{K/Q}(x_1)|                            (CS1)
> > ```
> >
> > and, unconditionally,
> >
> > ```text
> > |N_{K/Q}(x_1)|^2  <=  ( r' - a_{n/2}(S) )^h ,   h = n/2.          (CS2)
> > ```

> **THEOREM CS-M.** Let `n = 2^m`, `h = n/2`, `p` odd, `P` the half-system
> of `mu_n` in `F_{p^delta}`, and `Lambda ⊆ (Z/n)^*`. Let
> `eps in T(P,Lambda)`, `eps != 0`, and `X := sum_{j<h} eps_j zeta_n^j`.
> Then `X != 0` and
>
> ```text
>   p^{|Lambda^*|}  divides  |N_{K/Q}(X)| ,                          (CS1-M)
>   |N_{K/Q}(X)|^2  <=  wt(eps)^h ,                                  (CS2-M)
>   |Lambda^*| · log2 p  <=  (h/2) · log2 wt(eps) ,                  (CS3-M)
>   wt(eps)  >=  p^{2|Lambda^*|/h} .                                 (CS4-M)
> ```

*Proof.* `X != 0` by THEOREM CZ-M. Let `P` be a prime of `O_K` above `p`
with `zeta_n |-> xi`. For `l in Lambda`, `sigma_l(X) mod P = sum_j eps_j
xi^{lj} = 0`, so `X in P_l := sigma_l^{-1}(P)`. Frobenius fixes `P`
(`sigma_p(P) = P`), so `P_{pl} = P_l`: the prime depends only on the
`<p>`-coset of `l`, and `P_l = P_{l'}` iff `l/l'` lies in the decomposition
group `<p>`. Hence the `P_l` are `|Lambda^*|/delta` **distinct** primes of
residue degree `delta`, whose product divides `(X)`, giving (CS1-M). (CS2-M)
is LEMMA SM plus AM-GM over the `h` embeddings — and is exactly the banked
ceiling `dli_c1_ternary_relation_norm_sandwich/statement.md:27-28`, cited not
claimed. (CS3-M) is (CS1-M)+(CS2-M) in logarithms, legitimate because `X != 0`
makes `N(X)` a nonzero rational integer; (CS4-M) is (CS3-M) rearranged. ∎

**The answer to the mandate's question, stated exactly.** CS's proof reads
**verbatim** over `T(P,Lambda)` for **any** Frobenius-stable
`Lambda ⊆ (Z/n)^*`. It needs **no window structure and no consecutivity**.
Its three real hypotheses are:

1. `P` is a **half-system** — used twice, once so the char-0 lift is nonzero
   (CZ-M) and once in LEMMA SM (`j - j' = h` impossible). On the *full*
   system both fail: antipodal pairs are char-0 relations.
2. `Lambda ⊆ (Z/n)^*` — needed for `sigma_l` to exist. Even `l` have no
   Galois element; they are the next stratum (LEMMA OE), not a defect.
3. `n` a 2-power — used for `Phi_n = X^h+1` (via CZ-M) and for
   `sum_{c odd} zeta^{cd}`.

The only window-specific content of the banked CS is (CS4)'s uniform bound
`|Z_w^odd| >= ceil((w-1)/2)`, which at master level is the triviality
`|Lambda^*| >= |Lambda|`.

*Verified:* `check.py cs` — 30 cells at `n in {16,32}`, `p in {3,5,7,17}`,
**11,752 checks, 0 failures**, all exact integer arithmetic (cyclotomic norms
by fraction-free determinant). The tightest measured (CS3-M) margin is
**0.0000 bits** in 18 cells: the master bound is **SHARP**, exactly as (CS2)
is at the 0/1 level. The ternary counts reproduce
`efloor_sparsity/PROOFS.md:320-326`'s banked table exactly (6560 / 6560 /
16640 / 288 / 288 / 288 / 148224 / 288, and 0 wherever it records 0).

### 2.3 (iii) The orbit/symmetry structure at master level

> **LEMMA ROT-M.** For `P` a half-system and `Lambda ⊆ (Z/n)^*`,
> `T(P,Lambda)` is stable under
> (a) `eps -> -eps`; (b) the negacyclic shift `R`, `(R eps)_0 = -eps_{h-1}`,
> `(R eps)_j = eps_{j-1}`, of order `n = 2h`; (c) the dilates
> `D_m : V(X) -> V(X^m)` for `m in Stab(Lambda^*) := {m in (Z/n)^* :
> m Lambda^* = Lambda^*}`, a group that always contains `<p>`.

*Proof.* (b) `sum_j (R eps)_j xi^{lj} = -eps_{h-1}(1 + xi^{lh}) = 0` since
`xi^h = -1` and `l` is odd. (c) `D_m` maps `C(Lambda^*)` to
`C(m^{-1}Lambda^*)`, which is `C(Lambda^*)` iff `m in Stab`; `<p> ⊆ Stab`
by PROPOSITION HS(1). ∎

This contains LEMMA ROT (`crossing_low_w/PROOFS.md:330-332`) as the case
`Lambda = {1}`, where `R` has order `2L` — the banked orbit correction.

*Verified:* `check.py rot` — 15 cells, **4,057 checks, 0 failures**; every
orbit size divides `n = 2h`, `Stab(Lambda^*) ⊇ <p>` in every cell, and in the
tested cells `|Stab| = delta` exactly. **Honest limit:** I verified that
`D_m` preserves the *set* `T`; I did **not** determine whether `D_p` fuses
`<R>`-orbits, so I do **not** claim a refinement of LEMMA ROT's `2L` orbit
correction at `delta_a > 1`.

### 2.4 (iv) Z-FLOOR at master level — the exact scope

> **THEOREM Z-FLOOR-M.** Let `X ⊆ Z^M` be any finite set and
> `psi : X -> A` any map into any finite set. Then
>
> ```text
>   sum_{eps} #{(a,b) in X^2 : a - b = eps, psi(a) = psi(b)}
>       = sum_{s in A} |psi^{-1}(s)|^2  >=  |X|^2 / |A| .
> ```
> With `X = {0,...,k-1}^M` and `psi` the evaluation map of `(P,Lambda)`, the
> differences `eps` range over `{0,±1,...,±(k-1)}^M ∩ T_k(P,Lambda)` with
> multiplicity `prod_j (k - |eps_j|)`. The ternary case is `k = 2`, where
> the multiplicity is `2^{M-U}` and the statement is
>
> ```text
>   Z(P,Lambda) := sum_{eps in T(P,Lambda)} 2^{-U(eps)}  >=  2^M / |Im psi| ,
>   |T(P,Lambda)|  >=  2^M / |Im psi| .
> ```
> For `P` a half-system and `Lambda ⊆ (Z/n)^*`, `|Im psi| <= p^g`,
> `g = |Lambda^*|`.

*Proof.* Cauchy–Schwarz on `sum_s |psi^{-1}(s)| = |X|`; the multiplicity
count is coordinatewise. The count form follows by fixing one element of the
largest fibre (`z1_ternary_mass/PROOFS.md:175-178`). ∎

**The exact scope, as the mandate asks.** Z-FLOOR-M is *alphabet-agnostic*
in a precise and limited sense: it floors the mass **whose weight is a
difference multiplicity** — `2^{M-U}` for `k=2`, `prod_j(k-|eps_j|)` in
general — for **any** point set, **any** condition set, **any** field, and
indeed any map whatsoever. It is **not** weight-agnostic: it says nothing
about I2's crossing weight `C(L-U,(r'_a-U)/2)`, which is a fibre size of a
*constant-weight* map and not a difference multiplicity. That is the exact
boundary, and §4.1 is careful to stay inside it.

*Verified:* `check.py floor` — the collision identity and the Cauchy–Schwarz
floor exactly in 32 cells; the count floor in all 56 cells; 0 failures.

---

## §3. (M3) THE INSTRUMENT MATRIX

Verdicts: **MASTER** = proved at master level here, with its hypothesis
class; **INSTANCE-ONLY** = the exact obstruction is named; **CITED** = banked
and used unchanged.

| instrument | source | verdict | master-level hypothesis class / obstruction |
|---|---|---|---|
| **Z-FLOOR** | I1, `z1/PROOFS.md:130-135` | **MASTER** (§2.4) | none — any `P`, `Lambda`, field, alphabet; weight must be a difference multiplicity |
| **LEMMA Z / char-0** | `b1_char0_giant_coset_theorem` + `f2_sl1_powersums:260-265` | **MASTER** as CZ-M (§2.1) | `P` a half-system of `mu_n`; one unit in `Lambda`; emptiness iff `n` a 2-power |
| **CS (CS1/CS2/CS3)** | I3, `es_coprimality:202-225` | **MASTER** as CS-M (§2.2) | `n = 2^m`, `P` half-system, `Lambda ⊆ (Z/n)^*`. Fails on the full system (char-0 relations) and for even `l` (no `sigma_l`) |
| **AM-GM ceiling** | `dli_c1_ternary_relation_norm_sandwich:27-28` | **CITED** | already master-level and already ternary; `es_coprimality`'s (CS2) is its 0/1 shadow via LEMMA BR |
| **LEMMA AB** | I3, `efloor:88-96` | **MASTER** = PROPOSITION HS + LEMMA BR (§1.2–1.3) | `n` even, `p` odd; it *is* the half-system dictionary |
| **SP-COVER** | I3, `efloor:122-128` | **MASTER**: `Lambda^* = (Z/n)^*` `=>` `T = {0}` | proof: `deg V < h = deg Phi_n` forces `V = 0`. Equivalently `g = h`. **Vacuous at I1 and I2** — see §4.4 |
| **LEMMA COS / SP-UNIFORM** | I3, `efloor:153-179` | **MASTER**: coverage depends only on `Lambda mod 2^{v_2(p^2-1)}` | needs `m >= v_2(p^2-1)`; this is the `n`-uniformity, unchanged |
| **SP-TERNARY** | I3, `efloor:304-310` | **MASTER** trivially (`T = {0}` is the criterion) | per-`(n,p,w)` certified; no `n`-uniform form, as banked |
| **DSA (pigeonhole)** | I2, `crossing:207-233` | **SUBSUMED** by Z-FLOOR-M (§4.1) | Z-FLOOR-M gives a *count*, `2^{L}/p^{delta_a}`, where DSA gives existence; DSA's `2^{L-2}` buys the parity/support side conditions Z-FLOOR-M does not |
| **LEMMA ROT** | I2, `crossing:330-332` | **MASTER** as ROT-M (§2.3) | `Lambda ⊆ (Z/n)^*`; extends by the dilates `Stab(Lambda^*)` |
| **LEMMA TC** | I2, `crossing:172-178` | **INSTANCE-ONLY** | it is the *weight* `omega`, i.e. the fibre of a constant-weight map; not a statement about `T` |
| **LEMMA OE** | I2, `crossing:150-151` | **MASTER** as the alphabet recursion (§1.4) | odd `l` see `eps`; even `l` are the next instance at alphabet `{0,1,2}` |
| **LEMMA STRAT / DS / FREE** | I2/I3 | **INSTANCE-ONLY** | statements about 0/1 sets `S` and their periodicity, upstream of `T` |
| **Z-1 (Newton)** | I1, `dli_wcl_newton_short_window_exclusion` | **MASTER, PREFIX-ONLY** (§4.5) | `Lambda = {1,3,...,2ell-1}` a *prefix*, `char > U`; gives `U >= 2ell+1` |
| **Z-2 (`l1`)** | I1, `z1:200-238` | **MASTER**, same prefix class | already stated for all integer coefficients; the `k`-ary ladder of §2.4 is its natural home |
| **Z-NOGO** | I1, `z1:366-372` | **INSTANCE-ONLY**, but §4.4 gives its master shadow | it is a statement about a *family of bounds* at saturation, not about `T` |
| **LEMMA TWO** | I3, `es_coprimality:112-124` | **MASTER**: `X = sum_j eps_j zeta^j ≡ U (mod pi)`, so `2 | N(X)` iff `U` even | one line; the ternary analogue of the banked 0/1 form |
| **SPD (character sums)** | I3, `efloor:372-394` | **CITED, VACUOUS** | banked as proved-and-vacuous in every regime; master level changes nothing |

---

## §4. (M4) THE VALUE TEST

Four transfers were attempted, in the mandate's own order. Two pay, one is
dominated, one is vacuous. All four are reported.

### 4.1 Z-FLOOR at I2 — PAYS (a count where DSA gives existence)

> **COROLLARY DSA-COUNT.** At the crossing deep stratum
> (`P = (theta^j)_{j<L}`, `Lambda = {1}`, `g = delta_a`):
>
> ```text
>   |T(P,{1})|  >=  2^L / p^{delta_a} ,
> ```
> and, restricting the Cauchy–Schwarz to the `2^{L-2}` vectors `a` with
> `a_{L-1} = 0` and `|a|` even, at least `2^{L-2}/p^{delta_a} - 1` **distinct**
> `eps` with `U` even and `U <= L-2`, each of which contributes a **disjoint**
> LEMMA TC fibre to `W_w`.

*Proof.* Z-FLOOR-M with `X = {0,1}^L` resp. the even-parity subset; DSA's own
support bookkeeping (`crossing_low_w/PROOFS.md:224-233`) applies unchanged to
every difference from a fixed element of the largest fibre; disjointness is
LEMMA TC. ∎

**Honest pricing.** The *threshold* is unchanged: `p^{delta_a} < 2^{L-2}` is
DSA's hypothesis and mine. What is new is the multiplicity. At the banked
witness row (`p = 6597069766657`, `L = 128`, `delta_a = 1`) this gives
`>= 2^{83.4}` admissible relations where DSA gives one — but the banked
exhibit's single relation has `U = 20` and therefore a fibre `C(108,53) =
2^{104.267}`, which is **larger** than my `2^{83.4}` relations of guaranteed
fibre `>= 1`. **So the transfer does not improve the banked lower bound on
`|W_w|` at that row.** It is a strengthening of the *instrument*, not of the
*number*.

### 4.2 Z-FLOOR at I3 — PAYS (the first existence instrument on `C_odd`)

The (ES) lane has only exclusion instruments; the sweep confirms no floor and
no forcing exists there, and that the Ax–Katz route is banked dead.

> **THEOREM I3-FORCE.** Let `n = 2^m`, `p` odd, `Lambda = {odd s :
> 1 <= s <= w-1}`, `g = |Z_w^odd|`, `h = n/2`. If
>
> ```text
>         g · log2 p  <  h
> ```
> then `C_odd(n,p,w)` contains a **nonzero ternary vector**; equivalently
> (LEMMA AB) there is `S ⊆ Z/n` with `strat(S) = 0` satisfying **every odd**
> window condition. Consequently SP-COVER and SP-TERNARY — the entire
> odd-condition exclusion mechanism — **provably cannot exclude** at that
> `(n,p,w)`.

*Proof.* Z-FLOOR-M: `sum_{v in C_odd ternary} 2^{h - wt(v)} >= 2^{2h}/p^g`;
the zero word contributes `2^h`; `p^g < 2^h` makes the right side exceed
`2^h`. LEMMA AB(3) converts to sets. SP-TERNARY's criterion is literally
"`C_odd` contains no nonzero ternary vector" (`efloor:304-310`), which is now
false. ∎

**What it says at the prize rows** (`check.py thresh`): with `n = 2^41`,
`h = 2^40`, `delta = 1`, `g = 2^{v-1}` at `w = 2^v`, the threshold is
`log2 p < h/g = n/w`:

| `w` | `h/g = n/w` | recorded rows (`log2 p = 256`) | witness tower row (`log2 p = 42.585`) |
|---|---|---|---|
| `2^34` | 128 | silent | **FIRES** |
| `2^35` | 64 | silent | **FIRES** |
| `2^36` | 32 | silent | silent |

So at `w = 2^34` the mechanism provably fails on every `delta = 1` admissible
row with `log2 p < 128` — which, by the banked dichotomy
(`crossing_low_w/PROOFS.md:306-307`, verbatim: *"**`e = 1` rows are NEVER in
the provable regime.** `B* >= 3` forces `q = p >= 3·2^128`, i.e.
`log2 p >= 129.585 > 126 = L−2`"*), is exactly the tower rows and never the
`e = 1` rows. This **strengthens CATCH E-3** (`efloor:571-579`, which records
SP-COVER as *vacuous* at the official gate) from "vacuous" to "provably
fails, on a named row set".

**What it does NOT say.** A nonzero ternary `v` gives the odd conditions
only. It does **not** produce a bad set (`p | N(I_S)` needs the even
conditions too), and it does **not** refute CC-sparsity. It is a no-go on a
*method*, not a refutation of a *statement*. I state this because the
distinction is exactly where an over-claim would live.

*Verified:* `check.py floor` — **16 cells** where the floor fires, a nonzero
ternary codeword present in **every one**; **0 falsifications** of the
registered falsifier P4 (which would have been any cell with `g log2 p < h`
and an exact count of 0). Cross-checked against
`efloor_sparsity/PROOFS.md:320-326`'s banked exact counts.

### 4.3 THE MASTER THRESHOLD — the unification's actual payoff

> **THEOREM MT (the master threshold).** For `P` a half-system of `mu_n`,
> `Lambda ⊆ (Z/n)^*`, `g = |Lambda^*|`, `h = n/2`, the single quantity
>
> ```text
>                 g · log2 p     versus     h
> ```
> governs `T(P,Lambda)`:
>
> - `g · log2 p < h`  `=>`  `T != {0}`, indeed `|T| >= 2^h/p^g`   (Z-FLOOR-M);
> - `g = h`           `=>`  `T = {0}`                              (SP-COVER-M);
> - `T != {0}`        `=>`  every nonzero `eps` has `wt >= p^{2g/h}` (CS4-M).

> **COROLLARY MX (complementarity).** In the forcing regime
> `g log2 p < h`, CS4-M yields only `wt >= p^{2g/h} < p^{2/log2 p} = 4`.
> **The archimedean/norm mechanism is informative only where existence is
> not forced, and vice versa.** The two banked mechanisms can never both
> bite at the same row.

*Proof of MX.* `g log2 p < h` gives `2g/h < 2/log2 p`, and
`p^{2/log2 p} = 2^2 = 4`. ∎

**THE THREE INSTANCES ARE ONE INEQUALITY** (`check.py thresh`, exact,
80-digit decimal arithmetic):

**I1.** `p = 18446735827372343297`, `h = S = 2^38`, `g = R`. Then

```text
   h - g·log2 p  =  -46.0249 bits   at R = 4,294,967,340  (t = ceil(n/L))
   h - g·log2 p  =  +17.9751 bits   at R = 4,294,967,339  (t = n/L)
```

These are, to four decimals, **exactly the banked knife-edge numbers**
(`f2_z1_mass_knife_edge/statement.md:45-52`: *"silent by 46.02 bits ... FIRES
at +17.98 bits"*), re-derived here from the master threshold alone. And
`h/g = 63.999999344 = log2 p` — **I1's saturation `R/S = 1/log2 p` says
precisely that the F2 object sits ON the master threshold.** The banked
"one `Lambda` condition is worth `log2 p = 64` bits" is now the trivial
observation that `g` moves by 1.

**I2.** At `w = 2^v`, `L = n/w`, and the deep stratum has `g = delta_a`,
`h = L`, so the master threshold reads `delta_a log2 p < L` against DSA's
`p^{delta_a} < 2^{L-2}` — **the same inequality, to within 2**:

| `w` | `L = n/w` | DSA threshold `L-2` | stratum-0 `h/g` | agree |
|---|---|---|---|---|
| `2^34` | 128 | 126 | 128 | yes |
| `2^35` | 64 | 62 | 64 | yes |
| `2^36` | 32 | 30 | 32 | yes |
| `2^37` | 16 | 14 | 16 | yes |
| `2^38` | 8 | 6 | 8 | yes |
| `2^39` | 4 | 2 | 4 | yes |

**I3.** Stratum 0 has `g = 2^{v-1}`, `h = 2^40`, so `h/g = n/w = L` — the
*same number as the deep stratum*. The deepest stratum and stratum 0, which
the banked work treats by unrelated arguments at unrelated lengths, sit at
**identical** thresholds.

**Why this is the unification's payoff.** The three banked thresholds were
(i) a saturation identity in a GRS lane, (ii) a pigeonhole in a crossing
lane that *explicitly disclaims a balance functional*
(`crossing_dsa_refutation/statement.md:38-39`: *"No balance functional
appears."*), and (iii) an unstated boundary in an (ES) lane that had no
existence instrument at all. THEOREM MT says all three are
`(0/1 information) - (parity-check information) = h - g log2 p`, i.e. one
pigeonhole. The banked seam CATCH-Z3
(`z1_ternary_mass/PROOFS.md:300-307`) identified three faces of this
inequality **inside F2**; MT adds the two other instances.

**Consistency with every banked verdict** (`check.py thresh`, 24 checks):
the `e = 1` dichotomy (`log2 p >= 129.585 > 128 > 126`) puts the recorded
prime rows outside **both** regimes, reproducing "prime rows untouched"; the
witness row `p = 3·2^41+1` sits inside **both**.

### 4.4 SP-COVER at I1 — VACUOUS, and vacuous by exactly the saturation factor

SP-COVER-M requires `g = h`. At I1, `delta = 1` (the row has
`v_2(p-1) = e_p` exactly), so `Lambda^* = Lambda` and coverage demands
`R >= S`. The object has `R/S = 1/log2 p`. **So SP-COVER is vacuous at I1 by
exactly the factor `log2 p >= 39`** — the same constant that makes Z-NOGO's
family fail. This is the registered expectation P6 and it is an honest zero;
but it is a *quantified* zero, and it is the master shadow of Z-NOGO:
`g log2 p` cannot simultaneously be `< h` (forcing) and `= h·log2 p`
(coverage) — the gap between the two ends of THEOREM MT is a factor
`log2 p`, at every instance. This is the same two-sided structure banked at
I3 as *"THE BAD-PRIME RANGE IS TWO-SIDED"*
(`es_ternary_suppression_instruments/statement.md:41-42`), now seen to be an
instance-independent feature of `T(P,Lambda)`.

### 4.5 CS at I1 — the transfer works and is DOMINATED (registered P5)

CS4-M at I1 (`g = R`, `h = n/2`) gives `wt >= p^{2R/h} = p^{4R/n}`. With
`2R/n = 1/64` this is `p^{1/32} = 4.0000`. The banked route-(a) constant is
`2.0000` (`f2_z1_mass_knife_edge/statement.md:59-61`). Both are annihilated
by THEOREM Z-1's `2R+1 = 8,589,934,681`. **The transfer pays nothing at I1**,
exactly as registered — but it does expose a wrong constant of record, §5
CATCH-T3.

### 4.6 Z-1 at I2/I3 — MASTER, prefix-only; a registered expectation MISSED

Z-1 transports to any **prefix** `Lambda = {1,3,...,2ell-1}` with `char > U`,
giving `U >= 2ell+1`. At I2 (`ell = 1`) this gives `U >= 3`, hence `U >= 4`
by DSA's parity — a genuine but marginal strengthening (the banked witness
has `U = 20`). At I3 (`ell = ceil((w-1)/2)`) it gives `U >= w` for
`strat = 0` bad sets when `p > h`, which at `w = 2^34` is `2^30` times
stronger than CS4-M's `16`. **But it does not help I3's goal**: a *lower*
bound on `U = r' - a_{n/2}(S)` weakens CS-EXCL rather than strengthening it,
and the resulting census bound is vacuous at prize scale. Honest zero.

*Verified:* `check.py newton` — 16 prefix cells, 0 violations.
**REGISTERED EXPECTATION MISSED, reported not buried:** I expected shifted-`Lambda`
counterexamples (mirroring I1's 43) and found **zero**. My grid is 2-power
`n` only, and `z1_ternary_mass/PROOFS.md:536-539` records that of its 43
shifted counterexamples exactly **one** is at 2-power `2N` — *"a thin
sample"*. So my grid cannot see the scope failure and **I do not get to
claim the prefix hypothesis is load-bearing at 2-power orders**; at master
level that is OPEN, exactly as at I1.

---

## §5. CATCHES

1. **CATCH-T1 (the master threshold).** I1's knife edge, I2's DSA regime
   boundary and I3's stratum-0 boundary are ONE inequality
   `g·log2 p` vs `h` (§4.3). The banked four-face seam
   (`f2_o1_status_split/statement.md:61-65`) is F2-internal; two further
   faces exist in other lanes.
2. **CATCH-T2 (`r' - a_{n/2}(S) = wt(A-B)`).** CS2's archimedean quantity
   IS the ternary support size (§1.3). `PROPOSITION TAUT`
   (`efloor_sparsity/PROOFS.md:270-276`) *uses* CS3 with LEMMA AB live and
   still discards it as `<= r'`. Keeping it makes (CS2) a statement about
   `T` and is what lets CS read verbatim at master level.
3. **CATCH-T3 (a wrong constant of record, against a banked statement and a
   minted node).** `f2_sl1_powersums/PROOFS.md:271`, verbatim: *"`|N(alpha)|
   <= w^{n/2}`"*. The banked sharp ceiling is
   `dli_c1_ternary_relation_norm_sandwich/statement.md:27-28`,
   `Norm(f) <= w^(N/2)` with `N = [K:Q] = n/2` — i.e. `|N(alpha)| <= w^{n/4}`,
   the **square root** of what `f2_sl1_powersums` uses. The recorded dead-route
   constant is therefore a factor 2 out **in the exponent**: `w >= p^{2R/n}`
   should read `w >= p^{4R/n}`, i.e. **4.0000, not 2.0000**. This propagates
   into the minted node `f2_z1_mass_knife_edge/statement.md:59-61` (*"yields
   w >= 2.0000"*). **No verdict changes** — the route is dead either way — but
   the constant of record is wrong and two banked statements had never been
   put side by side.
4. **CATCH-T4 (citation drift).** `z1_ternary_mass/PROOFS.md:56-59` and
   `:383` cite the norm route as `f2_sl1_powersums/PROOFS.md:262-266`; the
   statement is at `:271-274`. Lines 262-266 are the Z-basis paragraph. A
   9-line drift in a campaign whose evidentiary standard is file:line.
5. **CATCH-T5 (CATCH-Z6 has a closed form).** The contamination at composite
   `2N` is the rank-`(N - phi(2N))` lattice `Phi_{2N}·Z[X]_{<N-phi}`, with
   exactly `3^{N-phi(2N)} - 1` ternary vectors in the three banked cases
   (8/8/80 reproduced). The grid rule "2-power only" is the statement
   `N = phi(2N)`.
6. **CATCH-T6 (complementarity).** COROLLARY MX: the norm/archimedean
   mechanism and the pigeonhole/existence mechanism are **never**
   simultaneously informative — in the forcing regime CS can only prove
   `wt < 4`. This is why route (a) is dead at I1 *structurally*, not
   numerically: I1 sits on the threshold.
7. **CATCH-T7 (I2's existence reading does not specialize).** THEOREM DSA's
   conclusion needs `U` even and `U <= r'_a`, which are not conditions on
   `T(P,Lambda)`. Only the *mass* reading of I2 is an exact specialization
   (§1.4). Reported rather than forced, per the mandate.

---

## §6. HONEST RESIDUALS

1. **The unification pays twice and no more.** It pays at §4.2 (a new
   existence/no-go instrument at I3, which had none) and at §4.3 (three
   thresholds are one). It pays **nothing** at §4.4 (SP-COVER at I1,
   vacuous), **nothing** at §4.5 (CS at I1, dominated), and **nothing new in
   the numbers** at §4.1 (a stronger instrument, a weaker bound than the
   banked exhibit).
2. **No open master question is closed.** The I1 mass bound
   `Z_1 <= 2^{o(m)}` at `k = e` is untouched; the I2/I3 mid-range primes are
   untouched; CC-sparsity is untouched (and by CATCH E-2 as hard as (ES)).
   The master statement reorganizes and transports; it resolves nothing.
3. **I3's specialization is partial.** Only the odd conditions live on `T`.
   The even conditions are a different instance over the alphabet `{0,1,2}`
   and I did not carry the recursion out.
4. **§4.2's no-go is a no-go on a method, not a refutation.** It shows
   SP-COVER/SP-TERNARY cannot exclude at named rows. It does not exhibit a
   bad set and does not touch `p | N(I_S)`.
5. **Scale.** All machine checks are `n in {8,16,32}` against official rows
   at `n = 2^39`–`2^41`. THEOREM MT's instance table (§4.3) is arithmetic on
   banked constants, not extrapolation; but CS-M, CZ-M, ROT-M and Z-FLOOR-M
   are proved for all `n` and only *verified* at toy scale.
6. **The `delta_a > 1` orbit refinement is not established** (§2.3), and the
   `delta > 1` rows at I3 are not covered by §4.2's row analysis, which
   assumes `delta = 1`.
7. **The registered shifted-`Lambda` expectation missed** (§4.6). Reported.
8. **Blind convergence, credited not claimed.** The one-framework object and
   the mass/census identity are independently registered by the live sibling
   `tern_small_scale_laws` (§0). I claim neither.
9. **Process.** DRAFT ONLY: every file written lies in
   `notes/pilots_20260806/tern_master_statement/`. No node, no `dag.json`, no
   `tools/` file was touched; no commit, no push. No status flip is proposed.
   `tern_unification_adversary/` was not read. Every execution went through
   `tools/ramguard tiny|local -- python3`; no bare `python3` was invoked at
   any point, including for file patching (Edit/Write were used instead).
