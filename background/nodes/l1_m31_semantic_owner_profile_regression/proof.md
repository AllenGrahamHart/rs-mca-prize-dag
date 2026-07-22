# Proof

## Deployed profile compilers

The deployed constants give

```text
n-a+=981129,       floor(n/(n-a+))=2.               (1)
```

For the near-rational branch, the input certificate already contains a
duplicate-free line-local slope list of length at most one. Equipping that
list with numerator `1` and slope denominator `p` proves its exact profile
bound. For the primitive one-pencil branch, the source incidence theorem is
represented by a certificate whose duplicate-free slope list has length at
most the quotient in `(1)`. Equipping it with numerator `2` and denominator
`p` proves the second exact profile bound.

The calibrated natural profile has denominator `p^w` and supplied audited
average ceiling `Abar=1993678`, hence natural numerator `1+Abar=1993679`.
Both exact numerators are at most this value and at most `p`. This proves the
two compilation statements while retaining the two denominators as distinct
typed fields. Notice that the constructors consume certified lists; they do
not produce or exhaust those lists.

## Semantic finite regression

The verifier reconstructs the order-twenty domain `D_i=235^i` in `F_241`.
For each of the eleven displayed records it checks:

1. the support is a duplicate-free ten-subset of the domain and has prefix
   `(92,135)`;
2. the stored degree-`<8` polynomial `h` satisfies
   `h(x)=u0(x)+gamma*u1(x)` at every support point;
3. the stored parity row annihilates `1,x,...,x^7` but not `u1`; and
4. the stored nonzero scale converts the normalized projective ray to the
   polynomial coefficient vector.

The parity condition proves that `u1` restricted to the support is not a
degree-`<8` codeword. Consequently every record is a genuine noncommon
explanation on the same received line, not merely a support with convenient
locator coefficients. The verifier also checks that all slopes and all
normalized rays are distinct.

Let `L_A,L_B` be the printed degree-ten support locators for explanation
indices `0` and `2`. Direct evaluation proves that their root sets are the
two selected supports and that their exact common root set is `{0,1,15}`.
After deleting that core, enumerate all `242` projective pencil parameters,
using `L_A+lambda L_B` for finite `lambda` and `L_B` at infinity. Exactly
`lambda=0` and infinity have at least seven moving domain roots. Their
semantic slopes are exactly `115` and `22`, so they form a genuine two-slope
earlier-owner profile.

The ten listed shell explanations are all at exchange distance six from the
anchor. Removing exactly indices `0` and `2` leaves eight states. Finally,

```text
binom(10,6)^2=44100,
241^2(8-3)=290405,
7*44100=308700,
308700-290405=18295.
```

This proves the residual `3+7` inequality and the claimed margin. QED.
