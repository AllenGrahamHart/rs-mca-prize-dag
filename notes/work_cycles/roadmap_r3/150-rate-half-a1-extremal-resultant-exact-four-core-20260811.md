# Cycle 150: rate-half `A=1` extremal resultant exact four-core (2026-08-11)

Cycle 149 proves that positive-excess fibers contain all of their padded-
heavy factors. Inserting those factors into the Cycle-148 resultant removes
the entire `r_bad` allowance:

```text
R_QG=L_M^(e-2) E_circ
     [product_(all off-line delta)R_delta] W_4,
deg W_4<=4.
```

Here `E_circ=(X-x_circ)^(e-3)` for `d_A=0` and is one for `d_A=1`.

There are no remaining vertical common factors on a supported off-line
fiber: `gcd(B_delta,H_delta)=1`, so its complete common-root polynomial is
`A_delta R_delta`. Every extra local intersection multiplicity and every
common point over a center-line, unsupported, or projective-infinity fiber
is charged to the same four degrees. Actual-support roots are universally
transverse and contribute no excess.

Projectively the count is exact. Bezout gives
`I=(9e^2-23e+8)/2`, while the sum of the `n-a_delta` mandatory common-root
degrees over all `3e` off-line slopes is `I-4`. The residual effective
intersection cycle therefore has degree exactly four; the affine
resultant quotient can be smaller only when some of that cycle projects to
domain infinity.

## Burn-down

```text
result:                  PROVED extremal exact four-core
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer subtraction/tamper only
new assumptions:         none
```

The extremal branch is now reduced to a constant-size obstruction outside
ordinary supported-fiber root supply: classify the four-core or force five
excess/nonordinary intersection units.
