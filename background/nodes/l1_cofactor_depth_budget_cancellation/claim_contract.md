# Claim contract - L1 cofactor-depth budget cancellation

## Inputs

- `l1_exact_shell_fixed_cofactor_prefix_transport`;
- the full degree-`a` split-locator slice and its depth-`d` prefix image;
- optional ambient- or image-normalized max-fiber constants.

## Outputs

- exact cancellation of the `q^e` cofactor count against `e` extra ambient
  prefix coordinates for `0<=e<k`;
- the exact effective-image penalty `q^d/L_(a,d)` under image normalization;
- the integer ceiling loss `<q^e`;
- the deployed-row route fence: raw per-cofactor union first becomes
  insufficient at `e=2` for KoalaBear and `e=1` for Mersenne-31.

## Consumer rule

Consume `(CD3)` only with a locator-prefix theorem covering the actual degree
`a`, depth `w+e`, field, residual owner convention, and constant.  If the
theorem is image-normalized, retain `q^d/L_(a,d)` or prove a full-image
certificate.  After the sparse-image threshold, count occupied cofactor
targets collectively through `l1_cofactor_prefix_pade_graph_normal_form`;
do not replace possible targets by occupied targets.

## Nonclaims

No deeper-depth locator-Q theorem is proved.  Upstream row-sharp Q at depth
`w` is not promoted to depth `w+e`.  F2 ladder/tower transfer is not such a
promotion.  No shell with `e>=k` is paid.  A failed raw-union budget is not a
counterexample to L1, and no divisor/Pade-section transversality is proved.
The all-cofactor section node supplies an exact representation above the cap,
not the missing payment.

## Falsifier

A valid exact shell violating `(CD1)`, a missing full-image factor in `(CD5)`,
an integer ceiling loss at least `q^e`, or a deployed-row integer comparison
opposite to the printed fence.
