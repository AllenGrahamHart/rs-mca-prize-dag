# Claim contract - L1 boundary shifted-lattice affine Q cell

## Inputs

- the exact-shell balanced shifted-lattice reduction;
- boundary degrees `(d_1,d_2)=(w+1,omega)`;
- monic/projective normalization and complete-agreement uniqueness.

## Outputs

- exact projective split `B=0` versus `B!=0`;
- at most one complete codeword from the point at infinity;
- one affine Q cell `g_2+A g_1` with `deg A<=omega-w-1`;
- injective affine parameterization of valid supports;
- exact locator-Q specialization when `W_1=1`.

## Consumer rule

Assign `d_1=w+1` to Q, not BC.  Pay the `B=0` ray by at most one exact
codeword, and retain the guarded affine cell as the boundary Q obligation.
Only profiles `d_1>=w+2` enter the interior BC sum.

## Nonclaims

No Q flatness, base-field owner classification, quotient coalescing, or
finite adjacent-row bound is proved.  A nonconstant `W_1` is not silently
identified with the fixed-column locator-Q atom.

## Falsifier

A boundary element outside `(BQ2)`, two complete codewords on the infinity
ray, duplicate valid affine parameters, a `W_1=1` member not characterized by
the prescribed top coefficients, or an interior profile assigned to Q by
this theorem.
