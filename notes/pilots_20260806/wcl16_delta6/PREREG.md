# WCL `(1,6)` rational unit-lift pricing pilot - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_6_emptiness`
- **proved supplier:**
  `dli_wcl_ell1_weight6_even_norm_divisor_descent`
- **route:** compute the six coefficients of
  `Y^256 mod (E(Y)^2-YB(Y)^2)-1`, then ask Singular for a rational standard
  basis and its transformation matrix.

## Decision

Price the exact integer-certificate route before attempting the direct
`185,569,028`-class `(1,6)` census.  The supplier proves that the six
coefficient polynomials generate the unit ideal over `Q`; the unresolved
object is an explicit rational lift which can be cleared to

```text
Delta_6 = H_0 R_0 + ... + H_5 R_5,    Delta_6 != 0.
```

One bounded Singular process will:

1. construct the monic degree-six modulus and its exact repeated-squaring
   remainder over `Q`;
2. check that all six generic remainder coefficients are present;
3. run `liftstd` on those coefficients;
4. identify a unit basis column and verify
   `matrix(J)=matrix(I)T` exactly inside Singular; and
5. report term/degree counts for the remainder ideal and transformation
   matrix.

The run deliberately does not serialize the lift matrix.  Serialization and
denominator clearing are authorized only if this pilot completes and reports
a tractable matrix envelope.  A timeout is a route-pricing result, not
evidence for or against slot emptiness.  A completed unit lift is still not a
node closure: the rational certificate must be exported, independently
replayed, cleared to a nonzero integer, completely factored, and every prime
divisor checked against the official ambient gate.

## Predictions

**P1.** Repeated squaring completes and produces six nonzero coefficient
polynomials.

**P2.** `liftstd` returns a one-element unit basis and an exact transformation
column within the cap.

**P3.** The transformation identity replays exactly.  If P2 fails by timeout,
the partial log will distinguish remainder construction from standard-basis
elimination and will end this representation unless a materially smaller
elimination is found.

## Resource ceiling

One Modal container, two CPUs, 4 GiB RAM, a 90-second function timeout, and a
60-second Singular subprocess timeout.  No retries, no parallel workers, no
volume, and no direct relation census.  The image installs Singular with
`--no-install-recommends` to avoid the dependency explosion observed in the
retired `(1,5)` packaging attempt.  Expected cost is below `$0.05` and the
conservative ceiling is `$0.15`.

```text
./tools/ramguard modal -- modal run \
  notes/pilots_20260806/wcl16_delta6/delta6_lift_pricing_modal.py
```

## Promotion rule

- `COMPLETE_UNIT`: authorize one separately preregistered artifact extraction
  only if the reported term counts are tractable.
- `TIMEOUT_REMAINDER`: abandon this expanded-remainder representation.
- `TIMEOUT_LIFT`: retain the proved divisor endpoint but seek a modular or
  structured elimination before spending more compute.
- `COMPLETE_NONUNIT` or an identity failure: treat as an implementation or
  supplier-audit alarm; do not promote the target.
