# Brief 6 — the ordinary-list adjacent crossing (RHL-ADJ)

**Node:** `critical/nodes/rate_half_list_adjacent_crossing/` ·
**status TARGET** · **consumer:** `list_adjacency_closing` · **upstream:**
OVERLAP with Lane L / `prob:list-completion` (przchojecki/rs-mca,
`experimental/notes/thresholds/zeroremainder_scale.md` Theorem 2.1 and the
July-integrated zero-remainder floor of PR #1101 — which extends OUR
positive-remainder construction to `c=1, s=0` without moving the unsafe
agreement).

## The mystery in one paragraph

For ordinary Reed-Solomon at every admissible official rate-1/2 row, the
worst-case list size `L_1(a)` crosses the prize budget `B* = floor(q/2^128)`
at *some* agreement `a_L(C)` — trivially, since `L_1` is monotone. The
mystery is **where**, and specifically: certifying an upper leg
`L_1(a) <= B*` at any explicit `a`. The lower leg is proved and sharp-ish
(the crossing is at least `k + 2^34`); the upper leg is genuinely
field-dependent — we *refuted* the natural field-independent form — and no
current technique certifies list sizes at agreements this close to the
radius on rows this large.

## Formal pose

For every admissible official rate-1/2 row `C = RS[F, D, k]`, with
`q = |F|`, `B* = floor(q/2^128)`, and
`L_1(a) = max_u #{c in C : agr(c,u) >= a}`:

```text
(RHL-ADJ)  there is a_L(C) with  L_1(a_L(C)) <= B* < L_1(a_L(C)-1).
```

At the prize-max razor row (`n = 2^41, k = 2^40, q < 2^256`) the proved
cyclically rotated prefix floor gives `L_1(k + 17,179,869,183) > B*`, so

```text
(RHL-LB)   a_L(C) >= k + 2^34.
```

The PROVED `list_large_m_scope_closure` transports the crossing pair to
every constant common-support interleaving arity — so ordinary lists
(`m=1`) are the whole remaining problem.

## Death ledger — read before proposing

- **The fixed-crossing form was REFUTED** (wave-9, audited): no single
  field-independent `a` works across admissible `q`. The node was re-posed
  field-dependently as above. Any proposal must let `a_L` depend on `q`.
- **A determination claim was WITHDRAWN** (our own overclaim, wave-9
  audit, recorded verbatim in `rate_half_band_closure/statement.md`): the
  "banked safe side" was planning prose; the LIST SAFE side is OPEN. Do
  not cite the withdrawn sentence — it survives in old notes.
- **Packing-bound triage: DEAD.** Standard packing arguments certify
  `L_1 <= B*` only within ~128 grid points of full agreement — uselessly
  far above the `k + 2^34` scale. Recorded in the node's upstream-wave
  note; do not respend that route.
- Johnson-bound comparison: our exact crossing target sits **below** the
  Johnson radius for these parameters — generic list-decoding bounds do
  not reach it. That is precisely why the node is red.
- Crosswalk nonclaim: never race upstream #1097/#1099 (their Lane L
  program); coordinate through the crosswalk instead.

## Structure available (footholds)

- The unsafe side is a *construction* (cyclic rotated prefix floor,
  strengthened through `sigma_0 = 8,594,128,895`), fully banked, with
  exact counts — any proposed upper leg can be sanity-checked against it
  instantly (it pins where `L_1` is provably large).
- `B*` is astronomically large (`~ 2^128`-scale for `q ~ 2^256`): the
  upper leg does NOT need small lists — it needs "not `2^128`-sized" at
  one explicit agreement. This is far weaker than classical list-decoding
  targets, which is the same "absurdly weak target, no technique reaches
  it" signature as brief 5.
- Admissible official rows constrain `(q, D, k)` sharply (razor row pinned;
  `q < 2^256`, structured `D`).

## The conversion ask

1. **Field-class case tree.** The refutation of the fixed crossing tells
   us `a_L` moves with `q`. Ask: stratify admissible `q` (by `v_2(q-1)`,
   by the razor row's evaluation-set structure, by `q mod` small moduli)
   and, per stratum, give an explicit `a_L(stratum)` with a certified
   upper leg. If each stratum's certificate is a bounded exact computation
   (an energy/moment count on the evaluation set), this is an m2-style
   program over strata.
2. **Budget form.** `L_1(a) <= B*` is a *counting* budget, and `B*` is
   enormous. Ask: a first-moment / second-moment argument on codewords at
   agreement `>= a` whose constants are explicit — even wildly lossy
   moment bounds may clear `2^128`. Identify exactly the agreement range
   where the second moment fails; that range becomes the case list.
3. **Dual use of the floor construction.** The unsafe-side construction
   enumerates the *reason* lists are large below `sigma_0`: rotated
   prefixes. Ask: a structure theorem — every codeword at agreement
   `>= k + 2^34 + delta` is "explained" by one of finitely many
   mechanisms (prefix-rotation, tail-fixing, ...) — with each mechanism's
   count certified. Completeness of the mechanism list is the hard part;
   its shape is exactly the witness-enumeration pattern of brief 3.

**Sharpest question:** at the razor row, is there ANY explicit agreement
`a > k + 2^34` with a proof that `L_1(a) <= B*` — by any method, with any
explicit constants? One such point converts the node from "mysterious" to
"sandwich the crossing", which is a bisection — a case program by
construction.

## Pointers

- Node: `critical/nodes/rate_half_list_adjacent_crossing/` (statement,
  attack, upstream-wave note with the packing triage).
- The floor: `rate_half_cyclic_rotated_prefix_floor` (PROVED) +
  `rate_half_fixed_tail_prefix_floor` (background).
- Scope transport: `list_large_m_scope_closure` (PROVED).
- Battlefield context: `critical/nodes/rate_half_band_closure/statement.md`
  (the corrected history is recorded inline there).

> **[CORRECTION + UPGRADE 2026-08-01 — from the Pro dossier, audited and
> accepted.]** (1) The literal (RHL-ADJ) display above is TRIVIALLY TRUE
> by monotonicity (L_1 integer-valued, nonincreasing, L_1(n+1)=0); the
> open content is the certificate-producing contract — a row-computable
> agreement with an independently checkable safe certificate and a
> same-received-word unsafe certificate. (2) The "sharpest question"
> bisection is sound only over a TOTAL decision oracle: failure of an
> upper-bound method is UNKNOWN, never UNSAFE. (3) UPGRADE: the banked
> cyclic floor already yields a six-tier field-independent unsafe
> staircase (e.g. 3 <= B* <= 312 gives L_1(5n/8-1) > B*) — now minted as
> `background/nodes/rate_half_list_cyclic_budget_staircase/` (PROVED).
> See `responses/BRIEF6_PRO_DOSSIER.md` and
> `responses/BRIEF6_DOSSIER_AUDIT.md`.
