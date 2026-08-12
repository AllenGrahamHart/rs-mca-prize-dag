# `A=1` collision ordinary-quadratic torus-gcd exclusion

- **status:** PROVED
- **closure:** bidegree-`(2,3)` companions and collision shapes B/D are empty
- **consumer:** `rate_half_band_crossing_location`

Retain the official first residual row and the notation of the
ordinary-quadratic subgroup-coincidence router:

```text
N=2^41,              H=mu_N subset F_P^*,
F=2^39-6,            P>2^167.                       (TGE1)
```

No bidegree-`(2,3)` ordinary companion can occur in collision shape B or D.
Indeed, every dense off-diagonal coincidence component supplied by the
router is either

1. an `S_3` component of bidegree at most `(4,4)` with at least `3F`
   distinct points of `H^2`; or
2. a cyclic orientation component of bidegree at most `(2,2)` with at
   least `3F/2` distinct points of `H^2`.

The Corvaja--Zannier positive-characteristic gcd theorem excludes every
such component that is not a translate of a one-dimensional subtorus. The
translated-subtorus case is incompatible with the degree-three `S_3/C_3`
fiber geometry. Therefore the quadratic companion is impossible.

The four-shape classification consequently reduces to

```text
A. one large factor of parameter degree e-2;
C. one large factor of parameter degree e-6 plus one (4,6) companion.
                                                            (TGE2)
```

Thus only A and C remain in this collision arm.

## Scope

This theorem does not exclude shape A or the bidegree-`(4,6)` companion in
shape C. It is confined to the official prime-field row and does not assert
an extension-field analogue.
