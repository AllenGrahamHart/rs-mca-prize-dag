# Dependency sub-DAG

```text
rate_half_kb_decomposition_source_pencil_compiler [PROVED]
                         |
                         +--req-->
rate_half_kb_source_pencil_rank_transverse_compiler [PROVED]
              |                              |
              +--req--> rate_half_kb_m12_outer_subdegree_route_cut [PROVED]
              |                              |
              |                              +--ev--> rate_half_band_closure [TARGET]
              |
              +--req--> rate_half_kb_m10_scott_strip_lower_degree_router [PROVED]
                                             |
                                             +--ev--> rate_half_band_closure [TARGET]
```

The degree-12 chain eventually removes all four of its transverse rows. The
degree-10 child routes all four of its rows strictly to degrees 2, 3, or 6.
The remaining degree-2,3,4,6 children must consume actual quartic/source-star
incidence or admit another strict block route; source-only enumeration is
exhausted.
