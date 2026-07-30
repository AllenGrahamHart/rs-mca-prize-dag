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
              |                              |
              |                              +--ev--> rate_half_band_closure [TARGET]
              |
              +--req--> rate_half_kb_m6_scott_cartesian_degree2_router [PROVED]
              |                              |
              |                              +--ev--> rate_half_band_closure [TARGET]
              |
              +--req--> rate_half_kb_m4_outer_a6s6_route_cut [PROVED]
                                             |
                                             +--ev--> rate_half_band_closure [TARGET]
```

The degree-12 chain eventually removes all four of its transverse rows. The
degree-10 child routes all four of its rows strictly to degrees 2, 3, or 6.
The degree-6 child then routes every producer to degree two or the excluded
degree-five row. The degree-4 outer child leaves one `A6/S6` type. The
remaining degree-2,3 children and that one degree-4 survivor must consume
actual quartic/source-star incidence or admit another strict block route;
source-only enumeration is exhausted.
