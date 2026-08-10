# Cycle 50: rate-half type-2 m=2 product-lift sweep (2026-08-10)

## Purpose

After excluding the natural quartic-coset lift, test the smallest unresolved
endpoint shape for a different algebraic countermodel before investing in a
general theorem.

## Forced shape

At `m=2`, `O=0` and `T=rho+2` force `N=32`, `rho=7`, and `T=9`. The 31
rows containing two supported parameter roots form `K_9` minus five edges;
the remaining row contains one supported and one residual root. The missing
graph is uniquely a two-edge path centered at the singleton vertex plus a
perfect matching on the other six vertices.

## Bounded Modal result

Eight workers tested random slope choices and placements over `F_97` for 52
seconds each. Every one of `599,897` exact stacked parity systems had rank
`32`. There were no positive-nullity systems, no full-support row-scale
vectors, and therefore no Hankel tests.

Artifacts:

- `experiments/prize_resolution/rh_type2_m2_product_lift_prereg.md`;
- `experiments/prize_resolution/rh_type2_m2_product_lift_modal.py`;
- `experiments/prize_resolution/rh_type2_m2_product_lift_result.json`;
- `experiments/prize_resolution/RH_TYPE2_M2_PRODUCT_LIFT_RESULT.md`.

Modal run:
`https://modal.com/apps/allengrahamhart/main/ap-dPpY3BMeJ2K3jWxK879KVv`.

## Route decision

This is a zero-power null for universal existence: generic placements are
expected to have full parity rank. Do not buy more random trials. The next
rate-half type-2 step must be theorem-led: classify the near-saturated
biform, prove an aggregate bound for the shortened-apolar family, or define
a structured search with a finite completeness boundary. No DAG status or
official budget changes.
