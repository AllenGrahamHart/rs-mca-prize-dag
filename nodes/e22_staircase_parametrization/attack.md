# ATTACK - e22_staircase_parametrization

Status: conditional. Use the n=16 exact profiles as calibration, not as
proof.

The proved `e22_tail_coset_locator_algebra` packet handles the forward
locator algebra. The remaining target is
`e22_agreement_coset_support_forcing`: start from a structured challenger
with at least two touched petals and write its agreement equations as equality
of locator cofactors. The expected output is a canonical datum:

```text
tail/core defect B + quotient modulus M + selected full cosets + scalar data
```

which reconstructs the codeword as a local `L_B G(X^M)`-type locator.

Do not promote from toy profile matching alone; the deliverable is a
surjective parametrization in the local notation.
