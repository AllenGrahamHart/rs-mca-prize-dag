# Attack plan

## Certificate interface

A proposed proof or computation must emit, for each official cell family:

1. the complete cell descriptor and generated field;
2. the exact integer `B*` and every paid-column subtraction defining
   `B_chal`;
3. an independently checkable upper certificate for the actual challenger
   set;
4. a soundness proof that the certificate covers every layout, scalar choice,
   and received word in the descriptor.

A symbolic rank route remains available, but it must define its matrix and
prove how rank bounds `N_chal`; naming the output `K_cell` is not sufficient.

## Falsification

An exact official cell with `N_chal>B_chal` falsifies the direct claim. Toy
cells and small-field windows remain evidence unless a proved transport maps
their normalized excess into an official cell. The existing F7 data support
the qualitative `q^-sigma` model but do not certify an official sup bound.

