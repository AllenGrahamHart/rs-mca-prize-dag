# Claim contract

| field | value |
|---|---|
| claim | The exact packed `p`-tuple profile `(UE1)` and the uniform official envelope `(UE2)`. |
| inputs | Fiber cap `ell`, the common-ray `m+1` owner cap, and the proved official `ell=1` endpoints. |
| output | A single linear inequality in `d,ell` that pays a higher-`ell` next-dimensional region. |
| load-bearing hypotheses | Positive capped fiber multiplicities, full affine dimension `s`, at least two selected blocks, and positivity of the tuple factors. |
| falsifier | A capped profile below `(UE1)` or an official tuple satisfying `(UE2)` whose exact cap exceeds the local budget. |
| nonclaim | `(UE2)` is not asserted to be the maximal paid higher-`ell` region. |
