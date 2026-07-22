# list_adjacency_closing conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `list_crossing_localization`
- `list_unsafe`
- `list_safe`
- `list_corridor_ledger`
- `rate_half_cyclic_rotated_prefix_floor`
- `rate_half_list_adjacent_crossing`

Evidence only:

- `list_planted_arithmetic`
- `worst_word_planted`
- `rate_half_coverage_gap`

## Claim

Conditional on the predicate nodes, every admissible ordinary code has
adjacent agreement indices `a0,a0+1` satisfying

```text
L_1(a0) > floor(|F|/2^128) >= L_1(a0+1).
```

## Clean rates

For rates `1/4`, `1/8`, and `1/16`, `list_unsafe` supplies an explicit
received word below the list window.  Its qcore construction is a lower
witness only; no upper classification of all planted receivers is needed.

`list_safe` supplies the uniform upper bound above the window from `imgfib`
and `codegree`.  The proved `list_corridor_ledger` shows, by exact arithmetic
at all three rates, that the available floor gain covers `W_list-1` grid
steps.  Hence the lower and upper endpoints collapse to adjacent agreement
indices.  `list_crossing_localization` turns that bracket into the unique
first integer crossing.

This argument does not consume `ww_row_envelope_clause`. W3's literal
safe-side claim remains open. The fiber-layout counterexample instead proves
that its upper inequality cannot be extended to the already unsafe lower
endpoint.

## Rate one half

`rate_half_cyclic_rotated_prefix_floor` supplies the optimized unsafe side.
`rate_half_list_adjacent_crossing` is the explicit safe-side and exact
crossing predicate for budgets `B*>=3`; the low-budget `B* in {1,2}` branches
are already proved by their dedicated exact certificates.  Thus the live
rate-half residue is precisely the named adjacent-crossing target, not W3.

## Arity

The proved `list_large_m_scope_closure` is deliberately outside this packet.
It consumes the ordinary crossing and transports the same adjacent pair to
every constant interleaving arity.

## Historical correction

The former packet required `list_planted_arithmetic`, which transitively
required the W3 upper envelope. That was stronger than the consumer needed:
an unsafe-side proof needs one witness, while its safe upper bound comes from
`list_safe`. The exact fiber-layout counterexample exposed this polarity
error at the unsafe endpoint. Replacing the unnecessary chain by the already
existing `list_unsafe` and `list_safe` predicates is a dependency repair, not
a new conjecture or a proof/refutation of safe-side W3.
