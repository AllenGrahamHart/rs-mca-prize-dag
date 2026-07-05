# petal_primitive_residue_kernel_rank

- **status:** TARGET (demoted from CONDITIONAL 2026-07-05: obligation FALSE as stated)

## Statement (re-posed)

Lemma PRK_pet: absolute B0,b0 s.t. for every full-petal in-regime chart and
squarefree-realizable cofactor family, after peeling the paid sheets the residual
has bounded primitive dimension (dim Pi_prim <= B_pet).

## Status: FALSIFIED AS STATED (needs repair before any proof effort)

The **c-independent** (absolute B_pet) form is FALSE. VERIFIED (Modal, bug-fixed):
generic MULTI-CHARACTER kernel families (F = sum_r X^r B_r(X^M), all mu_M-character
blocks active, each B_r in ker lambda) ESCAPE every existing paid class
(mu_k quotient/coset, antipodal, cyclotomic; low-defect is single-character-based)
-- 25/25 across M=3,5,7, growing c -- and their dimension GROWS linearly with excess
c (~(M-1)c/M). So peeling the current paid menu leaves an UNBOUNDED residual.

The old proof route (Gate N + D + L descent) is also refuted: Gate N's window
extraction is false (multi-character families have unbounded excess, bounded
primitive window). See REFUTED_DESCENT_ROUTE.md.

## Repair directions (unproven; the real open question)
1. If the real-problem excess c is bounded, re-pose with a c-DEPENDENT bound.
2. Add multi-character paid classes (structured: 2^M-M-1 c-independent types) + prove
   their chargeability to a ledger budget (a NEW obligation, analog of Gate L).
3. Show the multi-character families do not inflate the actual decoded list.
Same character-selection obstruction as q_cofactor_normal_form.

## Falsifier (met): a squarefree-realizable multi-character family, unpaid by the
current menu, whose primitive dimension grows with c. (Pro's two-character family;
generic multi-character families, verified.)
