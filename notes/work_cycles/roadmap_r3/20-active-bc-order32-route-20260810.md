### 2026-08-10 active-BC order-32 route

The direct upstream-v4 route is now the primary shared completion route for
the deployed rate-half rows.  The K3 endpoint route remains available, but
its same-record `Q=6,s=6,u=2` realization and six downstream payment tasks
are all open.  By contrast, upstream `main` already proves an exact
order-32 partial-relative classification and isolates three terminal inputs:

```text
(S) spread-component routing
(A) exclusive large-owner atom-image control
(E) complete exception routing.
```

The upstream theorem has been harvested at commit
`93fba1be3f3299b0ba4708d88715377bbb656e45`, file
`experimental/grande_finale.tex`, theorem `thm:partial-relative`.  For either
deployed adjacent MCA row and any 32 bad slopes, it gives slope degree
`18..31` and the exact thresholds

```text
KoalaBear: chi >= 2299571
M31:       chi >= 2299499.
```

Outside the named affine, common, pure-locator, denominator-root, and rational
cells, every residual 32-subset is affine/rational; coherence gives global
structure, while incoherence gives a 31-overlap near-sunflower.  This imported
statement is PROVED and source-pinned.  It does not prove `(S)`, `(A)`, or
`(E)` and therefore does not close either adjacent row.

The canonical active balanced-core source witnesses now feed this theorem
without a semantic jump.  If `|Z_BC| <= 31`, the class is already below the
paper's order-32 exception threshold.  Otherwise each 32-subset of the
canonical same-line certificates supplies the theorem's bad slopes,
explaining data, supports, and exact `m`-subsupports.  Maximalization changes
neither the received line nor slope identity.  The resulting adapter
preserves owner labels into the affine/rational/near-sunflower/primitive-
spread alternatives and is PROVED.

The current route is therefore

```text
active balanced-core source-witness compiler [PROVED]
                  |
                  v
order-32 partial-relative adapter             [PROVED]
                  |
          +-------+-------+
          |       |       |
          v       v       v
         (S)     (A)     (E)                  [TARGETS]
          |       |       |
          +-------+-------+
                  v
       deployed adjacent MCA rows             [CONDITIONAL]
```

The next useful proof increment is an exact sublemma inside `(E)`, whose
finite decomposition includes denominator-root, extension,
coordinate-clone, imperfect-quotient, and quantified near-sunflower cases.
The denominator-root lane already has a pole-tolerant localization theorem;
its remaining source-compiler/counting obligation is a smaller target than
the complete K3 endpoint-and-payment chain.  The K3 realization target stays
red and is not refuted by this route choice.

The first denominator-root increment is now banked. The upstream
pole-tolerant theorem is source-pinned and harvested: it localizes coherent
atoms without dividing by the denominator, then cancels the exact common
domain-pole locator after deleting at most one zero-scalar slope. A new exact
source dichotomy resolves the theorem's semantic gap. Every post-cancellation
support either remains MCA-nontrivial in the reduced certificate (with `Q'`
regular on its coincidence core, not necessarily on all of `D'`) or has a
unique simultaneous explaining pair. In the latter case the original
support obstruction becomes a nonzero rank-one defect on the deleted pole
set,

```text
u_i + gamma_i v_i = 0,  v_i != 0,
```

so the same slope and received-line owner are retained and distinct slopes
have distinct explaining pairs.

Interpolation also proves that two trivialized reduced supports meet in at
most `k-1` coordinates. Their `k`-shadows are disjoint, giving

```text
|T| binom(m-t,k) <= binom(n-t,k).
```

This is not a payment. Uniformly in `0<=t<=m-k`, the right-hand ratio is
larger than `(3/2)^k>2^58`, already above the KoalaBear budget and far above
the Mersenne-31 budget. The pure support-packing route is therefore fenced.
The next denominator-root step must couple the full divided scalar-locator
identity across indices and force a paid owner or correction space.

This packet was exported to upstream as draft PR `#1156`, **MCA (E): route
denominator-root puncture defects**. The PR carries a self-contained theorem
note, a standard-library certificate with normal and `-O` replay, five hostile
metadata mutations, and a narrow repair of the pre-existing pole verifier's
stale `grande_finale.tex` blob pin. The old and new pinned scalar-locator
definitions were compared byte-for-byte and are identical. The PR requests
independent review and makes no `(E)` or row-closure claim.

The coordinate-clone branch now has a separate exact reduction. After the
owner-pencil theorem's identically-zero, vertical, and horizontal component
branches are routed separately, group nonzero coordinate curves by shared
irreducible bidegree-`(1,1)` component. A class of size `2<=c<m` satisfies

```text
N_C(m-c) <= 2(n-c) <= 2c(m-c),
```

so `N_C<=2c`. Clone classes are disjoint coordinate sets; all subcritical
classes therefore cost at most `2n=4194304`, below both MCA budgets. Since
`n<2m`, at most one class can have size at least `m`. Thus all unpaid
coordinate-clone content is concentrated on one unique large component.
The excluded identically-zero coordinate branch and that unique large class
remain open and must retain the owner-pencil chronology. This theorem and its
independent certificate were added to draft PR `#1156`; the PR is now titled
**MCA (E): route denominator-root and coordinate-clone exceptions**.

#### Round-31 scope ruling

Canonical round 31 separates two rate-half completion programs that use
related language but live at different row sizes:

```text
n=2^41 prime razor rows:     rate_half_band_crossing_location [critical]
n=2^21 deployed rows:        order-32 partial-relative -> (S)/(A)/(E)
```

The first line is now the only required child of `rate_half_band_closure`.
The K3 structural-surplus arm is background evidence because its exact
certificates are confined to the deployed extension-field row and no proved
row-transport theorem carries them to the prime razor row. The round-31
analytic pilots (`rh_e_axis_audit`, `rh_overlap_cap`,
`rh_transport_dictionary`, and `rh_type2_stratum`) therefore own the current
critical attack on the crossing-location node.

The second line remains the direct route for Przemek's deployed adjacent MCA
rows and the scope of draft PR `#1156`. Progress on `(S)`, `(A)`, or `(E)` is
valuable upstream and may inform the razor analysis, but it is not a logical
premise of the `n=2^41` critical node without a separately proved transport
adapter. Conversely, a razor crossing theorem would not by itself discharge
the finite deployed-row exception ledger.
