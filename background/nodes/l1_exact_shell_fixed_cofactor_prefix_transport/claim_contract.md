# Claim contract - L1 fixed-cofactor prefix transport

## Inputs

- exact shell locator/cofactor data;
- codeword-shift invariance;
- monicity of agreement locators.

## Outputs

- forced cofactor degree `e=deg U-a`;
- one locator-prefix fiber for every fixed cofactor;
- exact top-shell equality with a locator-prefix fiber;
- a quantified `q^e` union cost.

## Consumer rule

Route `e=0` to locator Q exactly. For `e<k`, pass the `q^e` union and depth
`w+e` to `l1_cofactor_depth_budget_cancellation`; retain its ambient/image
normalization and integer-rounding guards. Do not call a possible cofactor
target occupied, and do not import a depth-`w` Q constant at depth `w+e`.
Then use `l1_cofactor_prefix_pade_graph_normal_form` to replace the target
union by its exact received-word graph before any collective count.

## Nonclaims

No locator-Q bound is proved. No useful estimate follows from `(FC5)` when
`e` grows. This node alone does not prove distinct prefix targets; the
follow-on Pade graph node does so for `e<k`. No full-image or graph-
intersection theorem is asserted here.

## Falsifier

An exact shell with `a>deg U`, a cofactor whose degree differs from
`deg U-a`, two locators for one fixed `Q` with different recursively forced
prefixes, or a scalar-cofactor locator in the prescribed prefix fiber that
has an extra domain agreement.
