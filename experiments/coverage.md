# Amber Stress Coverage Snapshot

Generated from the current DAG and the `experiments/amber_stress` harness.
This is a progress ledger, not a completion certificate.

| amber node | live non-proved reqs | current stress coverage |
| --- | --- | --- |
| `a_regular_collapse` | `a_regularity_forcing` | selected verifier: assembly/orphan logical surface check |
| `adjacency_closing` | `aperiodic_zero_at_crossing`, `rate_half_band_closure` | selected verifiers: MCA delta self-test + rate-half local |
| `aperiodic_zero_at_crossing` | `r2_clean_rates` | rate-scope repair + XR selected verifiers |
| `ext_lift` | `f1_classification` | selected verifier: f1_minimal_field_descent; F1 weakening audit |
| `f1_case_pole` | `f1_pole_list_threshold_location` | selected verifier: F1 pole-threshold probe; threshold still rides list adjacency |
| `f1_classification` | `f1_case_pole` | selected verifiers: f1_minimal_field_descent + pole-threshold probe; F1 weakening audit |
| `f1_pole_list_threshold_location` | `list_adjacency_closing` | selected verifier: F1 pole-threshold exact arithmetic probe |
| `free_pool_ladder` | `subgroup_expsum_input` | selected verifiers: assembly/orphan logical surface check + subgroup expsum probe |
| `gap1_noneq_mass` | `gap1_product_model` | selected verifier: GAP-1 telescope algebra; strip repair |
| `gap1_product_model` | `tr_perleaf_list_ident` | selected verifiers: GAP-1 telescope algebra; exact TR quotient dictionary probe |
| `hankel_slope_large_sieve` | `diffuse_triple_shadow` | selected verifiers: SPI/Hankel write-up checks + diffuse-shadow circuit scan |
| `imgfib` | `petal_growth` | petal fixed-excess verifier + petal excess local scan; petal_growth remains red |
| `list_adjacency_closing` | `list_planted_arithmetic`, `rate_half_band_closure` | selected verifiers: list corridor + rate-half local |
| `list_grand` | `list_adjacency_closing` | selected verifiers: list corridor |
| `list_planted_arithmetic` | `worst_word_planted`, `worst_word_challenger_pricing`, `imgfib` | selected verifiers: E22 two-class + fixed-scale staircase + extended + shuffled-layout censuses |
| `list_safe` | `imgfib` | petal fixed-excess verifier exercises imgfib/list-safe surface |
| `m_le3_route` | `imgfib` | selected verifier: assembly/orphan logical surface check |
| `mca_grand` | `mca_safe`, `adjacency_closing` | MCA delta self-test + explicit predicate-packet rewrite |
| `mca_safe` | `strip`, `ext_lift`, `r2_clean_rates`, `rate_half_band_closure` | selected verifiers: bounded scales + MCA delta self-test |
| `packaging` | `compiler`, `harness`, `dossier_partial` | selected verifier: assembly/orphan logical surface check |
| `petal_mixed_amplification` | `pma_wide_residual` | selected verifiers: PMA auxiliary-list probe + correlated-target search |
| `prize` | `mca_grand`, `list_grand`, `packaging` | selected verifier: assembly/orphan logical surface check |
| `r2_clean_rates` | `xr_clean_residual_any_gate` | selected verifiers: XR arithmetic/qpower/exponent + smallcore triangle + quadrilateral scans |
| `spi_point_counting` | `hankel_slope_large_sieve` | selected verifiers: SPI/Hankel write-up checks + diffuse-shadow circuit scan |
| `strip` | `gap1_noneq_mass` | selected verifier: gap2 seam; statement repair |
| `tr_perleaf_list_ident` | `x4_exactlist_staircase_split` | selected verifiers: dyadic profile; exact TR quotient dictionary probe |
| `worst_word_planted` | `imgfib`, `worst_word_challenger_pricing` | selected verifiers: E22 two-class + fixed-scale staircase + extended + shuffled-layout censuses |
| `x4_exactlist_staircase_split` | `u1_x4_direct_column_budget`, `dli_prime_weighted_large_block_support`, `u2c_giant_tnull_dichotomy` | selected verifier: dyadic profile; moment witness harness; U2-C t-null boundary scan; DLI weighted/RES probe; U1-for-X4 direct-column active-core probe |
| `xr_clean_residual_any_gate` | `xr_smallcore_spread_count` | selected verifiers: XR arithmetic/qpower/exponent + smallcore triangle + quadrilateral scans |

## Unlisted Amber Nodes

- none by this coarse coverage map

## Nodes Still Lacking A Direct Falsification Harness

- none
