# PMA rate-half two-petal support-fiber reduction

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **role:** eliminate contributor polynomials from the normalized rate-half tail

## Statement

Use the normalized labels `(0,1,lambda)` and numerator factorization from
`pma_ratehalf_source_crossratio_fiber_reduction`:

```text
P_2=L_1L_3R_2,       P_3=L_1L_2R_3,
deg R_2,deg R_3<ell.
```

Put

```text
F_lambda=L_3R_2+lambda L_2R_3.                      (SF1)
```

For an `m`-subset `S` of the core, let `L_S` be its monic locator. In the
quotient rings modulo `L_2` and `L_3`, define

```text
V_S = rem_(L_2)(L_3R_2 L_S^(-1)),
Phi(S)=rem_(L_3)(L_S V_S (L_2R_3)^(-1)).            (SF2)
```

All inverses exist. The exact degree-`<K_0` contributors in the fixed
normalized three-petal cell are in bijection with the subsets `S` satisfying

```text
deg V_S<=ell-a,                                     (SF3)
Phi(S)=lambda as a constant polynomial,             (SF4)
gcd(V_S,L_C/L_S)=1.                                 (SF5)
```

The contributor associated to such an `S` is

```text
H_S=(L_SV_S-F_lambda)/(L_2L_3),
P_S=L_1L_SV_S.                                      (SF6)
```

It has degree `deg H_S<=K_0-1`, the planted values on all three petals, and
exact core agreement set `S`. Conversely every exact contributor gives
(SF2)--(SF6).

Therefore the fixed-cell list size is exactly the guarded fiber size

```text
#{S subset C:|S|=m, (SF3), (SF5), Phi(S)=lambda}.   (SF7)
```

Any fourth-petal, first-match, or earlier-owner condition only removes members
from this fiber. If every tail fiber has size at most two, the complete
three-petal tail contributes at most `8n` codewords per carried source.

## Scope

This theorem does not bound (SF7). It identifies the precise support map that
a counting, image-flatness, or natural-scale owner theorem must control. A raw
fiber of `Phi` without the degree and exactness guards is an auxiliary
superset, not the exact PMA cell.
