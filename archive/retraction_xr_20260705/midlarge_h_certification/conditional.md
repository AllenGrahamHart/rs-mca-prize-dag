# midlarge_h_certification conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `star_pte_support_bound`
- `midlarge_partner_cap_reduction`
- `midlarge_h7_20`
- `midlarge_h20_A`

Evidence/route notes:

- `m1_trade_bijection`
- `m2_antinorm_lever`

## Claim

Conditional on the predicate nodes, the widened mid/large-`h` certification
gap is covered for all `h in (6, A]`.

## Proof

`star_pte_support_bound` proves that the relevant trade support parameter is
`h`, not `2h`, and that the live upper endpoint is

```text
H_max = A in {67, 133, 261}
```

depending on the rate. Thus the widened gap is the finite interval
`h in (6, A]`, after the low-`h` direct/descent certificates.

`midlarge_partner_cap_reduction` reduces the trade-count certification in this
range to an active-core count: once active cores at a fixed `h` are bounded by
the recorded per-`h` budget, the partner cap gives the required total trade
bound.

The remaining interval splits at `h = 20`:

- `midlarge_h7_20` supplies the active-core bound for `h = 7,...,20`;
- `midlarge_h20_A` supplies the active-core bound for `h in (20,A]`.

These two bands cover exactly `h in (6,A]`. Applying the partner-cap reduction
on each `h` gives the desired mid/large-`h` certification.

The evidence nodes explain why earlier routes do not by themselves close the
gap: `m1_trade_bijection` is a reparametrization rather than a bound, while
`m2_antinorm_lever` remains a possible row-specific lever.
