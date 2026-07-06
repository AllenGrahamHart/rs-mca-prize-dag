# proof status: DLI exact reduction plus weighted-average open obligation

## Lemma 1 — exact counting identity (PROVED, orthogonality; VERIFIED)

For a central level profile `M`,

```text
rho_j(M) = q^{L_j} |Z_j(M)| / U_j(M),
```

where `Z_j(M) = {d in prod_y D_y : A d = 0}` and `A` is the
`L_j x |Y|` odd-evaluation matrix.  The proof is additive-character
orthogonality: the inner frequency sum collapses to the indicator `1_{Ad=0}`.
This identity is banked and agrees with the exact harness values.

## Refuted stronger route

The earlier pointwise/sup flatness premise is false.  A low-mass full-rank
ternary profile can have only the zero skew in `Z_j`, giving
`rho_j = q^{L_j}/3^m`; when `m` is too small relative to `L_j log_3(q)`, this is
`q^{Omega(L_j)}` even though there is no rank defect.  The 2026-07-06
`dli_weighted_res_probe.py` reproduces this exactly at `n=16,L=4,m=8`
and `n=32,L=4,m=12`.

## Remaining obligation

The live target is therefore weaker and sharper: prove the primitive-core
`U`-weighted aggregate bound directly.  The RES/resultant-survivor set may be
large on low-mass profiles, but those profiles must be paid for by their small
profile weight in the actual central-profile sum.

The same 2026-07-06 exact probe supports this weakening locally: for ternary
active counts `m=16,20,24` in the `L=4` cells, the measured exponents drop to
`0.6599218293814246`, `-0.1750977132732192`, and `0.006826159202134505`,
respectively, with no unexpected large-active alarm.  This is not a proof of the
weighted aggregate theorem; it records that the repaired premise survived the
small exact falsification pass.
