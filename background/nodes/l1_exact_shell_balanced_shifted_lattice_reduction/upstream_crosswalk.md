# Upstream crosswalk - exact L1 shells and the balanced split pencil

## Imported normal form

Paper D v13.2's shifted lattice `M_U`, near-rational dichotomy, automatic
divisibility lemma, and two-generator split-pencil reduction apply verbatim
to the unguarded Pade/support census.

## New exact-shell consequence

In the active band, the near-rational branch has one codeword with at least
`m+1` agreements.  It can contribute `binom(n-d_1,m)` support witnesses but
zero codewords to the complete agreement shell at level `m`.  The L1 gcd
guard removes this branch exactly.  Every nonempty exact shell therefore
lies in the balanced profile `w+1<=d_1<=d_2<=omega`.

## Remaining active input

For L1 the object-level interior statement is now the guarded balanced
two-generator split-pencil census.  Apply
`l1_interior_bc_floor_higher_shell_q_routing` first: the realized base-field
discrete support floor is higher-shell Q mass, while the soft raw-census
model is not an unavoidable exact-BC baseline.  To consume an upstream certificate, the surviving
`BC_exact_guarded` numerator, quotient/prefix priority, local primitive
shift-pair term, and summed row reserve still need an exact integer crosswalk.
