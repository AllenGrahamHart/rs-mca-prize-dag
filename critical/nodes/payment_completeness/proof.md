# proof: payment_completeness

- **status:** PROVABLE -> (this document) modus-ponens discharge
- **closure:** proof
- **gate:** `any` (see `conditional.md`) — one complete classification route
  suffices.
- **delivered route:** `spi_exceptional_class` [PROVABLE -> proved, this batch],
  resting on `spi_component_control` [PROVED].

---

## 1. The gate

`payment_completeness` asks that the **ledger taxonomy be exhaustive**: not
assumed and not merely evidenced, but the *classification output* of whichever
enumeration route completes. Per `conditional.md` the node is `gate: any` over
four alternative complete-classification routes

```text
        xr_crystallization | spi_exceptional_class | es_regularity |
        monodromy_realization
```

with a further block of **evidence-only** nodes (`redteam_multiscale`,
`isotypic`, `dihedral_quotient_stratum`, `rigidity_kernel`,
`f_dih_subgroup_completeness`) that pressure-test but do not certify.

The conditional implication is already proved in `conditional.md`:

> **(C)** If any predicate route gives a *complete classification* of the
> relevant alignment/payment objects, then the ledger taxonomy is exhaustive
> (every contributing object lands in exactly one classified branch, or the
> classification emits a new named branch routed through the S9 protocol).

This document supplies the missing antecedent and fires modus ponens.

## 2. The antecedent is now discharged (the `spi` route)

`nodes/spi_exceptional_class/proof.md` proves, referee-grade, the
classification of the alignment-incidence components of the Hankel pencil
`M(Z) = Z0 M_u + Z1 M_v`. Using the PROVED component inventory of
`spi_component_control` (one horizontal scroll + at most `r <= t` vertical
rank-drop fibres, `# Irr <= t+1`), it shows:

> **(A)** Every rank-excess / super-slope component of `I_{u,v}` **other than**
> the generic row-full horizontal scroll is exactly one of
> — **tangent / common-divisor paid**,
> — **empty** (`cap D_j = emptyset`),
> — **degenerate**, excluded a priori by the noncontainment gate,
> — **quotient / extension paid**, or
> — an **apolar-principal scroll** (a *new named priceable class*, priced by
>   the `R(Z) = prod_{h in H} q_Z(h)` dichotomy: fixed common `H`-root =>
>   tangent-paid, else `O(n^2)` individually charged `H`-supported slopes).

(A) is a **complete classification** of the exceptional/super-threshold
structures: the case split of `spi_exceptional_class` §3–§4 is exhaustive over
the component inventory, and it uses no fibre-count circularity (only component
degrees and resultant degrees). Its two numeric anchors are reproduced by
`spi_exceptional_class/notes/verify_writeup.py` (`PASS`: 2500 pencils, 1600
tangent fibres).

Therefore the antecedent of **(C)** holds via the `spi` route. By modus ponens,
**the ledger taxonomy is exhaustive**. ∎

## 3. What the gate's satisfaction means (precise scope)

The taxonomy exhaustiveness proved here is exactly:

> **Every super-threshold alignment structure is a named paid class.** The
> named list is: **tangent / common-divisor**, **quotient / pullback**
> (the Luroth lattice, subsuming multiplicative, dihedral/Chebyshev,
> moment-trade/PTE), **extension / subfield**, and — added this batch —
> the **apolar-principal scroll**. Any component carrying rank excess or a
> super-slope alignment lands in one of these, or is empty, or is removed by
> the noncontainment gate.

This is the falsifier's target settled in the affirmative on the `spi` route's
scope: there is **no unnameable unstructured super-poly alignment family** among
the exceptional components — the one outcome the brief flagged as fatal. The
program's historical pattern holds: when a new family appeared (affine-net P3,
dihedral E30), the ledger *grew* and completeness *persisted*; the
apolar-principal scroll is the third such absorption.

**Honest boundary (this is not "everything is paid").** Exhaustiveness of the
*taxonomy* is a statement about *classification*, not about *counting*. The one
component deliberately left unclassified by the `spi` route — the **generic
row-full horizontal scroll** (the aperiodic incidence core) — is not an unnamed
paid class; it is the baseline core whose **`D_j`-count** is the separate,
still-open quantitative node `spi_point_counting` (the R2 lane). Its openness is
a counting gap, **not** a taxonomy gap: it produces no super-threshold structure
outside the named classes. So `payment_completeness` (taxonomy exhaustive) is
discharged; the strictly stronger "every pair is fully priced" additionally
requires R2 / `spi_point_counting`, which this node does **not** claim. This is
the same honesty distinction as `stratification_partition_thm` §4 (a partition
into named cells is not a proof that the residual cell is empty).

## 4. The other three routes remain as insurance, not obligations

Because the gate is `any`, completing the `spi` route suffices; the remaining
three classification routes are **unproved alternatives kept as insurance**,
not obligations:

- `xr_crystallization` — classifies the inverse class `C_XR`;
- `es_regularity` — classifies the regularity-lemma exceptional sets;
- `monodromy_realization` — classifies via the monodromy subgroup.

Each is an independent path to the *same* exhaustiveness conclusion; none is
required now, and none is asserted here. The evidence nodes (`redteam_multiscale`
et al.) have already refined the taxonomy (the E25/E30/E35 clause corrections,
the S9 moment-trade fifth-mechanism watch) but are, per `conditional.md`, red-
team pressure and **not** used as proof of exhaustiveness.

## 5. Conclusion

The conditional **(C)** is proved (`conditional.md`); its antecedent is
discharged by the completed `spi_exceptional_class` classification **(A)**,
which itself stands on the PROVED `spi_component_control`. By modus ponens the
**ledger taxonomy is exhaustive** on the `spi` route's scope: every
super-threshold alignment structure is a named paid class (now including the
apolar-principal scroll), with the sole open item being the *counting* of the
generic row-full core (`spi_point_counting` / R2), which is a quantitative gap
and not a missing taxonomy branch. The three sister routes remain live
insurance. **This discharges `payment_completeness`.** ∎
