# Audit

## Scope

Repeated colors are counted on the actual distinct roots of `P_s`, not in an
ambient quadratic fiber. A quadratic fiber has at most two roots, so every
repeat is one pair and all repeated pairs have the same center `S=-B/A`.

The proof does not assume that a color lies in `F_p`. It uses
`x^p=E_s(x)/x`, which follows directly from the definition of the color.
The nonzero-center argument requires two distinct repeated colors; it makes
no claim about zero or one repeat.

## Affine transport

The affine rigidity is derived from the weighted-derivative identity for
`P_s`, not from an identification between unrelated locator and codeword
ranks. The only two affine transports are the identity and reflection. The
reflection is tested against the original cyclotomic condition through
`P_s | [W(1-W)]^m-1`.

## Exact arithmetic

The two reflection remainder coefficients and the `m=8` pseudo-remainder
coefficient are polynomial identities over the rationals. Their denominators
have no official prime factor. The primary verifier reconstructs them by
symbolic polynomial arithmetic using only the standard library; the audit
verifier independently specializes at more points than their degree bounds.

## Nonclaims

At most one repeated color is not emptiness. The collision-free and
single-collision quadratic systems remain to be combined with the exact
Frobenius resultant, cyclotomic divisibility, and inner lift. The `m=16`
even quadratic multi-collision branch is retained explicitly.
