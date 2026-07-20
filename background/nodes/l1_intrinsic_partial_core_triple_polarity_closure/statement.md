# L1 intrinsic partial-core triple-polarity closure

- **status:** PROVED
- **role:** globally close bounded-polarity intrinsic quotient charts with
  arbitrary source cores
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix an intrinsic quotient partition of a length-`n` domain into `L=n/ell`
complete fibers `T_a` of size `ell`. Let a canonical source chart have an
arbitrary `(k-1)`-point core `C`, full petals chosen among fibers disjoint from
`C`, and source members determined by the received word. For an exact defect
set `D subset C` and exact petal supports `S_i`, put

```text
p_layout=sum_a min(|C intersect T_a|,
                    ell-|C intersect T_a|),

p_defect=sum_a min(|D intersect T_a|,
                    |C intersect T_a|-|D intersect T_a|),

p_petal=sum_i min(|S_i|,ell-|S_i|).                  (TP1)
```

Assume fixed caps and the L1 cutoff

```text
p_layout<=R_0,       p_defect<=B_0,       p_petal<=P_0,
ell>=c_0 n/log_2 n,       ell>2P_0,       q<=n^gamma. (TP2)
```

Across all canonical source charts at this intrinsic scale, every common-
pencil contributor in every degree strip is counted by at most

```text
(R_0+1)(B_0+1)(P_0+1)
  16^L n^(R_0+B_0+P_0) q^(2P_0).                    (TP3)
```

Across all intrinsic dyadic scales the total is at most

```text
(log_2 n+1)(R_0+1)(B_0+1)(P_0+1)
n^(4/c_0+R_0+B_0+P_0+2 gamma P_0),                  (TP4)
```

and is therefore polynomial. Thus an intrinsic-quotient common-pencil
counterfamily must have at least one of `p_layout,p_defect,p_petal` escape
every fixed cap.

## Scope

The theorem allows partial source cores but requires the petals to be full
fibers of an intrinsic quotient partition. It does not treat
contributor-dependent/non-intrinsic quotient maps, arbitrary petal locators,
or source structures not encoded by one of the intrinsic dyadic partitions.

