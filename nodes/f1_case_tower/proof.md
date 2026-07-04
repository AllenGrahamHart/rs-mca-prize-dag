# proof: f1_case_tower (assembly over proved pieces; maintainer-written)
Case (iii): a bad slope confined to an intermediate subfield B <= K <= F.
By f1_minimal_field_descent (PROVED), descend to the MINIMAL field K0 of the
slope's data: the slope is genuinely-K0-valued there (not confined to any
proper subfield of K0 — minimality). At K0 the trichotomy has no tower case:
the slope is B-pencil-rational (priced by b_rational_lift, PROVED) or
pole-type (priced by the imported list term, ext_import, PROVED). The tower
has at most log_2(log_2 |F|) levels (each a field extension); each level's
denominators are the per-level ledger prices printed by the two mechanisms
at that level. Admissibility of the case: axis8_generating (PROVED — the
official family admits non-generating rows, abf26 pinned). Hence case (iii)
closes recursively with per-level denominators, as stated.
