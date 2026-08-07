# Attack surface

1. Freeze the row set and priority order.
2. Give each column an actual set of list members, not a generator count or
   slope count.
3. Derive each integer bound with its coalescing and multiplicity factors.
4. Evaluate the exact floor `B*`; do not replace it by a logarithmic margin.
5. Include all quotient rows reached by `tr_perleaf_list_ident` or narrow
   that consumer explicitly.
6. Mutation-test ownership, the additive base member, the strict-to-nonstrict
   `u1` conversion, and the binding row.
