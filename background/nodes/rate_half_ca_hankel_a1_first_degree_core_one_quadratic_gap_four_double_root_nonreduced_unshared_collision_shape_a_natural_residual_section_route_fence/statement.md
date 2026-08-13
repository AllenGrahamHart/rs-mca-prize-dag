# `A=1` collision shape-A natural residual-section route fence

- **status:** PROVED
- **closure:** the Pade section is canonical and raw first jets do not descend
- **consumer:** `rate_half_band_crossing_location`

Retain shape A. On the normalized locator curve `C`, let `D_mand` be the
mandatory actual-support and padding intersection divisor removed in the
exact four-core. The residual line bundle is

```text
L_res=O_C(G)(-D_mand)=O_C(2B),
h^0(C,L_res)=1.                                    (NSF1)
```

The nonzero residual restriction of `G` spans this section space. The Pade
numerator does not give a second section: after its fixed infinity and
center factors are normalized, the syzygy

```text
Q B_source-Lambda G=L_U0 P_F                       (NSF2)
```

identifies its restriction on `Q=0` with the same residual section.

Nor do the raw first derivatives descend. On every pure split fiber
`t=delta` and every one of its `n=(3e-7)/2` actual-support roots `x`,

```text
G_t(delta,x)!=0,       G_X(delta,x)!=0.             (NSF3)
```

These points occur in `D_mand` with multiplicity one. Hence neither raw
derivative vanishes along `D_mand`; dividing it by the mandatory divisor
produces poles rather than a section of `L_res`.

## Scope

This fences only the automatic candidates `G`, `P_F`, `G_t`, and `G_X`.
It does not exclude a new source combination engineered to recover every
mandatory zero. Such a combination would be a genuinely new theorem and,
if independent, would contradict `(NSF1)` and close shape A.
