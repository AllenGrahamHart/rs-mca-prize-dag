# Proximity Prize Partial Dossier

Status: gate-checked partial result. This is not a full prize resolution.

Date: 2026-07-12.

## Certified Row

Let

```text
C = RS[F_(17^32), H, 256],  |H|=512,
epsilon*=2^-128,
slope sampler=finite affine slopes over F_(17^32).
```

The subgroup is generating because `ord_512(17)=32`. The finite-slope
denominator is `Q=17^32`, and exact arithmetic gives

```text
B*=floor(Q/2^128)=6,
6*2^128 < 17^32 < 7*2^128.
```

In the exact high-agreement tangent range,

```text
LD_sw(C,506)=7 > B*=6 >= LD_sw(C,507)=6.
```

Thus agreement `507` is the first safe agreement. The largest safe closed
integer-grid radius is `5/512`. The real closed-ball boundary supremum is
`6/512=3/256` and is not attained.

## Envelope Family

The cited high-agreement tangent theorem has exact numerator
`B_fin(a)=n-a+1` under its printed range hypothesis `3a-2n>=k`. For the row
above this range begins at `a=427`, so both adjacent cells are inside it. This
is a reusable exact high-agreement envelope, not a theorem about the lower
agreement capacity band.

## Convention Freeze

The S0 inventory is closed by `s0_zero_open`. Its component ledger resolves
object identity and batching, list/interleaving arity, predicate semantics,
sampler and denominator, generated-field normalization, endpoint convention,
and dimension dither by equality or an explicit bridge. The compiler schema
requires proved `object_identity`, `field_scope`, `denominator`, and `endpoint`
axes before emitting prize-facing output.

## Reproducibility

- Exact compiler: `tools/prize_certificate_compiler.py`.
- Compiler audit: `python3 background/nodes/compiler/audit.py`.
- Verifier manifest audit: `python3 background/nodes/harness/audit.py`.
- Tier-1 Lean audit: `python3 background/nodes/lean_tier1/audit.py`.
- Low-memory Lean replay: `lake -Kjobs=1 build` in
  `formal/lean/rs_mca_formalization`.
- Lean theorem map: `formal/lean/rs_mca_formalization/CERTIFICATION_MAP.md`.

## Proof Classification

The adjacent finite-row arithmetic is Lean-certified. The tangent numerator
identity and row pin are cited/proved project results and independently
compiler-checked. The Lean package's typed analytic targets are non-claims;
the certification map is not a blanket formal proof of Reed-Solomon or MCA
semantics.

## Non-Claims

This dossier does not claim:

- the grand MCA challenge for every admissible row;
- the grand list/interleaved-list challenge;
- any exact clean-rate capacity-band crossing;
- the rate-`1/2` razor-band closure;
- closure of any node listed in `PARTIAL_DOSSIER_MANIFEST.json` under
  `open_truth_leaves`.

The partial result is deliberately useful on its own: it gives one exact,
adjacent, convention-complete row and a reproducible template for later row
certificates, while preserving every unresolved mathematical obligation.
