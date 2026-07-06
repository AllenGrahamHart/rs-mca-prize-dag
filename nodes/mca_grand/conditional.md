# conditional proof: mca_grand

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `s0_zero_open`
- `mca_safe`
- `mca_unsafe`
- `mixed_radix_frontier`
- `adjacency_closing`

Evidence/support:

- `second_pin_or_wall`
- `ld_bridge`

## Claim

Conditional on the predicate nodes, for each admissible code row there is an
agreement index `a` such that

```text
B_C(a - 1) > floor(q_line / 2^128) >= B_C(a).
```

## Proof

`s0_zero_open` and `mixed_radix_frontier` fix the object and row conventions:
the row being certified is one of the admissible smooth-domain rows, with no
silent axis mismatch.

`mca_safe` supplies the safe-side inequality at the certified agreement
index `a`.  `mca_unsafe` supplies the unsafe witness inequality at the lower
agreement index.  `adjacency_closing` supplies the final missing assertion
that these two certified indices are adjacent for every admissible row.  The
rate-`1/2` residual band is included only through the strong
`rate_half_band_closure` premise inside the safe/adjacency chain.

Together these predicates are exactly the displayed adjacent crossing.  The
evidence edges support convention transfer and second-pin diagnostics, but are
not additional logical premises of this root assembly.

## Stress evidence

The lightweight command

```text
python3 tools/conjectural_mca_delta.py --self-test
```

checks the banked `n = 2^41, log2(q) = 255.9` corridor table and verifies that
the computed `a*` is safe while `a* - 1` is unsafe at all four official rates.
This is a self-consistency check of the arithmetic used by the assembly, not a
proof of the remaining red premises.
