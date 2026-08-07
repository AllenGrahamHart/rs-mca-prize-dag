# Rate-half FPC5 `M=4,t=3` first-layout atom collapse

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`

Fix a received word after all earlier global owners, and choose the first
admissible maximal `M=4` source layout in the canonical source order. Then the
complete global rate-half `M=4,t=3` FPC5 class is bounded by

```text
4 + sum_(T,a) L_LS6(T,a),                             (AC1)
```

where:

- `4` pays the first layout's planted anchors;
- `T` ranges over the four touched-petal triples in this one layout;
- `a` ranges over the surviving integer defects
  `1<=a<=floor((b-3)/4)`;
- for each fixed triple `T`, its three fixed source labels determine one
  normalized cross-ratio `lambda_T notin {0,1}`;
- `L_LS6(T,a)` is exactly the guarded complement-divisor atom with that
  source, triple, defect, and `lambda_T`.

In particular, if every surviving fixed LS6 atom has size at most `B(n)`,
uniformly over its parameters, then the complete target satisfies

```text
#FPC5_(M=4,t=3) <=4n B(n)+4.                          (AC2)
```

There is no additional sum over maximal source layouts or field-many
cross-ratios.

## Scope

This theorem removes outer composition only. It does not bound one LS6 atom,
replace its split/exactness guards, or make a dimension-dependent per-atom
exponent uniform.
