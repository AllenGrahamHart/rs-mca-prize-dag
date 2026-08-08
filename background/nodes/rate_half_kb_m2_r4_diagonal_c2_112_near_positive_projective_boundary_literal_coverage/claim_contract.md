# Claim contract

| field | contract |
|---|---|
| literal assignments | `F00--F07`, `M00--M03` |
| literal target roots | `A`, `TA`, `OB`, `OI` |
| census | `12*4=48` disjoint cells: `32` fixed-moving and `16` moving-moving |
| boundary chart | `q_hom=Y(T-dY)`, `w=0` |
| reconstruction | direct literal `5 x 5` solve; no endpoint normalization transport |
| necessary gate | projective q-slice `(KBLB-3) ~ (KBLB-4)` |
| complete chart | all label collisions, reconstruction/internal determinants, degree, and rational denominators localized |
| certificates | 48 one-step Rabinowitsch unit ideals and 48 sequential-saturation unit ideals |
| conclusion | positive projective-boundary literal residual is empty |
| nonclaim | no aligned-negative or near-negative literal coverage |

## Falsifier

A missed semantic cell, a failed reconstruction or projective-degree control,
or any nonunit complete-chart ideal.
