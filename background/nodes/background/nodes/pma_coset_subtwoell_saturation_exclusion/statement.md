# PMA constant-shift-pencil sub-two-ell saturation exclusion

- **status:** PROVED
- **role:** sharp low-defect full-petal common-locator-pencil exclusion
- **consumer:** evidential input to `petal_mixed_amplification`

## Statement

Let `K` be a field, let `P in K[X]` be monic of degree `ell>=1`, and let
`t>=3`. Fix distinct `a_1,...,a_t in K` and scalars
`c_1,...,c_t in K`. Suppose
`F,W in K[X]` satisfy

```text
ell<d=deg F<2ell,       deg W<=d,       gcd(F,W)=1,
P-a_i divides W-c_i F                     for every i.
```

Then no such pair `(F,W)` exists.

Consequently, an exact non-planted saturated full-petal constant-shift
locator-pencil chart has no contributor with

```text
t>=3,       ell<d<2ell.
```

The result is field-uniform and does not require separability of `P-a_i`.
The distinct constants make these petal locators pairwise coprime over every
characteristic. A multiplicative-coset chart is the special case
`P=X^ell`.

## Sharp Scope

Both strict boundaries are necessary.

- At `t=2`, there is a saturated example over `F_7` with `ell=2`, `d=3`.
- At `d=2ell`, the pair

  ```text
  F=X^(2ell)+1,       W=X^ell
  ```

  over `F_7`, with quotient labels `a_i=1,2,3` and values
  `c_i=4,6,1`, is saturated and satisfies all three petal congruences.

The theorem does not cover partial petals, arbitrary locator families outside
one constant-shift pencil, or defects `d>=2ell`. A PMA consumer must
separately prove that its carried below-band source has locators `P-a_i` for
one common `P`; the current G1 atlas supplies the coset instance only for
top-band contributors.
