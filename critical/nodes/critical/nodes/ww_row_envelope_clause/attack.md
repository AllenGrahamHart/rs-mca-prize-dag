# Attack plan

## Certificate interface

A proposed proof or computation must emit, for each official cell family:

1. the complete cell descriptor and generated field;
2. an ordered ownership descriptor covering every paid column and residual
   cell, with a proof that the resulting first-match classes are disjoint;
3. the exact integer `B*` and every disjoint paid-column subtraction defining
   the single per-word residual `B_chal(U)`;
4. residual first-match cell allocations `b_c(U)` whose sum is at most `B_chal(U)`,
   with an independently checkable upper certificate
   `N_chal^o(U,c)<=b_c(U)` for every cell;
5. a soundness proof that the certificate covers every layout, scalar choice,
   and received word in the descriptor.

A symbolic rank route remains available, but it must define its matrix and
prove how rank bounds `N_chal`; naming the output `K_cell` is not sufficient.

## Falsification

An exact official word with `sum_c N_chal^o(U,c)>B_chal(U)` falsifies the
direct claim. One cell with `N_chal^o(U,c)>B_chal(U)` is a sufficient special
case. Toy cells and small-field windows remain evidence unless a proved
transport maps their normalized excess into an official row. The existing F7
data support the qualitative `q^-sigma` model but do not certify an official
sup bound.

A purported falsifier must apply the same ordered ownership map as the paid
ledger. Counting a quotient/staircase word both in `P_paid` and in a residual
challenger cell is a bookkeeping error, not a falsification.
