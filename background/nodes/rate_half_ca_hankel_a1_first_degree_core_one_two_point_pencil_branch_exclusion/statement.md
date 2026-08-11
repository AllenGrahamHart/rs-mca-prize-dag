# `A=1` core-one two-point pencil-branch exclusion

- **status:** PROVED
- **closure:** local fibre-algebra modification directions
- **consumer:** `rate_half_band_crossing_location`

In the first core-one packet, the PENCIL splitting from `(TPD4)` is
impossible. The two-point pushforward necessarily has

```text
pi_*O_C(P_alpha+P_beta)
 =O direct_sum O(1-d)^2 direct_sum O(-d)^(e-3),       (PBE1)
```

and hence

```text
h^0(C,O_C(P_alpha+P_beta))=1.                         (PBE2)
```

The reason is intrinsic to the nonreduced vertical fibre. At `x_*` its
algebra has two double local factors, at `alpha,beta`, and `e-4` other
reduced factors. The two positive-modification directions are the nilpotent
classes in those two double factors. Their span vanishes on every other
factor, whereas the constant direction does not. Thus their projection to
the negative block has rank two, forcing the CANONICAL splitting.

## Scope

This eliminates the pencil branch but not the unique-section packet in
`(PBE1)`.
