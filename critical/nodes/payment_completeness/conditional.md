# payment_completeness conditional proof

- **status:** CONDITIONAL
- **closure:** proof from any complete classification route

## Predicate routes

The node has `gate: any`. One complete route suffices:

- `xr_crystallization`
- `spi_exceptional_class`
- `es_regularity`
- `monodromy_realization`

Evidence only:

- `redteam_multiscale`
- `isotypic`
- `dihedral_quotient_stratum`
- `rigidity_kernel`
- `f_dih_subgroup_completeness`

## Claim

If any predicate route gives a complete classification of the relevant
alignment/payment objects, then the ledger taxonomy is exhaustive.

## Proof

Payment completeness is not an empirical assumption. It is the output of a
complete classification: every object contributing to the ledger must appear
in exactly one classified branch, or the classification must emit a new branch
that is then routed through the S9 protocol.

Each `alt` route is stated as such a complete classification route:

- `xr_crystallization` classifies the inverse class `C_XR`;
- `spi_exceptional_class` classifies the component/exception list;
- `es_regularity` classifies the regularity-lemma exceptional sets;
- `monodromy_realization` classifies via the monodromy subgroup route.

Because the node is `gate: any`, completion of any one route supplies an
exhaustive list by construction. Once that list is matched to ledger charges,
there is no remaining unclassified payment mechanism in the route's scope.

The evidence nodes are useful red-team pressure and have already refined the
taxonomy, but they are not used as proof of exhaustiveness.
